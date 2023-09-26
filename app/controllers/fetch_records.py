from app.core import logger
from app.core import cfg
from app.schema.Action_Recommendation_API import ActionRecommendation

def get_filtered_record(db_connector, tablename, filters) -> ActionRecommendation:
        ICD = filters['ICD']
        PayerId = filters['PayerId']
        query = f"""SELECT * FROM {tablename} WHERE ("ICD"='{ICD}' AND "PayerId"='{PayerId}')"""
        record = db_connector.execute_query(query)[0]
        result = {}
        result['TopActionList'] = [int(i) for i in list(record['Actions'])][0:cfg['Number_of_Actions_Recommended']]
        result['Text'] = "Text"
        return ActionRecommendation(**result)
