import json
import firebase_admin
from firebase_admin import credentials
from .settings import SERVER_FIREBASE, SERVER_FIREBASE_PRIVATE_KEY

def initialize_firebase():
    firebase_credentials_dict = json.loads(SERVER_FIREBASE_PRIVATE_KEY)
    cred = credentials.Certificate(firebase_credentials_dict)
    firebase_admin.initialize_app(cred, {'storageBucket': SERVER_FIREBASE})