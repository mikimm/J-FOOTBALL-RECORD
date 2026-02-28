from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.response import Response
from jfootball_record.model_definition.teams_models import Teams
from jfootball_record.serializer.teams_serializer import TeamsSerializer
# Create your views here.
class TeamListView(generics.ListAPIView):
    serializer_class = TeamsSerializer
    
    def get_queryset(self):
        # URLからリーグIDを取得してフィルタ
        league_id = self.kwargs['league_id']
        return get_list_or_404(Teams, league_id=league_id)
