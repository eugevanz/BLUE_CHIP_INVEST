from fasthtml.common import FastHTML, serve
from fasthtml.components import Script, Link, Body, Div, Title

import admin
import advisors
import contact_us
import guides
import services
import who_we_serve
from interface import nav, potential_interest_calculators, hero, subhero, advisor_section, serve_section, \
    metric_section, preserve_section, whatwedo_section, testimonials_section, guides_section, footer

app = FastHTML(
    hdrs=(
        Script(src='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit.min.js'),
        Script(src='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit-icons.min.js'),
        Script(src='https://unpkg.com/hyperscript.org@0.9.12'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/css/uikit.min.css'),
        Link(rel='preconnect', href='https://fonts.googleapis.com'),
        Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
        Link(rel='stylesheet',
             href='https://fonts.googleapis.com/css2?family=Playfair+Display+SC:ital,wght@0,700;0,900;1,'
                  '700&display=swap')
    ), surreal=False, pico=False
)


@app.route('/')
def get():
    return Body(
        potential_interest_calculators(),
        hx_get='/home/', hx_trigger='load', hx_swap='innerHTML', id='page'
    )


@app.route('/home/')
def get():
    return Title('Blue Chip Invest'), nav(), Div(
        hero(),
        subhero(),
        advisor_section(),
        serve_section(),
        metric_section(),
        preserve_section(),
        whatwedo_section(),
        testimonials_section(),
        guides_section(),
        footer()
    )


@app.route('/who-we-serve/{title}')
def get():
    return Title('Who We Serve'), nav(), who_we_serve.page


@app.route('/contact-us/')
def get():
    return Title('Contact Us'), nav(), contact_us.page


@app.route('/services/')
def get():
    return Title('Services'), nav(), services.page


@app.route('/advisors/')
def get():
    return Title('Advisors'), nav(), advisors.page


@app.route('/guides/')
def get():
    return Title('Guides'), nav(), guides.page


@app.route('/admin/')
def get():
    return Title('Admin'), nav(), admin.page


serve()
