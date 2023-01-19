from transform.proceso_etl import proceso_etl
from transform.transform_clientes import traCliente
from transform.transform_contratos import traContrato
from transform.transform_detalle_contratos import traDetalle
from transform.transform_proformas import traProforma
from transform.transform_servicios import traServicio
from load.load_process import load_process

import traceback

codigoETL=proceso_etl()

def transform_process():

    try:
        print("COdigo etl proceso ",codigoETL )
        # TRANSFORMS 
        traCliente(codigoETL)
        traProforma(codigoETL)
        traContrato(codigoETL)
        traDetalle(codigoETL)
        traServicio(codigoETL)
        load_process(codigoETL)

    except:
        traceback.print_exc()
    finally:
        pass