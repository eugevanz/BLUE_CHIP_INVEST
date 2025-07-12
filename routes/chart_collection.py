import json
from collections import defaultdict
from datetime import datetime, timedelta

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import yfinance as yf
from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter()

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
    config=dict(displayModeBar=False, scrollZoom=False), full_html=False,
    post_script="""window.addEventListener("load", function() {
        setTimeout(function() {
            var plotDiv = document.getElementById("{plot_id}"); 
            if (plotDiv) { Plotly.Plots.resize(plotDiv); }
        }, 100);
    });"""
)


@router.get("/market-performance/", response_class=HTMLResponse)
async def market_performance(ticker_symbol: str = Query("AAPL")):
    stock_options = {
        "AAPL": "Apple (AAPL)",
        "TSLA": "Tesla (TSLA)",
        "GOOG": "Google (GOOGL)",
        "AMZN": "Amazon (AMZN)",
        "MSFT": "Microsoft (MSFT)"
    }
    options_html = "".join([
        f"""<option value="{ticker}" {"selected" if ticker == ticker_symbol else ""}>{name}</option>"""
        for ticker, name in stock_options.items()
    ])

    df = yf.download(list(stock_options.keys()), start=(datetime.today() - timedelta(days=30)), end=datetime.today())
    trace = go.Candlestick(
        x=df.index, open=df[('Open', ticker_symbol)], high=df[('High', ticker_symbol)], low=df[('Low', ticker_symbol)],
        close=df[('Close', ticker_symbol)]
    )

    markets = [
        {"ticker_symbol": name, "current_close": f"R {df['Close'][ticker].iloc[-1]:,.2f}",
         "change": f"{(df['Close'][ticker].iloc[-1] - df['Close'][ticker].iloc[-2]):,.2f}"}
        for ticker, name in stock_options.items()
    ]
    markets_html = "".join([
        f"""
            <div>
                <div class="uk-card uk-card-body uk-card-small">
                    <div class="uk-text-meta">{item['ticker_symbol']}</div>
                    <div class="uk-text-bold">{item['current_close']}</div>
                    <div class="uk-text-meta">
                        <strong class="{'uk-text-success' if float(item['change']) > 0 else 'uk-text-danger'}"
                        >{item['change']}%</strong>
                    </div>
                </div>
            </div>
            """
        for item in markets
    ])

    highest_high = df['High'][ticker_symbol].max()
    lowest_low = df['Low'][ticker_symbol].min()
    midpoint = (highest_high + lowest_low) / 2

    current_price = df['Close'][ticker_symbol].iloc[-1]
    previous_close = df['Close'][ticker_symbol].iloc[-2]
    price_change = current_price - previous_close
    percentage_change = (price_change / previous_close) * 100 if previous_close != 0 else 0

    market_layout = go.Layout(
        xaxis=dict(gridcolor="lightgray", rangeslider=dict(visible=False), tickformat="%d/%m"),
        yaxis=dict(gridcolor="lightgray", showticklabels=False), margin=dict(t=0, b=0, l=0, r=0),
        plot_bgcolor="white", height=450
    )
    fig = go.Figure(data=[trace], layout=market_layout)
    return HTMLResponse(content=f"""<div class="uk-card uk-card-body uk-width-1-1 uk-card-small" id="market-container">
            <div>
                <div class="uk-text-bold">Market Performance</div>
                <div class="uk-text-large uk-text-bold">{current_price:,.2f}</div>
                <div class="uk-text-meta">
                    Compared to previous price | 
                    <strong class="{'uk-text-success' if percentage_change > 0 else 'uk-text-danger'}">
                        {percentage_change:,.2f}%
                    </strong>
                </div>
            </div>
            <hr class="uk-margin-small-top">
            <form class="uk-align-right">
                <select aria-label="Select" class="uk-select uk-form-small uk-form-width-medium" name="ticker_symbol"
                hx-get="/market-performance/" hx-target="#market-container" hx-trigger="change" hx-swap="outerHTML"
                >{options_html}</select>
            </form>
            <div class="uk-grid-match uk-grid-divider uk-grid-small uk-margin" uk-grid>
                <div class="uk-width-auto">
                    <div class="uk-flex uk-flex-between uk-flex-column">
                        <div class="uk-text-meta">R {highest_high:,.2f}</div>
                        <div class="uk-text-meta">R {midpoint:,.2f}</div>
                        <div class="uk-text-meta uk-margin-medium-bottom">R {lowest_low:,.2f}</div>
                    </div>
                </div>
                <div class="uk-width-expand">
                    {pio.to_html(fig, **common_html_config)}
                    <hr class="uk-margin-small-top">
                    <div uk-slider>
                        <div class="uk-slider-items uk-child-width-1-2@s uk-child-width-1-4@m uk-grid">
                            {markets_html}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """)


@router.get("/inv-performance/", response_class=HTMLResponse)
async def inv_performance(inv_data: list):
    df = pd.DataFrame(inv_data)
    df["created_at"] = pd.to_datetime(df["created_at"])
    grouped = df.groupby("investment_type")["current_price"].sum().reset_index()
    trace = [go.Bar(x=grouped["investment_type"], y=grouped["current_price"])]
    fig = go.Figure(data=trace, layout=go_layout)
    return pio.to_html(fig, **common_html_config)


