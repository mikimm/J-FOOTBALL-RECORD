from django.http import Http404, HttpResponseServerError, JsonResponse
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.response import Response
from jfootball_record.exception.exceptions import ExternalAPIError, NotFoundError
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
        return get_list_or_404(Teams, league_id=league_id)


class TeamDetailView(APIView):
    usecase :Usecase = None   # ← クラス属性として定義
        
    def get(self, request, *args, **kwargs):
        try:
            output=self.usecase.handle(team_id=self.kwargs['team_id'])
        except NotFoundError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except ExternalAPIError as e:
            return JsonResponse({"error": str(e)}, status=500)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        return JsonResponse({"output":output})