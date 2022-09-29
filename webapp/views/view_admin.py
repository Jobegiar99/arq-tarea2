from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from ..containers import Container
from ..services import UserAdminService
from ..DTO.input import AdminInput


router = APIRouter(prefix="/admins")


@router.get("/")
@inject
def get_admin_users(
        user_admin_service: UserAdminService = Depends(
            Provide[Container.user_admin_service]),
):
    return user_admin_service.get_admin_users()


@router.post("/")
@inject
def add_admin_user(
        admin_input: AdminInput,
        user_admin_service: UserAdminService = Depends(
            Provide[Container.user_admin_service]),
):
    return user_admin_service.create_admin(admin_input)
