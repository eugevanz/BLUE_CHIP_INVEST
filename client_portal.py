import random
from datetime import datetime

from fasthtml.components import Div, Nav, Ul, Li, A, Span, P, H3, Img, Tr, Td, Tbody, Th, Thead, \
    Table, H2, Caption, Button, Article

from interface import calendar_view, sign_out_button


def nav_offcanvas(header: str):
    return Div(
        H3(header, cls='uk-width-small uk-margin-remove'),
        cls='uk-margin-medium-bottom uk-margin-small-top uk-padding',
        style='background-color: #88A9C3'
    )


def articles_offcanvas(articles: list, icon: str):
    return Div(
        *[Article(
            Div(uk_icon=f'icon: {icon}'), P(header, cls='uk-text-bolder'), P(article),
            cls='uk-article', id=element
        ) for header, article, element in articles],
        cls='uk-flex uk-flex-wrap'
    )


def offcanvas_messages():
    return Div(
        Div(
            Button(type='button', data_uk_close=True, cls='uk-offcanvas-close'),
            H3('Messages'),
            Div(
                *[Article(
                    Div(uk_icon='icon: mail'), P(meta, cls='uk-article-meta'),
                    P(header, cls='uk-text-bolder'), P(article),
                    cls='uk-article'
                ) for meta, header, article in [
                    ('Written by Super User on 08 March 2021. Posted in Blog',
                     'Understanding Inflation: What It Means for Your Savings',
                     'Inflation can significantly impact the value of your savings over time. This '
                     'article explores what inflation is, how it’s measured, and why it matters for '
                     'anyone with long-term financial goals. We’ll also offer tips on how to protect your '
                     'investments and savings from the negative effects of inflation.'),
                    ('Written by Super User on 15 June 2020. Posted in Blog',
                     'The Basics of Stock Market Investing',
                     'Whether you’re new to investing or looking to improve your portfolio, understanding '
                     'the basics of the stock market is essential. In this article, we break down key '
                     'concepts like stock prices, dividends, and market trends to help you get started on '
                     'the right foot.'),
                    ('Written by Super User on 22 November 2019. Posted in Blog',
                     'How to Build a Balanced Investment Portfolio',
                     'Creating a diversified investment portfolio is one of the most effective strategies '
                     'for long-term growth. Learn about the importance of balancing risk with reward, '
                     'and how to allocate assets across stocks, bonds, and other investment types to meet '
                     'your financial goals.'),
                    ('Written by Super User on 05 February 2022. Posted in Blog',
                     'Retirement Planning: Steps to Secure Your Future',
                     'Retirement planning can seem overwhelming, but starting early can make a huge '
                     'difference. This guide walks you through the key steps in building a retirement '
                     'strategy, from choosing the right savings accounts to understanding pension plans '
                     'and Social Security benefits.'),
                    ('Written by Super User on 30 September 2023. Posted in Blog',
                     'The Role of Cryptocurrency in Modern Finance',
                     'Cryptocurrency is becoming an increasingly popular alternative to traditional '
                     'finance. This article explores the rise of digital currencies like Bitcoin and '
                     'Ethereum, their potential benefits and risks, and what they mean for the future of '
                     'global financial systems.')
                ]],
                cls='uk-flex uk-flex-wrap'
            ),
            cls='uk-offcanvas-bar'
        ),
        id='messages', data_uk_offcanvas=True
    )


def offcanvas_contact_support():
    return Div(
        Div(
            Button(type='button', data_uk_close=True, cls='uk-offcanvas-close'),
            H3('Contact Support'),
            Div(
                *[Div(
                    Div(data_uk_icon=f'icon: {icon}; ratio: 1.8', cls='uk-icon'),
                    Div(title, cls='uk-text-large uk-text-bolder'),
                    Div(subtext, cls='uk-text-small'),
                    cls='uk-margin'
                ) for icon, title, subtext in [
                    ('location', 'Location', 'Unit 17, No.30 Surprise Road, Pinetown, 3610'),
                    ('receiver', 'Phone', '0860 258 2447'),
                    ('mail', 'Email', 'info@bluechipinvest.co.za'),
                    ('clock', 'Open hours', 'Mon - Sat, 08:00 - 16:00')
                ]],
                data_uk_grid=True,
                cls='uk-grid-match uk-child-width-1-1 uk-margin-medium-top'
            ),
            cls='uk-offcanvas-bar'
        ),
        id='contact-support', data_uk_offcanvas=True
    )


