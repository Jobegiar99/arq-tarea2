"""Application module."""

from fastapi import FastAPI

from .containers import Container
from .views import view_admin, view_status, view_users


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(view_admin.router)
    app.include_router(view_status.router)
    app.include_router(view_users.router)
    return app


app = create_app()
