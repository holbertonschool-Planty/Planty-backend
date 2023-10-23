from firebase_admin import storage

def upload_to_firebase(uploaded_file):
    bucket = storage.bucket()
    blob = bucket.blob(uploaded_file.name)
    blob.upload_from_file(uploaded_file.file)
    blob.make_public()
    return blob.public_url