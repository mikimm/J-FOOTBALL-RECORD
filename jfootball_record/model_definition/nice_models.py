from django.db import models
from jfootball_record.model_definition.match_records_models import MatchRecords
from jfootball_record.model_definition.users_models import Users
class Nice(models.Model):
    id = models.AutoField(primary_key=True)
    record=models.ForeignKey(MatchRecords,on_delete=models.CASCADE)
    post_by=models.ForeignKey(Users, on_delete=models.CASCADE,db_column='post_by')
    
    class Meta:
       constraints = [
           models.UniqueConstraint(fields=['record', 'post_by'], name='unique_nice')
       ]