import dash
from dash import Dash, html

from interface import nav, footer

app = Dash(
    external_scripts=[
        'https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit.min.js',
        'https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit-icons.min.js',
        'https://unpkg.com/hyperscript.org@0.9.12'
    ],
    external_stylesheets=[
        'https://cdn.jsdelivr.net/npm/charts.css/dist/charts.min.css',
        'https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/css/uikit.min.css',
        'https://fonts.googleapis.com',
        'https://fonts.gstatic.com',
        'https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap'
    ],
    use_pages=True
)
server = app.server

app.layout = html.Div([
    nav(),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)