def offcanvas_faqs():
    return Div(
        Div(
            Button(type='button', data_uk_close=True, cls='uk-offcanvas-close'),
            nav_offcanvas(header='Frequently Asked Questions'),
            articles_offcanvas([
                ('How do I create an account?',
                 'To create an account, get in contact with one our consultants. Once you have an account with '
                 'us, check your email for a confirmation link. Click it to activate your account, and you’re all '
                 'set!', 'create-an-account'),
                ('How can I reset my password?',
                 'No worries! You dont have a password to reset!. This app uses One-Time-Pin to sign in, '
                 'eliminating the need for passwords. Be sure to check your spam folder if you don’t see the '
                 'email right away!', 'reset-my-password'),
                ('How do I update my contact details (email, phone number, etc.)?',
                 'Updating your details is simple, but it needs to be done through our account management team. '
                 'Just give us a call, and submit a request to update your email, phone number, or other personal '
                 'details. Our team will process the changes, and you’ll receive a confirmation once they’re '
                 'complete.', 'my-contact-details'),
                ('What should I do if I can’t log in?',
                 'If you’re having trouble logging in, double-check that you’re entering the correct email. If '
                 'that doesn\'t work, feel free to reach out to us via the support form, and we’ll be happy to '
                 'assist.', 'cant-log-in'),
                ('What information do I need to provide when contacting support?',
                 'When submitting a support request, it helps to include as much detail as possible about your '
                 'issue. Provide the exact steps you took when the problem occurred, any error messages you '
                 'received, and screenshots or recordings if possible. This will help us resolve your issue '
                 'faster!', 'contacting-support'),
                ('How do you protect my personal data?',
                 'Your privacy is important to us. We use industry-standard encryption protocols and secure '
                 'servers to protect your personal information. ', 'my-personal-data'),
                ('What should I do if the portal is not loading properly?',
                 'If the portal isn’t loading, try refreshing your browser or clearing your cache and cookies. If '
                 'the issue persists, try switching browsers or disabling any browser extensions that might be '
                 'interfering.', 'not-loading-properly'),
                ('How can I clear my browser’s cache and cookies to resolve issues?',
                 'To clear your cache and cookies, go to your browser settings, find the “Privacy” section, '
                 'and look for “Clear Browsing Data.” Select “Cache” and “Cookies,” and click “Clear Data.” This '
                 'often resolves many issues with page loading.', 'to-resolve-issues'),
                ('Why am I getting error messages during login or while using services?',
                 'Error messages can sometimes occur due to incorrect login credentials or a temporary server '
                 'issue. Double-check your login details and try again. If the issue continues, please submit a '
                 'support request so we can look into it for you.', 'using-services')
            ], icon='question'),
            cls='uk-offcanvas-bar'
        ),
        id='faqs', data_uk_offcanvas=True
    )


