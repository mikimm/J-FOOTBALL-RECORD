from rest_framework import serializers

from django.db import models
from jfootball_record.model_definition.comments_models import Comments

# Comments用シリアライザー
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        exclude = ['record','comment_by']