from fastapi import APIRouter, Depends

from api_project.aplication.app import get_tariffs_service
from api_project.aplication.tariffs.services import TariffsService

whatcrm_router = APIRouter(
   prefix="/tariffs",
   tags=["Тарифы"],
)


@whatcrm_router.get("/tariffs")
async def get_tariffs(tariffs_service: TariffsService = Depends(get_tariffs_service)):
    return await tariffs_service.get_whatcrm_response()
