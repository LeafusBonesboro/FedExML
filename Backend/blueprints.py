from routes.data_routes import data_bp
from routes.model_routes import model_bp
from routes.static_routes import static_bp

def register_blueprints(app):
    """Registers all blueprints to the Flask app."""
    app.register_blueprint(data_bp, url_prefix='/data')
    app.register_blueprint(model_bp, url_prefix='/model')
    app.register_blueprint(static_bp)
