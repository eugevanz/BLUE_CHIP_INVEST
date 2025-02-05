from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/add_payout", response_class=HTMLResponse)
async def about():
    # Return a part of the page, with an image from the static folder
    return HTMLResponse(content="""<div class="uk-section uk-section-small">
        <div class="uk-container">
            <div class="uk-grid uk-child-width-1-2@m" uk-grid>

                <!-- Add Dividend/Payout Form -->
                <div class="uk-card uk-card-body uk-margin-large-bottom">
                    <h3>Add Dividend/Payout</h3>
                    <p class="uk-text-meta">
                        Adding a dividend or payout typically involves recording a financial transaction associated with an investment account to document income received from holdings like stocks or funds that distribute earnings to account holders.
                    </p>

                    <!-- Payout Date -->
                    <div class="uk-margin">
                        <div class="uk-text-small">Payout Date</div>
                        <div class="uk-inline">
                            <span class="uk-form-icon" uk-icon="icon: calendar"></span>
                            <input type="date" class="uk-input uk-width-large" id="payment_date" value="DATE_TODAY">
                        </div>
                    </div>

                    <!-- Account Selection -->
                    <div class="uk-margin">
                        <div class="uk-text-small">Account</div>
                        <select class="uk-select" id="account_id">
                            <!-- Dynamically populate account options -->
                            <option value="ACCOUNT_ID">Account 1</option>
                            <option value="ACCOUNT_ID_2">Account 2</option>
                        </select>
                    </div>

                    <!-- Amount -->
                    <div class="uk-margin">
                        <div class="uk-text-small">Amount</div>
                        <input type="number" class="uk-input uk-text-bolder uk-width-1-1" id="amount" placeholder="Amount">
                    </div>

                    <!-- Save Button -->
                    <button class="uk-button uk-button-primary uk-margin" id="add-pay-btn">Save</button>
                </div>

                <!-- Performance Metrics (Placeholder Sections) -->
                <div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Dividend/Payout Performance</h3>
                        <p>Performance data for dividends and payouts will go here.</p>
                    </div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Account Performance</h3>
                        <p>Account performance data will go here.</p>
                    </div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Investment Performance</h3>
                        <p>Investment performance data will go here.</p>
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