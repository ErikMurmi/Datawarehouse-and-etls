from util.db_connection import Db_Connection
import pandas as pd 
import traceback

def extData(filePath,name):
    try:
        con_db_stg = Db_Connection()
        ses_db_stg = con_db_stg.start()

        if ses_db_stg == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db_stg == -2:
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
            tableName = name+'_ext'
            try:
                query = "CALL truncate_if_exists(%s);"
                ses_db_stg.connect().execute(query,tableName)
                print('Se trunco la tabla ', tableName)
            except:
                print('Aun no existe la tabla')
            df_data_ext = pd.DataFrame(dic_headers)
            df_data_ext.to_sql(tableName,ses_db_stg,if_exists='append',index=False)
        #print(data_csv)
    except:
        traceback.print_exc()
    finally:
        pass