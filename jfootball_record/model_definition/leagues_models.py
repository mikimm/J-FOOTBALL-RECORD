from django.db import models

class Leagues(models.Model):
    id = models.AutoField(primary_key=True)
    api_foot_ball_league_id=models.IntegerField()
    divison = models.CharField()
    league_logo=models.CharField()