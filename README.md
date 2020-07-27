Ejempo de una aplicacion web desarrollado con flask, conectada con mongoDB, redis como base de datos, ejecutandose en Nginx.
## Instrucciones

1. Clonar el respositorio
```
$ git clone https://github.com/benit0Zr/flaskapp_container.git
```
2. Compilar el contenedor, hay que entrar en la carpeta donde este el archivo, posteriormente ejecutar el siguiente comando
```
$ sudo docker-compose up -d
```
3. Iniciar el contenedor 
```
$ sudo docker-compose up
```
4. Ingresar la siguiente dirección localhost:8181 en el navegador para ver la aplicacion flask funcionando
1. Para detener los contenedores
```
$ sudo docker stop
```
### Visualizar los datos en mongoDB
1. Verificar que los contenedores se estén ejecutando
```
$ sudo docker ps
```
2. Copiar el id del contenedor mongoDB y despues ejecutar el siguiente comando
```
$ sudo docker exec -it <ID> bash
```
3. Ejecutar mongo, para entrar a la consola interactiva

```
Listar las bases de datos
$ show dbs

```
```
Seleccionar una base
$ use testdb
```
```
Mostrar las colecciones
$ show collections
```
```
Ver los registros
$ db.users.find().pretty()
```
```
Salir de la consola
$ exit
```