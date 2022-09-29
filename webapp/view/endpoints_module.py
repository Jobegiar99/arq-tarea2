"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from .containers import Container
from .services import UserService,UserAdminService
from .repositories import NotFoundError
from .input import UserInput,AdminInput
from .view_users import UserView
from .view_admin import AdminView
from .view_status import StatusView

router = APIRouter()
UserView(router)
AdminView(router)
StatusView(router)