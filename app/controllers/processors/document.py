#####################################################################
# Copyright(C), 2022 IHX Private Limited. All Rights Reserved
# Unauthorized copying of this file, via any medium is
# strictly prohibited
#
# Proprietary and confidential
# email: care@ihx.in
#####################################################################
"""File Controller specific methods.

This provides a suite of methods to control the flow of logic
for files received for processing.

  Typical usage example:
  
  result = file._specif_Function(parameters)
"""
import os
import time
from app.core import logger
from typing import List
from joblib import Parallel, delayed, parallel_backend
from app.utils import constants as C
from app.utils import exceptions as E
from app.utils import utilities as U 
from app.core import cfg

_response = {
    "Classifer": []
}

async def process_lines(
    trxId: str,
    lines: List[str]):
    """Process each document provided during request.

    Args
    ----
        trxId: The request transaction ID. Used for logging purpose.
        document: List of bill particular lines

    Returns
    -------
        The classes for each line.
        example:

    Raises
    ------

    """
    # 1. Multiprocess each line item
    n_jobs = cfg.processing.Parallelization.Job_count
    backend = cfg.processing.Parallelization.backend
    logger.info(
            f"{U.prepend_msg(trxId)} - Joblib parameters -> {n_jobs}, {backend}"
        )
    print("Joblib parameters [n_jobs, backend]:", n_jobs, backend)
    return _response
