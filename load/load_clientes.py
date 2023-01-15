from distutils.util import execute
from util.db_connection import Db_Connection
import pandas as pd
import traceback
import configparser




def loadCliente(codigoETL):
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

        dim_clientes_dict = {
            "numero_cliente":[],
            "nombre":[],
            "direccion":[],
            "telefono":[],
            "correo":[],
            "sector":[],
            "representante":[]
        }
        cliente_tra = pd.read_sql(f"SELECT numero_cliente, nombre, direccion, telefono, correo, sector, representante FROM cliente_tra where codigo_etl={codigoETL} ", ses_db_stg)
        cliente_sor=pd.read_sql(f"SELECT numero_cliente, nombre, direccion, telefono, correo, sector, representante FROM cliente", ses_db_sor)
        cliente_sor.to_dict()
        if not cliente_tra.empty:
            for id,nom,dic,tel,cor,sec,rep \
                in zip(cliente_tra['numero_cliente'],cliente_tra['nombre'],
                cliente_tra['direccion'],cliente_tra['telefono']
                ,cliente_tra['correo'],cliente_tra['sector'],cliente_tra['representante']):
                dim_clientes_dict["numero_cliente"].append(id)
                dim_clientes_dict["nombre"].append(nom)
                dim_clientes_dict["direccion"].append(dic)
                dim_clientes_dict["telefono"].append(tel)
                dim_clientes_dict["correo"].append(cor)
                dim_clientes_dict["sector"].append(sec)
                dim_clientes_dict["representante"].append(rep)



        if dim_clientes_dict ["numero_cliente"]:
            df_dim_clientes = pd.DataFrame(dim_clientes_dict)
            merge_cliente = df_dim_clientes.merge(cliente_sor, indicator='i', how='outer').query('i == "left_only"').drop('i', axis=1)
            merge_cliente.to_sql('cliente', ses_db_sor, if_exists="append",index=False)

    except:
        traceback.print_exc()
    finally:
        pass     
