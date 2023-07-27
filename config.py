import os


class Config:
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'a-very-secret-key')

    # Session
    SESSION_COOKIE_SECURE=True
    REMEMBER_COOKIE_SECURE=True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE='Lax'

    # Time Zone
    TIME_ZONE = 'UTC'

    # Base URL
    BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')


class DevelopmentConfig(Config):
    DEBUG = True

    # mongo local config
    MONGODB_SETTINGS = {
        'db': 'your_db',
        'host': 'mongodb://localhost:27017/your_db'
    }


class ProductionConfig(Config):
    DEBUG = False

    # mongo production config
    MONGODB_SETTINGS = {
        'db': 'your_prod_db',
        'host': 'mongodb://your_user:your_password@mongo.yourdomain.com:27017/your_prod_db'
    }


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
