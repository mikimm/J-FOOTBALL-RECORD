from typing import Any
import requests

class Team_Adaptor():
    def call(self,**kwargs) -> Any:
        team_id=kwargs["team_id"]
        parameter = {
        "id": {team_id}
        }
        headers = {"x-apisports-key": ""}
        response = requests.get("https://v3.foqotball.api-sports.io/teams", params=parameter,headers=headers)
        if response.status_code !=200:
            raise Exception(response.json())  
        return_data = {"status": response.status_code, "data": response.json()}     
        return return_data