from dataclasses import dataclass
import aiohttp

from api_project.aplication.settings import AppSettings


@dataclass
class TariffsService:
    api_creds: AppSettings

    @staticmethod
    async def _fetch(session, url, headers):
        async with session.get(url, headers=headers) as response:
            return await response.json()

    async def get_whatcrm_response(self) -> None:

        headers = {
            'X-Whatsapp-Token': self.api_creds.TARIFFS_API_KEY,
        }

        async with aiohttp.ClientSession() as session:
            json_resp = await self._fetch(session, self.api_creds.TARIFFS_URL, headers)
            return json_resp
