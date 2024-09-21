head = '''<head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit-icons.min.js"></script>
        <script src="https://unpkg.com/hyperscript.org@0.9.12"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/css/uikit.min.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display+SC:ital,wght@0,700;0,900;1,700&amp;display=swap">
        <title>Blue Chip Invest</title>
    </head>'''




nav = f'''<nav class="uk-navbar-container">
            <div class="uk-container">
                <div class="uk-navbar" uk-navbar="mode: click; target: !.uk-navbar; align: center">
                    <div class="uk-navbar-left">
                        <a aria-haspopup="true" aria-label="Open menu"
                           class="uk-navbar-toggle uk-navbar-toggle-animate uk-hidden@l uk-icon uk-navbar-toggle-icon"
                           href="#" role="button" uk-navbar-toggle-icon="">
                        </a>
                        <div class="uk-navbar-dropdown uk-drop">
                            <ul class="uk-nav uk-navbar-dropdown-nav">
                                <li><a href="#">Culture</a></li>
                                <li><a href="#">Tailored Wealth Solutions</a></li>
                                <li>
                                    <a aria-haspopup="true" href="#" role="button">Precision Financial Tools
                                        <span uk-navbar-parent-icon></span>
                                    </a>
                                    <div class="uk-navbar-dropdown uk-drop uk-width-large">
                                        <ul class="uk-nav uk-navbar-dropdown-nav">
                                            <li class="uk-nav-header">Potential Interest Calculators</li>
                                            {calculator_group1}
                                            <li class="uk-nav-divider"></li>
                                            <li class="uk-nav-header">Return on Investment (ROI) Calculators</li>
                                            {calculator_group2}
                                            <li class="uk-nav-divider"></li>
                                            <li class="uk-nav-header">Loan Amortisation Calculators</li>
                                            {calculator_group3}
                                            <li class="uk-nav-divider"></li>
                                            <li class="uk-nav-header">Other Relevant Financial Metrics Calculators</li>
                                            {calculator_group4}
                                        </ul>
                                    </div>
                                </li>
                                <li><a href="#">Research &amp; Insights</a></li>
                                <li><button class="uk-button uk-button-secondary uk-button-small">Let's Talk</button></li>
                            </ul>
                        </div>
                        <a aria-label="Back to Home" class="uk-navbar-item uk-logo" href="#"
                           style="font-family: &quot;Playfair Display SC&quot;, serif; font-weight: 700; font-style: normal;">Blue
                            Chip Invest</a>
                        <ul class="uk-navbar-nav uk-visible@l">
                            <li><a href="#">Culture</a></li>
                            <li><a href="#">Tailored Wealth Solutions</a></li>
                            <li>
                                <a aria-haspopup="true" href="#" role="button">Financial Tools
                                    <span uk-navbar-parent-icon></span>
                                </a>
                                <div class="uk-navbar-dropdown uk-drop uk-width-large">
                                    <ul class="uk-nav uk-navbar-dropdown-nav">
                                        <li class="uk-nav-header">Potential Interest Calculators</li>
                                        {calculator_group1}
                                        <li class="uk-nav-divider"></li>
                                        <li class="uk-nav-header">Return on Investment (ROI) Calculators</li>
                                        {calculator_group2}
                                        <li class="uk-nav-divider"></li>
                                        <li class="uk-nav-header">Loan Amortisation Calculators</li>
                                        {calculator_group3}
                                        <li class="uk-nav-divider"></li>
                                        <li class="uk-nav-header">Other Relevant Financial Metrics Calculators</li>
                                        {calculator_group4}
                                    </ul>
                                </div>
                            </li>
                            <li><a href="#">Research &amp; Insights</a></li>
                        </ul>
                    </div>
                    <div class="uk-navbar-right">
                        <button class="uk-button uk-button-secondary uk-button-small uk-visible@l">Let's Talk</button>
                        <a class="uk-icon-button uk-button-secondary uk-icon" uk-icon="user"></a>
                    </div>
                </div>
            </div>
        </nav>'''


