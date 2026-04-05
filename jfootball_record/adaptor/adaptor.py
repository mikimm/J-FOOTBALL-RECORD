from typing import Any
import requests

from backend.settings import SEASON, X_API_SPORTS_KEY

class Adaptor():
    def call_api(url:str,parameter:dict) ->dict:
        headers = {"x-apisports-key": X_API_SPORTS_KEY}
        response = requests.get(url, params=parameter,headers=headers)
        if response.status_code !=200:
            raise Exception(response.json())  
        return_data = {"status": response.status_code, "data": response.json()}     
        return return_data
    @classmethod
    def get_ranking(self,**kwargs) -> Any:
        division_id=kwargs["division_id"]
        parameter = {
        "league": division_id,
        "season": SEASON 
        }
        return self.call_api("https://v3.football.api-sports.io/standings",parameter)
    @classmethod
    def get_team(self,**kwargs) -> Any:
        team_id=kwargs["team_id"]
        parameter = {
        "id": {team_id}
        }
        return self.call_api("https://v3.football.api-sports.io/teams",parameter)
    
