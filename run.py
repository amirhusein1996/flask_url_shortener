from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from config import config
from app.routers.index import blue_print as index_bp
from app.routers.redirect import blue_print as redirect_bp

# create an instance of Flask class
app = Flask(__name__)

# set config
app.config.from_object(config['development'])

# csrf protection of flask-wtf
csrf = CSRFProtect(app)

# flask_mongoengine configurations
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

#  register blue prints
app.register_blueprint(index_bp)
app.register_blueprint(redirect_bp)


if __name__ == '__main__':
    app.run()
