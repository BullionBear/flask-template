from flask import Flask
from flasgger import Swagger
from api.views import api_blueprint
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    Swagger(app)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app

app = create_app()

if __name__ == "__main__":
    app.run()