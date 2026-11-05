"""APP-003 server-enforced member/admin permissions."""

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app import security

router = APIRouter()


@router.get("/api/admin")
def api_admin(request: Request):
    """Allow only current database administrators."""
    user = security.require_admin(request)

    return {
        "message": "Admin access granted",
        "username": user["username"],
        "role": user["role"],
    }


@router.get("/admin", include_in_schema=False)
def admin_page(request: Request):
    """Protect the administration webpage."""
    user = security.authenticate(request)

    if user is None:
        return RedirectResponse("/login", status_code=303)

    if user["role"] != "admin":
        return request.app.state.templates.TemplateResponse(
            request=request,
            name="admin.html",
            context={"user": user, "allowed": False},
            status_code=403,
        )

    return request.app.state.templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={"user": user, "allowed": True},
    )
