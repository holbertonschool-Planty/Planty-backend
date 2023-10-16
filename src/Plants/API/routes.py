from ninja import Router
from src.Plants.schemas import Plants_info_Out
from src.Plants.models import Plants_info

router = Router()

@router.get("", response=list[Plants_info_Out])
def plants_info(request):
    plants_info = Plants_info.objects.get_list()
    return plants_info
