from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/dividend_performance", response_class=HTMLResponse)
async def about():
    # Return a part of the page, with an image from the static folder
    return HTMLResponse(content="""<div class="uk-card uk-card-default" style="background-color: custom_colours[-1];">
        <!-- Card Header -->
        <div class="uk-card-header">
            <div class="uk-text-small">Dividend/Payout performance</div>
            <span id="total_summary"></span>
            <div class="uk-text-small uk-margin-remove-top" id="card_header"></div>
        </div>

        <!-- Card Body -->
        <div class="uk-card-body">
            <div class="uk-grid-divider uk-child-width-expand uk-grid-small" data-uk-grid="true">
                <div class="uk-width-auto">
                    <div class="uk-flex uk-flex-column uk-height-medium" style="font-size: 8px;">
                        <div id="highest_"></div>
                        <div class="uk-margin-auto-vertical" id="mid_"></div>
                        <div id="lowest_"></div>
                    </div>
                </div>

                <div>
                    <!-- Graph -->
                    <div>
                        <div id="payouts_fig" style="height: 300px;"></div>
                        <hr/>
                        <div class="uk-flex uk-flex-between" id="legend" style="font-size: 8px;"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>""")