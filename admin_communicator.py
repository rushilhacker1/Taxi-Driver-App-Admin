from admin import finddriver
from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

class main(Resource):
    def get(self, cords):
        if len(cords.split(",")) != 2:
            abort(422, message="unprocessable cords")
        else:
            if cords.split(",")[1] == "":
                abort(422, message="unprocessable cords")
            else:
                results = finddriver(cords)
                if results != {}:
                    return results, 200
                else:
                    abort(400, message="no results found")
    
api.add_resource(main, "/<string:cords>")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
