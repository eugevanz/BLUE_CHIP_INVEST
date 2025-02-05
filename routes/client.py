from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/client/", response_class=HTMLResponse)
async def client(request: Request):
    profile_data = {
        "profile_picture_url": request.cookies.get("profile_picture_url"),
        "first_name": request.cookies.get("first_name"),
        "last_name": request.cookies.get("last_name"),
        "email": request.cookies.get("email")
    }
    return HTMLResponse(content="""<div class="uk-section uk-section-small">
        <div class="uk-container">
            <div class="uk-child-width-1-3@m uk-grid-small uk-padding-small uk-grid-match" data-uk-grid="true">
                <div>
                    <div class="client-menu">
                    </div>
                </div>

                <div>
                    <div class="market-performance">
                    </div>
                </div>

                <div>
                    <div class="performance-summary">
                    </div>
                </div>

                <div>
                    <div id="account_performance">
                    </div>
                </div>

                <div>
                    <div id="dividend_performance">
                    </div>
                </div>

                <div>
                    <div id="client_goal_performance">
                    </div>
                </div>

                <div>
                    <div id="investment_performance">
                    </div>
                </div>

                <div>
                    <div id="transaction_performance">
                    </div>
                </div>
            </div>
        </div>
    </div>""")