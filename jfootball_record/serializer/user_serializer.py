from rest_framework import serializers

from jfootball_record.model_definition.users_models import Users

        
# User用シリアライザー
class UserSerializer(serializers.ModelSerializer):
    team = serializers.IntegerField(source="favoriteteams.team_id")
    class Meta:
        model=Users
        fields = ['username', 'password', 'email', 'gender','team']
