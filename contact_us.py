from fasthtml.components import Button, Div, H3, Span, Br, Hr, P, Form, Input, Textarea

from interface import return_button

page = Div(
    Div(
        return_button,
        Div(
            Div(
                Div(
                    H3(Span('Request', style='color: #45ACFF'), ' an', Br(), 'Appointment', cls='uk-text-bolder'),
                    Hr(style='height: 0px; border: none; border-top: 2px solid;',
                       cls='uk-width-small uk-text-primary'),
                    P('Need help with something? Want a demo? Reach out to our friendly team, and we\'ll get back to you in '
                      'no time.'),
                    Div(
                        Div(
                            Div(
                                Div(
                                    Span(data_uk_icon='icon: location; ratio: 1.8', cls='uk-icon'),
                                    cls='uk-width-auto'
                                ),
                                Div(
                                    Div('Location', cls='uk-text-large uk-text-bolder'),
                                    Div('No. 30 Pinetown, Durban 3610', cls='uk-text-small')
                                ),
                                cls='uk-child-width-expand@s uk-grid-small'
                            )
                        ),
                        Div(
                            Div(
                                Div(
                                    Span(data_uk_icon='icon: receiver; ratio: 1.8', cls='uk-icon'),
                                    cls='uk-width-auto'
                                ),
                                Div(
                                    Div('Phone', cls='uk-text-large uk-text-bolder'),
                                    Div('0860 258 2447', cls='uk-text-small')
                                ),
                                cls='uk-child-width-expand@s uk-grid-small'
                            )
                        ),
                        Div(
                            Div(
                                Div(
                                    Span(data_uk_icon='icon: mail; ratio: 1.8', cls='uk-icon'),
                                    cls='uk-width-auto'
                                ),
                                Div(
                                    Div('Email', cls='uk-text-large uk-text-bolder'),
                                    Div('admin@bluechipinvest.co.za', cls='uk-text-small')
                                ),
                                cls='uk-child-width-expand@s uk-grid-small'
                            )
                        ),
                        Div(
                            Div(
                                Div(
                                    Span(data_uk_icon='icon: mail; ratio: 1.8', cls='uk-icon'), cls='uk-width-auto'
                                ),
                                Div(
                                    Div('Open hours', cls='uk-text-large uk-text-bolder'),
                                    Div('Mon - Sat, 08:00 - 16:00', cls='uk-text-small')
                                ),
                                cls='uk-child-width-expand@s uk-grid-small'
                            )
                        ),
                        data_uk_grid=True,
                        cls='uk-grid-match uk-child-width-1-2@m'
                    ),
                    cls='uk-card uk-card-body'
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
                               cls='uk-button uk-button-primary uk-button-large uk-width-1-1 uk-margin-top')
                    ),
                    cls='uk-card uk-card-primary uk-card-body'
                )
            ),
            data_uk_grid=True, cls='uk-child-width-expand@s'
        ),
        cls='uk-container'
    ),
    cls='uk-section uk-light', style='background-color: #00213B'
)
