from config.bd import  bd,app,ma

class Estudiante(bd.Model):
    __tablename__ ='tblEstudiante'
    codigoE = bd.Column(bd.Integer, primary_key = True)
    nombre = bd.Column(bd.String(50))
    apellido = bd.Column(bd.String(50))
    correo = bd.Column(bd.String(50))
    telefono = bd.Column(bd.String(50))
    

    #constructor
    def __init__(self,codigoE,nombre,apellido,correo,telefono):
        self.codigoE =codigoE
        self.nombre =nombre
        self.apellido = apellido
        self.corre=correo
        self.telefono=telefono
   

#Creacion de la tabla 
with app.app_context():
    bd.create_all()


#Descerializacion
class EstudianteSchema(ma.Schema):
    class Meta:
        fields=("nombre","apellido","correo","telefono")
