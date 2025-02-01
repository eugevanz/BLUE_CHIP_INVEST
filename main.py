import asyncio
import json
import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional, List

import numpy as np
import numpy_financial as npf
from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from redis_om import Field, JsonModel, get_redis_connection
from supabase import create_client


class Account(JsonModel):
    account_number: str = Field(index=True)
    account_type: str
    balance: float = Field(index=True)
    profile_id: str  # Add profile_id for reference
    created_at: datetime = Field(index=True)
    updated_at: Optional[datetime] = Field(index=True)

    class Meta:
        database = get_redis_connection(url=os.environ.get("REDIS_URL"), decode_responses=True)


class ClientGoal(JsonModel):
    goal_number: str = Field(index=True)
    goal_type: str
    target_amount: float
    current_savings: float
    target_date: datetime
    profile_id: str = Field(index=True)
    created_at: datetime = Field(index=True)
    updated_at: Optional[datetime] = Field(index=True)

    class Meta:
        database = get_redis_connection(url=os.environ.get("REDIS_URL"), decode_responses=True)


class DividendPayout(JsonModel):
    account_id: str
    payout_number: str = Field(index=True)
    amount: float
    payment_date: datetime
    created_at: datetime = Field(index=True)

    class Meta:
        database = get_redis_connection(url=os.environ.get("REDIS_URL"), decode_responses=True)


class Investment(JsonModel):
    account_id: str
    inv_number: str = Field(index=True)
    investment_type: str
    symbol: str
    quantity: float
    purchase_price: float
    current_price: float
    purchase_date: datetime
    created_at: datetime = Field(index=True)
    updated_at: Optional[datetime] = Field(index=True)

    class Meta:
        database = get_redis_connection(url=os.environ.get("REDIS_URL"), decode_responses=True)


class Transaction(JsonModel):
    account_id: str
    txn_number: str = Field(index=True)
    amount: float
    txn_type: str
    description: str
    created_at: datetime = Field(index=True)

    class Meta:
        database = get_redis_connection(url=os.environ.get("REDIS_URL"), decode_responses=True)


templates = Jinja2Templates(directory="templates")

EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
SUPABASE_SERVICE_ROLE_KEY = os.environ.get('SUPABASE_SERVICE_ROLE_KEY')
SUPABASE_PASSWORD = os.environ.get('SUPABASE_PASSWORD')
supabase_ = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_KEY)
supabase_admin = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_SERVICE_ROLE_KEY)

with open("static/data.json", "r") as file:
    data = json.load(file)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


# ACCOUNT Routes

@app.get("/select_all_from_accounts_where_profile_id/{profile_id}/", response_model=List[Account])
async def select_all_from_accounts_where_profile_id(profile_id: str):
    accounts = Account.find(Account.profile_id == profile_id).all()
    return accounts


@app.post("/create_account/", response_class=HTMLResponse)
async def create_account(profile_id: str = Form(...), account_type: str = Form(...), balance: float = Form(...)):
    account_number = Account.Meta.database.incr("account_number_counter")
    account_number = f"ACC{account_number + 100000}"

    new_account = Account(
        created_at=datetime.today().date().isoformat(),  # You could use a timestamp here
        profile_id=profile_id,
        account_number=account_number,
        account_type=account_type,
        balance=balance,
        updated_at=datetime.today().date().isoformat(),  # Same here for updates
    )
    new_account.save()
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Account created successfully with account number <span class="uk-text-bold">{account_number}</span>
    </p>""")


@app.post("/delete_account/{account_number}", response_class=HTMLResponse)
async def delete_account(account_number: str):
    account = Account.find(Account.account_number == account_number).first()
    account.delete()
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Account deleted successfully with account number <span class="uk-text-bold">{account_number}</span>
    </p>""")


# CLIENT GOAL Routes

@app.get("/select_all_from_client_goals_where_profile_id/{profile_id}/")
async def select_all_from_client_goals_where_profile_id(profile_id: str):
    goals = ClientGoal.find(ClientGoal.profile_id == profile_id).all()
    return goals


