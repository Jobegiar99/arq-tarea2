def class UserView:
    def __init__(self,router):
        self.router = router

    @self.router.get("/users")
    @inject
    def get_list(
        self,
        user_service: UserService = Depends(Provide[Container.user_service]),
    ):
        return user_service.get_users()


    @self.router.get("/users/{user_id}")
    @inject
    def get_by_id(
        self,
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
    ):
        try:
            return user_service.get_user_by_id(user_id)
        except NotFoundError:
            return Response(status_code=status.HTTP_404_NOT_FOUND)


    @self.router.post("/users", status_code=status.HTTP_201_CREATED)
    @inject
    def add(
        self,
        user_input: UserInput,
        user_service: UserService = Depends(Provide[Container.user_service])
    ):
        return user_service.create_user(user_input)


    @self.router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
    @inject
    def remove(
        self,
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
    ):
        try:
            user_service.delete_user_by_id(user_id)
        except NotFoundError:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status_code=status.HTTP_204_NO_CONTENT)