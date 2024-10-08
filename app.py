from fasthtml.common import FastHTML, serve
from fasthtml.components import Script, Link, Body, Div, Title, Label, Span, Input, P, Button, Style, Strong
from starlette.requests import Request

import admin
import advisors
import contact_us
import guides
import home
import services
import who_we_serve
from interface import nav, footer, supabase

app = FastHTML(
    hdrs=(
        Script(src='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit.min.js'),
        Script(src='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit-icons.min.js'),
        Script(src='https://unpkg.com/hyperscript.org@0.9.12'),
        Script(src='https://cdn.plot.ly/plotly-latest.min.js'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/css/uikit.min.css'),
        Link(rel='preconnect', href='https://fonts.googleapis.com'),
        Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
        Link(rel='stylesheet',
             href='https://fonts.googleapis.com/css2?family=Playfair+Display+SC:ital,wght@0,700;0,900;1,'
                  '700&display=swap'),
        Style('input::placeholder {color: #091235;}')
    ), surreal=False, pico=False, secret_key='theraininspain'
)


def user_login(email):
    try:
        response = supabase.auth.sign_in_with_otp({
            'email': email,
            'options': {'should_create_user': False}
        })
        if response and response['error'] is None:
            print(response)
            return 'OTP sent successfully'
        else:
            return f'Error sending OTP: response[\'error\'][\'message\']'
    except Exception as e:
        return f'Authentication error: {e}'


history = False


@app.route('/')
def get():
    return Body(
        Div(id='page'), footer(),
        hx_get='/home/', hx_trigger='load', hx_target='#page', hx_push_url=True
    )


@app.route('/home/')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Blue Chip Invest'), nav(user=user, history=req.url.path), home.page


@app.route('/who-we-serve/{title}')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Who We Serve'), nav(user=user, history=req.url.path), who_we_serve.page


@app.route('/contact-us/')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Contact Us'), nav(user=user, history=req.url.path), contact_us.page


@app.route('/services/')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Services'), nav(user=user, history=req.url.path), services.page


@app.route('/advisors/')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Advisors'), nav(user=user, history=req.url.path), advisors.page


@app.route('/guides/')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Guides'), nav(user=user, history=req.url.path), guides.page


@app.route('/request-code/', methods=['post'])
def post(data: dict):
    try:
        response = supabase.auth.sign_in_with_otp({
            'email': data['form-username'],
            'options': {'should_create_user': False}
        })
        if response and response.user is None:
            return Div(
                P('Please enter the ', Strong('verification code'),
                  ' that was sent to your email. This code is required to verify your identity and complete the login '
                  'process.',
                  cls='uk-text-small', style='color: #091235'),
                Div(
                    Label('CODE', cls='uk-form-label'),
                    Div(
                        Span(cls='uk-form-icon', data_uk_icon='icon: lock'),
                        Input(cls='uk-input uk-form-width-large', type='number',
                              aria_label='CODE', name='form-code'),
                        cls='uk-inline'
                    ),
                    cls='uk-margin'
                ),
                Div(
                    Button('Sign In', cls='uk-button uk-button-large uk-width-1-1 uk-light uk-margin-top',
                           style='background-color: #091235', hx_post=f'/admin/', hx_target='#page',
                           hx_include="[name='form-username'],[name='form-code']"),
                    cls='uk-margin'
                )
            )
        else:
            return P(f'Error sending OTP: response[\'error\'][\'message\']',
                     cls='uk-text-danger uk-text-bolder uk-margin')
    except Exception as e:
        return P(f'Authentication error: {e}', cls='uk-text-danger uk-text-bolder uk-margin')


@app.route('/admin/', methods=['post'])
def post(data: dict, req: Request, sess):
    try:
        if data:
            response = supabase.auth.verify_otp(
                {'email': data['form-username'], 'token': data['form-code'], 'type': 'email'}
            )
            sess['access_token'] = response.session.access_token
        else:
            response = supabase.auth.get_user(jwt=sess['access_token'])

        if response and response.user:
            return Title('Admin'), nav(user=response.user, history=req.url.path), admin.page
        else:
            print(response)
    except Exception as e:
        return P(f'Authentication error: {e}', cls='uk-text-danger uk-text-bolder')


@app.route('/send-invite/')
def post(data: dict):
    try:
        response = supabase.auth.sign_in_with_otp({
            'email': data['form-invite-name'],
            'options': {'should_create_user': True}
        })
        if response and response.user is None:
            return P(f'Invite sent to {data["form-invite-name"]}', cls='uk-text-success uk-text-bolder')
        else:
            return P(f'Error sending invite: response[\'error\'][\'message\']', cls='uk-text-danger uk-text-bolder')
    except Exception as e:
        return P(f'Invitation error: {e}', cls='uk-text-danger uk-text-bolder')


serve()
