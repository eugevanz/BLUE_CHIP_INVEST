from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from database import StoreSession

router = APIRouter()


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
        return HTMLResponse(content="""<div class="uk-section uk-section-small">
            <div class="uk-container">
                <div class="uk-child-width-1-4@m uk-grid-small uk-grid-match" uk-grid="true">
                    <div>
                        <div class="admin-menu">
                        </div>
                    </div>
    
                    <div>
                        <div class="market-performance">
                        </div>
                    </div>
    
                    <div>
                        <div class="performance-summary uk-width-1-2@m">
                        </div>
                    </div>
    
                    <div>
                        <div class="portfolio-performance uk-width-1-2@m">
                        </div>
                    </div>
    
                    <div>
                        <div class="asset-performance uk-width-2-3@m">
                        </div>
                    </div>
    
                    <div>
                        <div class="client-insights uk-width-1-3@m">
                        </div>
                    </div>
                </div>
            </div>
        </div>""")
    else:
        return RedirectResponse("/login/", status_code=302)
