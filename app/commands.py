import typer
from app.utils.logger import get_logger
from typing import Any
# from dataclasses import dataclass
# import sqlparse

logger = get_logger(__name__)


def db_info(db_path: str) -> Any:
    try:
        with open(db_path, "rb") as database_file:
            # INFO: First 16 bytes of file confirms its a valid SQlite database
            database_file.seek(16)  # Skip the first 16 bytes of the header
            page_size = int.from_bytes(database_file.read(2), byteorder="big")
        return {"page_size": page_size}

    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Invalid database file: {e}")
        typer.Exit(1)
