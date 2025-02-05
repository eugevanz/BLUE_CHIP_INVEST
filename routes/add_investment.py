from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/add_investment", response_class=HTMLResponse)
async def about():
    # Return a part of the page, with an image from the static folder
    return HTMLResponse(content="""<div class="uk-section uk-section-small">
        <div class="uk-container">
            <div class="uk-grid uk-child-width-1-2@m" uk-grid>
                <div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Add Investment</h3>
                        <p class="uk-text-meta">
                            Adding an investment involves recording a financial asset or contribution intended for growth, typically with specific goals or performance expectations.
                        </p>

                        <!-- Investment Start Date -->
                        <div class="uk-margin">
                            <label for="purchase_date" class="uk-text-small">Investment Start Date</label>
                            <input type="date" class="uk-input uk-width-large" id="purchase_date" value="DATE_TODAY">
                        </div>

                        <!-- Select Account -->
                        <div class="uk-margin">
                            <label for="account_id" class="uk-text-small">Select Account</label>
                            <select class="uk-select" id="account_id">
                                <!-- Dynamically generate account options -->
                                <option value="ACCOUNT_ID">Account 1</option>
                                <option value="ACCOUNT_ID_2">Account 2</option>
                            </select>
                        </div>

                        <!-- Investment Type -->
                        <div class="uk-margin">
                            <label for="investment_type" class="uk-text-small">Investment Type</label>
                            <select class="uk-select" id="investment_type">
                                <option value="Stocks">Stocks (Equities)</option>
                                <option value="Bonds">Bonds (Fixed Income)</option>
                                <option value="Mutual Funds">Mutual Funds</option>
                                <option value="ETFs">Exchange-Traded Funds (ETFs)</option>
                                <option value="Real Estate">Real Estate</option>
                                <option value="Commodities">Commodities</option>
                                <option value="Crypto">Cryptocurrency</option>
                                <option value="Private Equity">Private Equity</option>
                                <option value="Hedge Funds">Hedge Funds</option>
                                <option value="Savings">Savings Accounts & CDs</option>
                                <option value="Annuities">Annuities</option>
                                <option value="Options">Options</option>
                            </select>
                        </div>

                        <!-- Symbol -->
                        <div class="uk-margin">
                            <label for="symbol" class="uk-text-small">Symbol</label>
                            <div class="uk-inline">
                                <span class="uk-form-icon" uk-icon="icon: symbol"></span>
                                <input type="text" class="uk-input uk-form-width-large" id="symbol" placeholder="Symbol">
                            </div>
                        </div>

                        <!-- Investment Amount (Quantity) -->
                        <div class="uk-margin">
                            <label for="quantity" class="uk-text-small">Investment Amount (Quantity)</label>
                            <div class="uk-inline">
                                <span class="uk-form-icon" uk-icon="icon: cart"></span>
                                <input type="number" class="uk-input uk-form-width-large" id="quantity" placeholder="Investment Amount">
                            </div>
                        </div>

                        <!-- Investment Purchase Price -->
                        <div class="uk-margin">
                            <label for="purchase_price" class="uk-text-small">Investment Purchase Price</label>
                            <div class="uk-inline">
                                <span class="uk-form-icon" uk-icon="icon: bag"></span>
                                <input type="number" class="uk-input uk-form-width-large" id="purchase_price" placeholder="Investment Purchase Price">
                            </div>
                        </div>

                        <!-- Current Price -->
                        <div class="uk-margin">
                            <label for="current_price" class="uk-text-small">Current Price</label>
                            <div class="uk-inline">
                                <span class="uk-form-icon" uk-icon="icon: bag"></span>
                                <input type="number" class="uk-input uk-form-width-large" id="current_price" placeholder="Current Price">
                            </div>
                        </div>

                        <!-- Save Button -->
                        <button class="uk-button uk-button-primary uk-margin" id="add-inv-btn">Save</button>
                    </div>
                </div>

                <!-- Performance Metrics (Placeholder Sections) -->
                <div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Investment Performance</h3>
                        <p>Investment performance data will go here.</p>
                    </div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Account Performance</h3>
                        <p>Account performance data will go here.</p>
                    </div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Dividend Performance</h3>
                        <p>Dividend performance data will go here.</p>
                    </div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Client Goal Performance</h3>
                        <p>Client goal performance data will go here.</p>
                    </div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Transaction Performance</h3>
                        <p>Transaction performance data will go here.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>""")