@app.post("/create_client_goal/", response_class=HTMLResponse)
async def create_client_goal(
        profile_id: str = Form(...), goal_type: str = Form(...), target_amount: float = Form(...),
        current_savings: float = Form(...), target_date: str = Form(...)
):
    goal_number = ClientGoal.Meta.database.incr("goal_number_counter")
    goal_number = f"GL{goal_number + 100000}"

    new_client_goal = ClientGoal(
        created_at=datetime.today().date().isoformat(),  # You could use a timestamp here
        profile_id=profile_id,
        goal_type=goal_type,
        goal_number=goal_number,
        target_amount=target_amount,
        current_savings=current_savings,
        target_date=datetime.strptime(target_date, "%Y-%m-%d").date(),
        updated_at=datetime.today().date().isoformat(),  # Same here for updates
    )

    new_client_goal.save()
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Client Goal created successfully for <span class="uk-text-bold">{goal_type}</span>
    </p>""")


@app.post("/delete_client_goal/{goal_number}/", response_class=HTMLResponse)
async def delete_client_goal(goal_number: str):
    goal = ClientGoal.find(ClientGoal.goal_number == goal_number).first()
    goal.delete()
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Client Goal deleted successfully for goal <span class="uk-text-bold">{goal_number}</span>
    </p>""")


# DIVIDENDS AND PAYOUTS Routes

@app.get("/select_all_from_dividends_payouts_where_account/{account_number}/")
async def select_all_from_dividends_payouts_where_account(account_number: str):
    account = Account.find(Account.account_number == account_number).first()
    payouts = DividendPayout.find(DividendPayout.account_id == account.pk).all()
    return payouts


@app.post("/create_dividend_payout/", response_class=HTMLResponse)
async def create_dividend_payout(
        profile_id: str = Form(...), account_id: str = Form(...), amount: float = Form(...),
        payment_date: str = Form(...)
):
    payout_number = DividendPayout.Meta.database.incr("payout_number_counter")
    payout_number = f"DIV{payout_number + 100000}"

    new_dividend_payout = DividendPayout(
        payout_number=payout_number,
        created_at=datetime.today().date().isoformat(),  # You could use a timestamp here
        profile_id=profile_id,
        account_id=account_id,
        amount=amount,
        payment_date=payment_date
    )

    new_dividend_payout.save()
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Dividend/Payout created successfully for dividend/payout <span class="uk-text-bold">{payout_number}</span>
    </p>""")


@app.post("/delete_dividend_payout/{payout_number}/", response_class=HTMLResponse)
async def delete_dividend_payout(payout_number: str):
    payout = DividendPayout.find(DividendPayout.payout_number == payout_number).first()
    payout.delete()
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Dividend/Payout deleted successfully for <span class="uk-text-bold">{payout_number}</span>
    </p>""")


# INVESTMENTS Routes

@app.get("/select_all_from_investments_where_account/{account_number}/")
async def select_all_from_investments_where_account_id(account_number: str):
    account = Account.find(Account.account_number == account_number).first()
    investments = DividendPayout.find(DividendPayout.account_id == account.pk).all()
    return investments


@app.post("/create_investment/")
async def create_investment(
        account_id: str = Form(...), investment_type: str = Form(...),
        symbol: str = Form(...), quantity: float = Form(...), purchase_price: float = Form(...),
        current_price: float = Form(...), purchase_date: str = Form(...)
):
    inv_number = Investment.Meta.database.incr("inv_number_counter")
    inv_number = f"INV{inv_number + 100000}"

    new_investment = Investment(
        inv_number=inv_number,
        created_at=datetime.today().date().isoformat(),
        account_id=account_id,
        investment_type=investment_type,
        symbol=symbol,
        quantity=quantity,
        purchase_price=purchase_price,
        current_price=current_price,
        purchase_date=purchase_date,
        updated_at=datetime.today().date().isoformat()
    )

    new_investment.save()
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Investments created successfully for investment <span class="uk-text-bold">{inv_number}</span>
    </p>""")


@app.post("/delete_investment/{inv_number}/")
async def delete_investment(inv_number: str):
    investment = Investment.find(Investment.inv_number == inv_number).first()
    investment.delete()
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Investment deleted successfully for <span class="uk-text-bold">{inv_number}</span>
    </p>""")


