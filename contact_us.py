from fasthtml.components import Button, Div, H3, Span, Br, Hr, P, Form, Input, Textarea

page = Div(
    Div(
        Div(
            Div(
                Div(
                    H3(Span('Request', style='color: #88A9C3'), ' an', Br(), 'Appointment', cls='uk-text-bolder'),
                    Hr(style='height: 0px; border: none; border-top: 2px solid; color: #88A9C3;',
                       cls='uk-width-small'),
                    P('Need help with something? Want a demo? Reach out to our friendly team, and we\'ll get back to you in '
                      'no time.'),
                    Div(
                        Div(
                            Div(data_uk_icon='icon: location; ratio: 1.8', cls='uk-icon'),
                            Div('Location', cls='uk-text-large uk-text-bolder'),
                            Div('Unit 17, No.30 Surprise Road, Pinetown, 3610', cls='uk-text-small')
                        ),
                        Div(
                            Div(data_uk_icon='icon: receiver; ratio: 1.8', cls='uk-icon'),
                            Div('Phone', cls='uk-text-large uk-text-bolder'),
                            Div('0860 258 2447', cls='uk-text-small')
                        ),
                        Div(
                            Div(data_uk_icon='icon: mail; ratio: 1.8', cls='uk-icon'),
                            Div('Email', cls='uk-text-large uk-text-bolder'),
                            Div('info@', Br(), 'bluechipinvest.co.za', cls='uk-text-small')
                        ),
                        Div(
                            Div(data_uk_icon='icon: mail; ratio: 1.8', cls='uk-icon'),
                            Div('Open hours', cls='uk-text-large uk-text-bolder'),
                            Div('Mon - Sat, 08:00 - 16:00', cls='uk-text-small')
                        ),
                        data_uk_grid=True,
                        cls='uk-grid-match uk-child-width-1-2'
                    ),
                    cls='uk-card uk-card-body uk-light'
                )
            ),
            Div(
                Div(
                    Form(
                        Div(
                            Div(
                                Span(data_uk_icon='icon: user', cls='uk-form-icon'),
                                Input(type='text', placeholder='Your name', aria_label='Not clickable icon',
                                      cls='uk-input uk-width-large'),
                                cls='uk-inline'
                            ),
                            cls='uk-margin'
                        ),
                        Div(
                            Div(
                                Span(data_uk_icon='icon: mail', cls='uk-form-icon'),
                                Input(type='text', placeholder='you@company.com', aria_label='Email',
                                      cls='uk-input uk-width-large'),
                                cls='uk-inline'
                            ),
                            cls='uk-margin'
                        ),
                        Div(
                            Textarea(rows='5', placeholder='Leave a message', aria_label='Message',
                                     cls='uk-textarea'),
                            cls='uk-margin'
                        ),
                        Div('No worries, your info stays with us. We don’t do the oversharing thing.',
                            cls='uk-text-small uk-margin'),
                        Button('Send your message',
                               cls='uk-button uk-button-large uk-width-1-1 uk-margin-top uk-text-bolder',
                               style='color: #88A9C3; background-color: #091235')
                    ),
                    cls='uk-card uk-card-body uk-card-default'
                )
            ),
            data_uk_grid=True, cls='uk-child-width-1-2@m'
        ),
        cls='uk-container'
    ),
    cls='uk-section', style='background-color: #091235'
)
