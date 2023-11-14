from config.bd import app, ma,bd

#Relacion muchos a muchos entre proyecto y estudiante
class EstudianteP(bd.Model):
 __tablename__="tblEstudianteP"
 codigoEstudianteP=bd.Column(bd.Integer,primary_key=True)
 codProyectoFk =bd.Column(bd.Integer,bd.ForeignKey("tblProyecto.codProyecto"))#Relacion con tblProyecto
 idEstudianteFk =bd.Column(bd.Integer,bd.ForeignKey("tblEstudiante.codigoE"))#Relacion con Estudiante
#Constructor
 def __init__(self,codigoEstudianteP,codProyectoFk,idEstudianteFk):
        self.codigoEstudianteP=codigoEstudianteP
        self.codProyectoFk=codProyectoFk
        self.idEstudianteFk=idEstudianteFk


#Creacion de la tabla 
with app.app_context():
    bd.create_all()

#Descerializacion
class EstudiantePSchema(ma.Schema):
    class Meta:
        fields=("codigoEstudianteP","codProyectoFk","idEstudianteFk")