potential_interest_calculators = f'''<div id="potential-interest-calculators" class="uk-modal-full" uk-modal>
    <div class="uk-modal-dialog">
        <button class="uk-modal-close-full uk-close-large" type="button" uk-close></button>
        
        <div class="uk-section uk-section-medium">
            <div class="uk-container">
                <h3 class="uk-text-uppercase uk-text-bolder" 
                style="font-family: &quot;Playfair Display SC&quot;, serif; font-weight: 700; font-style: normal;">
                Potential Interest Calculators</h3>
                <div class="uk-text-small uk-width-2-3@s">
                These are tools designed to help individuals or businesses estimate the amount of interest they could 
                earn or owe over time based on various financial scenarios. These calculators typically focus on 
                interest accumulated from savings, loans, or investments and can be tailored for specific financial 
                goals.</div>
                
                <div class="uk-child-width-1-2@s uk-margin-medium-top" uk-grid="masonry: pack">
                    <div>
                        <div class="uk-card uk-card-default uk-card-body">
                            <h4>Simple Interest Calculator</h4> 
                            <form>
                                <fieldset class="uk-fieldset">
                                    {calc_input(label='Principal (P)', icon='bag',
                                                description='The initial amount of money that is being invested or loaned.')}
                                    {calc_input(label='Interest Rate (R)', icon='arrow-up-right',
                                                description='The annual interest rate, usually provided as a percentage (e.g., 5%)')}
                                    {calc_input(label='Time (T)', icon='clock',
                                                description='The time period for which the interest is calculated, typically in years.')}
                                    <div class="uk-margin">
                                        <div class="uk-text-bolder uk-text-small">Result</div>
                                        <hr>
                                        <div><span class="uk-text-bolder">0.00</span> per year</div>
                                        <hr>
                                    </div>
                                </fieldset>
                            </form>
                        </div>
                    </div>
                   
                    <div>
                        <div class="uk-card uk-card-default uk-card-body">
                            <h4>Compound Interest Calculator</h4>
                            <form>
                                <fieldset class="uk-fieldset">
                                    {calc_input(label='Principal (P)', icon='bag',
                                                description='The initial amount of money that is being invested or loaned.')}
                                    {calc_input(label='Interest Rate (R)', icon='arrow-up-right',
                                                description='The annual interest rate, usually provided as a percentage (e.g., 5%)')}
                                    {calc_input(label='Time (T)', icon='clock',
                                                description='The time period for which the interest is calculated, typically in years.')}
                                    {calc_input(label='Compounding Frequency (n)', icon='calendar',
                                                description='The number of times the interest is compounded per year (e.g., annually, semi-annually, quarterly, monthly, daily).')}
                                        <div class="uk-text-small uk-padding-small uk-padding-remove-top">Common 
                                        values for compounding frequency:</div>
                                        <div class="uk-text-small uk-padding-small uk-padding-remove-top">
                                            <ul class="uk-list uk-list-collapse uk-list-disc">
                                                <li>Annually (n = 1)</li>
                                                <li>Semi-Annually (n = 2)</li>
                                                <li>Quarterly (n = 4)</li>
                                                <li>Monthly (n = 12)</li>
                                                <li>Daily (n = 365)</li>
                                            </ul>
                                        </div>
                                    <div class="uk-margin">
                                        <div class="uk-text-bolder uk-text-small">Result</div>
                                        <hr>
                                        <div><span class="uk-text-bolder">0.00</span> per year</div>
                                        <hr>
                                    </div>
                                </fieldset>
                            </form>
                        </div>
                    </div>
                    
                    <div>
                        <div class="uk-card uk-card-default uk-card-body">
                            <h4>Savings Interest Calculator</h4>
                            <form>
                                <fieldset class="uk-fieldset">
                                    {calc_input(label='Principal (P)', icon='bag',
                                                description='The initial amount of money that is being invested or loaned.')}
                                    {calc_input(label='Monthly Contributions (C)', icon='mail',
                                                description='The amount of money added to the account each month, if applicable.')}
                                    {calc_input(label='Annual Interest Rate (R)', icon='mail',
                                                description='The interest rate provided by the savings account, usually expressed as a percentage.')}
                                    {calc_input(label='Time (T)', icon='clock',
                                                description='The duration for which the savings will accumulate interest, typically measured in years.')}
                                    {calc_input(label='Compounding Frequency (n)', icon='calendar',
                                                description='The number of times the interest is compounded per year (e.g., annually, semi-annually, quarterly, monthly, daily).')}
                                        <div class="uk-text-small uk-padding-small uk-padding-remove-top">Common values for compounding frequency:</div>
                                        <div class="uk-text-small uk-padding-small uk-padding-remove-top">
                                            <ul class="uk-list uk-list-collapse uk-list-disc">
                                                <li>Annually (n = 1)</li>
                                                <li>Semi-Annually (n = 2)</li>
                                                <li>Quarterly (n = 4)</li>
                                                <li>Monthly (n = 12)</li>
                                                <li>Daily (n = 365)</li>
                                            </ul>
                                        </div>
                                    <div class="uk-margin">
                                        <div class="uk-text-bolder uk-text-small">Result</div>
                                        <hr>
                                        <div><span class="uk-text-bolder">0.00</span> per year</div>
                                        <hr>
                                    </div>
                                </fieldset>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>'''

