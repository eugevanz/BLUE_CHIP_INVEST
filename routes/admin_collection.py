import json
from collections import defaultdict
from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from database import Account, ClientGoal, DividendPayout, Investment, Transaction, StoreSession

router = APIRouter()
templates = Jinja2Templates(directory="templates")

go_layout = go.Layout(
    xaxis=dict(showticklabels=False, showgrid=False, gridcolor="lightgray", rangeslider=dict(visible=False)),
    yaxis=dict(gridcolor="lightgray", showticklabels=False, showgrid=False), margin=dict(t=0, b=0, l=0, r=0),
    plot_bgcolor="white", height=300, showlegend=False
)
px_layout = dict(
    xaxis=dict(showticklabels=False, rangeslider=dict(visible=False), showgrid=False, title=None),
    yaxis=dict(showticklabels=False, showgrid=False, title=None), margin=dict(t=0, b=0, l=0, r=0), plot_bgcolor="white",
    showlegend=False, height=300
)
common_html_config = dict(
    config=dict(displayModeBar=False, scrollZoom=True), full_html=False,
    post_script="""window.addEventListener('load', function() {
        var plotDiv = document.getElementById('{plot_id}'); Plotly.Plots.resize(plotDiv);
    });"""
)


def account_performance(acc_data: list):
    df = pd.DataFrame(acc_data)
    df["created_at"] = pd.to_datetime(df["created_at"])
    fig = px.scatter(df, x="created_at", y="balance", size="balance", color="account_type",
                     hover_name="account_number", size_max=60)
    fig.update_layout(**px_layout)
    return pio.to_html(fig, **common_html_config)


def dividend_performance(dividends_data: list):
    df = pd.DataFrame(dividends_data)
    df["payment_date"] = pd.to_datetime(df["payment_date"])
    df = df.sort_values(by="payment_date")
    df["cumulative_payout"] = df["amount"].cumsum()
    trace = go.Scatter(x=df["payment_date"], y=df["cumulative_payout"], fill="tozeroy", mode="lines+markers",
                       line=dict(color="blue", width=6, shape="spline"), fillcolor="rgba(0, 0, 255, 0.2)",
                       marker=dict(color="blue", size=10))
    fig = go.Figure(data=[trace], layout=go_layout)
    return pio.to_html(fig, **common_html_config)


def goal_performance(goals_data: list):
    df = pd.DataFrame(goals_data)
    trace = [
        go.Bar(name="Current Savings", x=df["goal_type"], y=df["current_savings"]),
        go.Bar(name="Target Amount", x=df["goal_type"], y=df["target_amount"])
    ]
    fig = go.Figure(data=trace, layout=go_layout)
    fig.update_layout(barmode="stack")
    return pio.to_html(fig, **common_html_config)


def inv_performance(inv_data: list):
    df = pd.DataFrame(inv_data)
    df["created_at"] = pd.to_datetime(df["created_at"])
    grouped = df.groupby("investment_type")["current_price"].sum().reset_index()
    trace = [go.Bar(x=grouped["investment_type"], y=grouped["current_price"])]
    fig = go.Figure(data=trace, layout=go_layout)
    return pio.to_html(fig, **common_html_config)


# LOGGED IN USER

@router.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="admin_html/login.html")


@router.get("/admin/", response_class=HTMLResponse)
async def admin(request: Request):
    user = StoreSession.find(StoreSession.user_id == request.cookies.get('user_id')).first()
    if user:
        profile_data = {
            "profile_picture_url": user.profile_picture_url,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }
        return templates.TemplateResponse(request=request, name="admin_html/admin.html", context=profile_data)
    else:
        return RedirectResponse("/login/", status_code=302)


