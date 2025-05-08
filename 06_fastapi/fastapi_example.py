from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

class UserSignUp(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "Chai App"
    admin_email: str = "admin@chai.com"

def getSettings():
    return Settings()

app = FastAPI()

@app.route("/signup")
def userSignup(user: UserSignUp):
    return {"message": f"User - {user.username} signed up successfully"}

@app.route("/settings")
def adminSettings(settings: Settings = Depends(getSettings)):
    return settings