hero = '''<div class="uk-background-bottom-right uk-background-cover"
             style="background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/marten-bjork-6dW3xyQvcYE-unsplash.jpg)"
             tabindex="0">
            <div class="uk-container">
                <div class="uk-child-width-1-2@s" uk-grid>
                    <div class="uk-card uk-card-body"></div>
                    <div class="uk-flex" style="min-height: max(0px, 60vh);" uk-height-viewport="offset-bottom: 40">
                        <div class="uk-card uk-card-body uk-margin-auto-vertical">
                            <h1 class="uk-text-bolder">Get a clear path to <br><span>your financial goals.</span></h1>
                            <p>Our Wealth Activating team can help you</p>
                            <button class="uk-button uk-button-secondary uk-button-small">Get Started</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

subhero = '''<div class="uk-child-width-expand@s uk-grid-collapse uk-grid-match uk-light" uk-grid>
            <div class="uk-background-secondary uk-width-2-5@m">
                <div class="uk-margin-auto-vertical uk-card uk-card-body uk-card-large">
                    <h2 class="uk-text-bolder uk-margin-xlarge-left">Planning objective <br><span>financial advice</span></h2>
                    <button class="uk-button uk-button-text uk-margin-xlarge-left">View All</button>
                </div>
            </div>
            <div class="uk-background-primary">
                <div class="uk-margin-auto-vertical uk-card uk-card-body">
                    <span class="uk-icon" uk-icon="icon: settings; ratio: 2"></span>
                    <div class="uk-text-bolder uk-margin-small-top">
                        <span class="uk-text-success">Risk Management</span></div>
                    <div class="uk-text-small">Risk management is critical to long-term success and sustainability</div>
                </div>
            </div>
            <div class="uk-background-primary">
                <div class="uk-margin-auto-vertical uk-card uk-card-body">
                    <span class="uk-icon" uk-icon="icon: image; ratio: 2"></span>
                    <div class="uk-text-bolder uk-margin-small-top">
                        <span class="uk-text-success">Investment Analytics</span></div>
                    <div class="uk-text-small">Leveraging investment analytics and make more informed decisions</div>
                </div>
            </div>
            <div class="uk-background-primary">
                <div class="uk-margin-auto-vertical uk-card uk-card-body">
                    <span class="uk-icon" uk-icon="icon: credit-card; ratio: 2"></span>
                    <div class="uk-text-bolder uk-margin-small-top">
                        <span class="uk-text-success">Cash Flow</span></div>
                    <div class="uk-text-small">Effective cash flow management is crucial for business survival</div>
                </div>
            </div>
        </div>'''

advisor_section = '''<div class="uk-section uk-section-xlarge uk-padding-remove-bottom">
            <div class="uk-container">
                <div class="uk-child-width-1-2@s uk-child-width-1-3@m uk-grid-small uk-grid uk-flex-top uk-flex-wrap-top"
                     style="height: 627px;" uk-grid="masonry: pack">
                    <div class="uk-visible@s uk-first-column" style="transform: translate(0px, 0px);">
                        <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                             style="height: 100px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/redd-f-5U_28ojjgms-unsplash.jpg)"
                             tabindex="0"></div>
                    </div>
                    <div class="uk-visible@s" style="transform: translate(0px, 0px);">
                        <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                             style="height: 150px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/santi-vedri-O5EMzfdxedg-unsplash.jpg)"
                             tabindex="0"></div>
                    </div>
                    <div class="uk-visible@s" style="transform: translate(0px, 0px);">
                        <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                             style="height: 300px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/youssef-naddam-iJ2IG8ckCpA-unsplash.jpg);"
                             tabindex="0"></div>
                    </div>
                    <div class="uk-visible@s uk-grid-margin uk-first-column" style="transform: translate(0px, -200px);">
                        <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                             style="height: 120px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jakub-zerdzicki-eGI0aGwuE-A-unsplash.jpg);"
                             tabindex="0"></div>
                    </div>
                    <div class="uk-visible@s uk-grid-margin" style="transform: translate(0px, -150px);">
                        <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                             style="height: 180px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/nandhu-kumar-5NGTf4oD8RA-unsplash.jpg)"
                             tabindex="0"></div>
                    </div>
                    <div class="uk-visible@s uk-grid-margin" style="transform: translate(-810px, -65px);">
                        <div class="uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle"
                             style="height: 140px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/accuray-5VkNa1LrS8A-unsplash.jpg)"
                             tabindex="0"></div>
                    </div>
                    <div class="uk-grid-margin uk-first-column" style="transform: translate(810px, -195px);">
                        <div class="uk-card uk-card-body uk-margin-auto-vertical">
                            <h2 class="uk-text-bolder">
                                <span class="uk-text-primary">We Help</span> financial <br><span>Advisors that </span><br><span>exclusively serve.</span>
                            </h2>
                            <p class="uk-width-medium">We empower financial advisors dedicated to serving a select clientele</p>
                            <button class="uk-button uk-button-text">Read More</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

