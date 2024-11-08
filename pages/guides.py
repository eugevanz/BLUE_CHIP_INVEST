import dash
from dash import html

dash.register_page(__name__)

items = [
    ('Why don\'t you change as much as other financial planners?',
     'Unlike many financial planners who frequently adjust strategies in response to '
     'short-term market changes, we believe in a more stable, long-term approach. Our focus '
     'is on developing personalized plans based on your unique goals and risk tolerance, '
     'which reduces the need for constant changes. This method helps minimize unnecessary fees '
     'and ensures we stay aligned with your financial future, rather than reacting to market '
     'noise.', 'question'),
    ('How do you work with people in other provinces and countries?',
     'We effectively work with clients in other provinces and countries by leveraging technology and clear '
     'communication. Our virtual consultations allow us to meet with you via video calls or phone, making it easy to '
     'discuss your financial needs regardless of your location. We also ensure compliance with relevant regulations '
     'and tailor our services to accommodate your specific financial landscape. This approach helps us provide the '
     'same level of personalized support and expertise to all our clients, no matter where they are', 'question'),
    ('How will I know I\'m getting my money\'s worth with you?',
     'You’ll know you’re getting your money’s worth through clear, consistent updates on your '
     'portfolio’s performance and personalized financial advice. We prioritize transparency, '
     'so you’ll always understand where your money is going and how it’s working for you. Our '
     'approach focuses on achieving your specific financial goals while maximizing returns '
     'and minimizing unnecessary fees, ensuring that every decision adds real value to your '
     'financial future.', 'question'),
    ('What if I need help but I\'m not ready for a full plan',
     'If you’re not ready for a full financial plan, we offer flexible options to meet you '
     'where you are. Whether you need advice on a specific financial decision, '
     'help with budgeting, or guidance on investments, we can provide targeted support '
     'without the commitment of a comprehensive plan. This way, you can get the help you need '
     'now, and when you’re ready, we can expand our services to fit your evolving needs.', 'question'),
    ('What are Portfolio Accounting Systems?',
     'Portfolio Accounting Systems are specialized software solutions designed to track, manage, and report on '
     'investment portfolios. These systems are primarily used by financial institutions, investment firms, '
     'and individual investors to provide comprehensive accounting and reporting functions.', 'question'),
    ('Investing Basics for New Grads',
     'Investing basics for new graduates emphasize the importance of understanding financial growth and setting clear '
     'financial goals. Start by creating a budget to track income and expenses, ensuring to allocate funds for '
     'investments after covering necessities and building an emergency fund that can cover 3-6 months of expenses. '
     'Familiarize yourself with different investment options, such as stocks, bonds, mutual funds, ETFs, '
     'and real estate, while assessing your risk tolerance and the principle of diversification to minimize risk. '
     'Starting early is crucial, as time allows for compounding growth; even small investments can accumulate '
     'significantly over time. Consider retirement accounts like a 401(k) or an IRA for long-term savings. Educate '
     'yourself through books and financial news, and seek professional advice if needed. Finally, stay committed to a '
     'long-term focus and regularly review your portfolio to make necessary adjustments while remaining patient '
     'through market fluctuations.', 'info'),
    ('What is the Average Net Worth by Age?',
     'In South Africa, the average net worth varies significantly by age group, influenced by economic factors, '
     'education, and employment opportunities. For individuals under 35, the average net worth is approximately R 540,'
     '000, as many are still paying off student loans and starting their careers, resulting in lower net worth. In '
     'the 35-44 age group, the average rises to about R 1.6 million, with career advancements and home ownership '
     'contributing to increased wealth. Those aged 45-54 see their average net worth climb to around R 4 million, '
     'reflecting peak earning potential and savings accumulation. For individuals aged 55-64, the average net worth is '
     'approximately R 6.4 million as they approach retirement with substantial savings and investments. Finally, '
     'South Africans aged 65 and older have an average net worth of about R 5.8 million, often possessing significant '
     'assets despite reduced income. These figures illustrate the disparities in wealth accumulation across age '
     'groups and underscore the importance of distinguishing between average and median net worth, as the average can '
     'be skewed by exceptionally wealthy individuals, offering a less accurate representation of financial health for '
     'the broader population.', 'question'),
    ('Wealth Management vs. Investment Banking',
     'Wealth management and investment banking are two distinct areas within the financial services industry, '
     'each serving different client needs and offering unique services. Wealth management focuses on providing '
     'personalized financial planning, investment management, and advisory services to individuals, families, '
     'and businesses. Wealth managers assess clients’ financial situations, goals, and risk tolerances to develop '
     'tailored investment strategies, estate planning, tax optimization, and retirement planning. Their primary aim is '
     'to grow and preserve clients’ wealth over time while ensuring that their financial needs are met.', 'info'),
    ('2024\'s Best Provinces to Retire in South Africa',
     'When considering the best provinces to retire in South Africa in 2024, several factors such as cost of living, '
     'climate, healthcare services, and lifestyle opportunities play a crucial role. The Western Cape, '
     'known for its stunning landscapes and vibrant lifestyle, particularly in areas like Cape Town and the Garden '
     'Route, offers a mild climate, beautiful beaches, and excellent healthcare facilities. KwaZulu-Natal boasts a '
     'warm climate, rich cultural heritage, and beautiful coastline, with affordable living in areas like Durban and '
     'the North Coast. The Eastern Cape is recognized for its affordability and natural beauty, particularly in '
     'Port Elizabeth and Grahamstown, providing a quieter lifestyle with access to scenic landscapes. Mpumalanga, '
     'renowned for attractions like the Kruger National Park and Blyde River Canyon, offers a serene environment and '
     'lower cost of living. Gauteng, the most urbanized province, particularly Pretoria and Johannesburg, '
     'provides retirees with excellent healthcare and cultural activities despite a higher cost of living. Limpopo '
     'presents a tranquil setting with its rural charm and lower living costs, while the Free State appeals to '
     'retirees seeking a slower pace of life in picturesque towns like Clarens. Ultimately, the best provinces for '
     'retirement depend on individual preferences regarding lifestyle, climate, and amenities, as each offers unique '
     'advantages.', 'info')
]

