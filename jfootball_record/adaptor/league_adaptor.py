import os
from typing import Any
import requests

from backend.settings import SEASON, X_API_SPORTS_KEY

class League_Adaptor():
    def call(self,**kwargs) -> Any:
        division_id=kwargs["division_id"]
        parameter = {
        "league": division_id,
        "season": SEASON 
        }
        headers = {"x-apisports-key": X_API_SPORTS_KEY}
        response = requests.get("https://v3.football.api-sports.io/standings",params=parameter,headers=headers)
        if response.status_code !=200:
            raise Exception(response.json())  
        return_data = {"status": response.status_code, "data": response.json()}     
        return return_data