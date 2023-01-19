from util.db_connection import Db_Connection
import pandas as pd 
import traceback

def extDataDB(origin,table):
    try:
        con_origin_db = Db_Connection(database=origin)
        ses_origin_db = con_origin_db.start()

        con_db = Db_Connection()
        ses_db = con_db.start()

        if ses_origin_db == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_origin_db == -2:
            raise Exception("Error trying to connect to the b2b_dwh_staging")
        #data_csv = pd.read_csv(f"data/{filePath}")
        query = f"SELECT * FROM {table}"
        data = pd.read_sql(query, ses_origin_db)
        dim_data_dict= data.to_dict()
        headers = data.columns

        if dim_data_dict[headers[0]]:
            tableName = table+'_ext'
            try:
                query = "CALL truncate_if_exists(%s);"
                ses_db.connect().execute(query,tableName)
                print('Se trunco la tabla ', tableName)
            except:
                print('Aun no existe la tabla')
            df_data_ext = pd.DataFrame(dim_data_dict)
            df_data_ext.to_sql(tableName,ses_db,if_exists='append',index=False)
        #print(data_csv)
    except:
        traceback.print_exc()
    finally:
        pass

def loadInitialDB(filePath,name,db):
    try:
        con_db = Db_Connection(database=db)
        ses_db = con_db.start()

        if ses_db == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db == -2:
            raise Exception("Error trying to connect to the b2b_dwh_staging")
            
        data_csv = pd.read_csv(f"data/{filePath}")
        #print('nombre:',name)
        headers = data_csv.columns
        dic_headers = {header:[] for header in headers}
        #print(dic_headers)
        if not data_csv.empty:
            for row in data_csv.itertuples(index=False):
                for header, value in zip(headers, row):
                    dic_headers[header].append(value)

        if dic_headers[headers[0]]:
            tableName = name
            try:
                query = "CALL truncate_if_exists(%s);"
                ses_db.connect().execute(query,tableName)
                print('Se trunco la tabla ', tableName)
            except:
                print('Aun no existe la tabla')
            df_data_ext = pd.DataFrame(dic_headers)
            df_data_ext.to_sql(tableName,ses_db,if_exists='append',index=False)
        #print(data_csv)
    except:
        traceback.print_exc()
    finally:
        pass