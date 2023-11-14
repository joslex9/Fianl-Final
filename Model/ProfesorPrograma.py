from config.bd import app,bd,ma

class ProfesorPrograma(bd.Model):
    __tablename__ = 'tblProfesorPrograma'
    idProfesorPrograma = bd.Column(bd.Integer, primary_key=True)
    profesorId = bd.Column(bd.Integer, bd.ForeignKey("tblProfesor.codigoProfesor"))
    programaId = bd.Column(bd.Integer, bd.ForeignKey("tblPrograma.codigoPrograma"))

    def __init__(self, profesorId, programaId):
        self.profesorId = profesorId
        self.programaId = programaId
        

# Creación de la tabla
with app.app_context():
    bd.create_all()

# Descerialización
class GProfesorPrograma_Schema(ma.Schema):
    class Meta:
        fields = ("profesorId", "programaId")