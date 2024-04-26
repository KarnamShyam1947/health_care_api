from flask_restx import Api, Namespace, Resource, reqparse
from werkzeug.datastructures import FileStorage
from utils.FirebaseUtils import upload_to_cloud
from flask_jwt_extended import jwt_required
from flask import request

uploadArgs = reqparse.RequestParser()
uploadArgs.add_argument("email", location="form", type=str)
uploadArgs.add_argument("resume", location="files", type=FileStorage)
uploadArgs.add_argument("profile", location="files", type=FileStorage)

modelUploadArgs = reqparse.RequestParser()
modelUploadArgs.add_argument("model", location="files", type=FileStorage, required=True)

authorization = {
    "jsonWebToken" : {
        "type" : "apiKey",
        "in" : "header",
        "name" : "Authorization"
    }
}

fileUploadController = Namespace(
    name="uploads", 
    description="to manage uploading of files and updating the models ", 
    path="/upload",
    authorizations=authorization
)

@fileUploadController.route('/file')
class UploadController(Resource):
    @fileUploadController.expect(uploadArgs)
    def post(self):
        args = uploadArgs.parse_args()
        email = args['email']
        resume = args['resume']
        profile = args['profile']

        result = dict()

        if resume:
            result['resume'] = upload_to_cloud(resume, email, "resume")
            
        if profile:
            result['profile'] = upload_to_cloud(profile, email, "profile")

        print(result)
        return result

@fileUploadController.route("/multi-file")
class MultipleFileUploadResource(Resource):
    # def get(self):
    #     return {'use' : 'post'}
    
    def post(self):
        names = request.form.getlist("name[]")
        files = request.files.getlist("files[]")

        result = {}

        for name, file in zip(names, files):
            result[name] = upload_to_cloud(file, name, "reports", True)

        return result

@fileUploadController.route("/brain-tumor-model")
class BrainTumorUploadResource(Resource):
    method_decorators = [jwt_required()]

    @fileUploadController.doc(security="jsonWebToken")
    @fileUploadController.expect(modelUploadArgs)
    def post(self):
        args = modelUploadArgs.parse_args()
        model = args['model']

        with open("models/brain_tumor_epochs_10.h5", "wb") as file:
            file.write(model.read())

        return {
            "status" : "ok",
            "msg" : "model updated...!!"
        }