@router.get("/client/", response_class=HTMLResponse)
async def client(request: Request):
    user_id = request.cookies.get("user_id")
    if user_id:
        accounts = request.app.state.supabase_.table("accounts").select("*").eq("profile_id", user_id).execute()
        client_goals = request.app.state.supabase_.table("client_goals").select("*").eq("profile_id", user_id).execute()
        account_ids = [acc["id"] for acc in accounts.data] if accounts.data else []
        dividends_and_payouts = request.app.state.supabase_.table("dividends_and_payouts").select("*").in_(
            "account_id", account_ids).execute() if accounts.data else []
        investments = request.app.state.supabase_.table("investments").select("*").in_(
            "account_id", account_ids).execute() if accounts.data else []
        transactions = request.app.state.supabase_.table("transactions").select("*").in_(
            "account_id", account_ids).execute() if accounts.data else []

        account_totals = defaultdict(float)
        for entry in accounts.data:
            account_totals[entry["account_type"]] += entry["balance"]

        investment_totals = defaultdict(float)
        for entry in investments.data:
            investment_totals[entry["investment_type"]] += entry['current_price']

        account_chart_html = account_performance(accounts.data)
        div_chart_html = dividend_performance(dividends_and_payouts.data)
        goal_chart_html = goal_performance(client_goals.data)
        inv_chart_html = inv_performance(investments.data)

        profile_data = {
            "profile_id": user_id,
            "profile_picture_url": request.cookies.get("profile_picture_url"),
            "first_name": request.cookies.get("first_name"),
            "last_name": request.cookies.get("last_name"),
            "email": request.cookies.get("email")
        }
        return templates.TemplateResponse(request=request, name="admin_html/client.html", context={
            "profile_data": profile_data, "account_chart_html": account_chart_html, "div_chart_html": div_chart_html,
            "goal_chart_html": goal_chart_html, "inv_chart_html": inv_chart_html, "accounts": accounts.data,
            "client_goals": client_goals.data, "dividends_and_payouts": dividends_and_payouts.data,
            "investments": investments.data, "transactions": transactions.data,
            "account_totals": dict(account_totals), "investment_totals": dict(investment_totals)})
    else:
        return RedirectResponse("/login/", status_code=302)


# LOGON

@router.get("/sign_out/")
async def sign_out(request: Request):
    request.app.state.supabase_admin.auth.sign_out()
    user = StoreSession.find(StoreSession.user_id == request.cookies.get('user_id')).first()
    StoreSession.delete(user.pk)

    return RedirectResponse("/login/")


@router.post("/request_otp/", response_class=HTMLResponse)
async def request_otp(request: Request, email: str = Form(...)):
    response = request.app.state.supabase_admin.auth.sign_in_with_otp(
        {"email": email, "options": {"should_create_user": False}})

    if response and response.user is None:
        return HTMLResponse(content=f"""<form action="/verify_otp/" method="post" class="uk-margin">
            <h3 class="uk-card-title uk-text-bolder uk-margin-remove-bottom">Ready to sign-in?</h3>
            <p class="uk-text-small uk-margin-remove-top" style="color: #091235;">
                Please enter the <strong>verification code</strong> that was sent to your email. This code is required
                to verify your identity and complete the login process.
            </p>
            <div class="uk-text-small">One-time PIN</div>
            <div class="uk-inline">
                <span class="uk-form-icon" uk-icon="icon: lock"></span>
                <input class="uk-input uk-form-width-large" name="sent_code" type="text">
            </div>
            <input name="sent_email" type="hidden" value="{email}" required>
            <p class="uk-text-meta">Please enter your OTP and click Sign In.</p>
            <button class="uk-button uk-button-large uk-light" style="background-color:#091235;">Sign In</button>
        </form>""")
    else:
        return HTMLResponse(
            content=f"<p class='uk-text-danger' id='send_code_notifications'>{response.error_message}</p>")


@router.post("/verify_otp/")
async def verify_otp(request: Request, sent_email: str = Form(...), sent_code: str = Form(...)):
    auth_response = request.app.state.supabase_admin.auth.verify_otp(
        {"email": sent_email, "token": sent_code, "type": "email"})

    if auth_response and auth_response.user:
        profile_response = request.app.state.supabase_.table("profiles").select("*").eq(
            "id", auth_response.user.id
        ).single().execute()
        profile = profile_response.data
        response = RedirectResponse(
            "/admin/", status_code=302
        ) if profile["profile_type"] == "admin" else RedirectResponse(
            "/client/", status_code=302
        )

        accounts = request.app.state.supabase_.table("accounts").select("id").eq(
            "profile_id", auth_response.user.id
        ).execute()

        response.set_cookie(key="account_ids", value=json.dumps(accounts.data), httponly=True, max_age=3600)
        response.set_cookie(key="user_id", value=auth_response.user.id, httponly=True, max_age=3600)
        response.set_cookie(key="first_name", value=profile["first_name"], httponly=True, max_age=3600)
        response.set_cookie(key="last_name", value=profile["last_name"], httponly=True, max_age=3600)
        response.set_cookie(key="profile_picture_url", value=profile["profile_picture_url"], httponly=True,
                            max_age=3600)
        response.set_cookie(key="profile_type", value=profile["profile_type"], httponly=True, max_age=3600)
        response.set_cookie(key="email", value=profile["email"], httponly=True, max_age=3600)
        return response
    else:
        RedirectResponse("/login/")


