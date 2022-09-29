from .endpoints_module import router

class StatusView:
    def __init__(self,router):
        self.router = router

    @self.router.get("/status")
    def get_status(self,):
        return {"status": "OK"}