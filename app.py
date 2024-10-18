from datetime import datetime

from fasthtml.common import FastHTML, serve
from fasthtml.components import Script, Link, Body, Div, Title, Label, Span, Input, P, Button, Style, Strong, H4
from starlette.requests import Request

import admin
import advisors
import client_edit
import client_portal
import contact_us
import guides
import home
import services
import who_we_serve
from interface import nav, footer, supabase, supabase_admin
from utility_functions import get_clients, get_client

app = FastHTML(
    hdrs=(
        Script(src='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit.min.js'),
        Script(src='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit-icons.min.js'),
        Script(src='https://unpkg.com/hyperscript.org@0.9.12'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/charts.css/dist/charts.min.css'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/css/uikit.min.css'),
        Link(rel='preconnect', href='https://fonts.googleapis.com'),
        Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
        Link(rel='stylesheet',
             href='https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap'),
        Style('.charts-css {--color-1: #88A9C3; --color-2: #CD5B45; --color-3: #5F9EA0; --color-4: #FF7F50; '
              '--color-5: #CCCCFF; margin: 0 auto;} .area td {opacity: 0.5;} .column {--aspect-ratio: 4 / 4;} '
              '.bar {--aspect-ratio: 4 / 1;} .area {--aspect-ratio: 4 / 3;} .line {--aspect-ratio: 4 / 4;}')
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
            return f'Error sending OTP: {response["error"]["message"]}'
    except Exception as e:
        return f'Authentication error: {e}'


@app.route('/')
def get():
    return Body(
        Div(id='page'), footer(),
        hx_get='/home/', hx_trigger='load', hx_target='#page', hx_push_url=True, id='super-page'
    )


@app.route('/home/')
def get(req: Request, sess):
    get_clients()
    user = None
    try:
        if sess['access_token']:
            response = supabase.auth.get_user(sess['access_token'])
            user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Blue Chip Invest'), nav(user=user, current_path=req.url.path), home.page


@app.route('/home/')
def post(sess, data: dict):
    if data['sign_out'] and data['sign_out'] == 'signed-out':
        try:
            response = supabase.auth.sign_out()
            print(response)
            if response is None: sess['access_token'] = None
        except Exception as e:
            print(f'Signing out error: {e}')

    return Title('Blue Chip Invest'), nav(), home.page


@app.route('/who-we-serve/{title}')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Who We Serve'), nav(user=user, current_path=req.url.path), who_we_serve.page


@app.route('/contact-us/')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Contact Us'), nav(user=user, current_path=req.url.path), contact_us.page


@app.route('/services/')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Services'), nav(user=user, current_path=req.url.path), services.page


@app.route('/advisors/')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Advisors'), nav(user=user, current_path=req.url.path), advisors.page


@app.route('/guides/')
def get(req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    return Title('Guides'), nav(user=user, current_path=req.url.path), guides.page


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
            admin_users = ['travis@bluechipinvest.co.za', 'eugevanz@gmail.com', 'raymondanthony.m@gmail.com']
            print()
            if response.user.email in admin_users:
                return Title('Admin'), nav(user=response.user, current_path=req.url.path), admin.page(
                    user=response.user)
            else:
                return Title('Client'), nav(user=response.user, current_path=req.url.path), client_portal.page
        else:
            print(response)
    except Exception as e:
        return P(f'Authentication error: {e}', cls='uk-text-danger uk-text-bolder')


@app.route('/send-invite/')
def post(data: dict):
    try:
        response = supabase_admin.auth.admin.invite_user_by_email(data['form-invite-name'])
        if response and response.user:
            return P(f'Invite sent to {data["form-invite-name"]}', cls='uk-text-success uk-text-bolder')
        else:
            return P(f'Error sending invite: {response["error"]["message"]}', cls='uk-text-danger uk-text-bolder')
    except Exception as e:
        return P(f'Invitation error: {e}', cls='uk-text-danger uk-text-bolder')


@app.route('/edit-client/{id}/')
def get(id: str, req: Request, sess):
    try:
        response = supabase.auth.get_user(sess['access_token'])
        user = response.user
    except Exception as e:
        print(f'Authentication error: {e}')
        user = None

    client = get_client(id)
    return Title('Edit Client'), nav(user=user, current_path=req.url.path), client_edit.page(client)


@app.route('/update-client/', methods=['POST'])
def post(data: dict):
    return Div(
        Div(
            Div(
                Div(
                    Div('Account Balance', cls='uk-text-small'),
                    H4(f'R {data["account-balance"]}', cls='uk-text-bolder uk-margin-remove-top')
                ),
                Div(
                    Div(
                        Div('Account Type', cls='uk-text-small'),
                        H4(data['account-type'], cls='uk-margin-remove-top uk-text-bolder')
                    ),
                    Div(
                        Div('Account Number', cls='uk-text-small'),
                        H4(data['account-number'], cls='uk-text-bolder uk-margin-remove-top')
                    ),
                    Div(
                        Div('Last Updated', cls='uk-text-small'),
                        H4(datetime.now().strftime('%B %d, %Y'), cls='uk-text-bolder uk-margin-remove-top')
                    )
                ),
                data_uk_grid=True, cls='uk-child-width-1-2@m uk-grid-divider'
            ),
            cls='uk-card uk-card-body uk-card-default', style='background-color: #88A9C3;'
        ),
        Span(data_uk_icon='icon: trash;', cls='uk-icon-button uk-position-medium uk-position-top-right uk-light',
             style='background-color: #CD5B45;'),
        cls='uk-card uk-card-body uk-card-default uk-inline uk-width-expand'
    )


# datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')

serve()
