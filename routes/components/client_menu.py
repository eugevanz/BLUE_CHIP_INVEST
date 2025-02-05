from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/client_menu", response_class=HTMLResponse)
async def about():
    # Return a part of the page, with an image from the static folder
    return HTMLResponse(content="""<div class="uk-card" style="width: 20%;">
        <!-- Stores for profile data -->
        <div id="profile_picture_url"></div>
        <div id="first_name"></div>
        <div id="last_name"></div>
        <div id="email"></div>
    
        <div class="uk-card-header">
            <img alt="profile-pic" class="uk-border-circle" height="44" id="picture_url" width="44"/>
            <h3 class="uk-margin-remove-bottom uk-margin-remove-top uk-text-truncate">
                <span class="uk-text-bolder" id="profile_first_name"></span><br/>
                <span id="profile_last_name"></span>
            </h3>
            <div class="uk-text-small uk-margin-remove-top" id="profile_email"></div>
        </div>
    
        <div class="uk-card-body">
            <ul class="uk-nav uk-nav-default">
                <li>
                    <a class="uk-flex uk-flex-middle uk-link-reset" data-uk-toggle="target: #messages">
                        <span class="uk-margin-small-right" data-uk-icon="icon: mail"></span>Messages
                    </a>
                    <div data-uk-offcanvas="mode: push; overlay: true" id="messages">
                        <div class="uk-offcanvas-bar">
                            <button class="uk-offcanvas-close" data-uk-close="true"></button>
                            <h3>Messages</h3>
                            <!-- Dynamic message content will be inserted here -->
                            <div class="uk-flex uk-flex-wrap">
                                <article class="uk-article">
                                    <div data-uk-icon="icon: mail"></div>
                                    <p class="uk-article-meta">Meta info</p>
                                    <p class="uk-text-bolder">Header</p>
                                    <p>Article content</p>
                                </article>
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>""")