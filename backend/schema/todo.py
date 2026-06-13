from pydantic import BaseModel, field_validator, Field

class Todo(BaseModel):
    title: str
    body: str
    completed: bool = False

class Auth(BaseModel):
    name: str
    email: str
    password: str = Field(min_lenth=8) # Pydantic v2

    @field_validator("password") # Custom Validation
    @classmethod
    def validate_password(cls, value):
        # if len(value)<8: ### this is an alternate method to validate that password must contain minimum of 8 char
        #     raise ValueError("Password must have 8 characters of length")

        if not any(c.isupper() for c in value):
            raise ValueError("Password must contain atleast 1 Uppercase letter")

        if not any(c.isdigit() for c in value):
            raise ValueError("Password must contain atleast 1 digit")