from transform.transformations import *
from util.db_connection import Db_Connection
import pandas as pd
import traceback

def traDetalle(process):
    try:
        con_db_stg = Db_Connection()
        ses_db_stg = con_db_stg.start()

        if ses_db_stg == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db_stg == -2:
            raise Exception("Error trying to connect to the b2b_dwh_staging")

        detalle_tra_dict = {
            "numero_contrato":[],
            "inversion":[],
            "ganancia":[],
            "valor_hora_estimado":[],
            "codigo_etl":[]
        }

        #Reading the CSV file
        con_ext=pd.read_sql("SELECT numero_contrato, inversion, ganancia, valor_hora_estimado from detalle_contrato_ext", ses_db_stg)

        #Processing the CSV file content
        if not con_ext.empty:
            for id,inv,gan,val \
                in zip(con_ext["numero_contrato"],con_ext["inversion"],
                con_ext["ganancia"],con_ext["valor_hora_estimado"]):
                detalle_tra_dict["numero_contrato"].append(id)
                detalle_tra_dict["inversion"].append(inv)
                detalle_tra_dict["ganancia"].append(gan)
                detalle_tra_dict["valor_hora_estimado"].append(val)         
                detalle_tra_dict["codigo_etl"].append(process)
        if detalle_tra_dict['numero_contrato']:
            df_cha_tra=pd.DataFrame(detalle_tra_dict)
            df_cha_tra.to_sql('detalle_contrato_tra',ses_db_stg,if_exists='append',index=False)
    except:
        traceback.print_exc()
    finally:
        pass