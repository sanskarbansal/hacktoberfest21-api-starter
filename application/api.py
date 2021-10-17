
from flask_restful import Resource, reqparse, fields, marshal_with
from application.database import db
from application.models import Contestant

output_fields = {
    'id': fields.String, 
    'name': fields.String, 
    'costumeTitle': fields.String, 
    'costumeImgUrl': fields.String,
    'votes': fields.Integer, 
    'city': fields.String, 
    'country': fields.String, 

}


parser = reqparse.RequestParser()
parser.add_argument("name", required=True, help='Must provide name')
parser.add_argument("costumeTitle", required=True, help='Must provide costumeTitle')
parser.add_argument("costumeImgUrl", required=True, help='Must provide costumeImgUrl')
parser.add_argument("city", required=True, help='Must provide city' )
parser.add_argument("country", required=True, help='Must provide country')



class ContestantResource(Resource): 
    def get(self):
        pass
    def patch(self):
        pass
    def delete(self): 
        pass

class ContestantsResource(Resource): 
    @marshal_with(output_fields)
    def get(self): 
        constestants = db.session.query(Contestant).all()
        return constestants
    def post(self): 
        args = parser.parse_args()
        name = args.get("name", None)
        costumeTitle = args.get("costumeTitle", None)
        costumeImgUrl = args.get("costumeImgUrl", None)
        city = args.get("city", None)
        country = args.get("country", None)

        contestant = Contestant(name = name, costumeImgUrl = costumeImgUrl, costumeTitle = costumeTitle, city = city, country = country)

        db.session.add(contestant)
        db.session.commit()
        return {
            "id": contestant.id
        }, 201