# PROFILES Routes

@router.post("/update_profile/", response_class=HTMLResponse)
def update_profile(
        request: Request, profile_id: str = Form(...), profile_picture_url: str = Form(...),
        first_name: str = Form(...),
        last_name: str = Form(...)
):
    update_data = {}
    if profile_picture_url is not None:
        update_data["profile_picture_url"] = profile_picture_url
    if first_name is not None:
        update_data["first_name"] = first_name
    if last_name is not None:
        update_data["last_name"] = last_name

    response = request.app.state.supabase_.table("profiles").update(update_data).eq("id", profile_id).execute()
    if response.error:
        return HTMLResponse(content=f"""<p>Failed to update profile: {response.error_message}</p>""")
    if response.data:
        return HTMLResponse(content=f"""<p>Profile updated successfully.</p>""")


@router.post("/send_invite/", response_class=HTMLResponse)
def send_invite(request: Request, email: str = Form(...)):
    response = request.app.state.supabase_admin.auth.admin.invite_user_by_email(email)
    if response and response.user:
        return HTMLResponse(content=f"""<p>Invite sent to {response.user.email}</p>""")
    else:
        return HTMLResponse(content=f"""<p>Error sending invite: {response["error"]["message"]}</p>""")


# ACCOUNT Routes

@router.get("/accounts/{profile_id}/", response_class=HTMLResponse)
async def accounts_(request: Request):
    return templates.TemplateResponse(request=request, name="admin_html/accounts.html", context={})


@router.get("/select_all_from_accounts_where_profile_id/{profile_id}/")
async def select_all_from_accounts_where_profile_id(profile_id: str):
    accounts = Account.find(Account.profile_id == profile_id).all()
    return accounts


@router.post("/create_account/", response_class=HTMLResponse)
async def create_account(profile_id: str = Form(...), account_type: str = Form(...), balance: float = Form(0.0)):
    account_data = Account(
        account_type=account_type,
        balance=balance,
        profile_id=profile_id,
    )
    account_data.save()
    return HTMLResponse(content=f"""<p class="uk-text-meta">Account created successfully</p>""")


@router.post("/delete_account/{account_number}", response_class=HTMLResponse)
async def delete_account(account_number: str):
    account_ = Account.find(Account.account_number == account_number).first()
    Account.delete(account_.pk)
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Account deleted successfully with account number <span class="uk-text-bold">{account_number}</span>
    </p>""")


# CLIENT GOAL Routes

@router.get("/client_goals/", response_class=HTMLResponse)
async def client_goals_(request: Request):
    return templates.TemplateResponse(request=request, name="admin_html/goals.html", context={})


@router.get("/select_all_from_client_goals_where_profile_id/{profile_id}/")
async def select_all_from_client_goals_where_profile_id(profile_id: str):
    goals = ClientGoal.find(ClientGoal.profile_id == profile_id).all()
    return goals


@router.post("/create_client_goal/", response_class=HTMLResponse)
async def create_client_goal(
        profile_id: str = Form(...), goal_type: str = Form(...), target_amount: float = Form(...),
        current_savings: float = Form(...), target_date: str = Form(...)
):
    goal_data = ClientGoal(
        profile_id=profile_id,
        goal_type=goal_type,
        target_amount=target_amount,
        current_savings=current_savings,
        target_date=datetime.strptime(target_date, "%Y-%m-%d").timestamp()
    )
    goal_data.save()
    return HTMLResponse(content=f"""<p class="uk-text-meta">Client Goal created successfully</p>""")


@router.post("/delete_client_goal/{goal_number}/", response_class=HTMLResponse)
async def delete_client_goal(goal_number: str):
    goal = ClientGoal.find(ClientGoal.goal_number == goal_number).first()
    ClientGoal.delete(goal.pk)
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Client Goal deleted successfully for goal <span class="uk-text-bold">{goal_number}</span>
    </p>""")


# DIVIDENDS AND PAYOUTS Routes

