from pydantic import BaseModel

class UserInput(BaseModel):
    email : str
    hashed_password : str
    is_active : bool
    first_name : str
    last_name : str
    phone : str

class AdminInput(BaseModel):
    user_id : int
    is_admin : bool
    