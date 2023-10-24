from firebase_admin import storage

def upload_to_firebase(uploaded_file):
    bucket = storage.bucket()
    blob = bucket.blob("planty_users/" + uploaded_file.name)
    content_type = uploaded_file.content_type or "application/octet-stream"
    blob.content_type = content_type
    blob.upload_from_file(uploaded_file.file)
    blob.make_public()
    return blob.public_url

def delete_from_firebase(file_path):
    try:
        bucket = storage.bucket()
        blob = bucket.blob(file_path)
        blob.delete()
        return 200
    except Exception as e:
        return 400