def offcanvas_investment_faqs():
    return Div(
        Div(
            Button(type='button', data_uk_close=True, cls='uk-offcanvas-close'),
            nav_offcanvas(header='Investment Frequently Asked Questions'),
            articles_offcanvas([
                ('How do I start investing?',
                 'To start investing, you’ll need to open an investment account. Once your account is set up, '
                 'you can deposit funds and choose from various investment options, such as stocks, bonds, '
                 'mutual funds, or ETFs. If you’re unsure where to begin, it’s a good idea to determine your '
                 'financial goals and risk tolerance before selecting investments.', 'start-investing'),
                ('Can I get advice on which investments to choose?',
                 'Yes, you can receive advice on your investment options. Our team offers personalized investment '
                 'recommendations based on your financial goals, risk tolerance, and time horizon. You can also '
                 'schedule a consultation with an advisor for more detailed guidance.', 'investments-to-choose'),
                ('How can I track my investments?',
                 'You can track your investments through your account dashboard, where you’ll find real-time '
                 'updates on performance, gains, and losses. You can also set up alerts to notify you of '
                 'significant changes in your portfolio or the market.', 'my-investments'),
                ('What’s the difference between a conservative, balanced, and aggressive portfolio?',
                 'Conservative portfolios are lower risk and focus on preserving capital by investing in safer '
                 'assets like bonds. Balanced portfolios aim to provide moderate growth by combining stocks and '
                 'bonds, balancing risk and return. Aggressive portfolios carry higher risk but offer higher '
                 'potential returns, primarily investing in stocks or high-growth assets.', 'aggressive-portfolio'),
                ('What does diversification mean, and why is it important?',
                 'Diversification means spreading your investments across different asset classes (like stocks, '
                 'bonds, and real estate) to reduce risk. It’s important because it helps protect your portfolio '
                 'from significant losses if one type of investment performs poorly, thus balancing overall '
                 'returns.', 'is-it-important'),
                ('What level of risk should I expect with my investments?',
                 'The level of risk depends on the types of investments you choose and your investment strategy. '
                 'Conservative investments tend to be lower risk, while aggressive investments come with higher '
                 'risk but higher potential rewards. We help you align your risk tolerance with your investment '
                 'goals.', 'with-my-investments'),
                ('Is there a limit on how much I can invest?',
                 'There is generally no upper limit on how much you can invest, though some investment products '
                 'may have minimum investment requirements. Additionally, certain tax-advantaged accounts (like '
                 'IRAs) have annual contribution limits based on government regulations.', 'can-invest'),
                ('Can I withdraw money from my investments?',
                 'The level of risk depends on the types of investments you choose and your investment strategy. '
                 'Conservative investments tend to be lower risk, while aggressive investments come with higher '
                 'risk but higher potential rewards. We help you align your risk tolerance with your investment '
                 'goals.', 'from-my-investments'),
                ('How can I add money to my investment account?',
                 'To add money to your investment account, log in, go to the “Funding” section, and select your '
                 'preferred deposit method. You can typically transfer funds from your bank account or set up '
                 'recurring contributions.', 'my-investment-account'),
                ('Is there a limit on how much I can invest?',
                 'There is generally no upper limit on how much you can invest, though some investment products '
                 'may have minimum investment requirements. Additionally, certain tax-advantaged accounts (like '
                 'IRAs) have annual contribution limits based on government regulations.', 'much-i-can-invest'),
                ('Can I withdraw money from my investments?',
                 'Yes, you can withdraw money from your investments. However, the process and timeframe can vary '
                 'depending on the type of investments and whether they are in tax-advantaged accounts. Keep in '
                 'mind that withdrawing funds may impact your investment strategy and long-term growth potential.',
                 'money-from-my-investments'),
                ('Do I need to report my investment earnings for tax purposes?',
                 'Yes, investment earnings are typically subject to taxes. You’ll receive documentation outlining '
                 'your earnings (such as dividends, interest, and capital gains) to help you file your taxes. '
                 'Specific tax treatment may depend on the type of account and investment.', 'for-tax-purposes'),
                ('Do you offer socially responsible or sustainable investment options?',
                 'Yes, we offer socially responsible and sustainable investment options that focus on companies '
                 'and funds aligned with environmental, social, and governance (ESG) criteria. These portfolios '
                 'allow you to invest in line with your values while aiming for financial returns.',
                 'investment-options'),
                ('Can I customize my portfolio to focus on sustainability?',
                 'Absolutely. You can work with our team to tailor your portfolio to prioritize sustainable and '
                 'socially responsible investments. We offer a range of ESG-focused funds that you can '
                 'incorporate into your investment strategy.', 'on-sustainability'),
                ('Who can I contact if I have questions about my investments?',
                 'You can reach out to our support team for any investment-related questions. We also offer '
                 'access to financial advisors who can help address your concerns and provide personalized '
                 'guidance.', 'about-my-investments'),
                ('How do I schedule a consultation with an investment advisor?',
                 'To schedule a consultation, simply log in to your account and navigate to the “Consultation” '
                 'section. From there, you can choose a time that works for you, and one of our advisors will '
                 'reach out to provide personalized investment advice.', 'an-investment-advisor')
            ], icon='question'),
            cls='uk-offcanvas-bar'
        ),
        id='investment_faqs', data_uk_offcanvas=True
    )


