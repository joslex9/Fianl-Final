from config.bd import ma , bd, app

class ResultadosOb(bd.Model):
  __tablename__="tblResultadosOb"
  codigoRO = bd.Column(bd.Integer, primary_key = True)
  descripcionOb=bd.Column(bd.String(50))
  idProyectoObFk =bd.Column(bd.Integer,bd.ForeignKey("tblProyecto.codProyecto"))#Relacion con tblProyecto

#Constructor
  def __inti__(self,codigoRO,descripcionOb,idProyectoObFk):
   self.codigoRO=codigoRO
   self.descripcionOb=descripcionOb
   self.idProyectoObFk=idProyectoObFk


#Creacion de la tabla 
with app.app_context():
    bd.create_all()

#Descerializacion
class ResultadosObSchema(ma.Schema):
    class Meta:
        fields=("codigoRO","descripcionOb","idProyectoObFk")


 