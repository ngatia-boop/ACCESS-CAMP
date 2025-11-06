from flask import Flask
from .config import Config
from .models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    Migrate(app, db)
    
    # Register blueprints
    from .routes.campers import campers_bp
    from .routes.activities import activities_bp
    from .routes.signups import signups_bp
    
    app.register_blueprint(campers_bp, url_prefix='/campers')
    app.register_blueprint(activities_bp, url_prefix='/activities')
    app.register_blueprint(signups_bp, url_prefix='/signups')
    
    return app