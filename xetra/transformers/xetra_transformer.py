"""Xetra ETL Component"""

from typing import NamedTuple
import logging
from xetra.common.s3 import S3BucketConnector


class XetraSourceConfig(NamedTuple):
    """
    Class for source configuration data

    :param src_first_extract_date: determines the date for extracting the source
    :param src_columns: source column names
    :param src_col_date: column name for date in source
    :param src_col_isin: column name for isin in source
    :param src_col_time: column name for time in source
    :param src_col_start_price: column name for starting price in source
    :param src_col_min_price: column name for minimum price in source
    :param src_col_max_price: column name for maximum price in source
    :param src_col_traded_vol: column name for traded volume in source
    """

    src_first_extract_date: str
    src_columns: list
    src_col_date: str
    src_col_isin: str
    src_col_time: str
    src_col_start_price: str
    src_col_min_price: str
    src_col_max_price: str
    src_col_traded_vol: str


class XetraTargetConfig(NamedTuple):
    """
    Class for target configuration data

    :param trg_col_isin: column name for isin in target
    :param trg_col_date: column name for date in target
    :param trg_col_op_price: column name for opening price in target
    :param trg_col_clos_price: column name for closing price in target
    :param trg_col_min_price: column name for minimum price in target
    :param trg_col_max_price: column name for maximum price in target
    :param trg_col_dail_trad_vol: column name for daily traded volume in target
    :param trg_ch_prev_clos: column name for change to previous day's closing price in target
    :param trg_key: basic key of target file
    :param trg_key_date_format: date format of target file
    :param trg_format: file format of the target file
    """

    trg_col_isin: str
    trg_col_date: str
    trg_col_op_price: str
    trg_col_clos_price: str
    trg_col_min_price: str
    trg_col_max_price: str
    trg_col_dail_trad_vol: str
    trg_ch_prev_clos: str
    trg_key: str
    trg_key_date_format: str
    trg_format: str


class XetraETL:
    """
    Reads the Xetra data, transforms and writes the transformed to target
    """

    def __init__(
        self,
        s3_bucket_src: S3BucketConnector,
        s3_bucket_trg: S3BucketConnector,
        meta_key: str,
        src_args: XetraSourceConfig,
        trg_args: XetraTargetConfig,
    ):

        """
        Constructor for XetraTransformer

        :param s3_Bucket_src: connection to source S3 bucket
        :param s3_Bucket_trg: connection to target S3 bucket
        :param meta_key: used as self.meta_key -> key of the meta file
        :param src_args: NamedTouple class with source configuration data
        :param trg_args: NamedTouple class with target configuration data
        """
        self._logger = logging.getLogger(__name__)
        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_trg = s3_bucket_trg
        self.meta_key = meta_key
        self.src_args = src_args
        self.trg_args = trg_args
        # self.extract_date =
        # self.extract_date_list =
        # self.meta_update_list =

    def extract(self):
        pass

    def transform_report1(self):
        pass

    def load(self):
        pass

    def etl_report1(self):
        """
        Extract, transform and load to create report 1
        """
        # Extraction
        data_frame = self.extract()

        # Transformation
        data_frame = self.transform_report1(data_frame)

        # Load
        self.load(data_frame)

        return True
