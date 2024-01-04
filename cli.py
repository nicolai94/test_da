import click

from src import User
from src.db import SessionLocal
from src.logger import get_logger

logger = get_logger("cli")

@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--login', prompt='Enter login', help='User login')
@click.option('--password', prompt='Enter password', hide_input=True, confirmation_prompt=True, help='User password')
def createuser(login: str, password: str) -> None:
    try:
        with SessionLocal() as session:
            user = User(login=login, password=password)
            session.add(user)
            session.commit()
            logger.info("Successfully created user")
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")



if __name__ == "__main__":
    cli()
