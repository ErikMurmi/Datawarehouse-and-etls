# Proyecto-Analisis-DOS
El siguiente proyecto consistió en la selección de una empresa para identificar las necesidades analíticas que se requieren solventar al interior de esta
organización y así desarrollar el modelo de datos analítico en base a las necesidades identificadas e implementar una solución analítica para la adecuada y efectiva 
toma de desiciones.

El proyecto consta de cuatro partes fundamentales:

* [Generación de datos con Faker](#)

* [Procesos ETL](#)

* [Base de Datos MySQL](#)

* [Visualización de datos en Power BI](#)

## :hammer:Transform

- Se generó un archivo transform por cada tabla en stagin.

![image](https://user-images.githubusercontent.com/62667937/198377192-a8dfc6dc-0bc8-46ca-9448-ebb1258ab42c.png)

- Se agregó un archivo transformations el cual contiene todas las funciones que nos servirá para realizar las transformaciones de los datos.

- ![image](https://user-images.githubusercontent.com/62667937/198377560-7f662294-e070-4adb-a801-faf84def58f8.png)



## :white_check_mark:Load

- Se generó un archivo load por cada tabla en sor.

![image](https://user-images.githubusercontent.com/62667937/198377785-43286d62-90f0-4801-ba49-7aee089a3357.png)


- En cada load se utilizó la función merge de la librería de python pandas, que nos permite fucionar dos tablas en este caso la de stg y la del sor con el fin de que al hacer una nueva carga en el sor no se dupliquen datos y solo queden los últimos transformados.

![image](https://user-images.githubusercontent.com/62667937/198378958-f938cf99-ac1c-44e4-a0b5-500b4dcf8f3c.png)


