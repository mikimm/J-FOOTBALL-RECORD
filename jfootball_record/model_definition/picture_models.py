from django.db import models

from jfootball_record.model_definition.match_records_models import MatchRecords
from jfootball_record.model_definition.teams_models import Teams
from jfootball_record.model_definition.users_models import Users

class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    record_id = models.OneToOneField(MatchRecords,on_delete=models.CASCADE)
    picture_image = models.BinaryField()