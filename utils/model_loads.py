from django.apps import apps

def get_plant_model():
    return apps.get_model("Plants", "Plants_info")
