from config import create_app
from controllers.pessoa_controller import pessoa_bp
from database import db

app = create_app()
db.init_app(app)

app.register_blueprint(pessoa_bp, url_prefix='/pessoas')

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(host='localhost', port=5001, debug=True)