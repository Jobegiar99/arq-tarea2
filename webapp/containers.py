"""Containers module."""

from dependency_injector import containers, providers

from .database import Database
from .repositories import UserRepository,UserAdminRepository
from .services import UserService,UserAdminService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )
    
    user_admin_repository = providers.Factory(
        UserAdminRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
    user_admin_service = providers.Factory(
        UserAdminService,
        user_admin_repository=user_admin_repository,
    )
