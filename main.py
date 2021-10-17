import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db 
from flask_restful import Api

def create_app(): 
    app = Flask(__name__)
    if os.getenv('ENV', "development") == "production": 
        raise Exception("CURRENTLY ONLY DEVELOPMENT!")
    else: 
        print("Starting Local Development")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    api = Api(app)
    return app, api

app, api = create_app()


@app.route("/")
def health(): 
    return {
        "message": "ok"
    }

if __name__ == "__main__": 
    app.run("0.0.0.0", port=8080)




