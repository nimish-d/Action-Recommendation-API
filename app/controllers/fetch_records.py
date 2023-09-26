from app.core import cfg

def get_filtered_record(db_connector, tablename, filters):
        ICD = filters['ICD']
        PayerId = filters['PayerId']
        query = f"""SELECT * FROM {tablename} WHERE ("ICD"='{ICD}' AND "PayerId"='{PayerId}')"""
        record = db_connector.execute_query(query)[0]
        result = {}
        result['TopActionList'] = [int(i) for i in list(record['Actions'])][0:cfg['Number_of_Actions_Recommended']]
        result['Text'] = 'Text'
        return result
