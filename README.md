# tarea2_ISS

## Descripción 
APIRest, para la gestión y mantenimiento de una base de datos de candidatos por parte del personal de recursos humanos. 

## Tabla de contenidos 
-[Tecnologías](#Tecnologías)
-[Instalación de las tecnologías](#Instalación-de-las-tecnologías)
-[Comandos del servicio](#Comandos-del-servicio)

## Tecnologías
Lista de las distintas tecnologías del sistema:
* Sistema operativo Ubuntu-22.04
* Flask
* PostgreSQL
* Clouding.io
## Instalación de las tecnologías 
1. Instalación de python3-pip si se no se tiene instalado 
   ```bash
    sudo apt install python3-pip
2. Instalación de Flask
     ```bash
    pip install Flask
3. Instalar psycopg2
   ```bash
    pip install psycopg2_binary
4. Instalar psycopg2
```bash
 sudo apt install curl 

## [Comandos del servicio
A continuación se comentarán los pasos que hay que realizar para arrancar el servicio 
1. ```bash
    Tener la base de datos en clouding.io para ello hay que pagar una subscripción.
    Después se arranca el servidor en una terminal:
                    python3 servidor.py -m Flask 
    y en otra terminal para comprobar si el servidor funciona: 
                   curl -X GET 'http://127.0.0.1:5000/datos_candidatos?perfil=ingeniero&experiencia=1'

   
