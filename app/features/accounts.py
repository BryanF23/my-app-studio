"""APP-002 account routes for signup, login, dashboard and logout."""

from fastapi import APIRouter, Form, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from pydantic import ValidationError

from app import security
from app.schemas import LoginInput, SignupInput

router = APIRouter()


def _render(request: Request, template: str, **context):
    """Render an account page with the shared template context."""
    return request.app.state.templates.TemplateResponse(
        request=request,
        name=template,
        context=context,
    )


def _csrf(request: Request, response: Response):
    """Issue a CSRF token for the current browser session."""
    return security.csrf_token(request, response)


def _copy_cookies(source: Response, target: Response):
    """Copy cookies without overwriting the target response's content headers."""
    for cookie in source.headers.getlist("set-cookie"):
        target.raw_headers.append((b"set-cookie", cookie.encode("latin-1")))


@router.get("/api/csrf")
def api_csrf(request: Request, response: Response):
    """Provide a CSRF token for API requests."""
    return {"csrf_token": _csrf(request, response)}


@router.post("/api/signup", status_code=201)
def api_signup(request: Request, credentials: SignupInput):
    """Create a new member account through the API."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    security.limit_signup(request)
    return security.signup(
        request.app.state.settings,
        credentials.username,
        credentials.password,
    )


@router.post("/api/login")
def api_login(request: Request, response: Response, credentials: LoginInput):
    """Authenticate a user through the API."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    return security.login(request, response, credentials.username, credentials.password)


@router.get("/api/me")
def api_me(request: Request):
    """Return the currently authenticated user."""
    return security.require_user(request)


@router.post("/api/logout")
def api_logout(request: Request, response: Response):
    """Revoke the current API session."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    security.logout(request, response)
    return {"message": "Logged out"}


@router.get("/signup", include_in_schema=False)
def signup_page(request: Request):
    """Display the account registration page."""
    response = Response()
    token = _csrf(request, response)
    page = _render(
        request,
        "signup.html",
        csrf_token=token,
        username="",
        error=None,
    )
    _copy_cookies(response, page)
    return page


@router.post("/signup", include_in_schema=False)
def signup_form(
    request: Request,
    csrf_token: str = Form(""),
    username: str = Form(""),
    password: str = Form(""),
):
    """Process an account registration form."""
    response = Response()

    try:
        security.require_csrf(request, csrf_token)
        credentials = SignupInput(username=username, password=password)
        security.limit_signup(request)
        security.signup(
            request.app.state.settings,
            credentials.username,
            credentials.password,
        )

    except HTTPException as error:
        if error.status_code == 403:
            raise

        page = _render(
            request,
            "signup.html",
            csrf_token=_csrf(request, response),
            username=(credentials.username if "credentials" in locals() else ""),
            error=error.detail,
        )
        page.status_code = error.status_code
        _copy_cookies(response, page)
        return page

    except ValidationError:
        page = _render(
            request,
            "signup.html",
            csrf_token=_csrf(request, response),
            username=username[:32],
            error="Please enter a valid username and password.",
        )
        page.status_code = 422
        _copy_cookies(response, page)
        return page

    return RedirectResponse("/login", status_code=303)


@router.get("/login", include_in_schema=False)
def login_page(request: Request):
    """Display the login page."""
    response = Response()
    token = _csrf(request, response)
    page = _render(
        request,
        "login.html",
        csrf_token=token,
        username="",
        error=None,
    )
    _copy_cookies(response, page)
    return page


@router.post("/login", include_in_schema=False)
def login_form(
    request: Request,
    csrf_token: str = Form(""),
    username: str = Form(""),
    password: str = Form(""),
):
    """Process a submitted login form."""
    response = Response()

    try:
        security.require_csrf(request, csrf_token)
        credentials = LoginInput(username=username, password=password)
        security.login(
            request,
            response,
            credentials.username,
            credentials.password,
        )

    except HTTPException as error:
        if error.status_code == 403:
            raise

        page = _render(
            request,
            "login.html",
            csrf_token=_csrf(request, response),
            username=username.strip().lower()[:32],
            error=error.detail,
        )
        page.status_code = error.status_code
        _copy_cookies(response, page)
        return page

    except ValidationError:
        page = _render(
            request,
            "login.html",
            csrf_token=_csrf(request, response),
            username=username.strip().lower()[:32],
            error="Please enter valid login credentials.",
        )
        page.status_code = 422
        _copy_cookies(response, page)
        return page

    redirect = RedirectResponse("/dashboard", status_code=303)
    _copy_cookies(response, redirect)
    return redirect


@router.get("/dashboard", include_in_schema=False)
def dashboard(request: Request):
    """Display the private member dashboard."""
    user = security.authenticate(request)

    if not user:
        return RedirectResponse("/login", status_code=303)

    response = Response()
    token = _csrf(request, response)
    page = _render(
        request,
        "dashboard.html",
        user=user,
        csrf_token=token,
    )
    _copy_cookies(response, page)
    return page


@router.post("/logout", include_in_schema=False)
def logout_form(
    request: Request,
    csrf_token: str = Form(""),
):
    """Process logout and revoke the browser session."""
    response = Response()
    security.require_csrf(request, csrf_token)
    security.logout(request, response)

    redirect = RedirectResponse("/login", status_code=303)
    _copy_cookies(response, redirect)
    return redirect
