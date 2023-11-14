from config.bd import app,ma,bd

class Proyecto(bd.Model):
    __tablename__="tblProyecto"
    codProyecto =bd.Column(bd.Integer,primary_key=True)
    nombreProyecto=bd.Column(bd.String(50))
    fechaInicio=bd.Column(bd.String(50))
    fechaFinal=bd.Column(bd.String(50))
    descripcion=bd.Column(bd.String(50))

    idSemilleroFk =bd.Column(bd.Integer,bd.ForeignKey("tblSemillero.codigoSemillero"))#Relacion con Semillero

    #Constructor
    def __init__(self,nombreProyecto,fechaInicio,fechaFinal,objetivos,descripcion,resultadosObtenidos,idSemilleroFk):
        self.nombreProyecto=nombreProyecto
        self.fechaInicio=fechaInicio
        self.fechaFinal=fechaFinal
        self.objetivos=objetivos
        self.descripcion=descripcion
        self.resultadosObtenidos=resultadosObtenidos
       
        self.idSemilleroFk=idSemilleroFk
#Creacion de la tabla y contexto 
with app.app_context():
    bd.create_all()

#Descerializacion
class ProyectoSchema(ma.Schema):
    class Meta:
        fields=("nombreProyecto","fechaInicio","fechaFinal","descripcion","resultadosObtenidos","idSemilleroFk")
