from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes import main_bp  # import کردن Blueprint

# راه‌اندازی دیتابیس و مهاجرت
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # تنظیمات مربوط به دیتابیس
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/ip_management.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # برای جلوگیری از هشدار

    # راه‌اندازی db و migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # ثبت Blueprint
    app.register_blueprint(main_bp, url_prefix='/')  # اضافه کردن Blueprint با url_prefix

    return app
