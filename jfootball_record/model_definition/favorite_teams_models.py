from django.db import models
from jfootball_record.model_definition.users_models import Users
from jfootball_record.model_definition.teams_models import Teams
from django.core.validators import MinValueValidator,MaxValueValidator
class FavoriteTeams(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(Users,on_delete=models.CASCADE)
    team=models.ForeignKey(Teams,validators=[MinValueValidator(1),MaxValueValidator(60)],on_delete=models.CASCADE)