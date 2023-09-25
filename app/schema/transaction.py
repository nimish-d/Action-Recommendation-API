#####################################################################
# Copyright(C), 2022 IHX Private Limited. All Rights Reserved
# Unauthorized copying of this file, via any medium is
# strictly prohibited
#
# Proprietary and confidential
# email: care@ihx.in
#####################################################################
from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class TransactionInfo(BaseModel):
    Transaction_ID: str
    Received_TS: datetime
    Processed_TS: datetime
    
class OperationStatus(str, Enum):
    SUCCCESS = "Success"
    ERROR = "Error"
    INPROGRESS = "InProgress"
     