from transform.transformations import *
from util.db_connection import Db_Connection
import pandas as pd
import traceback

def traCliente(codigoETL):
    try:
        con_db_stg = Db_Connection()
        ses_db_stg = con_db_stg.start()

        if ses_db_stg == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db_stg == -2:
            raise Exception("Error trying to connect to the b2b_dwh_staging")

        cliente_tra_dict = {
           "numero_cliente":[],
            "nombre":[],
            "direccion":[],
            "telefono":[],
            "correo":[],
            "sector":[],
            "representante":[],
            "codigo_etl":[]
        }

        #Reading the CSV file
        cli_ext=pd.read_sql("SELECT numero_cliente, nombre, direccion, telefono, correo, sector, representante from cliente_ext", ses_db_stg)

        #Processing the CSV file content
        if not cli_ext.empty:
            for id,nom,dir,tel,cor,sec,rep  \
                in zip(cli_ext["numero_cliente"],cli_ext["nombre"],
                cli_ext["direccion"],cli_ext["telefono"],
                cli_ext["correo"],cli_ext["sector"],
                cli_ext["representante"]):
                cliente_tra_dict["numero_cliente"].append(id)
                cliente_tra_dict["nombre"].append(nom)
                cliente_tra_dict["direccion"].append(dir)
                cliente_tra_dict["telefono"].append(func_telefono(tel))         
                cliente_tra_dict["correo"].append(cor)
                cliente_tra_dict["sector"].append(sec)
                cliente_tra_dict["representante"].append(rep)
                cliente_tra_dict["codigo_etl"].append(codigoETL)
        if cliente_tra_dict['numero_cliente']:
            df_cha_tra=pd.DataFrame(cliente_tra_dict)
            df_cha_tra.to_sql('cliente_tra',ses_db_stg,if_exists='append',index=False)
    except:
        traceback.print_exc()
    finally:
        pass