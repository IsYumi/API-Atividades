from .config import create_app
from .controller.atividade_controller import atividade_bp
from .database import db

app = create_app()
db.init_app(app)
app.register_blueprint(atividade_bp,url_prefix='/atividades')

with app.app_context():
    db.create_all( )

if __name__ == '__main__':
    app.run(host='localhost',port=5001)