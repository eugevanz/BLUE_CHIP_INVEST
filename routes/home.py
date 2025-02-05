from fastapi import APIRouter
from fastapi.responses import HTMLResponse
router = APIRouter()

@router.get("/home/", response_class=HTMLResponse)
async def get():
    return HTMLResponse(content="""<div class="uk-animation-fade">
        <div class="uk-background-bottom-right uk-background-cover header-image">
            <div class="uk-container">
                <div class="uk-child-width-1-2@s uk-flex-right" uk-grid>
                    <div class="uk-flex" style="min-height: max(0px, 60vh);" uk-height-viewport="offset-bottom: 40">
                        <div class="uk-card uk-card-body uk-margin-auto-vertical">
                            <h1 class="uk-text-bolder uk-width-medium">Get a clear path to your financial goals.</h1>
                            <p>Our Wealth Activating team can help you</p>
                            <a class="uk-button uk-button-small uk-light" href="/contact-us/"
                               style="background-color: #091235;">Get Started</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    
        <div class="uk-height-match uk-grid-collapse" uk-grid>
            <div class="uk-width-2-5@m" style="background-color: #091235;">
                <div class="uk-card uk-card-body uk-light uk-float-right">
                    <h2 class="uk-text-bolder">
                        Planning objective<br><span class="uk-light">financial advice</span>
                    </h2>
                    <a class="uk-button uk-button-text" href="/services/">View All</a>
                </div>
            </div>
            <div class="uk-width-expand" style="color: #36454F; background-color: #88A9C3">
                <div class="uk-flex-middle" uk-grid>
                    {% for item in ctas %}
                    <div class="uk-width-medium@m">
                        <div class="uk-card uk-card-body">
                            <img height="40" src="{{ item.icon }}" uk-svg width="40">
                            <div class="uk-text-bolder uk-margin-small-top">{{ item.title }}</div>
                            <div class="uk-text-small">{{ item.subtitle }}</div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    
        <div class="uk-container uk-margin-xlarge-top advisor-section" id="advisor-section">
            <div class="uk-child-width-1-2@s uk-child-width-1-3@m uk-grid-small uk-grid uk-flex-top uk-flex-wrap-top"
                 style="height: 627px;" uk-grid="masonry: pack">
                <div class="uk-visible@s">
                    <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                         style="height: 100px; background-image: url({{ url_for('static', path='redd-f-5U_28ojjgms-unsplash_10_11zon-grayscale.webp') }});"></div>
                </div>
                <div class="uk-visible@s">
                    <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                         style="height: 150px; background-image: url({{ url_for('static', path='santi-vedri-O5EMzfdxedg-unsplash_11_11zon-grayscale.webp') }});"></div>
                </div>
                <div class="uk-visible@s">
                    <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                         style="height: 300px; background-image: url({{ url_for('static', path='youssef-naddam-iJ2IG8ckCpA-unsplash_15_11zon-grayscale.webp') }});"></div>
                </div>
                <div class="uk-visible@s">
                    <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                         style="height: 120px; background-image: url({{ url_for('static', path='jakub-zerdzicki-eGI0aGwuE-A-unsplash_29_11zon-grayscale.webp') }});"></div>
                </div>
                <div class="uk-visible@s">
                    <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                         style="height: 180px; background-image: url({{ url_for('static', path='nandhu-kumar-5NGTf4oD8RA-unsplash_8_11zon-grayscale.webp') }});"></div>
                </div>
                <div class="uk-visible@s">
                    <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                         style="height: 140px; background-image: url({{ url_for('static', path='charlesdeluvio-Lks7vei-eAg-unsplash_24_11zon-grayscale.webp') }});"></div>
                </div>
                <div>
                    <div class="uk-card uk-card-body">
                        <h2 class="uk-text-bolder">
                            <span style="color: #88A9C3;">We Help</span> financial<br>
                            <span>Advisors that</span><br>
                            <span>exclusively serve.</span>
                        </h2>
                        <img height="40" src="{{ url_for('static', path='icons/handshake-regular.svg') }}"
                             style="color: #88A9C3"
                             uk-svg width="40">
                        <p class="uk-width-medium">
                            We empower financial advisors dedicated to serving a select clientele
                        </p>
                        <a class="uk-button uk-button-text" href="/advisors/">Read More</a>
                    </div>
                </div>
            </div>
        </div>
    
        <div class="uk-container serve-section">
            <div class="uk-card uk-card-body uk-margin-auto-vertical">
                <h2 class="uk-text-bolder">
                    <span style="color: #88A9C3;">Who</span>
                    <span> We Serve</span>
                    <hr class="uk-width-small" style="height: 0px; border: none; border-top: 2px solid; color: #88A9C3;">
                </h2>
                <p class="uk-width-medium">Focused support for financial advisors with a unique clientele.</p>
            </div>
            <div class="uk-child-width-1-5@m uk-child-width-1-3@s uk-margin-medium-top uk-grid-collapse"
                 uk-grid>
                {% for item in whoweserve %}
                <div>
                    <div class="uk-card uk-card-small">
                        <div class="uk-background-cover"
                             style="height: 240px; background-image: url('{{ item.img }}'); mask-image: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0));">
                            <img class="uk-margin-left uk-margin-top" height="40" src="{{ item.icon }}"
                                 style="color: #FC8C3A" uk-svg width="40">
                        </div>
                        <h3 class="uk-text-bolder uk-position-bottom"
                            style="padding: 20px; padding-bottom: 38px; line-height: 24px; color: #88A9C3;">
                            {{ item.name }}</h3>
                        <div class="uk-card-body">
                            <a class="uk-button uk-button-text" href="/who-we-serve/#{{ item.id }}">Read More</a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    
        <div class="uk-section uk-section-large">
            <div class="uk-container">
                <div class="uk-grid-divider uk-child-width-expand@s" uk-grid>
                    <div class="uk-text-center">
                        <div class="uk-heading-small"
                             style="font-family: 'Playfair Display SC', serif; font-weight: 700; font-style: normal;">R142M
                        </div>
                        <div class="uk-text-small">Assets Under Management</div>
                    </div>
                    <div class="uk-text-center">
                        <div class="uk-heading-small"
                             style="font-family: 'Playfair Display SC', serif; font-weight: 700; font-style: normal;">6
                        </div>
                        <div class="uk-text-small">Office Locations in RSA</div>
                    </div>
                    <div class="uk-text-center">
                        <div class="uk-heading-small"
                             style="font-family: 'Playfair Display SC', serif; font-weight: 700; font-style: normal;">2019
                        </div>
                        <div class="uk-text-small">Year founded company</div>
                    </div>
                    <div class="uk-text-center">
                        <div class="uk-heading-small"
                             style="font-family: 'Playfair Display SC', serif; font-weight: 700; font-style: normal;">1,097
                        </div>
                        <div class="uk-text-small">Clients represented through our firm</div>
                    </div>
                </div>
            </div>
        </div>
    
        <div class="uk-container" style="position: relative;">
            <div class="uk-height-large uk-background-cover uk-background-center-center"
                 style="background-image: url({{ url_for('static', path='scott-webb-hDyO6rr3kqk-unsplash_12_11zon-grayscale.webp') }});"></div>
            <div class="uk-card uk-card-body uk-overlay" style="position: absolute; bottom: 0px;">
                <h1 class="uk-text-bolder uk-width-1-2" style="color: #2A3A58;">Preserve and Grow Your Financial Legacy</h1>
                <a class="uk-button uk-light" href="/contact-us/" style="background-color: #091235;">Contact Us</a>
            </div>
        </div>
    
        <div class="uk-section uk-section-xlarge">
            <div class="uk-container">
                <div class="uk-grid-match uk-text-center" uk-grid>
                    <div class="uk-width-1-2@m">
                        <div class="uk-card uk-card-body uk-margin-auto-vertical uk-text-left uk-light"
                             style="background-color: #091235;">
                            <h2 class="uk-text-bolder">
                                <span style="color: #88A9C3;">What</span> We Do
                                <hr class="uk-width-small"
                                    style="height: 0px; border: none; border-top: 2px solid; color: #88A9C3;">
                            </h2>
                            <p class="uk-width-medium uk-light">Providing tailored solutions for financial advisors to
                                elevate client success.</p>
                            <a class="uk-button uk-button-text" href="/services/">View All</a>
                        </div>
                    </div>
                    {% for item in whatwedo %}
                    <div class="uk-width-1-4@m uk-width-1-2@s">
                        <div class="uk-card uk-card-default uk-card-body">
                            <img height="40" src="{{ item.icon }}" style="color: #88A9C3;" uk-svg width="40">
                            <p class="uk-text-bolder">{{ item.title }}</p>
                            <div class="uk-text-small">{{ item.subtitle }}</div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    
        <div class="uk-section uk-light" style="background-color: #091235;">
            <div class="uk-container">
                <div class="uk-card uk-card-body uk-text-center">
                    <div class="uk-text-small uk-text-bolder uk-light">WHAT OUR CUSTOMERS SAY</div>
                    <h2 class="uk-text-bolder uk-margin-remove-top">
                        <span style="color: #88A9C3;">Our</span> Testimonials
                    </h2>
                </div>
                <div class="uk-grid-match uk-child-width-expand@m" uk-grid>
                    {% for item in testimonials %}
                    <div>
                        <div class="uk-card uk-card-default uk-card-body uk-inline">
                            <div>
                                {% for star in range(5) %}
                                <img class="uk-text-warning" height="24"
                                     src="{{ url_for('static', path='icons/star-regular.svg') }}" uk-svg width="24">
                                {% endfor %}
                            </div>
                            <p class="uk-text-italic uk-margin-xlarge-bottom">
                                <span class="uk-text-bolder">{{ item.header }}</span><br>{{ item.body }}
                            </p>
                            <div class="uk-grid-small uk-position-bottom-left uk-padding" uk-grid>
                                <div class="uk-width-auto">
                                    <img class="uk-border-circle" height="64" src="{{ item.img }}" width="64">
                                </div>
                                <div class="uk-margin-auto-vertical">
                                    <div class="uk-text-bolder">{{ item.name }}</div>
                                    <div class="uk-text-small">{{ item.title }}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    
        <div class="uk-section uk-section-xlarge">
            <div class="uk-container">
                <div class="uk-grid-match uk-child-width-expand@s" uk-grid>
                    <div>
                        <div class="uk-card uk-card-body">
                            <h2 class="uk-text-bolder">
                                <span style="color: #88A9C3;">Personal</span> Finance Guides
                                <hr class="uk-width-small"
                                    style="height: 0px; border: none; border-top: 2px solid; color: #88A9C3;">
                            </h2>
                            <a class="uk-button uk-button-text" href="/guides/">Read Our Blog</a>
                        </div>
                        <div class="uk-card uk-card-body">
                            <h5 class="uk-text-bolder">Most Popular</h5>
                            <ul class="uk-list uk-list-disc uk-text-small" style="color: #88A9C3;">
                                <li><a class="uk-link-muted" href="/guides/">What are Portfolio Accounting
                                    Systems</a></li>
                                <li><a class="uk-link-muted" href="/guides/">Investing Basics for New
                                    Grads</a></li>
                                <li><a class="uk-link-muted" href="/guides/">What is the Average Net Worth by
                                    Age</a></li>
                                <li><a class="uk-link-muted" href="/guides/">Wealth Management vs. Investment
                                    Banking</a></li>
                                <li><a class="uk-link-muted" href="/guides/">2024's Best Provinces to Retire
                                    in South Africa</a></li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-small uk-card-body">
                            <div class="uk-background-cover"
                                 style="height: 320px; background-image: url('{{ url_for('static', path='krzysztof-hepner-o_x11ORH9vQ-unsplash_4_11zon-grayscale.webp') }}');"></div>
                            <div class="uk-card-body">
                                <h4 class="uk-card-title uk-text-bolder">How to Achieve True Wealth</h4>
                                <p class="uk-text-small">Unlocking true wealth involves strategic planning, smart
                                    investments, and a holistic approach to managing your financial resources.
                                    Discover the steps to build and sustain genuine financial prosperity.</p>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-small uk-card-body">
                            <div class="uk-background-cover"
                                 style="height: 320px; background-image: url('{{ url_for('static', path='pedro-miranda-3QzMBrvCeyQ-unsplash_9_11zon-grayscale.webp') }}');"></div>
                            <div class="uk-card-body">
                                <h4 class="uk-card-title uk-text-bolder">Step Focused Planning</h4>
                                <p class="uk-text-small">Achieve your financial goals with step-by-step, focused
                                    planning that guides you through every stage of wealth building and
                                    preservation.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>""")