serve_section = '''<div class="uk-section uk-padding-remove-vertical">
            <div class="uk-container">
                <div class="uk-card uk-card-body uk-margin-auto-vertical">
                    <h2 class="uk-text-bolder">
                        <span class="uk-text-success">Who</span><span> We Serve</span>
                        <hr class="uk-width-small uk-text-success" style="height: 0px; border: none; border-top: 2px solid;">
                    </h2>
                    <p class="uk-width-medium">Focused support for financial advisors with a unique clientele.</p>
                </div>
                <div class="uk-child-width-1-5@m uk-child-width-1-3@s uk-child-width-1-2 uk-margin-medium-top" uk-grid>
                    <div>
                        <div class="uk-card uk-card-small">
                            <div class="uk-card-media-top uk-background-cover" style="height: 240px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/ellicia-24HcJhf0u6M-unsplash.jpg);mask-image: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0));"
                                 tabindex="0"></div>
                            <div class="uk-card-body">
                                <h3 class="uk-text-bolder">Business Owners</h3>
                                <button class="uk-button uk-button-text">Read More</button>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-small">
                            <div class="uk-card-media-top uk-background-cover" style="height: 240px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jc-gellidon-j_5sxxspFtc-unsplash.jpg);mask-image: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0));"
                                 tabindex="0"></div>
                            <div class="uk-card-body">
                                <h3 class="uk-text-bolder">Private Client</h3>
                                <button class="uk-button uk-button-text">Read More</button>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-small">
                            <div class="uk-card-media-top uk-background-cover"
                                 style="height: 240px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/birmingham-museums-trust-T2AmpV9qWqw-unsplash.jpg);mask-image: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0));"
                                 tabindex="0"></div>
                            <div class="uk-card-body">
                                <h3 class="uk-text-bolder">Pre-Retirees</h3>
                                <button class="uk-button uk-button-text">Read More</button>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-small">
                            <div class="uk-card-media-top uk-background-cover" style="height: 240px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/huy-phan-QCF2ykBsC2I-unsplash.jpg); mask-image: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0));"
                                 tabindex="0"></div>
                            <div class="uk-card-body">
                                <h3 class="uk-text-bolder">Retirees</h3>
                                <button class="uk-button uk-button-text">Read More</button>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-small">
                            <div class="uk-card-media-top uk-background-cover" style="height: 240px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/ali-morshedlou-WMD64tMfc4k-unsplash.jpg); mask-image: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0));"
                                 tabindex="0"></div>
                            <div class="uk-card-body">
                                <h3 class="uk-text-bolder">Young Investor</h3>
                                <button class="uk-button uk-button-text">Read More</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

metric_section = '''<div class="uk-section uk-section-large">
            <div class="uk-container">
                <div class="uk-grid-divider uk-child-width-expand@s" uk-grid>
                    <div class="uk-text-center">
                        <div class="uk-heading-small"
                             style="font-family: &quot;Playfair Display SC&quot;, serif; font-weight: 700; font-style: normal;">
                            $15B
                        </div>
                        <div class="uk-text-small">Assets Under Management</div>
                    </div>
                    <div class="uk-text-center">
                        <div class="uk-heading-small"
                             style="font-family: &quot;Playfair Display SC&quot;, serif; font-weight: 700; font-style: normal;">
                            56
                        </div>
                        <div class="uk-text-small">Office Locations in RSA</div>
                    </div>
                    <div class="uk-text-center">
                        <div class="uk-heading-small"
                             style="font-family: &quot;Playfair Display SC&quot;, serif; font-weight: 700; font-style: normal;">
                            1995
                        </div>
                        <div class="uk-text-small">Year founded company</div>
                    </div>
                    <div class="uk-text-center">
                        <div class="uk-heading-small"
                             style="font-family: &quot;Playfair Display SC&quot;, serif; font-weight: 700; font-style: normal;">
                            2,541
                        </div>
                        <div class="uk-text-small">Clients represented through our firm</div>
                    </div>
                </div>
            </div>
        </div>'''

preserve_section = '''<div class="uk-container">
            <div class="uk-height-medium uk-flex uk-flex-start uk-flex-middle uk-background-cover uk-background-center-center"
                 style="background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/scott-webb-hDyO6rr3kqk-unsplash.jpg)"
                 tabindex="0">
                <div class="uk-card uk-card-body uk-width-1-2@s">
                    <h1 class="uk-text-success uk-text-bolder">Preserve and Grow Your Financial Legacy</h1>
                    <button class="uk-button uk-button-secondary">Contact Us</button>
                </div>
            </div>
        </div>'''

whatwedo_section = '''<div class="uk-section uk-section-xlarge">
            <div class="uk-container">
                <div class="uk-grid-match uk-text-center" uk-grid>
                    <div class="uk-width-1-2@m">
                        <div class="uk-card uk-card-body uk-card-secondary uk-margin-auto-vertical uk-text-left">
                            <h2 class="uk-text-bolder">
                                <span class="uk-text-success">What</span> We Do
                                <hr class="uk-width-small uk-text-success"
                                    style="height: 0px; border: none; border-top: 2px solid;">
                            </h2>
                            <p class="uk-width-medium">Providing tailored solutions for financial advisors to elevate client success.</p>
                            <button class="uk-button uk-button-text">View All</button>
                        </div>
                    </div>
                    <div class="uk-width-1-4@m uk-width-1-2@s">
                        <div class="uk-card uk-card-default uk-card-body">
                            <span class="uk-text-primary uk-icon" uk-icon="icon: crosshairs; ratio: 2.5"></span>
                            <p class="uk-text-bolder">Financial Planning</p>
                            <div class="uk-text-small">Comprehensive strategies to secure your financial future.</div>
                        </div>
                    </div>
                    <div class="uk-width-1-4@m uk-width-1-2@s">
                        <div class="uk-card uk-card-default uk-card-body">
                            <span class="uk-text-primary uk-icon" uk-icon="icon: unlock; ratio: 2.5"><</span>
                            <p class="uk-text-bolder">Retirement Planning</p>
                            <div class="uk-text-small">Creating personalized pathways to a secure and fulfilling retirement.</div>
                        </div>
                    </div>
                    <div class="uk-width-1-4@m uk-width-1-2@s">
                        <div class="uk-card uk-card-default uk-card-body">
                            <span class="uk-text-primary uk-icon" uk-icon="icon: file-text; ratio: 2.5"></span>
                            <p class="uk-text-bolder">Insurance</p>
                            <div class="uk-text-small">Protecting what matters most with tailored insurance solutions.</div>
                        </div>
                    </div>
                    <div class="uk-width-1-4@m uk-width-1-2@s">
                        <div class="uk-card uk-card-default uk-card-body">
                            <span class="uk-text-primary uk-icon" uk-icon="icon: cart; ratio: 2.5"></span>
                            <p class="uk-text-bolder">Investment Management</p>
                            <div class="uk-text-small">Maximizing growth through strategic and personalized investment.</div>
                        </div>
                    </div>
                    <div class="uk-width-1-4@m uk-width-1-2@s">
                        <div class="uk-card uk-card-default uk-card-body">
                            <span class="uk-text-primary uk-icon" uk-icon="icon: search; ratio: 2.5"></span>
                            <p class="uk-text-bolder">Tax Planning</p>
                            <div class="uk-text-small">Optimizing your financial strategy with proactive tax planning solutions.</div>
                        </div>
                    </div>
                    <div class="uk-width-1-4@m uk-width-1-2@s">
                        <div class="uk-card uk-card-default uk-card-body">
                            <span class="uk-text-primary uk-icon" uk-icon="icon: bag; ratio: 2.5"></span>
                            <p class="uk-text-bolder">Business Planning</p>
                            <div class="uk-text-small">Building robust strategies for sustainable business growth and success.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

