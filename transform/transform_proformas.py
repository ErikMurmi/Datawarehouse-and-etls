from transform.transformations import *
from util.db_connection import Db_Connection
import pandas as pd
import traceback

def traProforma(process):
    try:
        pro_db_stg = Db_Connection()
        ses_db_stg = pro_db_stg.start()

        if ses_db_stg == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db_stg == -2:
            raise Exception("Error trying to connect to the b2b_dwh_staging")

        proforma_tra_dict = {
            "numero":[],
            "fecha":[],
            "vendedor":[],
            "numero_cliente":[],
            "subtotal":[],
            "iva":[],
            "total":[],
            "descripcion":[],
            "codigo_etl":[]
        }

        #Reading the CSV file
        pro_ext=pd.read_sql("SELECT numero, fecha, vendedor, numero_cliente, subtotal, iva, total, descripcion from proforma_ext", ses_db_stg)

        #Processing the CSV file content
        if not pro_ext.empty:
            for id,fec,ven,cli,sub,iva,tot,des  \
                in zip(pro_ext["numero"],pro_ext["fecha"],
                pro_ext["vendedor"],pro_ext["numero_cliente"],
                pro_ext["subtotal"],pro_ext["iva"],
                pro_ext["total"], pro_ext["descripcion"]):
                proforma_tra_dict["numero"].append(id)
                proforma_tra_dict["fecha"].append(fec)
                proforma_tra_dict["vendedor"].append(ven)
                proforma_tra_dict["numero_cliente"].append(cli)         
                proforma_tra_dict["subtotal"].append(sub)
                proforma_tra_dict["iva"].append(iva)
                proforma_tra_dict["total"].append(tot)
                proforma_tra_dict["descripcion"].append(des)
                proforma_tra_dict["codigo_etl"].append(process)
        if proforma_tra_dict['numero']:
            df_cha_tra=pd.DataFrame(proforma_tra_dict)
            df_cha_tra.to_sql('proforma_tra',ses_db_stg,if_exists='append',index=False)
    except:
        traceback.print_exc()
    finally:
        pass