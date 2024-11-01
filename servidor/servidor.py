from flask import Flask, request
from flask import jsonify
import psycopg2, psycopg2.extras
import json
from Candidato import Candidato

app = Flask(__name__)




@app.route ('/')
def home():
     return "Bienvenido al servidor de Flask"



def getConnection():

    conn = psycopg2.connect(database="candidatosBBDD", user="admin_candidatos", password="padmin", host="217.71.204.148")

    return conn


@app.route('/datos_candidatos', methods=['GET'])
def obtener_candidato():

    # Obtención de datos de la URL
    perfil = request.args.get("perfil")
    experiencia = request.args.get("experiencia")

    # Conexión y consultas a la BBDD
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM candidatos WHERE perfil='" + perfil + "' AND experiencia>=" + str(experiencia))
    candidatos_filtrados = cursor.fetchall()

    lista_candidatos_filtrados = []

    for candidato in candidatos_filtrados:
        
        candidato_obj = Candidato(
        dni = candidato[0],
        nombre = candidato[1],
        apellidos = candidato[2],
        perfil = candidato[3],
        experiencia = candidato[4],
        correo = candidato[5],
        cv = candidato[6])
    
        lista_candidatos_filtrados.append(candidato_obj)

    ultimo_execute = cursor.rowcount
    cursor.close()
    conn.close()
    if ultimo_execute > 0 : 
        return jsonify([candidato.a_diccionario() for candidato in lista_candidatos_filtrados]),200
    else :
        return jsonify({'mensaje': 'No se ha podido obtener candidatos'}),200  
    
@app.route('/nuevo_candidato', methods=['POST'])
def agregar_candidato():

    conn = getConnection()
    nuevo_candidato = Candidato (
        dni = request.json['dni'],
        nombre = request.json['nombre'],
        apellidos = request.json['apellidos'],
        perfil = request.json['perfil'],
        experiencia = request.json['experiencia'],
        correo = request.json['correo'],
        cv = request.json['cv'])
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO candidatos (dni, nombre, apellidos, perfil, experiencia, correo, cv) VALUES (" + nuevo_candidato.dni + "," + nuevo_candidato.nombre + "," + nuevo_candidato.apellidos + "," + nuevo_candidato.perfil + "," + nuevo_candidato.experiencia + "," + nuevo_candidato.correo + "," + nuevo_candidato.cv + ")")
    
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Se ha añadido correctamente al candidato a la BBDD'}),200   

        


@app.route('/candidato_concreto', methods=['PUT'])
def actualizar_candidato():

    conn = getConnection()
    cursor = conn.cursor()
   
    cursor.execute("SELECT dni FROM candidatos WHERE dni = " + request.json['dni'])
    dni_existente = cursor.fetchall()
    # print(dni_existente)

    if dni_existente is not None:
        if request.json['nombre'] is not None:
            cursor.execute("UPDATE candidatos SET nombre = " + request.json['nombre'] + " WHERE dni = " + dni_existente)

        if request.json['apellidos'] is not None:
            cursor.execute("UPDATE candidatos SET apellidos = " + request.json['apellidos'] + " WHERE dni = " + dni_existente)
            
        if request.json['perfil'] is not None:
            cursor.execute("UPDATE candidatos SET perfil = " + request.json['perfil'] + " WHERE dni = " + dni_existente)
            
        if request.json['experiencia'] is not None:
            cursor.execute("UPDATE candidatos SET experiencia = " + request.json['experiencia'] + " WHERE dni = " + dni_existente)
            
        if request.json['correo'] is not None:
            cursor.execute("UPDATE candidatos SET correo = " + request.json['correo'] + " WHERE dni = " + dni_existente)
            
        if request.json['cv'] is not None:
            cursor.execute("UPDATE candidatos SET cv = " + request.json['cv'] + " WHERE dni = " + dni_existente)

    else:
        cursor.close()
        conn.close()
        return jsonify({'mensaje': 'No se ha encontrado un candidato con ese DNI en la base de datos'}),200

    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Se ha actualizado correctamente la BBDD'}),200 

@app.route('/candidato/', methods=['DELETE'])
def eliminar_candidato():
    dni_eliminar = request.json['dni']
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM candidatos WHERE dni="+ dni_eliminar)
    cursor.commit()
    ultimo_execute = cursor.rowcount
    cursor.close() 
    conn.close()
    if ultimo_execute > 0 :
        return jsonify({'mensaje': 'Se ha eliminado correctamente al candidato de la BBDD'}),200
    else : 
        return jsonify({'mensaje' : 'No existe el candidato en la base de datos'})
    

    
if __name__ == '__main__':
    app.run(debug=True)
    