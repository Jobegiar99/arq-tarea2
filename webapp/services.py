"""Services module."""

from uuid import uuid4
from typing import Iterator

from .repositories import UserRepository,UserAdminRepository
from .models import User,UserAdmin
from .input import UserInput,AdminInput


class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self,user_input : UserInput) -> User:
        return self._repository.add(user_input)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)


class UserAdminService:

    def __init__(self, user_admin_repository: UserAdminRepository) -> None:
        self._repository: UserAdminRepository = user_admin_repository

    def get_admin_users(self) -> Iterator[UserAdmin]:
        return self._repository.get_all()
    
    def create_admin(self,admin_input : AdminInput) -> UserAdmin:
        return self._repository.add(admin_input)

    