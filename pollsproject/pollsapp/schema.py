from ninja import Schema

class ProfileSchema(Schema):
    profile_id_int: int
    f_name: str
    l_name: str
    email: str
    company: str
    position: str
    looking_for: str

class NotFoundSchema(Schema):
    message: str