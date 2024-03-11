from config import firebaseConfig
import pyrebase
import uuid

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

def upload_to_cloud(file, email=uuid.uuid4(), type=""):
    name = email.split("@")[0].lower()
    extension = file.filename.split('.')[-1].lower()

    if type == "":
        filename = f"{name}.{extension}"

    else:
        filename = f"{name}_{type}.{extension}"

    result = storage.child(filename).put(file.read(), "working")
    downloadToken = result['downloadTokens']
    url = f"https://firebasestorage.googleapis.com/v0/b/test-app-68958.appspot.com/o/{filename}?alt=media&token={downloadToken}"

    return url


    