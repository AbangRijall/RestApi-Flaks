from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

CORS(app)

#inisiasi variabel kosong bertipe dirtionary (dictionary = json)
indentitas = {} #variabel global

#class resurce
class ContohResource(Resource):
    #metode get dan post
    def get(self):
        # response = {"msg":"Halo dunia, ini app restful pertamaku"}
        return indentitas
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        indentitas["nama"] = nama
        indentitas["umur"] = umur
        response = {"msg" : "Data berhasil dimasukkan"}
        return response
    
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)