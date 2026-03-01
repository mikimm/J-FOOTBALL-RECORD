from rest_framework import serializers

from jfootball_record.model_definition.nice_models import Nice

# Comments用シリアライザー
class NiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nice
        fields =  ['record', 'post_by']