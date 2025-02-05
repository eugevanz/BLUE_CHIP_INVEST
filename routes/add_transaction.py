from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/add_transaction", response_class=HTMLResponse)
async def about():
    # Return a part of the page, with an image from the static folder
    return HTMLResponse(content="""<div class="uk-section uk-section-small">
        <div class="uk-container">
            <div class="uk-grid uk-child-width-1-2@m" uk-grid>
    
                <div class="uk-card uk-card-body uk-margin-large-bottom">
                    <h3>Add Transaction</h3>
                    <p class="uk-text-meta">
                        Adding a transaction involves recording a financial event, typically either a debit (expense) or a
                        credit (income), associated with a client’s account.
                    </p>
    
                    <!-- Select Account -->
                    <div class="uk-margin">
                        <div class="uk-text-small">Select Account</div>
                        <div class="uk-text-bolder uk-margin-remove-top">
                            <select class="uk-select" id="account_id">
                                <!-- Dynamically populate account options -->
                                <option value="ACCOUNT_ID">Account 1</option>
                                <option value="ACCOUNT_ID_2">Account 2</option>
                            </select>
                        </div>
                    </div>
    
                    <!-- Transaction Type -->
                    <div class="uk-margin">
                        <div class="uk-text-small">Transaction Type</div>
                        <div class="uk-text-bolder uk-margin-remove-top">
                            <select class="uk-select" id="trans_type">
                                <option value="debit">Debit</option>
                                <option value="credit">Credit</option>
                            </select>
                        </div>
                    </div>
    
                    <!-- Description -->
                    <div class="uk-margin">
                        <div class="uk-text-small">Description</div>
                        <div class="uk-inline">
                            <span class="uk-form-icon" uk-icon="icon: info"></span>
                            <input class="uk-input uk-text-bolder uk-form-width-large" id="description" placeholder="Transaction Description"
                                   type="text">
                        </div>
                    </div>
    
                    <!-- Transaction Amount -->
                    <div class="uk-margin">
                        <div class="uk-text-small">Transaction Amount</div>
                        <div class="uk-inline">
                            <span class="uk-form-icon" uk-icon="icon: bag"></span>
                            <input class="uk-input uk-text-bolder uk-form-width-large" id="amount" placeholder="Transaction Amount"
                                   type="number">
                        </div>
                    </div>
    
                    <!-- Save Button -->
                    <button class="uk-button uk-button-primary uk-margin" id="add-tra-btn">Save</button>
                </div>
    
                <!-- Performance Metrics (Placeholder Sections) -->
                <div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Transaction Performance</h3>
                        <p>Performance data for transactions will go here.</p>
                    </div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Account Performance</h3>
                        <p>Account performance data will go here.</p>
                    </div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Dividend/Payout Performance</h3>
                        <p>Dividend and payout performance data will go here.</p>
                    </div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Investment Performance</h3>
                        <p>Investment performance data will go here.</p>
                    </div>
                    <div class="uk-card uk-card-body uk-margin-large-bottom">
                        <h3>Client Goal Performance</h3>
                        <p>Client goal performance data will go here.</p>
                    </div>
                </div>
    
            </div>
        </div>
    </div>""")