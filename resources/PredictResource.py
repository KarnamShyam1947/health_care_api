from flask_restx import Namespace, Resource, reqparse
from utils.PredictUtils import classify_using_bytes
from werkzeug.datastructures import FileStorage

predictController = Namespace(
    name="predict",
    description="Upload the brain tumor MRI image to get prediction of disease",
    path="/predict",
)

predictArgs = reqparse.RequestParser()
predictArgs.add_argument(name = "image", location="files", type=FileStorage, required=True)

class PredictResource(Resource):
    
    @predictController.expect(predictArgs)
    def post(self):
        args = predictArgs.parse_args()

        image = args['image']

        result = classify_using_bytes(image.read(), "models/brain_tumor_epochs_10.h5", 224)

        return result
    
predictController.add_resource(PredictResource, "/brain_tumor")
