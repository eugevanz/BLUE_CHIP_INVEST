from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/login/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(content=f"""<div class="uk-grid-collapse uk-child-width-1-2@m" uk-grid="true">
        <!-- Background image section -->
        <div class="uk-background-cover uk-visible@m header-image"
             style="background-image: url(/static/marten-bjork-6dW3xyQvcYE-unsplash_6_11zon-grayscale.webp);"
             uk-height-viewport="true">
        </div>
    
        <!-- Main content section -->
        <div class="uk-padding-large">
            <div class="uk-margin-large">
                <img height="128" src="/static/icons/blue-keys.svg"
                     style="fill: none; color: #091235" uk-svg width="128">
                <div class="uk-heading-small uk-margin-small uk-width-medium logo-text" style="line-height: 50px;">
                    BLUE CHIP INVESTMENTS
                </div>
                <div class="uk-text-small">Building Your Legacy with Trusted Growth</div>
            </div>
    
            <!-- Email Input Section -->
            <form class="uk-margin" hx-post="/request_otp/">
                <h3 class="uk-card-title uk-text-bolder uk-margin-remove-bottom">Welcome Back</h3>
                <p class="uk-text-small uk-margin-remove-top" style="color: #091235;">
                    Please enter your <strong>email address</strong> to log in. A magic link will be sent to your email,
                    allowing you to securely access your account.
                </p>
                <div class="uk-text-small">Email</div>
                <div class="uk-inline">
                    <span class="uk-form-icon" uk-icon="icon: mail"></span>
                    <input class="uk-input uk-form-width-large" name="email" type="email" required>
                </div>
                <p class="uk-text-meta">Please enter your email and click Send Code.</p>
                <button class="uk-button uk-button-large uk-light" type="submit" style="background-color: #091235;">
                    Send Code
                </button>
            </form>
    
            <p id="send_code_notifications"></p>
        </div>
    </div>""")