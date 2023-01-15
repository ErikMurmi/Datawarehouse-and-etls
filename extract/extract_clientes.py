from util.db_connection import Db_Connection
import pandas as pd 
import traceback

def extCliente():
    try:
        con_db_stg = Db_Connection()
        ses_db_stg = con_db_stg.start()

        if ses_db_stg == -1:
            raise Exception(f"The give database type {type} is not valid")
        elif ses_db_stg == -2:
            raise Exception("Error trying to connect to the b2b_dwh_staging")
        clientes_csv = pd.read_csv("data/clientes.csv")
        
        clientes_dict = {
            "numero_cliente":[],
            "nombre":[],
            "direccion":[],
            "telefono":[],
            "correo":[],
            "sector":[],
            "representante":[]
        }

        if not clientes_csv.empty:
            for id,nom,dir,tel,cor,sec,rep \
                in zip(clientes_csv["numero_cliente"],clientes_csv["nombre"],
                clientes_csv["direccion"],clientes_csv["telefono"],
                clientes_csv["correo"],clientes_csv["sector"],
                clientes_csv["representante"]):
                clientes_dict["numero_cliente"].append(id),
                clientes_dict["nombre"].append(nom),
                clientes_dict["direccion"].append(dir),
                clientes_dict["telefono"].append(tel),
                clientes_dict["correo"].append(cor),
                clientes_dict["sector"].append(sec),
                clientes_dict["representante"].append(rep)

        if clientes_dict["numero_cliente"]:
            ses_db_stg.connect().execute("TRUNCATE TABLE cliente_ext")
            df_clientes_ext = pd.DataFrame(clientes_dict)
            df_clientes_ext.to_sql('cliente_ext',ses_db_stg,if_exists='append',index=False)
        print(clientes_csv)
    except:
        traceback.print_exc()
    finally:
        pass