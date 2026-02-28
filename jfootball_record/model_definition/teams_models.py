from django.db import models
from jfootball_record.model_definition.leagues_models import Leagues
class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    api_foot_ball_team_id=models.IntegerField()
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE)
    team_name=models.CharField(max_length=15,unique=True)
    team_logo=models.CharField()