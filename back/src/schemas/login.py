from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "admin",
                    "password": "password",
                }
            ]
        }
    }