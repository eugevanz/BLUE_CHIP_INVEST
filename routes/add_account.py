from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/add_account", response_class=HTMLResponse)
async def about():
    # Return a part of the page, with an image from the static folder
    return HTMLResponse(content="""<div class="uk-section uk-section-small">
        <div class="uk-container">
            <div class="uk-child-width-1-2@m" data-uk-grid="masonry: pack">
                <!-- Account Setup Form -->
                <div class="uk-card uk-card-body uk-margin-large-bottom">
                    <h3>Add Account</h3>
                    <p class="uk-text-meta">
                        Adding an account involves setting up a record to track financial data specific
                        to a client’s finances. This includes creating a unique account name, like “Savings” or
                        “Investment,”
                        and specifying the type of account, such as “Checking,” “Loan,” or “Retirement.”
                    </p>
    
                    <!-- Account Type Dropdown -->
                    <div class="uk-margin">
                        <div class="uk-text-small">Account Type</div>
                        <select class="uk-select uk-text-bolder uk-margin-remove-top" id="account_type">
                            <option value="Savings Account">Savings Account</option>
                            <option value="Investment Account">Investment Account</option>
                            <option value="Retirement Account">Retirement Account</option>
                            <option value="Brokerage Account">Brokerage Account</option>
                            <option value="Trust Account">Trust Account</option>
                            <option value="Custodial Account">Custodial Account</option>
                            <option value="Taxable Account">Taxable Account</option>
                            <option value="Tax-Deferred Account">Tax-Deferred Account</option>
                            <option value="Tax-Exempt Account">Tax-Exempt Account</option>
                            <option value="Money Market Account">Money Market Account</option>
                            <option value="Certificate of Deposit (CD) Account">Certificate of Deposit (CD) Account
                            </option>
                            <option value="Mutual Fund Account">Mutual Fund Account</option>
                            <option value="Pension Account">Pension Account</option>
                            <option value="Self-Directed Investment Account">Self-Directed Investment Account</option>
                            <option value="High-Yield Savings Account">High-Yield Savings Account</option>
                            <option value="Fixed-Income Account">Fixed-Income Account</option>
                            <option value="Annuity Account">Annuity Account</option>
                            <option value="Forex Trading Account">Forex Trading Account</option>
                            <option value="Commodities Trading Account">Commodities Trading Account</option>
                        </select>
                    </div>
    
                    <!-- Account Number Input -->
                    <div class="uk-margin">
                        <div class="uk-text-small">Account Number</div>
                        <div class="uk-inline">
                            <span class="uk-form-icon" data-uk-icon="icon: hashtag"></span>
                            <input class="uk-input uk-text-bolder uk-form-width-large" id="account_number"
                                   placeholder="Account Number" type="text">
                        </div>
                    </div>
    
                    <!-- Balance Input -->
                    <div class="uk-margin">
                        <div class="uk-text-small">Balance</div>
                        <div class="uk-inline">
                            <span class="uk-form-icon" data-uk-icon="icon: bag"></span>
                            <input class="uk-input uk-text-bolder uk-form-width-large" id="balance"
                                   placeholder="Balance" type="number">
                        </div>
                    </div>
    
                    <!-- Save Button -->
                    <button class="uk-button uk-button-primary uk-margin" id="add-acc-btn">Save</button>
                </div>
    
                <!-- Dynamic Content Sections -->
                <div id="account_performance">
                    <!-- Account performance content (dynamically filled) -->
                </div>
                <div id="dividend_performance">
                    <!-- Dividend performance content (dynamically filled) -->
                </div>
                <div id="investment_performance">
                    <!-- Investment performance content (dynamically filled) -->
                </div>
                <div id="client_goal_performance">
                    <!-- Client goal performance content (dynamically filled) -->
                </div>
                <div id="transaction_performance">
                    <!-- Transaction performance content (dynamically filled) -->
                </div>
            </div>
        </div>
    </div>""")