testimonials_section = '''<div class="uk-section uk-section-secondary">
            <div class="uk-container">
                <div class="uk-card uk-card-body uk-text-center">
                    <div class="uk-text-small uk-text-bolder">WHAT OUR CUSTOMERS SAY</div>
                    <h2 class="uk-text-bolder uk-margin-remove-top">
                        <span class="uk-text-success">Our</span> Testimonials </h2>
                </div>
                <div class="uk-grid-match uk-child-width-expand@m" uk-grid>
                    <div>
                        <div class="uk-card uk-card-default uk-card-body">
                            <div>
                                <span class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span>
                            </div>
                            <p class="uk-text-italic">
                                <span class="uk-text-bolder">Exceptional Guidance for Every Stage</span><br>Working with this
                                company has been a game-changer for my practice.
                                Their expertise in financial and business planning helped me develop strategies tailored to my
                                clients’ unique needs. The personalized support and dedication to excellence have elevated the
                                service I offer, and my clients couldn't be happier. </p>
                            <div class="uk-grid-small" uk-grid>
                                <div class="uk-width-auto">
                                    <img alt="Border pill"
                                         class="uk-border-circle" height="64" src="https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jurica-koletic-7YVZYZeITc8-unsplash.jpg" width="64"></div>
                                <div class="uk-margin-auto-vertical">
                                    <div class="uk-text-bolder">— Sarah T.</div>
                                    <div class="uk-text-small">Financial Advisor</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-default uk-card-body">
                            <div>
                                <span class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span>
                            </div>
                            <p class="uk-text-italic">
                                <span class="uk-text-bolder">A True Partner in Growth</span><br>From investment management to
                                retirement planning, they’ve provided me with the tools
                                and insights to serve my clients better. Their proactive approach to tax and insurance
                                planning has saved my clients both time and money, allowing me to build stronger,
                                long-term relationships. They’re not just a service provider; they’re a trusted partner
                                in my success. </p>
                            <div class="uk-grid-small" uk-grid>
                                <div class="uk-width-auto">
                                    <img alt="Border pill"
                                         class="uk-border-circle" height="64" src="https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jurica-koletic-7YVZYZeITc8-unsplash.jpg" width="64"></div>
                                <div class="uk-margin-auto-vertical">
                                    <div class="uk-text-bolder">— John M.</div>
                                    <div class="uk-text-small">Certified Financial Planner</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-default uk-card-body">
                            <div>
                                <span class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span><span
                                    class="uk-text-warning uk-icon" uk-icon="star"></span>
                            </div>
                            <p class="uk-text-italic">
                                <span class="uk-text-bolder">Unmatched Expertise and Support</span><br>The business planning
                                strategies offered by this team have been instrumental in
                                helping me grow my advisory firm. Their in-depth understanding of financial planning,
                                combined with their dedication to serving a niche clientele, has made all the difference.
                                I highly recommend them to any financial advisor looking to take their business to the
                                next level. </p>
                            <div class="uk-grid-small" uk-grid>
                                <div class="uk-width-auto">
                                    <img alt="Border pill"
                                         class="uk-border-circle" height="64" src="https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jurica-koletic-7YVZYZeITc8-unsplash.jpg" width="64"></div>
                                <div class="uk-margin-auto-vertical">
                                    <div class="uk-text-bolder">— Alex P.</div>
                                    <div class="uk-text-small">Wealth Management Advisor</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

guides_section = '''<div class="uk-section uk-section-xlarge">
            <div class="uk-container">
                <div class="uk-grid-match uk-child-width-expand@s" uk-grid>
                    <div>
                        <div class="uk-card uk-card-body uk-margin-auto-vertical">
                            <h2 class="uk-text-bolder">
                                <span class="uk-text-success">Personal</span> Finance Guides
                                <hr class="uk-width-small uk-text-success"
                                    style="height: 0px; border: none; border-top: 2px solid;">
                            </h2>
                            <button class="uk-button uk-button-text">Read Our Blog</button>
                        </div>
                        <div class="uk-card uk-card-body uk-margin-auto-vertical">
                            <h5 class="uk-text-bolder">Most Popular</h5>
                            <ul class="uk-list uk-list-disc uk-list-primary uk-text-small">
                                <li><a class="uk-link-muted" href="#">What are Portfolio Accounting Systems</a></li>
                                <li><a class="uk-link-muted" href="#">Investing Basics for New Grads</a></li>
                                <li><a class="uk-link-muted" href="#">What is the Average Net Worth by Age</a></li>
                                <li><a class="uk-link-muted" href="#">Wealth Management vs. Investment Banking</a></li>
                                <li><a class="uk-link-muted" href="#">2024's Best Provinces to Retire in South Africa</a></li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-small uk-card-body">
                            <div class="uk-background-cover" style="height: 320px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/krzysztof-hepner-o_x11ORH9vQ-unsplash.jpg)"
                                 tabindex="0"></div>
                            <div class="uk-card-body">
                                <h4 class="uk-card-title, uk-text-bolder">How to Achieve True Wealth</h4>
                                <p class="uk-text-small">Unlocking true wealth involves strategic planning, smart investments,
                                    and a holistic approach to managing your financial resources. Discover the steps to build and
                                    sustain genuine financial prosperity.</p>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-small uk-card-body">
                            <div class="uk-background-cover" style="height: 320px; background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/pedro-miranda-3QzMBrvCeyQ-unsplash.jpg)"
                                 tabindex="0"></div>
                            <div class="uk-card-body">
                                <h4 class="uk-card-title, uk-text-bolder">Step Focused Planning</h4>
                                <p class="uk-text-small">Achieve your financial goals with step-by-step, focused planning that
                                    guides you through every stage of wealth building and preservation.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

