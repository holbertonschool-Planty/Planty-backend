from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from src.Plants.API.routes import router as Plants_info_router

api = NinjaAPI()
api.add_router("plants_info", Plants_info_router)

# @api.get("/hello")
# def hello(request):
#     return "Hello world"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls)
]
