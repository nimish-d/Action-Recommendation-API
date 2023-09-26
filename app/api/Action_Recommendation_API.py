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
from app.core import cfg
from app.schema.Action_Recommendation_API import ClassiferResponse, ActionRecommendationResponse
from app.controllers.read_table import DatabaseConnector


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


# Nimish's code starts here. Remove this comment later
# remove printing configuration 
logger.info(f'[configuration]: [{cfg}]')

connection_settings = cfg['store']['sqlalchemy']

tablename = cfg['store']['tablename']
# query = text(f"SELECT * FROM {tablename} limit 3")
query = f"""SELECT * FROM {tablename} WHERE ("ICD"='S02' AND "PayerId"='516572')"""

# Define your database connection parameters here as a dictionary
driver = cfg['SQLToolKit']
db_connector = DatabaseConnector(driver, connection_settings)
logger.info(f'[Connected to the DB][{connection_settings}]')
db_connector.connect()
logger.info(f'[Test Query:][{query}]')

result = db_connector.execute_query(query)
logger.info(f'[Result of the Test Query]:[{result}]')

for row in result[0:1]:
    print(row)

# include the following command in the shutdown method
# db_connector.close()

@router.post("/", response_model=ActionRecommendationResponse)
async def input_filter(PayerId:int, ICD:str):
    """API route to get action recommendation stored in a database given a set of filter values"""
    _response = {
        "Transaction_Info": {
                        "Transaction_ID": "1234",
                        "Received_TS" : "",
                        "Processed_TS" : "",
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
        query = f"""SELECT * FROM {tablename} WHERE ("ICD"='{ICD}' AND "PayerId"='{PayerId}')"""
        logger.info(query)
        result = db_connector.execute_query(query)[0]

        _response['Action_Recommendation'] = {}
        _response['Action_Recommendation']['TopActionList'] = [int(i) for i in list(result['Actions'])][0:3]
        _response['Action_Recommendation']['Text'] = 'Text'
        logger.info(
            f"{U.prepend_msg(trxId)} - End Processing Request -> {end_time} - Time Taken -> {end_time - start_time}"
        )
        end_dt = datetime.now()
        _response['Transaction_Info']['Transaction_ID'] = trxId
        _response['Transaction_Info']['Received_TS'] = start_dt
        _response['Transaction_Info']['Processed_TS'] = end_dt
    except Exception as e:
        logger.error(
            f"{U.prepend_msg(trxId)} - There's an Error in Fetching Action Recommendations. Please Try Again!",
            exc_info=True,
        )
        error_message = {
            "Status": C.ERROR,
            "Error": "Error while Uploading file. TRY AGAIN!!",
            "Error-Message": str(e),
        }
        raise HTTPException(status_code=418, detail= f"Error - Unable to Fetch Action Recommendations. Please Try Again!")
    logger.info(
            f"{U.prepend_msg(trxId)} - Response Request -> {_response}"
        )
    return _response