def menu_card():
    return Div(
        Ul(
            Li('Menu', cls='uk-nav-header', style='color: white;'),
            Li(A(Span(data_uk_icon='icon: home', cls='uk-margin-small-right'), 'Dashboard',
                 cls='uk-flex uk-flex-middle')),
            Li(
                A(
                    Span(data_uk_icon='icon: credit-card', cls='uk-margin-small-right'), 'Transactions',
                    cls='uk-flex uk-flex-middle',
                    _='on click js const element = document.getElementById("transactions"); if (element) { '
                      'window.scrollTo({top: element.offsetTop - 96, behavior: "smooth"}); }'
                )
            ),
            Li(
                A(Span(data_uk_icon='icon: mail', cls='uk-margin-small-right'), 'Messages',
                  cls='uk-flex uk-flex-middle', data_uk_toggle=True, href='#messages'),
                offcanvas_messages()
            ),
            Li(A(Span(data_uk_icon='icon: nut', cls='uk-margin-small-right'), 'Investment',
                 cls='uk-flex uk-flex-middle',
                 _='on click js const element = document.getElementById("holdings"); if (element) { '
                   'window.scrollTo({top: element.offsetTop - 96, behavior: "smooth"}); }')),
            Li(cls='uk-nav-divider uk-margin'),
            Li(
                Div(
                    Img(cls='uk-border-circle', width='44', height='44',
                        src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                            '/jurica-koletic-7YVZYZeITc8-unsplash_3_11zon.webp', alt='profile-pic'),
                    cls='uk-width-auto'
                ),
                Div(
                    H3('Title', cls='uk-card-title uk-margin-remove-bottom', style='color: white;'),
                    P('April 01, 2016', cls='uk-text-meta uk-margin-remove-top'),
                    cls='uk-width-expand'
                ),
                cls='uk-grid-small uk-flex-middle uk-margin-left uk-margin-top', data_uk_grid=True
            ),
            Li(cls='uk-nav-divider uk-margin'),
            Li('Support', cls='uk-nav-header', style='color: white;'),
            Li(A('Contact Support', data_uk_toggle=True, href='#contact-support'), offcanvas_contact_support()),
            Li(A('FAQs', data_uk_toggle=True, href='#faqs'), offcanvas_faqs()),
            Li(A('Investment FAQs', data_uk_toggle=True, href='#investment_faqs'), offcanvas_investment_faqs()),
            Li(
                A('Service Status'),
                Div('No reported issues. All services are functioning normally.',
                    data_uk_drop='mode: click', cls='uk-card uk-card-body uk-card-default'),
                cls='uk-inline'
            ),
            sign_out_button(),
            cls='uk-nav uk-nav-default'
        ),
        cls='uk-card uk-card-body uk-card-default', style='background-color: #2A3A58'
    )


