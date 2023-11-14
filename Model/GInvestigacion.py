
from config.bd import app, bd, ma
from Model.ProfesorPrograma import ProfesorPrograma


class GInvestigacion(bd.Model):
    __tablename__ ='tblGInvestigacion'
    codigoGI = bd.Column(bd.Integer, primary_key = True)
    nombre = bd.Column(bd.String(50))
    lider = bd.Column(bd.String(50))
    lineaInvestigacion = bd.Column(bd.String(50))
    # Relación unidireccional con profesor_programa
    profesor_programaPk =bd.Column(bd.Integer,bd.ForeignKey("tblProfesorPrograma.idProfesorPrograma"))
    
     
    
    #Constructor
    def __init__(self,nombre,lider,lineaInvestigacion,idProfesorFk):
        self.nombre=nombre
        self.lider=lider
        self.lineaInvestigacion=lineaInvestigacion
        self.idProfesorFk=idProfesorFk



#Creacion de la tabla 
with app.app_context():
    bd.create_all()

#Descerializacion
class GrupoInvestigacion_Schema(ma.Schema):
    class Meta:
        fields=("nombre","lider","lineaInvestigacion","idProfesorFk")
