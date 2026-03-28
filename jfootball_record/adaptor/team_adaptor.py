from typing import Any
import requests

from backend.settings import X_API_SPORTS_KEY

class Team_Adaptor():
    def call(self,**kwargs) -> Any:
        team_id=kwargs["team_id"]
        parameter = {
        "id": team_id
        }
        headers = {"x-apisports-key": X_API_SPORTS_KEY}
        response = requests.get("https://v3.football.api-sports.io/teams", params=parameter,headers=headers)
        if response.status_code !=200:
            raise Exception(response.json())  
        return_data = {"status": response.status_code, "data": response.json()}     
        return return_data