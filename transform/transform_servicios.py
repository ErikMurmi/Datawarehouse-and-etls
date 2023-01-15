from transform.transformations import *
from util.db_connection import Db_Connection
import pandas as pd
import traceback

def traServicio(process):
    try:
        ser_db_stg = Db_Connection()
        ses_db_stg = ser_db_stg.start()

        if ses_db_stg == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db_stg == -2:
            raise Exception("Error trying to connect to the b2b_dwh_staging")

        servicio_tra_dict = {
            "numero_servicio":[],
            "numero_contrato_servicio":[],
            "tecnico":[],
            "horas":[],
            "costos_extras":[],
            "costos_subsanados":[],
            "descripcion":[],
            "codigo_etl":[]
        }

        #Reading the CSV file
        ser_ext=pd.read_sql("SELECT numero_servicio, numero_contrato_servicio, tecnico, horas, costos_extras, costos_subsanados, descripcion from servicio_ext", ses_db_stg)

        #Processing the CSV file content
        if not ser_ext.empty:
            for id,con,tec,hor,cos_ext,cos_sub,des  \
                in zip(ser_ext["numero_servicio"],ser_ext["numero_contrato_servicio"],
                ser_ext["tecnico"],ser_ext["horas"],
                ser_ext["costos_extras"],ser_ext["costos_subsanados"],
                ser_ext["descripcion"]):
                servicio_tra_dict["numero_servicio"].append(id)
                servicio_tra_dict["numero_contrato_servicio"].append(con)
                servicio_tra_dict["tecnico"].append(tec)         
                servicio_tra_dict["horas"].append(hor)
                servicio_tra_dict["costos_extras"].append(func_nulls(cos_ext))
                servicio_tra_dict["costos_subsanados"].append(func_nulls(cos_sub))
                servicio_tra_dict["descripcion"].append(des)
                servicio_tra_dict["codigo_etl"].append(process)
        if servicio_tra_dict['numero_servicio']:
            df_cha_tra=pd.DataFrame(servicio_tra_dict)
            df_cha_tra.to_sql('servicio_tra',ses_db_stg,if_exists='append',index=False)
    except:
        traceback.print_exc()
    finally:
        pass