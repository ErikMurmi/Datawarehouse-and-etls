from transform.transform_clientes import traCliente
from transform.transform_contratos import traContrato
from transform.transform_detalle_contratos import traDetalle
from transform.transform_proformas import traProforma
from transform.transform_servicios import traServicio
from data.generator import generateData
from extract.generic import extData
from load.generic import loadData
from datetime import datetime
import pandas as pd

import traceback

try:

    generateData()
    extData('clientes.csv','cliente')
    extData('proformas.csv','proforma')
    extData('contratos.csv','contrato')
    extData('wrd_Contratos.csv','detalle_contrato')
    extData('servicios.csv','servicio')
    
    traCliente(1)
    traProforma(1)
    traContrato(1)
    traDetalle(1)
    traServicio(1)
    
    loadData(1,'clientes.csv','cliente')
    loadData(1,'proformas.csv','proforma')
    loadData(1,'contratos.csv','contrato')
    loadData(1,'wrd_Contratos.csv','detalle_contrato')
    loadData(1,'servicios.csv','servicio')
    
except:
    traceback.print_exc()
finally:
    pass