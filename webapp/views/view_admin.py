from .endpoints_module import router

class AdminView:
        def __init__(self,router):
                self.router = router

        @self.router.get("/admins")
        @inject
        def get_admin_users(
                self,
                user_admin_service: UserAdminService = Depends(Provide[Container.user_admin_service]),
        ):
        return user_admin_service.get_admin_users()

        @self.router.post("/admins")
        @inject
        def add_admin_user(
                self,
                admin_input: AdminInput,
                user_admin_service: UserAdminService = Depends(Provide[Container.user_admin_service]),
        ):
        return user_admin_service.create_admin(admin_input)