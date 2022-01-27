"""
File to store constants used in the xetra package.
"""

from enum import Enum


class S3FileTypes(Enum):
    """
    Enum to store the different types of files that can be stored in S3.
    """

    CSV = "csv"
    PARQUET = "parquet"


class MetaProcessFormat(Enum):
    """
    Formation for MetaProcess class
    """

    META_DATE_FORMAT = "%Y-%m-%d"
    META_PROCESS_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    META_SOURCE_DATE_COL = "source_date"
    META_PROCESS_COL = "datetime_of_processing"
    META_FILE_FORMAT = "csv"
