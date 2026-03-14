from django.forms import IntegerField
from rest_framework import serializers

from jfootball_record.model_definition.match_records_models import MatchRecords
from jfootball_record.model_definition.nice_models import Nice
from jfootball_record.model_definition.users_models import Users

# Nice用シリアライザー
class NiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nice
        fields =  ['record', 'post_by']
        read_only_fields = ['record', 'post_by']
        
            
    def check_create(self,data):
            """
            Check Record and User
            """
            if not Users.objects.filter(id=data["post_by_id"]).exists():
                raise serializers.ValidationError("user not found")
            elif not MatchRecords.objects.filter(id=data["record_id"]).exists():
                raise serializers.ValidationError("record not found")
            
            u=Users.objects.get(id=data["post_by_id"])
            m=MatchRecords.objects.get(id=data["record_id"])
            
            if u.id == m.created_by_id:
                raise serializers.ValidationError("not permissioned")
            return data
        
            