from config.bd import app,bd,ma

class Profesor(bd.Model):
    __tablename__="tblProfesor"
    codigoProfesor=bd.Column(bd.Integer,primary_key=True)
    codigo=bd.Column(bd.Integer,unique=True) #Campo unico
    telefono=bd.Column(bd.String(50))
    nombre=bd.Column(bd.String(50))
    Apellido=bd.Column(bd.String(50))
    correo=bd.Column(bd.String(50))

#Constructor
    def __init__(self,codigo,telefono,nombre,Apellido,correo):
        self.codigo=codigo
        self.telefono=telefono
        self.nombre=nombre
        self.Apellido=Apellido
        self.correo=correo


#Creacion de la tabla 
with app.app_context():
    bd.create_all()

#Descerializacion
class ProfesorSchema(ma.Schema):
    class Meta:
        fields=("codigo","telefono","nombre","Apellido","correo")
