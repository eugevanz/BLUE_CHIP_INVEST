import asyncio
import json
import os
import smtplib
from contextlib import asynccontextmanager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from redis_om import Migrator
from starlette.middleware.base import RequestResponseEndpoint
from supabase import create_client

from routes import admin_collection
from routes import chart_collection
from routes import financial_tools_collection

templates = Jinja2Templates(directory="templates")


@asynccontextmanager
async def lifespan(_: FastAPI):
    app.state.EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
    app.state.EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    supabase_url = os.environ.get('SUPABASE_URL')
    supabase_key = os.environ.get('SUPABASE_KEY')
    supabase_service_role_key = os.environ.get('SUPABASE_SERVICE_ROLE_KEY')
    # SUPABASE_PASSWORD = os.environ.get('SUPABASE_PASSWORD')
    app.state.supabase_ = create_client(supabase_url=supabase_url, supabase_key=supabase_key)
    app.state.supabase_admin = create_client(supabase_url=supabase_url, supabase_key=supabase_service_role_key)

    Migrator().run()
    with open("static/data.json", "r") as file:
        app.state.data = json.load(file)

    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(financial_tools_collection.router)
app.include_router(admin_collection.router)
app.include_router(chart_collection.router)


# async def auth_middleware(request: Request, call_next: RequestResponseEndpoint) -> Response:
#     protected_routes = ["/client/", "/admin/"]
#     if any(request.url.path.startswith(route) for route in protected_routes):
#         user_id = request.cookies.get("user_id")
#         if not user_id:
#             return RedirectResponse("/login/")
#     response = await call_next(request)
#     return response
#
#
# app.middleware('http')(auth_middleware)


# ------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={
            "ctas": app.state.data["ctas"], "whatwedo": app.state.data["whatwedo"],
            "testimonials": app.state.data["testimonials"],
            "whoweserve": app.state.data["whoweserve"]
        }
    )


@app.get("/home/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html", context={}
    )


@app.get("/advisors/", response_class=HTMLResponse)
async def get(request: Request):
    advisors = [
        dict(name='Aidan Mercer', position='Senior Investment Strategist'),
        dict(name='Fiona Drake', position='Chief Financial Officer (CFO)'),
        dict(name='Liam Caldwell', position='Wealth Management Advisor'),
        dict(name='Chloe Rutherford', position='Portfolio Manager'),
        dict(name='Ethan Carrington', position='Head of Corporate Finance'),
        dict(name='Isabelle Thornton', position='Private Relationship Manager'),
        dict(name='Marcus Ellison', position='Director of Risk Management'),
        dict(name='Sophia Bennett', position='Chief Compliance Officer (CCO)')
    ]
    return templates.TemplateResponse(
        request=request, name="advisors.html", context={"advisors": advisors}
    )


@app.get("/services/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="services.html", context={"services": app.state.data["services"]}
    )


@app.get("/contact-us/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="contact-us.html", context={}
    )


@app.get("/guides/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="guides.html", context={"qas": app.state.data["qas"]}
    )


@app.get("/who-we-serve/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="who-we-serve.html", context={"whoweserve": app.state.data["whoweserve"]}
    )


@app.get("/financial-tools/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        request=request, name="financial-tools.html", context={}
    )


# SENDING EMAILS

async def send_email(name: str, sender_email: str, message: str):
    msg = MIMEMultipart()
    msg["Subject"] = "New contact from bluechip-invest.co.za"
    msg["From"] = sender_email
    msg["To"] = "blueche3j9g3@bluechip-invest.co.za"

    # Attach plain text and HTML versions
    msg.attach(MIMEText(message, "plain"))
    msg.attach(MIMEText(f"<html><body><p>{name}</p><p>{message}</p></body></html>", "html"))

    def smtp_send():
        try:
            with smtplib.SMTP_SSL("webmail.bluechip-invest.co.za", 465) as server:
                server.login(app.state.EMAIL_LOGIN, app.state.EMAIL_PASSWORD)
                server.send_message(msg)
        except Exception as e:
            print(f"Email sending failed: {e}")  # Log errors (replace with proper logging in production)

    await asyncio.to_thread(smtp_send)


@app.post("/send-contact-form/", response_class=HTMLResponse)
async def post(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    await send_email(name, email, message)
    return HTMLResponse(content="""<article class="uk-article">
    <h1 class="uk-article-title">We look forward to the journey ahead!</h1>
    <p class="uk-article-meta">Your message has been sent</p>
    <p class="uk-text-lead">Thank you for reaching out to Blue Chip Investments! We appreciate your interest and the 
    opportunity to help you navigate the world of smart investing.</p>
    </article>""")
