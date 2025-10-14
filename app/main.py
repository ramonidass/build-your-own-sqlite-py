import typer
from app.commands import db_info
from app.utils.logger import get_logger
# from dataclasses import dataclass
# import sqlparse

logger = get_logger(__name__)
app = typer.Typer()

commands = {
    ".dbinfo": lambda db_path: typer.echo(
        f"database page size: {db_info(db_path)['page_size']}\nnumber of tables: {
            db_info(db_path)['number_of_tables']
        }\n"
    ),
}


@app.callback(invoke_without_command=True)
def main(
    db_path: str = typer.Argument(help="Path to SQLite DB"),
    command: str = typer.Argument(help="Command"),
):
    if command in commands:
        commands[command](db_path)
    else:
        typer.echo("Unknown command")


if __name__ == "__main__":
    app()