footer = '''<div class="uk-section uk-section-medium uk-section-secondary">
            <div class="uk-container">
                <div class="uk-grid-match uk-child-width-1-3@s uk-child-width-1-4@l" uk-grid>
                    <div>
                        <div class="uk-card uk-card-body">
                            <div aria-label="Back to Home" class="uk-heading-small uk-margin-small-bottom"
                                 style="font-family: &quot;Playfair Display SC&quot;, serif; font-weight: 700; font-style: normal;">
                                Blue Chip Invest
                            </div>
                            <div class="uk-text-small">Building Your Legacy with Trusted Growth</div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-body">
                            <div class="uk-text-bolder uk-text-success uk-text-large uk-margin-medium-bottom">Our Services</div>
                            <ul class="uk-list uk-text-small">
                                <li><a href="#">Financial Planning</a></li>
                                <li><a href="#">Investment Management</a></li>
                                <li><a href="#">Retirement Planning</a></li>
                                <li><a href="#">Investment Analysis</a></li>
                                <li><a href="#">Insurance</a></li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-body">
                            <div class="uk-text-bolder uk-text-success uk-text-large uk-margin-medium-bottom">Explore</div>
                            <ul class="uk-list uk-text-small">
                                <li><a href="#">About</a></li>
                                <li><a href="#">Services</a></li>
                                <li><a href="#">Careers</a></li>
                                <li><a href="#">FAQ's</a></li>
                                <li><a href="#">Partner</a></li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-body">
                            <div class="uk-text-bolder uk-text-success uk-text-large uk-margin-medium-bottom">Let's Talk</div>
                            <div class="uk-text-small">We're Here to Help You Grow Your Wealth, Plan Your Future, and Achieve
                                Your Financial Goals
                            </div>
                            <button class="uk-button uk-button-primary uk-button-large uk-margin-top">Contact Us</button>
                        </div>
                    </div>
                </div>
                <div class="uk-grid-match uk-child-width-1-2 uk-child-width-1-3@s uk-child-width-1-4@l" uk-grid>
                    <div>
                        <div class="uk-card uk-card-body">
                            <div class="uk-child-width-1-2 uk-grid-small">
                                <div class="uk-width-auto">
                                    <span class="uk-icon" uk-icon="icon: location; ratio: 1.8"></span>
                                </div>
                                <div class="uk-margin-auto-vertical">
                                    <div class="uk-text-large uk-text-bolder">Location</div>
                                    <div class="uk-text-small">No. 30 Pinetown, Durban 3610</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-body">
                            <div class="uk-child-width-1-2 uk-grid-small">
                                <div class="uk-width-auto">
                                    <span class="uk-icon" uk-icon="icon: receiver; ratio: 1.8"></span>
                                </div>
                                <div class="uk-margin-auto-vertical">
                                    <div class="uk-text-large uk-text-bolder">Phone</div>
                                    <div class="uk-text-small">0860 258 2447</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-body">
                            <div class="uk-child-width-1-2 uk-grid-small">
                                <div class="uk-width-auto">
                                    <span class="uk-icon" uk-icon="icon: mail; ratio: 1.8"></span>
                                </div>
                                <div class="uk-margin-auto-vertical">
                                    <div class="uk-text-large uk-text-bolder">Email</div>
                                    <div class="uk-text-small">
                                        admin<br>@bluechipinvest<br>.co.za
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="uk-card uk-card-body">
                            <div class="uk-grid-small uk-child-width-auto" uk-grid>
                                <div><span class="uk-icon-button uk-icon" uk-icon="icon: facebook"></span></div>
                                <div><span class="uk-icon-button uk-icon" uk-icon="icon: linkedin"></span></div>
                                <div><span class="uk-icon-button uk-icon" uk-icon="icon: instagram"></span></div>
                                <div><span class="uk-icon-button uk-icon" uk-icon="icon: x"></span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>'''
