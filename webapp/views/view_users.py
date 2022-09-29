from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from ..containers import Container
from ..services import UserService
from ..repositories import NotFoundError
from ..DTO.input import UserInput


router = APIRouter(prefix="/users")


@router.get("/")
@inject
def get_list(
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.get_users()


@router.get("/{user_id}")
@inject
def get_by_id(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        return user_service.get_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def add(
    user_input: UserInput,
    user_service: UserService = Depends(Provide[Container.user_service])
):
    return user_service.create_user(user_input)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        user_service.delete_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
