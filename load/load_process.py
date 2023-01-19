from load.generic import loadData



def load_process(codigoETL):
    try:
    #LOADS
     print("Codigo ETL load",codigoETL)
     loadData(codigoETL,'clientes.csv','cliente')
     loadData(codigoETL,'proformas.csv','proforma')
     loadData(codigoETL,'contratos.csv','contrato')
     loadData(codigoETL,'wrd_Contratos.csv','detalle_contrato')
     loadData(codigoETL,'servicios.csv','servicio')
    
    except:
        traceback.print_exc()
    finally:
        pass  