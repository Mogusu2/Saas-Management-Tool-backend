from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    # Import and register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.budget_routes import budget_bp
    from app.routes.expense_routes import expense_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(budget_bp, url_prefix='/budgets')
    app.register_blueprint(expense_bp, url_prefix='/expenses')

    return app
