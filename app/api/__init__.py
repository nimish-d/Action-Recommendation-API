#####################################################################
# Copyright(C), 2022 IHX Private Limited. All Rights Reserved
# Unauthorized copying of this file, via any medium is
# strictly prohibited
#
# Proprietary and confidential
# email: care@ihx.in
#####################################################################
from fastapi import APIRouter

from app.api import admin
from app.api import Action_Recommendation_API

api_router = APIRouter()

api_router.include_router(admin.router, tags=["Administration"])
api_router.include_router(Action_Recommendation_API.router, tags=["Classifer"])