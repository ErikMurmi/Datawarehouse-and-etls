from transform.transformations import *
from util.db_connection import Db_Connection
import pandas as pd
import traceback

def traContrato(process):
    try:
        con_db_stg = Db_Connection()
        ses_db_stg = con_db_stg.start()

        if ses_db_stg == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db_stg == -2:
            raise Exception("Error trying to connect to the b2b_dwh_staging")

        contrato_tra_dict = {
            "numero_contrato":[],
            "numero_proforma":[],
            "fecha_inicio":[],
            "fecha_fin":[],
            "descripcion":[],
            "horas_contratadas":[],
            "tipo_solucion_tecnologica":[],
            "codigo_etl":[]
        }

        #Reading the CSV file
        con_ext=pd.read_sql("SELECT numero_contrato, numero_proforma, fecha_inicio, fecha_fin, descripcion, horas_contratadas, tipo_solucion_tecnologica from contrato_ext", ses_db_stg)

        #Processing the CSV file content
        if not con_ext.empty:
            for id,pro,fec_ini,fec_fin,des,hor,tip  \
                in zip(con_ext["numero_contrato"],con_ext["numero_proforma"],
                con_ext["fecha_inicio"],con_ext["fecha_fin"],
                con_ext["descripcion"],con_ext["horas_contratadas"],
                con_ext["tipo_solucion_tecnologica"]):
                contrato_tra_dict["numero_contrato"].append(id)
                contrato_tra_dict["numero_proforma"].append(pro)
                contrato_tra_dict["fecha_inicio"].append(fec_ini)
                contrato_tra_dict["fecha_fin"].append(fec_fin)         
                contrato_tra_dict["descripcion"].append(des)
                contrato_tra_dict["horas_contratadas"].append(hor)
                contrato_tra_dict["tipo_solucion_tecnologica"].append(tip)
                contrato_tra_dict["codigo_etl"].append(process)
        if contrato_tra_dict['numero_contrato']:
            df_cha_tra=pd.DataFrame(contrato_tra_dict)
            df_cha_tra.to_sql('contrato_tra',ses_db_stg,if_exists='append',index=False)
    except:
        traceback.print_exc()
    finally:
        pass