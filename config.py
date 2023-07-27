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


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
