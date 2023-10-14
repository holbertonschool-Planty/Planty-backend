from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

# @api.get("/hello")
# def hello(request):
#     return "Hello world"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls)
]
