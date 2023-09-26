def get_filtered_record(db_connector, tablename, filters):
        ICD = filters['ICD']
        PayerId = filters['PayerId']
        query = f"""SELECT * FROM {tablename} WHERE ("ICD"='{ICD}' AND "PayerId"='{PayerId}')"""
        result = db_connector.execute_query(query)[0]
        return result
