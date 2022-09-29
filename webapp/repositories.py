"""Repositories module."""

from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from .models import User,UserAdmin
from .input import UserInput,AdminInput


class UserRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[User]:
        with self.session_factory() as session:
            return session.query(User).all() 

    def get_by_id(self, user_id: int) -> User:
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundError(user_id)
            return user

    def add(self, user_input: UserInput) -> User:
        with self.session_factory() as session:
            user = User(
                email = user_input.email,
                hashed_password = user_input.hashed_password,
                is_active = user_input.is_active,
                first_name = user_input.first_name,
                last_name = user_input.last_name,
                phone = user_input.phone,
                )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, user_id: int) -> None:
        with self.session_factory() as session:
            entity: User = session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            session.commit()

class UserAdminRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[UserAdmin]:
        with self.session_factory() as session:
            return session.query(UserAdmin).all() 

    
    def add(self, admin_input: AdminInput) -> User:
        with self.session_factory() as session:
            user_admin = UserAdmin(
                user_id = admin_input.user_id,
                is_admin = admin_input.is_admin,
                )
            session.add(user_admin)
            session.commit()
            session.refresh(user_admin)
            return user_admin


class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class UserNotFoundError(NotFoundError):

    entity_name: str = "User"
