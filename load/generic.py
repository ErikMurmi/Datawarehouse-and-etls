from distutils.util import execute
from util.db_connection import Db_Connection
import pandas as pd
import traceback
import configparser




def loadData(codigoETL,filePath,name):
    try:
   
        con_db_stg = Db_Connection()
        ses_db_stg = con_db_stg.start()

        if ses_db_stg == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db_stg == -2:
            raise Exception("Error trying to connect to the b2b_dwh_staging")

        con_db_sor = Db_Connection(database='proydos_sor')
        ses_db_sor = con_db_sor.start()

        if ses_db_sor == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db_sor == -2:
            raise Exception("Error trying to connect to the b2b_dwh_sor")


        data_csv = pd.read_csv(f"data/{filePath}")
        #print('nombre:',name)
        headers = data_csv.columns
        dim_data_dict = {header:[] for header in headers}

        query_stg = f"SELECT {', '.join(dim_data_dict)} FROM {name}_tra WHERE codigo_etl={codigoETL}"
        query_sor = f"SELECT {', '.join(dim_data_dict)} FROM {name}"
        data_tra = pd.read_sql(query_stg, ses_db_stg)
        data_sor = pd.read_sql(query_sor, ses_db_sor)
        data_sor.to_dict()

        if not data_tra.empty:
            for row in data_tra.itertuples(index=False):
                for header, value in zip(headers, row):
                    dim_data_dict[header].append(value)
        # print("data tra",data_tra)
        if dim_data_dict[headers[0]]:
            df_dim_data = pd.DataFrame(dim_data_dict)
            merge_data = df_dim_data.merge(data_sor, indicator='i', how='outer').query('i == "left_only"').drop('i', axis=1)
            merge_data.to_sql(name, ses_db_sor, if_exists="append",index=False)

    except:
        traceback.print_exc()
    finally:
        pass     