# TRANSACTIONS Routes

@app.get("/select_all_from_transactions_where_account/{account_number}/")
async def select_all_from_transactions_where_account_id(account_number: str):
    account = Account.find(Account.account_number == account_number).first()
    transactions = DividendPayout.find(DividendPayout.account_id == account.pk).all()
    return transactions


@app.post("/create_transaction/")
async def create_transaction(
        account_id: str = Form(...), amount: float = Form(...), txn_type: str = Form(...),
        description: str = Form(...)
):
    txn_number = Transaction.Meta.database.incr("txn_number_counter")
    txn_number = f"TXN{txn_number + 100000}"

    new_transaction = Transaction(
        txn_number=txn_number,
        created_at=datetime.today().date().isoformat(),
        account_id=account_id,
        txn_type=txn_type,
        amount=amount,
        description=description
    )

    new_transaction.save()
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Transaction created successfully for transaction <span class="uk-text-bold">{new_transaction}</span>
    </p>""")


@app.post("/delete_transaction/{txn_number}/")
async def delete_from_transactions(txn_number: str):
    transaction = Transaction.find(Transaction.txn_number == txn_number).first()
    transaction.delete()
    return HTMLResponse(content=f"""<p class="uk-text-meta">
        Transaction deleted successfully for <span class="uk-text-bold">{txn_number}</span>
    </p>""")


# ------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={
            "ctas": data["ctas"], "whatwedo": data["whatwedo"], "testimonials": data["testimonials"],
            "whoweserve": data["whoweserve"]
        }
    )


@app.get("/home/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html", context={}
    )


@app.get("/advisors/", response_class=HTMLResponse)
async def get(request: Request):
    advisors = [
        dict(name='Aidan Mercer', position='Senior Investment Strategist'),
        dict(name='Fiona Drake', position='Chief Financial Officer (CFO)'),
        dict(name='Liam Caldwell', position='Wealth Management Advisor'),
        dict(name='Chloe Rutherford', position='Portfolio Manager'),
        dict(name='Ethan Carrington', position='Head of Corporate Finance'),
        dict(name='Isabelle Thornton', position='Private Relationship Manager'),
        dict(name='Marcus Ellison', position='Director of Risk Management'),
        dict(name='Sophia Bennett', position='Chief Compliance Officer (CCO)')
    ]
    return templates.TemplateResponse(
        request=request, name="advisors.html", context={"advisors": advisors}
    )


@app.get("/services/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="services.html", context={"services": data["services"]}
    )


@app.get("/contact-us/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="contact-us.html", context={}
    )


@app.get("/guides/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="guides.html", context={"qas": data["qas"]}
    )


@app.get("/who-we-serve/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="who-we-serve.html", context={"whoweserve": data["whoweserve"]}
    )


@app.get("/financial-tools/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="financial-tools.html", context={}
    )


# Financial Tools

@app.post("/calculate-adjusted-roi/", response_class=HTMLResponse)
async def calculate_adjusted_roi(
        initial: int = Form(0), final: int = Form(0), years: int = Form(1), taxes: int = Form(0), fees: int = Form(0)
):
    # Default inputs to zero if they are None
    initial, final, years, taxes, fees = float(initial), float(final), float(years), float(taxes), float(fees)

    # Validate inputs to avoid errors
    if initial <= 0 or final <= 0 or years <= 0:
        return HTMLResponse(content="<span>Please make sure all values are positive and greater than zero.</span>")

    # Calculate basic ROI
    basic_roi = ((final - initial) / initial) * 100

    # Apply taxes and fees adjustments to the ROI
    tax_adjustment = basic_roi * (taxes / 100)
    fee_adjustment = basic_roi * (fees / 100)
    adjusted_roi = basic_roi - tax_adjustment - fee_adjustment

    # Annualise the ROI if the period is more than 1 year
    annualised_roi = ((1 + adjusted_roi / 100) ** (1 / years) - 1) * 100 if years > 1 else adjusted_roi

    # Return formatted result
    return HTMLResponse(content=f"""<span>
        <span class='uk-text-bolder'>{annualised_roi:,.2f}%</span> Adjusted ROI after Taxes and Fees
    </span>""")


@app.post("/calculate-annualised-roi/", response_class=HTMLResponse)
async def calculate_annualised_roi(initial: int = Form(0), final: int = Form(0), years: int = Form(1)):
    # Default inputs to zero if they are None
    initial, final, years = float(initial), float(final), float(years)

    # Validate inputs to avoid division by zero or invalid calculations
    if initial <= 0 or final <= 0 or years <= 0:
        return HTMLResponse(content="<span>Please make sure all values are positive and greater than zero.</span>")

    # Calculate Annualised ROI
    annualised_roi = ((final / initial) ** (1 / years) - 1) * 100

    # Return formatted result
    return f"<span><span class='uk-text-bolder'>{annualised_roi:,.2f}%</span> Annualised ROI</span>"


@app.post("/calculate-roi/", response_class=HTMLResponse)
async def calculate_roi(initial: int = Form(0), final: int = Form(0)):
    # Default inputs to zero if they are None
    initial, final = float(initial), float(final)

    # Avoid division by zero
    if initial == 0:
        return HTMLResponse(
            content="<span>Please make sure all values are positive and greater than zero.</span>"
        ) if final != 0 else HTMLResponse(
            content="<span>0.00%</span>"
        )

    # Calculate ROI
    roi = ((final - initial) / initial) * 100

    # Return formatted result
    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>{roi:,.2f}%</span> ROI</span>")


@app.post("/calculate-bep/", response_class=HTMLResponse)
async def calculate_bep(fixed_costs: int = Form(0), variable_costs: int = Form(0), price_per_unit: int = Form(0)):
    # Default inputs to zero if they are None or invalid
    fixed_costs, variable_costs, price_per_unit = float(fixed_costs), float(variable_costs), float(price_per_unit)

    # Handle invalid or negative values for any parameter
    if price_per_unit <= variable_costs or price_per_unit <= 0:
        return HTMLResponse(
            content="<span>BEP can't be calculated if price is less than or equal to variable cost.</span>"
        )
    if fixed_costs < 0 or variable_costs < 0:
        return HTMLResponse(content="<span>BEP can't be calculated if costs are negative.</span>")

    # Calculate the Break-Even Point (Units) using the formula:
    # BEP (Units) = Fixed Costs / (Price per Unit - Variable Cost per Unit)
    bep_units = fixed_costs / (price_per_unit - variable_costs)

    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>{bep_units:,.0f}</span> units</span>")


@app.post("/calculate-monthly-car-loan/", response_class=HTMLResponse)
async def calculate_monthly_car_loan(
        car_price: int = Form(0), down_payment_pct: int = Form(0), loan_term_years: int = Form(1), annual_rate=Form(0)
):
    # Default inputs to zero if they are None
    car_price, down_payment_pct, loan_term_years, annual_rate = (
        float(car_price), float(down_payment_pct), int(loan_term_years), float(annual_rate)
    )

    if car_price <= 0 or down_payment_pct < 0 or loan_term_years <= 0 or annual_rate < 0:
        return HTMLResponse(content="<span>Please make sure all values are positive and greater than zero.</span>")

    # Calculate loan amount after down payment
    loan_amount = car_price * (1 - (down_payment_pct / 100))

    # Convert annual rate to monthly and term to months
    monthly_rate = (annual_rate / 100) / 12
    num_payments = loan_term_years * 12

    # Monthly car loan payment calculation using the fixed-rate loan formula
    if monthly_rate == 0:
        # Handle case where interest rate is 0 (simple division)
        monthly_payment = loan_amount / num_payments
    else:
        monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)

    # Return formatted monthly payment
    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>R {monthly_payment:,.2f}</span> per month</span>")


@app.post("/calculate-net-cash-flow/", response_class=HTMLResponse)
async def calculate_net_cash_flow(inflows: int = Form(0), outflows: int = Form(0)):
    # Default inputs to zero if they are None or invalid
    inflows, outflows = float(inflows), float(outflows)

    # Handle invalid or negative values for any parameter
    if inflows < 0 or outflows < 0:
        return HTMLResponse(content="<span>Cash flow can't be calculated if there are negative values.</span>")

    # Calculate Net Cash Flow
    net_cash_flow = inflows - outflows

    return HTMLResponse(content=f"<span class='uk-text-bolder'>R {net_cash_flow:,.2f}</span>")


@app.post("/update-compound-interest/", response_class=HTMLResponse)
async def update_compound_interest(
        principal: int = Form(0), rate: int = Form(0), time: int = Form(0), frequency: int = Form(1)
):
    # Default inputs to zero if they are None
    principal, rate, time, frequency = float(principal), float(rate) / 100, float(time), int(frequency)

    # Calculate compound interest
    amount = principal * (1 + rate / frequency) ** (frequency * time)
    compound_interest = amount - principal

    # Return the formatted result
    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>R {compound_interest:,.2f}</span> per year</span>")


@app.post("/calculate-dti/", response_class=HTMLResponse)
async def calculate_dti(debt_payments: int = Form(0), income: int = Form(0)):
    # Default inputs to zero if they are None or invalid
    debt_payments, income = float(debt_payments), float(income)

    # Handle invalid or negative values for any parameter
    if income <= 0:
        return HTMLResponse(content="<span>Can't calculate DTI if income is zero or less.</span>")
    if debt_payments < 0:
        return HTMLResponse(content="<span>DTI can't be negative.</span>")

    # Calculate DTI as a percentage
    dti = (debt_payments / income) * 100

    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>{dti:,.2f}</span> %</span>")


@app.post("/calculate-monthly-payment/", response_class=HTMLResponse)
async def calculate_monthly_payment(loan: int = Form(0), annual_rate: int = Form(0), term_years: int = Form(1)):
    # Default inputs to zero if they are None
    loan, annual_rate, term_years = float(loan), float(annual_rate), int(term_years)

    if loan <= 0 or annual_rate < 0 or term_years <= 0:
        return HTMLResponse(content="<span>Please make sure all values are positive and greater than zero.</span>")

    # Convert annual rate to monthly and term to months
    monthly_rate = (annual_rate / 100) / 12
    num_payments = term_years * 12

    # Monthly payment calculation using the formula for fixed-rate loans
    if monthly_rate == 0:
        # Handle case where interest rate is 0 (simple division)
        monthly_payment = loan / num_payments
    else:
        monthly_payment = (loan * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)

    return f"<span><span class='uk-text-bolder'>R {monthly_payment:,.2f}</span> per month</span>"


@app.post("/calculate-fv/", response_class=HTMLResponse)
async def calculate_fv(present: int = Form(0), annual: int = Form(0), periods: int = Form(0), compound: int = Form(0)):
    # Default inputs to zero if they are None or invalid
    present, annual, periods, compound = float(present), float(annual) / 100, float(periods), float(compound)

    # Handle invalid or negative values for any parameter
    if present <= 0 or annual <= 0 or periods <= 0 or compound <= 0:
        return HTMLResponse(content="<span>FV can't be calculated if any of the inputs are zero or negative</span>")

    # Calculate the Future Value (FV) using the compound interest formula
    fv = present * (1 + annual / compound) ** (compound * periods)

    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>R {fv:,.2f}</span></span>")


@app.post("/calculate-irr/", response_class=HTMLResponse)
async def calculate_irr(
        initial_investment: int = Form(0), cash_flow_1: int = Form(0), cash_flow_2: int = Form(0),
        cash_flow_3: int = Form(0), cash_flow_4: int = Form(0), cash_flow_5: int = Form(0)
):
    # Default inputs to zero if they are None or invalid
    initial_investment, cash_flow_1, cash_flow_2, cash_flow_3, cash_flow_4, cash_flow_5 = (
        float(initial_investment), float(cash_flow_1), float(cash_flow_2), float(cash_flow_3), float(cash_flow_4),
        float(cash_flow_5)
    )

    # Handle invalid or negative values for any parameter
    if initial_investment <= 0 or any(
            cash_flow < 0 for cash_flow in [cash_flow_1, cash_flow_2, cash_flow_3, cash_flow_4, cash_flow_5]):
        return HTMLResponse(content="<span>Please make sure all values are positive and greater than zero.</span>")

    # Cash flow array including initial investment (as a negative value)
    cash_flows = np.array([-initial_investment, cash_flow_1, cash_flow_2, cash_flow_3, cash_flow_4, cash_flow_5])

    # Use numpy_financial's irr calculation (the result in decimal form)
    irr = npf.irr(cash_flows)

    if irr is None:
        return HTMLResponse(content="<span>Unable to calculate IRR.</span>")

    # Convert IRR to percentage
    irr_percent = irr * 100

    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>{irr_percent:,.2f}</span> %</span>")


@app.post("/calculate-monthly-mortgage/", response_class=HTMLResponse)
async def calculate_monthly_mortgage(
        home_price: int = Form(0), down_payment_pct: int = Form(0), loan_term_years: int = Form(1),
        annual_rate: int = Form(0)
):
    # Default inputs to zero if they are None
    home_price, down_payment_pct, loan_term_years, annual_rate = (
        float(home_price), float(down_payment_pct), int(loan_term_years), float(annual_rate)
    )

    if home_price <= 0 or down_payment_pct < 0 or loan_term_years <= 0 or annual_rate < 0:
        return HTMLResponse(content="<span>Please make sure all values are positive and greater than zero.</span>")

    # Calculate loan amount after down payment
    loan_amount = home_price * (1 - (down_payment_pct / 100))

    # Convert annual rate to monthly and term to months
    monthly_rate = (annual_rate / 100) / 12
    num_payments = loan_term_years * 12

    # Monthly mortgage payment calculation using the fixed-rate loan formula
    if monthly_rate == 0:
        # Handle case where interest rate is 0 (simple division)
        monthly_payment = loan_amount / num_payments
    else:
        monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)

    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>R {monthly_payment:,.2f}</span> per month</span>")


@app.post("/calculate-npv/", response_class=HTMLResponse)
async def calculate_npv(
        initial_investment: int = Form(0), discount_rate: int = Form(0), cash_flow_1: int = Form(0),
        cash_flow_2: int = Form(0), cash_flow_3: int = Form(0)
):
    # Default inputs to zero if they are None or invalid
    initial_investment, discount_rate, cash_flow_1, cash_flow_2, cash_flow_3 = (
        float(initial_investment), float(discount_rate), float(cash_flow_1), float(cash_flow_2), float(cash_flow_3)
    )

    # Handle invalid or negative values for any parameter
    if initial_investment <= 0 or discount_rate < 0 or any(
            cash_flow < 0 for cash_flow in [cash_flow_1, cash_flow_2, cash_flow_3]):
        return HTMLResponse(content="<span>Please make sure all values are positive and greater than zero.</span>")

    # Convert discount rate percentage to decimal
    discount_rate /= 100

    # NPV Calculation formula: NPV = Σ (Cash Flow / (1 + discount rate) ^ year) - Initial Investment
    npv = (-initial_investment) + (
            cash_flow_1 / (1 + discount_rate) ** 1 +
            cash_flow_2 / (1 + discount_rate) ** 2 +
            cash_flow_3 / (1 + discount_rate) ** 3
    )

    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>R {npv:,.2f}</span></span>")


@app.post("/calculate-payback-period/", response_class=HTMLResponse)
async def calculate_payback_period(initial_investment: int = Form(0), annual_inflows: int = Form(0)):
    # Default inputs to zero if they are None or invalid
    initial_investment, annual_inflows = float(initial_investment), float(annual_inflows)

    # Handle invalid or zero values for any parameter
    if initial_investment <= 0 or annual_inflows <= 0:
        return HTMLResponse(content="<span>Payback period can't be calculated if values are invalid or zero.</span>")

    # Calculate the Payback Period
    payback_period = initial_investment / annual_inflows

    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>{payback_period:,.2f}</span> years</span>")


@app.post("/calculate-profit-margin/", response_class=HTMLResponse)
async def calculate_profit_margin(revenue: int = Form(0), net_profit: int = Form(0)):
    # Default inputs to zero if they are None or invalid
    revenue, net_profit = float(revenue), float(net_profit)

    # Handle invalid or zero values for any parameter
    if revenue <= 0 or net_profit < 0:
        return HTMLResponse(content="<span>Please make sure all values are positive and greater than zero.</span>")

    # Calculate the Profit Margin
    profit_margin = (net_profit / revenue) * 100

    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>{profit_margin:,.2f}</span> %</span>")


@app.post("/calculate-savings-interest/", response_class=HTMLResponse)
async def calculate_savings_interest(
        principal: int = Form(0), monthly_contrib: int = Form(0), annual_rate: int = Form(0), time: int = Form(0),
        frequency: int = Form(1)
):
    # Default inputs to zero if they are None
    principal, monthly_contrib, annual_rate, time, frequency = (
        float(principal), float(monthly_contrib), float(annual_rate) / 100, float(time), int(frequency)
    )

    # Calculate total amount using the formula
    if annual_rate > 0 and time > 0:
        amount = principal * (1 + annual_rate / frequency) ** (frequency * time) + \
                 (monthly_contrib * ((1 + annual_rate / frequency) ** (frequency * time) - 1)) / (
                         annual_rate / frequency)
    else:
        amount = principal + monthly_contrib * time  # No interest if the rate is 0

    # Return the result
    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>R {amount:,.2f}</span> per year</span>")


@app.post("/calculate-simple-interest/", response_class=HTMLResponse)
async def calculate_simple_interest(principal: int = Form(0), rate: int = Form(0), time: int = Form(0)):
    # Set default values if any input is None
    principal, rate, time = float(principal), float(rate), float(time)

    # Calculate simple interest
    simple_interest = (principal * rate * time) / 100

    # Return only the formatted numerical result
    return HTMLResponse(content=f"<span><span class='uk-text-bolder'>R {simple_interest:,.2f}</span> per year</span>")


# SENDING EMAILS

async def send_email(name: str, sender_email: str, message: str):
    msg = MIMEMultipart()
    msg["Subject"] = "New contact from bluechip-invest.co.za"
    msg["From"] = sender_email
    msg["To"] = "blueche3j9g3@bluechip-invest.co.za"

    # Attach plain text and HTML versions
    msg.attach(MIMEText(message, "plain"))
    msg.attach(MIMEText(f"<html><body><p>{name}</p><p>{message}</p></body></html>", "html"))

    def smtp_send():
        try:
            with smtplib.SMTP_SSL("webmail.bluechip-invest.co.za", 465) as server:
                server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
                server.send_message(msg)
        except Exception as e:
            print(f"Email sending failed: {e}")  # Log errors (replace with proper logging in production)

    await asyncio.to_thread(smtp_send)


@app.post("/send-contact-form/", response_class=HTMLResponse)
async def post(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    await send_email(name, email, message)
    return HTMLResponse(content="""<article class="uk-article">
    <h1 class="uk-article-title">We look forward to the journey ahead!</h1>
    <p class="uk-article-meta">Your message has been sent</p>
    <p class="uk-text-lead">Thank you for reaching out to Blue Chip Investments! We appreciate your interest and the 
    opportunity to help you navigate the world of smart investing.</p>
    </article>""")


# LOGGED IN USER

@app.get("/login/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="administrative/login.html")


@app.get("/admin/", response_class=HTMLResponse)
async def admin(request: Request):
    profile_data = {
        "profile_picture_url": request.cookies.get("profile_picture_url"),
        "first_name": request.cookies.get("first_name"),
        "last_name": request.cookies.get("last_name"),
        "email": request.cookies.get("email")
    }
    return templates.TemplateResponse(request=request, name="admin.html", context=profile_data)


@app.get("/client/", response_class=HTMLResponse)
async def client(request: Request):
    profile_data = {
        "profile_picture_url": request.cookies.get("profile_picture_url"),
        "first_name": request.cookies.get("first_name"),
        "last_name": request.cookies.get("last_name"),
        "email": request.cookies.get("email")
    }
    return templates.TemplateResponse(request=request, name="client.html", context=profile_data)


# LOGON

@app.get("/sign_out/")
async def sign_out(response: Response):
    supabase_admin.auth.sign_out()
    response.delete_cookie("profile_picture_url")
    response.delete_cookie("first_name")
    response.delete_cookie("last_name")
    response.delete_cookie("profile_type")
    response.delete_cookie("email")
    response.delete_cookie("access_token")

    return RedirectResponse("/")


@app.post("/request_otp/", response_class=HTMLResponse)
async def request_otp(email: str = Form(...)):
    response = supabase_admin.auth.sign_in_with_otp({"email": email, "options": {"should_create_user": False}})

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


@app.post("/verify_otp/", response_class=HTMLResponse)
async def verify_otp(response: Response, sent_email: str = Form(...), sent_code: str = Form(...)):
    auth_response = supabase_admin.auth.verify_otp({"email": sent_email, "token": sent_code, "type": "email"})

    if auth_response and auth_response.user:
        profile_response = supabase_.table("profiles").select("*").eq("id", auth_response.user.id).single().execute()
        profile = profile_response.data[0]
        response.set_cookie(key="profile_picture_url", value=profile['profile_picture_url'])
        response.set_cookie(key="first_name", value=profile['first_name'])
        response.set_cookie(key="last_name", value=profile['last_name'])
        response.set_cookie(key="profile_type", value=profile['profile_type'])
        response.set_cookie(key="email", value=profile['email'])
        response.set_cookie(key="access_token", value=auth_response.session.access_token, httponly=True, secure=True)

        return RedirectResponse("/admin/") if profile["profile_type"] == "admin" else RedirectResponse("/client/")
    else:
        RedirectResponse("/login/")


# PROFILES Routes

@app.post("/update_profile/", response_class=HTMLResponse)
def update_profile(
        profile_id: str = Form(...), profile_picture_url: str = Form(...), first_name: str = Form(...),
        last_name: str = Form(...)
):
    update_data = {}
    if profile_picture_url is not None:
        update_data["profile_picture_url"] = profile_picture_url
    if first_name is not None:
        update_data["first_name"] = first_name
    if last_name is not None:
        update_data["last_name"] = last_name

    response = supabase_.table("profiles").update(update_data).eq("id", profile_id).execute()
    if response.error:
        return HTMLResponse(content=f"""<p>Failed to update profile: {response.error_message}</p>""")
    if response.data:
        return HTMLResponse(content=f"""<p>Profile updated successfully.</p>""")


@app.post("/send_invite/", response_class=HTMLResponse)
def send_invite(email: str = Form(...)):
    response = supabase_admin.auth.admin.invite_user_by_email(email)
    if response and response.user:
        return HTMLResponse(content=f"""<p>Invite sent to {response.user.email}</p>""")
    else:
        return HTMLResponse(content=f"""<p>Error sending invite: {response["error"]["message"]}</p>""")
