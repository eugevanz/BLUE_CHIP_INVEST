from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/edit", response_class=HTMLResponse)
async def about():
    # Return a part of the page, with an image from the static folder
    return HTMLResponse(content="""<div class="uk-section uk-section-small">
        <div class="uk-container">
    
            <div class="uk-grid-small uk-child-width-1-2@m uk-padding-small" uk-grid>
    
                <div class="uk-card uk-card-body uk-margin-small-bottom">
                    <h3>Client Profile</h3>
                    <p>Client profile data goes here.</p>
                </div>
    
                <div class="uk-card uk-card-body uk-margin-small-bottom">
                    <h3>Accounts</h3>
                    <table class="uk-table uk-table-divider">
                        <thead>
                        <tr>
                            <th>Account Number</th>
                            <th>Balance</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>Account 1</td>
                            <td>$1000</td>
                        </tr>
                        <tr>
                            <td>Account 2</td>
                            <td>$1500</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
    
                <div class="uk-card uk-card-body uk-margin-small-bottom">
                    <h3>Investments</h3>
                    <table class="uk-table uk-table-divider">
                        <thead>
                        <tr>
                            <th>Investment</th>
                            <th>Value</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>Investment 1</td>
                            <td>$2000</td>
                        </tr>
                        <tr>
                            <td>Investment 2</td>
                            <td>$3000</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
    
                <div class="uk-card uk-card-body uk-margin-small-bottom">
                    <h3>Transactions</h3>
                    <table class="uk-table uk-table-divider">
                        <thead>
                        <tr>
                            <th>Transaction Date</th>
                            <th>Amount</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>01/01/2024</td>
                            <td>$500</td>
                        </tr>
                        <tr>
                            <td>02/01/2024</td>
                            <td>$300</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
    
                <div class="uk-card uk-card-body uk-margin-small-bottom">
                    <h3>Client Goals</h3>
                    <table class="uk-table uk-table-divider">
                        <thead>
                        <tr>
                            <th>Goal</th>
                            <th>Status</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>Retirement</td>
                            <td>In Progress</td>
                        </tr>
                        <tr>
                            <td>Education</td>
                            <td>Completed</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
    
                <div class="uk-card uk-card-body uk-margin-small-bottom">
                    <h3>Payouts</h3>
                    <table class="uk-table uk-table-divider">
                        <thead>
                        <tr>
                            <th>Payout Date</th>
                            <th>Amount</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>01/02/2024</td>
                            <td>$200</td>
                        </tr>
                        <tr>
                            <td>02/02/2024</td>
                            <td>$150</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
    
            </div>
        </div>
    </div>""")