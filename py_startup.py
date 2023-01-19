
from data.generator import generateData
from extract.extract_db import loadInitialDB
from extract.extract_db import extDataDB
from datetime import datetime
import pandas as pd
from extract.extract_process import extraction_process
from transform.transform_process import transform_process


import traceback

try:

   
     generateData()
     loadInitialDB('clientes.csv','cliente','compuequip_dos')
     extDataDB('compuequip_dos','cliente')

#EXTRACTS

     extraction_process()

# METODO QUE EJECUTA LA TRANSFORMACION Y CARGA DE LOS DATOS

     transform_process()
    
    
    
except:
    traceback.print_exc()
finally:
    pass