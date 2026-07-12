from fastapi import HTTPException


class AuthService:

    USERNAME = "admin"
    PASSWORD = "admin123"

    @staticmethod
    def login(username: str, password: str):

        if (
            username == AuthService.USERNAME
            and password == AuthService.PASSWORD
        ):
            return {
                "status": "success",
                "message": "Login Successful"
            }

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )