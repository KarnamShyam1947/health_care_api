from flask_restx import Namespace, Resource, reqparse
from flask_jwt_extended import create_access_token

auth_controller = Namespace(
    name="Authentication ",
    description="to authenticate the admin to update the model",
    path="/auth"
)

login_args = reqparse.RequestParser()
login_args.add_argument(
    type=str, 
    required=True, 
    name="email", 
    location="json", 
    help="email is required"
)
login_args.add_argument(
    type=str, 
    required=True, 
    name="password", 
    location="json", 
    help="Password is required"
)

@auth_controller.route("/authenticate")
class AuthController(Resource):

    @auth_controller.expect(login_args)
    def post(self):
        args = login_args.parse_args()

        email = args['email']
        password = args['password']

        if password == "admin" and email == "admin@gmail.com":
            return {
                "access-token" : create_access_token(
                    identity=email
                )
            }
        
        else:
            return {
                "error" : "invalid email or password"
            }
