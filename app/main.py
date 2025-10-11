import typer
from app.settings import settings
from app.commands import db_info
from app.utils.logger import get_logger
# from dataclasses import dataclass
# import sqlparse

logger = get_logger(__name__)
app = typer.Typer()


@app.command(".dbinfo")
def dbinfo(
    db_path: str = typer.Option(
        settings.db_path, help="Path to SQlite DB", show_default=False
    ),
):
    result = db_info(db_path)
    typer.echo(f"database page size: {result['page_size']}")


if __name__ == "__main__":
    app()