layout = html.Div([
    html.Div([
        html.Div([
            html.H2([
                html.Span(['Personal'], style={'color': '#88A9C3'}),
                ' Finance Guides',
                html.Hr(style={'height': '0px', 'border': 'none', 'border-top': '2px solid', 'color': '#88A9C3'},
                        className='uk-width-small'),
            ], className='uk-text-bolder')
        ], className='uk-card uk-card-body uk-light'),
        html.Div([
            html.Div([
                html.Img(src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/tingey'
                             '-injury-law-firm-9SKhDFnw4c4-unsplash_14_11zon.webp', alt='',
                         **{'data-uk-cover': 'true'}),
                html.Canvas(width='600', height='400')
            ], className='uk-card-media-left uk-cover-container'),
            html.Div([
                html.Div([
                    html.H3([
                        html.Span(['Frequently'], style={'color': '#88A9C3'}),
                        html.Span([' Asked Questions']),
                        html.Hr(
                            style={'height': '0px', 'border': 'none', 'border-top': '2px solid', 'color': '#88A9C3'},
                            className='uk-width-small')
                    ], className='uk-text-bolder'),
                    html.Ul([
                        html.Li([
                            html.A([question], href='', className='uk-accordion-title uk-text-default uk-text-bolder'),
                            html.Div([
                                html.P(answer)
                            ], className='uk-accordion-content')
                        ], className='uk-open' if idx == 0 else None) for idx, (question, answer, _) in
                        enumerate(items[:4])
                    ], **{'data-uk-accordion': 'true'})
                ], className='uk-card-body')
            ])
        ], **{'data-uk-grid': 'true'},
            className='uk-card uk-card-secondary uk-grid-collapse uk-child-width-1-2@s uk-margin',
            style={'background-color': '#091235'}),
        html.Div([
            html.Div([
                html.Div([
                    html.H3([
                        html.Span(**{'data-uk-icon': f'icon: {icon}; ratio: 3'}, className='uk-width-auto'),
                        html.Span([question])
                    ], **{'data-uk-grid': 'true'},
                        className='uk-child-width-expand@s uk-grid-small uk-flex-middle uk-text-bolder'),
                    html.P(answer)
                ], className='uk-card uk-card-body uk-light')
            ]) for question, answer, icon in items[4:]
        ], **{'data-uk-grid': 'masonry: pack'}, className='uk-child-width-1-2@s')
    ], className='uk-container')
], className='uk-section', style={'background-color': '#2A3A58'})
