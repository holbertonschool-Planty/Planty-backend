from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from src.Plants.API.routes import router as plants_info_router
from src.Users.API.users_routes import router as users_router
from src.Users.API.userphone_routes import router as userphone_router
from src.Devices.API.planty_routes import router as planty_router
from src.User_devices.API.routes import router as userplanty_router
from src.schemas.schemas import CustomBadRequest
from src.schemas.schemas import BadRequestResponse 
from .firebase_config import initialize_firebase
from django.contrib.sitemaps.views import sitemap
from .sitemaps import APISitemap

initialize_firebase()

api = NinjaAPI(
    title="Planty",
    description="Backend of Planty",
    auth=None,
)

@api.exception_handler(CustomBadRequest)
def handle_bad_request(request, exc: CustomBadRequest):
    return api.create_response(request, BadRequestResponse(detail=exc.detail), status=400)


api.add_router("users", users_router)
api.add_router("users/{users_id}/token", userphone_router)
api.add_router("users_planty", userplanty_router)
api.add_router("plants_info", plants_info_router)
api.add_router("planty", planty_router)

sitemaps = {
    'api': APISitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
