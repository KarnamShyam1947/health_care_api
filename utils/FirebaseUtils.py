from config import firebaseConfig
import pyrebase
import uuid

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

def upload_to_cloud(file, email=uuid.uuid4(), type="", unique=False):
    name = email.split("@")[0].lower()
    extension = file.filename.split('.')[-1].lower()

    if type == "":
        filename = f"{name}_{uuid.uuid4()}.{extension}" if unique  else f"{name}.{extension}"

    else:
        filename = f"{type}/{name}_{type}_{uuid.uuid4()}.{extension}" if unique else f"{type}/{name}_{type}.{extension}"
    
    result = storage.child(filename).put(file.read(), "working")
    downloadToken = result['downloadTokens']
    url = storage.child(filename).get_url(None)
     
    return url


    