@router.get("/payouts/", response_class=HTMLResponse)
async def payouts_(request: Request):
    return templates.TemplateResponse(request=request, name="admin_html/payouts.html", context={})


@router.get("/select_all_from_dividends_payouts_where_account/{account_number}/")
async def select_all_from_dividends_payouts_where_account(account_number: str):
    payouts = DividendPayout.find(DividendPayout.account_number == account_number).all()
    return payouts


@router.post("/create_dividend_payout/", response_class=HTMLResponse)
async def create_dividend_payout(
        profile_id: str = Form(...), account_number: str = Form(...), amount: float = Form(...),
        payment_date: str = Form(...)
):
    payout_data = DividendPayout(
        profile_id=profile_id,
        account_number=account_number,
        amount=amount,
        payment_date=datetime.strptime(payment_date, "%Y-%m-%d").timestamp()
    )
    payout_data.save()
    return HTMLResponse(content=f"""<p class="uk-text-meta">Dividend/Payout created successfully</p>""")


@router.post("/delete_dividend_payout/{payout_number}/", response_class=HTMLResponse)
async def delete_dividend_payout(payout_number: str):
    payout = DividendPayout.find(DividendPayout.payout_number == payout_number).first()
    DividendPayout.delete(payout.pk)
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Dividend/Payout deleted successfully for <span class="uk-text-bold">{payout_number}</span>
    </p>""")


# INVESTMENTS Routes

@router.get("/investments/", response_class=HTMLResponse)
async def investments_(request: Request):
    return templates.TemplateResponse(request=request, name="admin_html/investments.html", context={})


@router.get("/select_all_from_investments_where_account/{account_number}/")
async def select_all_from_investments_where_account_id(account_number: str):
    investments = Investment.find(Investment.account_number == account_number).all()
    return investments


@router.post("/create_investment/")
async def create_investment(
        account_number: str = Form(...), investment_type: str = Form(...),
        symbol: str = Form(...), quantity: float = Form(...), purchase_price: float = Form(...),
        current_price: float = Form(...), purchase_date: str = Form(...)
):
    investment_data = Investment(
        account_number=account_number,
        investment_type=investment_type,
        symbol=symbol,
        quantity=quantity,
        purchase_price=purchase_price,
        current_price=current_price,
        purchase_date=datetime.strptime(purchase_date, "%Y-%m-%d").timestamp()
    )
    investment_data.save()
    return HTMLResponse(content=f"""<p class="uk-text-meta">Investments created successfully</p>""")


@router.post("/delete_investment/{inv_number}/")
async def delete_investment(inv_number: str):
    investment = Investment.find(Investment.inv_number == inv_number).first()
    Investment.delete(investment.pk)
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Investment deleted successfully for <span class="uk-text-bold">{inv_number}</span>
    </p>""")


# TRANSACTIONS Routes

@router.get("/transactions/{profile_id}/", response_class=HTMLResponse)
async def transactions_(profile_id: str, request: Request):
    account_ids = request.app.state.supabase_.table("accounts").select("id").eq("profile_id", profile_id).execute().data
    if not account_ids:
        return []
    account_ids = [acc["id"] for acc in account_ids]
    response = request.app.state.supabase_.table("transactions").select("*").in_(
        "account_id", account_ids).execute()
    return templates.TemplateResponse(request=request, name="admin_html/transactions.html",
                                      context={"transactions": response.data if response.data else []})


@router.get("/select_all_from_transactions_where_account/{account_number}/")
async def select_all_from_transactions_where_account_id(account_number: str):
    transactions = Transaction.find(Transaction.account_number == account_number).all()
    return transactions


@router.post("/create_transaction/")
async def create_transaction(
        account_number: str = Form(...), amount: float = Form(...), txn_type: str = Form(...),
        description: str = Form(...)
):
    transaction_data = Transaction(
        account_number=account_number,
        txn_type=txn_type,
        amount=amount,
        description=description
    )
    transaction_data.save()
    return HTMLResponse(content=f"""<p class="uk-text-meta">Transaction created successfully</p>""")


@router.post("/delete_transaction/{txn_number}/")
async def delete_from_transactions(txn_number: str):
    transaction = Transaction.find(Transaction.txn_number == txn_number).first()
    Transaction.delete(transaction.pk)
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Transaction deleted successfully for <span class="uk-text-bold">{txn_number}</span>
    </p>""")
