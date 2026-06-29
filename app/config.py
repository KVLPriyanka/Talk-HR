"""
Configuration management for HR Portal Backend
"""
import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "your-very-secret-key-here")
    
    # Flask-Session settings
    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    
    # SQLAlchemy configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    
    # Safely escape special characters (like '@') in the password
    _raw_password = "Jyothi@1978"
    _escaped_password = quote_plus(_raw_password)
    
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"mysql+pymysql://root:{_escaped_password}@localhost/hr_portal"
    )

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}