@router.get("/goal-performance/", response_class=HTMLResponse)
async def goal_performance(goals_data: list):
    df = pd.DataFrame(goals_data)
    trace = [
        go.Bar(name="Current Savings", x=df["goal_type"], y=df["current_savings"]),
        go.Bar(name="Target Amount", x=df["goal_type"], y=df["target_amount"])
    ]
    fig = go.Figure(data=trace, layout=go_layout)
    fig.update_layout(barmode="stack")
    return pio.to_html(fig, **common_html_config)


@router.get("/dividend-performance/", response_class=HTMLResponse)
async def dividend_performance(request: Request):
    account_ids = json.loads(request.cookies.get("account_ids"))
    dividends_and_payouts = request.app.state.supabase_.table("dividends_and_payouts").select("*").in_(
        "account_id", [item["id"] for item in account_ids]
    ).execute()

    df = pd.DataFrame(dividends_and_payouts.data)
    df["payment_date"] = pd.to_datetime(df["payment_date"])
    df = df.sort_values(by="payment_date")
    df["cumulative_payout"] = df["amount"].cumsum()
    trace = go.Scatter(x=df["payment_date"], y=df["cumulative_payout"], fill="tozeroy", mode="lines+markers",
                       line=dict(color="blue", width=6, shape="spline"), fillcolor="rgba(0, 0, 255, 0.2)",
                       marker=dict(color="blue", size=10))
    fig = go.Figure(data=[trace], layout=go_layout)
    print(dividends_and_payouts.data)

    table_html = "".join([f"""<tr>
        <td>R <strong>{item["amount"]:,.2f}</strong></td>
        <td>{item["payment_date"]}</td>
    </tr>""" for item in dividends_and_payouts.data])
    html_content = f"""<div class="uk-card uk-card-body uk-width-1-1 uk-card-small">
            <div class="uk-text-bold">Dividend/Payout Performance</div>
            <div class="uk-text-large uk-text-bold">School fees</div>
            <div class="uk-text-meta">Compared to last month | <span class="uk-text-bold">2.4</span>%</div>
            <hr class="uk-margin-small-top">
            <div class="uk-flex">
                <div class="uk-grid-match uk-grid-divider uk-grid-small uk-width-1-2@m uk-margin-right" uk-grid>
                    <div class="uk-width-auto">
                        <div class="uk-flex uk-flex-between uk-flex-column">
                            <div class="uk-text-meta">R 1M</div>
                            <div class="uk-text-meta">R 500K</div>
                            <div class="uk-text-meta uk-margin-medium-bottom">R 10K</div>
                        </div>
                    </div>
                    <div class="uk-width-expand">
                        {pio.to_html(fig, **common_html_config)}
                        <hr class="uk-margin-small-top">
                    </div>
                </div>
                <div class="uk-width-1-2@m uk-overflow-auto">
                    <table class="uk-table uk-table-divider">
                        <thead>
                        <tr>
                            <th>Amount</th>
                            <th>Payment Date</th>
                        </tr>
                        </thead>
                        <tbody>
                        {table_html}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>"""
    return HTMLResponse(content=html_content)


@router.get("/account-performance/", response_class=HTMLResponse)
async def account_performance(request: Request):
    user_id = request.cookies.get("user_id")
    if user_id:
        accounts = request.app.state.supabase_.table("accounts").select("*").eq("profile_id", user_id).execute()

        df = pd.DataFrame(accounts.data)
        df["created_at"] = pd.to_datetime(df["created_at"])
        fig = px.scatter(df, x="created_at", y="balance", size="balance", color="account_type",
                         hover_name="account_number", size_max=60)

        account_totals = defaultdict(float)
        for entry in accounts.data:
            account_totals[entry["account_type"]] += entry["balance"]
        legend_html = "".join([f"""<span>
            <img height="10" src="/static/icons/circle-solid.svg" style="color: green" uk-svg width="10">
            R{"{:,.2f}".format(balance)} {account_type}
        </span>""" for account_type, balance in account_totals.items()])

        table_html = "".join([f"""<tr>
            <td>{item["account_number"]}</td>
            <td>{item["account_type"]}</td>
            <td>R <strong>{item["balance"]:,.2f}</strong></td>
        </tr>""" for item in accounts.data])

        fig.update_layout(**px_layout)
        html_content = f"""<div class="uk-card uk-card-body uk-width-1-1 uk-card-small">
            <div class="uk-text-bold">Account Performance</div>
            <div class="uk-text-large uk-text-bold">School fees</div>
            <div class="uk-text-meta">Compared to last month | <span class="uk-text-bold">2.4</span>%</div>
            <hr class="uk-margin-small-top">
            <div class="uk-flex">
                <div class="uk-grid-match uk-grid-divider uk-grid-small uk-width-1-2@m uk-margin-right" uk-grid>
                    <div class="uk-width-auto">
                        <div class="uk-flex uk-flex-between uk-flex-column">
                            <div class="uk-text-meta">R 1M</div>
                            <div class="uk-text-meta">R 500K</div>
                            <div class="uk-text-meta uk-margin-medium-bottom">R 10K</div>
                        </div>
                    </div>
                    <div class="uk-width-expand">
                        {pio.to_html(fig, **common_html_config)}
                        <hr class="uk-margin-small-top">
                        {legend_html}
                    </div>
                </div>
                <div class="uk-width-1-2@m uk-overflow-auto">
                    <table class="uk-table uk-table-divider">
                        <thead>
                        <tr>
                            <th>Account</th>
                            <th>Type</th>
                            <th>Balance</th>
                        </tr>
                        </thead>
                        <tbody>
                        {table_html}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>"""
        return HTMLResponse(content=html_content)
    else:
        return RedirectResponse("/login/", status_code=302)
