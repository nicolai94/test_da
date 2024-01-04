from sqladmin.authentication import AuthenticationBackend
from sqlalchemy import select
from starlette.requests import Request

from src import User
from src.admin.exceptions import UserDoesNotExistsException
from src.db import SessionLocal
from src.logger import get_logger

logger = get_logger('auth')


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        with SessionLocal() as session:
            stmt = select(User).where(User.login == username, User.password == password)
            try:
                user = session.execute(statement=stmt).one()
            except:
                logger.info("User not found")
                raise UserDoesNotExistsException
        token = f'token_{user}'

        request.session.update({"access_token": token})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()

        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("access_token")

        if not token:
            return False

        return True
