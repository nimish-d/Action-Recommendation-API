#####################################################################
# Copyright(C), 2022 IHX Private Limited. All Rights Reserved
# Unauthorized copying of this file, via any medium is
# strictly prohibited
#
# Proprietary and confidential
# email: care@ihx.in
#####################################################################
from dataclasses import dataclass
import os
import sys
import time
from datetime import datetime
import tempfile

from fastapi import APIRouter, HTTPException, UploadFile

from app.core import logger
from app.utils import utilities as U 
from app.utils import constants as C 
from app.schema.Action_Recommendation_API import ClassiferResponse

router = APIRouter(prefix="/recommendation")
#logger = logger.log_setup(cfg, "app")
# create a temporary directory for processing
temp_dirpath = tempfile.mkdtemp()

@router.post("/template", response_model=ClassiferResponse)
async def Classifer(file: UploadFile):
    """API route to Classifer Claims."""
    _response = {
        "Transaction_Info": {
                        "Transaction_ID": "1234",
                        "Received_TS" : "",
                        "Processed_TS" : ""
                    },
        }
    # 1. Get the line items
    start_time = time.time()
    start_dt = datetime.now()
    trxId = start_dt.strftime(r"%Y%m%d%H%M%S%f")
    logger.info(
        f"{U.prepend_msg(trxId)}{C.HEADER_10} Received Request {C.HEADER_10}"
    )
    try:
        # Begin process
        logger.info(
            f"{U.prepend_msg(trxId)} - Begin Processing Request -> {start_time}"
        )
        end_time = time.time()
        logger.info(
            f"{U.prepend_msg(trxId)} - End Processing Request -> {end_time} - Time Taken -> {end_time - start_time}"
        )
        end_dt = datetime.now()
        _response['Transaction_Info']['Transaction_ID'] = trxId
        _response['Transaction_Info']['Received_TS'] = start_dt
        _response['Transaction_Info']['Processed_TS'] = end_dt
    except Exception as e:
        logger.error(
            f"{U.prepend_msg(trxId)} - there's an error uploading file. Please try again!!!",
            exc_info=True,
        )
        error_message = {
            "Status": C.ERROR,
            "Error": "Error while Uploading file. TRY AGAIN!!",
            "Error-Message": str(e),
        }
        raise HTTPException(status_code=418, detail= f"Error - there's an error uploading file. Please try again!!!")
    logger.info(
            f"{U.prepend_msg(trxId)} - Response Request -> {_response}"
        )
    return _response


@router.post("/", response_model=ClassiferResponse)
async def input_filter(PayerId:int, ICD:str):
    """API route to get action recommendation stored in a database given a set of filter values"""
    _response = {
        "Transaction_Info": {
                        "Transaction_ID": "1234",
                        "Received_TS" : "",
                        "Processed_TS" : "",
                        "PayerId": PayerId,
                        "ICD": ICD
                    },
        }
    # 1. Get the line items
    start_time = time.time()
    start_dt = datetime.now()
    trxId = start_dt.strftime(r"%Y%m%d%H%M%S%f")
    logger.info(
        f"{U.prepend_msg(trxId)}{C.HEADER_10} Received Request {C.HEADER_10}"
    )
    try:
        # Begin process
        logger.info(
            f"{U.prepend_msg(trxId)} - Begin Processing Request -> {start_time}"
        )
        end_time = time.time()
        logger.info(
            f"{U.prepend_msg(trxId)} - End Processing Request -> {end_time} - Time Taken -> {end_time - start_time}"
        )
        end_dt = datetime.now()
        _response['Transaction_Info']['Transaction_ID'] = trxId
        _response['Transaction_Info']['Received_TS'] = start_dt
        _response['Transaction_Info']['Processed_TS'] = end_dt
    except Exception as e:
        logger.error(
            f"{U.prepend_msg(trxId)} - there's an error uploading file. Please try again!!!",
            exc_info=True,
        )
        error_message = {
            "Status": C.ERROR,
            "Error": "Error while Uploading file. TRY AGAIN!!",
            "Error-Message": str(e),
        }
        raise HTTPException(status_code=418, detail= f"Error - there's an error uploading file. Please try again!!!")
    logger.info(
            f"{U.prepend_msg(trxId)} - Response Request -> {_response}"
        )
    return _response