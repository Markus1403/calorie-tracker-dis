from flask import Flask
from dotenv import load_dotenv
load_dotenv()
                                        
from config import Config
from core.extensions import db, migrate
                                        
# initialize flask app                                     
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
                                        
    db.init_app(app)
    migrate.init_app(app, db)
                                        
    import core.models
                                        
    from blueprints import main_bp
    app.register_blueprint(main_bp)
    return app
