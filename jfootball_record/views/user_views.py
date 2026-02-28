from rest_framework import generics

from jfootball_record.serializer.user_serializer import UserSerializer
from jfootball_record.model_definition.users_models import Users
from jfootball_record.model_definition.favorite_teams_models import FavoriteTeams
from jfootball_record.model_definition.teams_models import Teams
from django.db import transaction,IntegrityError
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
# Create your views here.
@transaction.non_atomic_requests
class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                #登録処理
                with transaction.atomic():
                    #ユーザーの登録
                    u = Users(username=request.data['username'], password=request.data['password'],email=request.data['email'],gender=request.data['gender'])
                    u.save()
                    #チームのモデルオブジェクト取得
                    t=Teams.objects.get(id=request.data['team'])
                    #お気に入りチームの登録
                    f = FavoriteTeams(user_id=u.id,team_id=t.id)
                    f.save()
            except Teams.DoesNotExist:
                    return JsonResponse({"error": "チーム情報が存在しません"}, status=status.HTTP_404_NOT_FOUND)
            except IntegrityError:
                    return JsonResponse({"error": "サーバーエラーが発生しました"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)