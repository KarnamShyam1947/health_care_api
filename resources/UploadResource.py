from flask_restx import Api, Namespace, Resource, reqparse
from werkzeug.datastructures import FileStorage
from utils.FirebaseUtils import upload_to_cloud

uploadArgs = reqparse.RequestParser()
uploadArgs.add_argument("email", location="form", type=str)
uploadArgs.add_argument("resume", location="files", type=FileStorage)
uploadArgs.add_argument("profile", location="files", type=FileStorage)

fileUploadController = Namespace("uploads", "upload files to firebase cloud storage - used for doctor registration ", "/upload")

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
