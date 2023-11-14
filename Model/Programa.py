
from config.bd  import ma, bd, app
class Programa(bd.Model):
    __tablename__="tblPrograma"
    codigoPrograma = bd.Column(bd.Integer, primary_key=True)
    codigo=bd.Column(bd.Integer, unique=True)
    nombre=bd.Column(bd.String(50))
    facultad=bd.Column(bd.String(50))

#Constructor
    def  __init__(self,codigo,nombre,facultad):
        self.codigo=codigo
        self.nombre=nombre
        self.facultad=facultad


#Creacion de la tabla 
with app.app_context():
    bd.create_all()


#Descerializacion
class ProgramaSchema(ma.Schema):
    class Meta:
        fields=("codigo","nombre","facultad")
