from config.bd import ma , bd, app

class Objetivos(bd.Model):
 __tablename__="tblObjetivos"
 codigoOb = bd.Column(bd.Integer, primary_key = True)
 descripcion=bd.Column(bd.String(50))
 idProyectoOFk =bd.Column(bd.Integer,bd.ForeignKey("tblProyecto.codProyecto"))#Relacion con tblProyecto

#Constructor
 def __inti__(self,codigoOb,descripcion,idProyectoFk):
  self.codigoOb=codigoOb
  self.descripcion=descripcion
  self.idProyectoOFk=idProyectoFk


#Creacion de la tabla 
with app.app_context():
    bd.create_all()

#Descerializacion
class ObjetivosSchema(ma.Schema):
    class Meta:
        fields=("codigoOb","descripcion","idProyectoOFk")


 