from extract.generic import extData

import traceback

def extraction_process():
    try:
        #EXTRACTS
        extData('proformas.csv','proforma')
        extData('contratos.csv','contrato')
        extData('wrd_Contratos.csv','detalle_contrato')
        extData('servicios.csv','servicio')
    except:
        traceback.print_exc()
    finally:
        pass