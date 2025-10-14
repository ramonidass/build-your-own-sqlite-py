import struct
from app.utils.logger import get_logger
from typing import Any
# from dataclasses import dataclass
# import sqlparse

logger = get_logger(__name__)


def db_info(db_path: str) -> Any:
    try:
        with open(db_path, "rb") as database_file:
            # INFO: Header is 100 bytes
            database_header = database_file.read(100)

            # INFO: First 16 bytes of file confirms its a valid SQlite database
            #      Offset 16-17 represents the database page size in bytes
            page_size = int.from_bytes(database_header[16:18], byteorder="big")

            database_without_header = database_file.read(page_size - 100)
            # INFO: One-byte flag at offset 0 after header is the b-tree page type.
            # page_type = struct.unpack_from(">B", database_without_header, 0)[0]

            # INFO: The number of cells is a 2-byte integer at offset 3. Format '>H'
            #        (Big-endian Unsigned Short)
            cell_count = struct.unpack_from(">H", database_without_header, 3)[0]

        return {
            "page_size": page_size,
            "number_of_tables": cell_count,
        }

    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Invalid database file: {e}")
        return None
