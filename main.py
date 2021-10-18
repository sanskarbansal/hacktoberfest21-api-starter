import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db 
from flask_restful import Api

from application.models import Contestant

def create_app(): 
    app = Flask(__name__)
    if os.getenv('ENV', "development") == "production": 
        raise Exception("CURRENTLY ONLY DEVELOPMENT!")
    else: 
        print("Starting Local Development")
        app.config.from_object(LocalDevelopmentConfig)

    db.init_app(app)
    app.app_context().push()
    db.create_all()
    api = Api(app)

    return app, api

app, api = create_app()


@app.route("/")
def health(): 
    return {
        "status": "OK"
    }

@app.route("/contestants/<string:id>/upvote", methods=["PATCH"])
def upvote(id): 
    player = db.session.query(Contestant).get(id)
    if player is None: 
        return {
            "status": "Contestant Not Found!"
        }, 404
    player.votes += 1
    db.session.commit()
    return {
        "status": "ok", 
        "votes": player.votes
    }, 200

from application.api import ContestantsResource, ContestantResource

api.add_resource(ContestantResource, "/contestants/<string:id>")
api.add_resource(ContestantsResource, "/contestants")


if __name__ == "__main__": 
    app.run("0.0.0.0", port=8080)




