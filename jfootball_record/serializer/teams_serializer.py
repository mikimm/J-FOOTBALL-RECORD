from rest_framework import serializers

from jfootball_record.model_definition.teams_models import Teams

# Teams用シリアライザー
class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teams
        fields = ['team_name', 'team_logo']