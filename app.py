from resources.UploadResource import fileUploadController
from resources.PredictResource import predictController
from resources.AuthResource import auth_controller
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
app.secret_key = "this-is-secret"

jwt = JWTManager(app)
CORS(app)

api = Api(
    app=app,
    version="1.0",
    title="Health Care API",
    description="This api is used to get predict the type of disease",
    doc="/",
    validate=True
)


api.add_namespace(fileUploadController)
api.add_namespace(predictController)
api.add_namespace(auth_controller)

if __name__ == "__main__":
    app.run(debug=True)
