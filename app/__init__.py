# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/ip_management.db'
    
    db.init_app(app)  # در اینجا db را به اپلیکیشن متصل می‌کنیم.
    migrate.init_app(app, db)  # مشابه بالا.

    from .routes import main_bp  # اینجا از routes پس از ایجاد app استفاده می‌کنیم.
    app.register_blueprint(main_bp)

    return app
