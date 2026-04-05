import json
from typing import Any

from jfootball_record.adaptor.adaptor import Adaptor
from jfootball_record.exception.exceptions import ExternalAPIError, NotFoundError
from jfootball_record.model_definition.teams_models import Teams


class Team_Usecase:
        
    def handle(self,**kwargs) -> Any:
        team_id=kwargs['team_id']
        try:
            t=Teams.objects.get(id=team_id)
        except Teams.DoesNotExist:
             raise NotFoundError("team not found")
        try:
            output= Adaptor.get_team(team_id= t.api_foot_ball_team_id)
        except Exception as e:
            raise ExternalAPIError(e)
        
        return output