def overview_card():
    return Div(
        Div(
            Div(
                Div('Overview', cls='uk-text-default uk-text-bolder'),
                Div(datetime.now().strftime('%B %Y'), cls='uk-text-small'),
                cls='uk-flex uk-flex-between'
            ),
            cls='uk-card-header'
        ),
        Div(
            Div(
                Div(
                    Div('40', cls='uk-text-large uk-text-bolder'),
                    Div('Transactions', cls='uk-text-truncate', style='font-size: 11px;')
                ),
                Div(Div('24', cls='uk-text-large uk-text-bolder'), Div('Income', style='font-size: 11px;')),
                Div(Div('16', cls='uk-text-large uk-text-bolder'), Div('Outcome', style='font-size: 11px;')),
                data_uk_grid=True, cls='uk-child-width-expand uk-text-center'
            ),
            cls='uk-card-body'
        ),
        Div(
            calendar_view(),
            Nav(
                Ul(
                    Li(
                        A(
                            Span(data_uk_pagination_previous=True, cls='uk-margin-small-right'),
                            'September',
                            href='#'
                        )
                    ),
                    Li(
                        A(
                            'November',
                            Span(data_uk_pagination_next=True, cls='uk-margin-small-left'),
                            href='#'
                        ),
                        cls='uk-margin-auto-left'
                    ),
                    cls='uk-pagination', data_uk_margin=True
                ),
                cls='uk-margin-medium-top'
            ),
            A(
                Div(
                    Span(data_uk_icon='icon: mail', cls='uk-margin-small-right', style='color: #89CFF0;'),
                    cls='uk-width-auto'
                ),
                Div(
                    Div('Top 5 Portfolio Holdings: Tech Giants Lead with Apple, Tesla, and Amazon Driving Strong '
                        'Returns'[:80] + '...', style='color: #89CFF0;', cls='uk-text-bolder')
                ),
                data_uk_grid=True, data_uk_toggle=True, href='#messages',
                cls='uk-child-width-expand uk-grid-small uk-margin-medium-top uk-text-muted'
            ),
            cls='uk-card-footer'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
    )


def portfolio_value_card():
    return Div(
        Div(
            Div(
                Div('Portfolio Value', cls='uk-text-default uk-text-bolder'),
                A('US Dollar', Span(data_uk_drop_parent_icon=True), cls='uk-link-muted uk-text-small'),
                Div(
                    Ul(
                        Li(A('US Dollar', cls='uk-link-muted uk-text-small')),
                        Li(A('ZA Rand', cls='uk-link-muted uk-text-small')),
                        Li(A('EURO', cls='uk-link-muted uk-text-small')),
                        Li(A('British Pound', cls='uk-link-muted uk-text-small')),
                        cls='uk-list uk-list-divider'
                    ),
                    cls='uk-card uk-card-body', style='background-color: #2A3A58;', data_uk_dropdown=True
                ),
                cls='uk-flex uk-flex-between'
            ),
            cls='uk-card-header'
        ),
        Div(
            Div('Balance', cls='uk-text-small'),
            H2('R8,167,514.57', cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
            Div('Compared to last month ', Span('+24.17%', cls='uk-text-success'),
                cls='uk-text-small uk-margin-remove-top'),
            Div(
                Div(
                    Div(Div('142M'), Div('71M', cls='uk-margin-auto-vertical'), Div('0M'),
                        cls='uk-flex uk-flex-column uk-flex-between uk-text-bolder', style='font-size: 8px;'),
                    cls='uk-width-auto'
                ),
                Div(
                    Table(
                        Caption('Portfolio Value'),
                        Thead(
                            Tr(
                                *[Th(title, scope='col') for title in ['Month', 'Income', 'Expenses']]
                            )
                        ),
                        Tbody(
                            *[Tr(
                                Th(x['month'], scope='row'),
                                *[Td(style=f'--size: 0.{amount * 2}') for amount in x['data']]
                            ) for x in [
                                dict(month='Jul', data=[random.randint(1, 142), random.randint(1, 142)]),
                                dict(month='Aug', data=[random.randint(1, 142), random.randint(1, 142)]),
                                dict(month='Sep', data=[random.randint(1, 142), random.randint(1, 142)]),
                                dict(month='Oct', data=[random.randint(1, 142), random.randint(1, 142)])
                            ]]
                        ),
                        cls='charts-css column multiple show-data-on-hover show-3-secondary-axes data-spacing-10 '
                            'show-labels',
                        style='--aspect-ratio: 4 / 4;'
                    )
                ),
                data_uk_grid=True,
                cls='uk-grid-divider uk-child-width-expand uk-grid-match uk-grid-small uk-margin-medium-top'
            ),
            # Div(Div('Jul'), Div('Aug'), Div('Sep'), Div('Oct'),
            #     cls='uk-flex uk-flex-around uk-text-bolder uk-text-small uk-margin-small uk-width-large',
            #     style='padding-left: 54px; padding-right: 128px;'),
            cls='uk-card-body'
        ),
        Div(
            Ul(
                *[Li(title, Span(amount, cls='uk-text-bolder uk-margin-small-left'))
                  for title, amount in [('Income', '$31,885'), ('Expenses', '$8,994')]],
                cls='charts-css legend legend-inline legend-square', style='border: 0'
            ),
            cls='uk-card-footer'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
    )


def transactions():
    return Div(
        Div(
            Div(
                Div('Recent Transactions', cls='uk-text-default uk-text-bolder'),
                Div(
                    Span(data_uk_icon='icon: table;'),
                    Span('Filter', cls='uk-margin-small-left'),
                    cls='uk-text-small uk-flex uk-flex-middle'
                ),
                cls='uk-flex uk-flex-between'
            ),
            cls='uk-card-header'
        ),
        Div(
            Table(
                Thead(
                    Tr(
                        Th('Type'),
                        Th('Amount'),
                        Th('Method')
                    )
                ),
                Tbody(
                    *[Tr(
                        Td(
                            Span(
                                uk_icon=f'icon:  {"plus-circle" if tx_type[0] == "Received" else "minus-circle"}; ratio: 1.5',
                                cls=f'uk-text-{"success" if tx_type[0] == "Received" else "danger"}'),
                            Div(
                                Div(title, cls='uk-text-bolder'),
                                Div(f'{tx_type[0]} • {tx_type[1]}', cls='uk-text-small'),
                                cls='uk-margin-small-left'
                            ),
                            cls='uk-flex uk-flex-middle'
                        ),
                        Td(Div(f'R {amount[0]}', cls='uk-text-bolder'), Div(f'R {amount[1]}', cls='uk-text-small')),
                        Td(Div(method[0], cls='uk-text-bolder'), Div(method[1], cls='uk-text-small'))
                    ) for title, tx_type, amount, method in [
                        ('Company', ('Sent', 'Aug 24 2024'), (1500.00, 1371.81), ('Credit Card', '**** 3560')),
                        ('Revenue', ('Received', 'Aug 24 2024'), (1500.00, 1371.81), ('Bank Transfer', '**** 3560')),
                        ('Bonus', ('Received', 'Aug 24 2024'), (1500.00, 1371.81), ('Credit Card', '**** 3560')),
                        ('Dog food', ('Sent', 'Aug 24 2024'), (1500.00, 1371.81), ('Bank Transfer', '**** 3560')),
                        ('Company', ('Sent', 'Aug 24 2024'), (1500.00, 1371.81), ('Bank Transfer', '**** 3560'))
                    ]]
                ),
                cls='uk-table uk-table-divider'
            ),
            cls='uk-card-body'
        ),
        Div(
            Nav(
                Ul(
                    Li(
                        A(
                            Span(data_uk_pagination_previous=True, cls='uk-margin-small-right'),
                            'Previous',
                            href='#'
                        )
                    ),
                    Li(
                        A(
                            'Next',
                            Span(data_uk_pagination_next=True, cls='uk-margin-small-left'),
                            href='#'
                        ),
                        cls='uk-margin-auto-left'
                    ),
                    cls='uk-pagination', data_uk_margin=True
                )
            ),
            cls='uk-card-footer'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;', id='transactions'
    )


def holdings():
    return Div(
        Div(
            Div(
                Div('Holdings', cls='uk-text-default uk-text-bolder'),
                # Div(
                #     Span(data_uk_icon='icon: table;'),
                #     Span('Filter', cls='uk-margin-small-left'),
                #     cls='uk-text-small uk-flex uk-flex-middle'
                # ),
                cls='uk-flex uk-flex-between'
            ),
            cls='uk-card-header'
        ),
        Div(
            Div(
                Div(
                    Div('Stocks (Equities)', cls='uk-text-small'),
                    H2('R8,167,514.57',
                       cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                    Div('Compared to last month ', Span('+24.17%', cls='uk-text-success'),
                        cls='uk-text-small uk-margin-remove-top')
                ),
                Button('View All', style='background-color: #88A9C3; color: #091235', cls='uk-button uk-button-small'),
                cls='uk-flex uk-flex-between uk-flex-middle'
            ),
            Div(
                Div(
                    Table(
                        Caption('Portfolio Value'),
                        Tbody(
                            *[Tr(
                                Td(style=f'--start: {values[0]}; --end: {values[1]}')
                            ) for title, values in [
                                ('Apple Inc. (AAPL)', (0, 0.3)),
                                ('Tesla Inc. (TSLA)', (0.3, 0.44)),
                                ('Amazon.com Inc. (AMZN)', (0.44, 0.6)),
                                ('Microsoft Corp. (MSFT)', (0.6, 0.68)),
                                ('Alphabet Inc. (GOOGL)', (0.68, 1))
                            ]]
                        ),
                        cls='charts-css pie'
                    )
                ),
                Div(
                    Ul(
                        *[Li(title, Span(amount, cls='uk-text-bolder uk-margin-small-left'), cls='uk-text-small')
                          for title, amount in [
                              ('Apple Inc. (AAPL)', '$31,885'), ('Tesla Inc. (TSLA)', '$8,994'),
                              ('Amazon.com Inc. (AMZN)', '$8,994'), ('Microsoft Corp. (MSFT)', '$8,994'),
                              ('Alphabet Inc. (GOOGL)', '$8,994')
                          ]],
                        cls='charts-css legend legend-inline legend-square', style='border: 0'
                    ),
                    cls='uk-width-2-3@m'
                ),
                data_uk_grid=True,
                cls='uk-grid-divider uk-child-width-expand@m uk-grid-match uk-grid-small uk-margin-medium-top'
            ),
            P('Apple Inc. (AAPL) is a multinational technology company based in Cupertino, California, best known for its '
              'innovative hardware, software, and digital services. Listed on the NASDAQ stock exchange under the ticker '
              'symbol AAPL, Apple is one of the most valuable companies in the world, consistently maintaining its '
              'position as a leader in the tech industry.', cls='uk-text-small'),
            cls='uk-card-body'
        ),
        Div(
            Nav(
                Ul(
                    Li(
                        A(
                            Span(data_uk_pagination_previous=True, cls='uk-margin-small-right'),
                            'Bonds (Fixed Income Securities)',
                            href='#'
                        )
                    ),
                    Li(
                        A(
                            'Real Estate',
                            Span(data_uk_pagination_next=True, cls='uk-margin-small-left'),
                            href='#'
                        ),
                        cls='uk-margin-auto-left'
                    ),
                    cls='uk-pagination', data_uk_margin=True
                )
            ),
            cls='uk-card-footer'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;', id='holdings'
    )


page = Div(
    Div(
        Div(
            Div(menu_card(), cls='uk-width-1-3@m'), Div(overview_card(), cls='uk-width-1-3@m'),
            Div(portfolio_value_card(), cls='uk-width-1-3@m'),
            # Div(assets_card()),
            Div(transactions(), cls='uk-width-1-2@m'),
            Div(holdings(), cls='uk-width-1-2@m'),
            data_uk_grid=True, cls='uk-child-width-1-4@m uk-grid-small uk-grid-match uk-flex-right',
            style='padding-top: 16px'
        ),
        cls='uk-container'
    ),
    style='background-color: #091235'
)
