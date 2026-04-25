from django.http import JsonResponse
from rest_framework import generics
from jfootball_record.exception.exception_handler import hundle_exception
from rest_framework.views import APIView

from jfootball_record.usecase.palyers_usecase import players_usecase_handle

# Create your views here.
class TeamPlayersView(APIView):
        
    def get(self, request, *args, **kwargs):
        try:
            output=players_usecase_handle(team_id=self.kwargs['team_id'],player_id=self.kwargs['player_id'])
        except Exception as e:
            return hundle_exception(e)
        return JsonResponse(output)