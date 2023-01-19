#Generar datos
from faker import Faker
#Sumar fechas
from datetime import timedelta
#Leer .csv
import csv 
#Generar randoms
import random


#Generar clientes
def generarClientes():
    sectores = ['Gubernamental','Banca','Educacion','Comunicaciones','Alimentos']
    header = ['numero_cliente', 'nombre', 'direccion', 'telefono','correo','sector','representante']
    fake = Faker('es_ES')
    fake1 = Faker('en_US')
    clientes =[]
    with open('data/clientes.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        for _ in range(1,100):
            #['numero_cliente', 'nombre', 'direccion', 'telefono','correo','sector','representante']
            clientes += [[_,fake1.company(),fake.address(),fake.phone_number(),fake.email(),
            random.choice(sectores),fake1.name()]]
            #print(clientes)
        # write multiple rows
        writer.writerows(clientes)
    return clientes

#Generar datos
def generateData():

    tipos_solucion = ['RP','TELEFONICA','SEGURIDAD','STORAGE','IMPRESION','AZURE','OFFICE 365','CALL CENTER','HIPERCONVERGENCIA']
    costos_horas= {'RP':15,'TELEFONICA':10,'SEGURIDAD':12,'STORAGE':12,'IMPRESION':13,'AZURE':17,'OFFICE 365':20,'CALL CENTER':16,'HIPERCONVERGENCIA':20}
    #Lista de objetos
    proformas =[]
    contratos =[]
    d_Contratos =[]
    servicios =[]
    numContratos = 0
    numServicio = 0
    #Generadores de faker
    fake = Faker('es_ES')
    fakeEs = Faker('en_US')
    clientes = generarClientes()

    for numProforma in range(1,300):
        fechaProforma = fake.date_this_year()
        #print('fecha:',fechaProforma)
        subtotal = round(random.uniform(3000,20000),2)
        iva = subtotal * 0.12
        total = subtotal + iva
        #['numero', 'fecha', 'vendedor','cliente' ,'subtotal','iva','total','descripcion']
        proformas += [[numProforma,fechaProforma,fake.name(),random.randint(1,len(clientes)),subtotal,iva,total,fakeEs.text()]]
        hayContrato = bool(random.choice([True, False]))
        
        if hayContrato:
            fechaInicio = fechaProforma+timedelta(days=random.randint(1,30))
            #fechaInicio = fake.date_between(fechaProforma,end_date=maximo_aceptacion)
            meses = random.randint(6,36)
            fechaFin=fechaInicio+timedelta(30*meses)
            #fechaFin = fake.date_between(fechaInicio,end_date=end_date)
            numContratos+=1
            #['numero_contrato', 'numero_proforma', 'fecha_inicio', 'fecha_fin','descripcion','horas_contratadas','tipo_solucion_tecnologica']
            tipoSolucion = random.choice(tipos_solucion)
            valorHora = costos_horas[tipoSolucion]
            horasContratadas = random.randint(10,1500)

            while horasContratadas*valorHora > total*0.6:
                horasContratadas = random.randint(10,1500)

            contratos += [[numContratos,numProforma,fechaInicio,fechaFin,fakeEs.text(),horasContratadas,tipoSolucion]]
            #Guardar los detalles del contrato
            #['numero_contrato', 'inversion','ganancia' ,'valor_hora_estimado']
            #inversion > valorHora * horasContratadas
            inversion = round(random.uniform(valorHora*horasContratadas,total*0.8),2)
            d_Contratos+=[[numContratos,inversion,total,valorHora]]
            cantidadServicios = random.randint(1,20)
            for _ in range(cantidadServicios):
                numServicio+=1
                #['numero_servicio', 'horas', 'numero_contrato','tecnico' ,'costos_extras','costos_extras_subsanados','descripcion']
                horas = random.randint(1,72)
                hayExtras = bool(random.choice([True, False]))
                costos_extras = 'null'
                costos_extras_subsanados = 'null'
                if hayExtras:
                    costos_extras = round(random.uniform(1,10000),2)
                    subsanados = bool(random.choice([True, False]))
                    if subsanados:
                        costos_extras_subsanados = round(random.uniform(1,2000),2)

                servicios+=[[numServicio,horas,numContratos,fakeEs.name(), costos_extras ,costos_extras_subsanados,fakeEs.text()]]
            
        # write multiple rows

        #Proforma
        hdProforma = ['numero', 'fecha', 'vendedor','numero_cliente' ,'subtotal','iva','total','descripcion']
        proformasF = open('data/proformas.csv', 'w', encoding='UTF8', newline='')
        wrProformas = csv.writer(proformasF)
        wrProformas.writerow(hdProforma)
        wrProformas.writerows(proformas)
        proformasF.close()

        #Contratos
        hdContratos = ['numero_contrato', 'numero_proforma', 'fecha_inicio', 'fecha_fin','descripcion','horas_contratadas','tipo_solucion_tecnologica']
        contratosF = open('data/contratos.csv', 'w', encoding='UTF8', newline='')
        wrContratos = csv.writer(contratosF)
        wrContratos.writerow(hdContratos)
        wrContratos.writerows(contratos)
        contratosF.close()

        #Detalle Contratos
        hdDetalleContratos = ['numero_contrato', 'inversion','ganancia' ,'valor_hora_estimado']
        d_ContratosF = open('data/wrd_Contratos.csv', 'w', encoding='UTF8', newline='')
        wrd_Contratos = csv.writer(d_ContratosF)
        wrd_Contratos.writerow(hdDetalleContratos)
        wrd_Contratos.writerows(d_Contratos)
        d_ContratosF.close()

        #Servicios
        hdServicios = ['numero_servicio', 'horas', 'numero_contrato_servicio','tecnico' ,'costos_extras','costos_subsanados','descripcion']
        serviciosF = open('data/servicios.csv', 'w', encoding='UTF8', newline='')
        wrServicios = csv.writer(serviciosF)
        wrServicios.writerow(hdServicios)
        wrServicios.writerows(servicios)
        serviciosF.close()

