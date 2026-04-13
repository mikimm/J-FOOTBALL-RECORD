from django.http import JsonResponse
from rest_framework import generics
from django.shortcuts import get_list_or_404
from jfootball_record.exception.exception_handler import hundle_exception
from jfootball_record.model_definition.teams_models import Teams
from jfootball_record.serializer.teams_serializer import TeamsSerializer
from rest_framework.views import APIView

from jfootball_record.usecase.usecase_protocol import Usecase
# Create your views here.
class TeamListView(generics.ListAPIView):
    serializer_class = TeamsSerializer
    
    def get_queryset(self):
        # URLからリーグIDを取得してフィルタ
        league_id = self.kwargs['league_id']
        return Teams.objects.filter(league_id=league_id)


class TeamDetailView(APIView):
    usecase :Usecase = None   # ← クラス属性として定義
        
    def get(self, request, *args, **kwargs):
        try:
            output=self.usecase.handle(team_id=self.kwargs['team_id'])
        except Exception as e:
            return hundle_exception(e)
        return JsonResponse({"output":output})