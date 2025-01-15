"""
Эта структурная папка, нужна на случай если к сервисам привязаны репозитории
"""
from api_project.aplication.settings import AppSettings
from api_project.aplication.tariffs.services import TariffsService

api_creds = AppSettings()

tariffs_repository = TariffsService(api_creds)


def get_tariffs_service() -> TariffsService:
    return tariffs_repository
