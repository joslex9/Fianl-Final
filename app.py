
from flask import Flask, request, jsonify, render_template
from config.bd import app, bd, ma
from Model.Estudiante import Estudiante, EstudianteSchema
from Model.Profesor import ProfesorSchema
from Model.Programa import ProgramaSchema
from Model.GInvestigacion import GrupoInvestigacion_Schema
from Model.Semillero import Semillero, SemilleroSchema

from Model.Proyecto import Proyecto, ProyectoSchema
from Model.Objetivos import Objetivos ,ObjetivosSchema
from Model.ResultadosOb import ResultadosOb,ResultadosObSchema
from Model.EstudianteP import EstudianteP ,EstudiantePSchema





Estudiante_schema = EstudianteSchema()
Estudiantes_schema = EstudianteSchema(many=True)

GruppoInvestigacion_Schema = GrupoInvestigacion_Schema()
GrupposInvestigacion_schema = GrupoInvestigacion_Schema(many=True)

passrofesorSchema = ProfesorSchema()
profesores_schema = ProfesorSchema(many=True)

programaSchema = ProgramaSchema()
programas_schema = ProgramaSchema(many=True)

proyectoSchema = ProyectoSchema()
proyectos_schema = ProyectoSchema(many=True)


semilleroSchema = SemilleroSchema()
semilleros_schema = SemilleroSchema(many=True)


@app.route("/", methods=['GET'])
def index():
    nombre= "Login"
    return render_template('index.html')


@app.route("/traerSemilleros", methods=['GET'])
def GetSemilleros():
     results = bd.session.query(Semillero).all() 
     dato={}   
     i=0
     for s in results:
        i+=1	       
        dato[i] = {
        "codigoSemillero":s.codigoSemillero,
        'nombre' :s.nombre, 
        'facultad':s.facultad,  

        }
      
     print(dato)
    
     return jsonify(dato)

@app.route("/Semillero", methods=['GET'])
def GoSemilleros():  
  return render_template("Semilleros.html")

@app.route("/Proyectos", methods=['GET'])
def GoProyectos():  
  return render_template("Proyectos.html")


@app.route('/FiltroProyecto', methods=['GET'])
def GetData():
    idSemillero = request.args.get("idSemillero")
    print(idSemillero)
    # Verifica si idSemillero está presente en la solicitud JSON
    if idSemillero is None:
        return {"error": "Se requiere el campo 'idSemillero' en la solicitud JSON"}, 400

    # Consulta en la entidad proyecto donde su fk de semillero sea igual a idSemillero
    results = bd.session.query(Proyecto) \
        .filter(Proyecto.idSemilleroFk == idSemillero).all()

    dato = {}
    i = 0
    for proyecto in results:
        i += 1
        dato[i] = {
            'codProyecto':proyecto.codProyecto,
            'nombreProyecto':proyecto.nombreProyecto,
            'fechaInicio' :proyecto.fechaInicio,
            'fechaFinal' :proyecto.fechaFinal,
            'descripcion': proyecto.descripcion,
            'idSemilleroFk': proyecto.idSemilleroFk       
        }
    return jsonify(dato)

@app.route('/Detalle', methods=['GET'])
def GetDetalle():
    codProyecto = request.args.get("codProyecto")
    print(codProyecto)
    # Verifica si idSemillero está presente en la solicitud JSON
    if codProyecto is None:
        return {"error": "Se requiere el campo 'idSemillero' en la solicitud JSON"}, 400

    # Consulta en la entidad proyecto donde su fk de semillero sea igual a idSemillero
    results = bd.session.query(Proyecto,Estudiante,EstudianteP,Objetivos,ResultadosOb) \
        .join(EstudianteP, Proyecto.codProyecto == EstudianteP.codProyectoFk) \
        .join(Estudiante, EstudianteP.idEstudianteFk == Estudiante.codigoE) \
        .join(Objetivos,  Proyecto.codProyecto == Objetivos.idProyectoOFk) \
        .join(ResultadosOb,  Proyecto.codProyecto == ResultadosOb.idProyectoObFk) \
        .filter(Proyecto.codProyecto == codProyecto).all()

      # Listas donde se almacenarán los datos de cada entidad
    estudiantes_list = []
    proyectos_list = []
    estudiantesP_list = []
    objetivos_list = []
    resultadosOb_list = []
    for  proyecto,estudiante,estudiantep,objetivos, resultadosOb in results: 
        proyectos_list.append({
            "codProyecto": proyecto.codProyecto,
            "nombreProyecto": proyecto.nombreProyecto,
        })
        estudiantes_list.append({
            "codigoE": estudiante.codigoE,
            "nombre": estudiante.nombre,
            "apellido": estudiante.apellido,
        })
        estudiantesP_list.append({
            "codigoEstudianteP": estudiantep.codigoEstudianteP,
            "codProyectoFk": estudiantep.codProyectoFk,
            "idEstudianteFk": estudiantep.idEstudianteFk,
        })
        
        objetivos_list.append({
            "codigoOb": objetivos.codigoOb,
            "descripcion": objetivos.descripcion,
        })

        resultadosOb_list.append({
            "codigoRO": resultadosOb.codigoRO,
            "descripcionOb": resultadosOb.descripcionOb,
        })

    # Eliminar duplicados de las listas
    estudiantes_list = [dict(t) for t in {tuple(d.items()) for d in estudiantes_list}]
    estudiantesP_list = [dict(t) for t in {tuple(d.items()) for d in estudiantesP_list}]
    objetivos_list = [dict(t) for t in {tuple(d.items()) for d in objetivos_list}]
    resultadosOb_list = [dict(t) for t in {tuple(d.items()) for d in resultadosOb_list}]

    return jsonify({
        "Estudiantes": estudiantes_list,
        "EstudiantesP":estudiantesP_list,
        "Objetivos": objetivos_list,
        "ResultadosOb": resultadosOb_list
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9566)