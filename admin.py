from fasthtml.components import Div

page = Div(
    Div(
        Div(
            Div(
                Div('Item', cls='uk-card uk-card-default uk-card-body')
            ),
            Div(
                Div('Item', cls='uk-card uk-card-default uk-card-body')
            ),
            Div(
                Div('Item', cls='uk-card uk-card-default uk-card-body')
            ),
            Div(
                Div('Item', cls='uk-card uk-card-default uk-card-body')
            ),
            data_uk_grid=True, cls='uk-child-width-expand@s uk-text-center'
        ),
        cls='uk-padding'
    ),
    cls='uk-section uk-light', style='background-color: #00213B'
)
