from resources.UploadResource import fileUploadController
from resources.PredictResource import predictController
from flask_restx import Api
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
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

if __name__ == "__main__":
    app.run(debug=True)
