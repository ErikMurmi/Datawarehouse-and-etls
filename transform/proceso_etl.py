from distutils.util import execute
from util.db_connection import Db_Connection
import pandas as pd
import traceback
import configparser


def proceso_etl():
    try:
   
        con_db_stg = Db_Connection()
        ses_db_stg = con_db_stg.start()

        if ses_db_stg == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db_stg == -2:
            raise Exception("Error trying to connect to the b2b_dwh_staging")

        ses_db_stg.execute('INSERT INTO  proceso_etl VALUES ()') #The date in the database is declared by default with the CURRENT_DATE
        etl=ses_db_stg.execute('SELECT CODIGO_ETL  FROM proceso_etl ORDER BY CODIGO_ETL DESC LIMIT 1').scalar()
        return etl
    except:
        traceback.print_exc()
    finally:
        pass