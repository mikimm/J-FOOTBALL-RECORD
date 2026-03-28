
from django.urls import path
from jfootball_record.adaptor.team_adaptor import Team_Adaptor
from jfootball_record.adaptor.league_adaptor import League_Adaptor
from jfootball_record.usecase.team_usecase import Team_Usecase
from jfootball_record.usecase.league_usecase import League_Usecase
from jfootball_record.views.picture_views import PictureView
from jfootball_record.views.user_views import UserView
from jfootball_record.views.league_views import LeagueRankingView
from jfootball_record.views.team_views import TeamDetailView, TeamListView
from jfootball_record.views.match_records_views import MatchRecordsViewSet
from jfootball_record.views.comments_views import CommentsView
from jfootball_record.views.nice_views import NiceView
from rest_framework.routers import DefaultRouter

ta=Team_Adaptor()
la=League_Adaptor()
tu = Team_Usecase(ta)
lu= League_Usecase(la)
router = DefaultRouter()
router.register('records',MatchRecordsViewSet)
urlpatterns = [
    path('user', UserView.as_view()),
    path('comments/<int:record_id>', CommentsView.as_view()),
    path('picture/<int:record_id>', PictureView.as_view()),
    path('teams/<int:league_id>', TeamListView.as_view()),
    path('teams/detail/<int:team_id>', TeamDetailView.as_view(usecase=tu)),
    path('league/ranking/<int:division_id>', LeagueRankingView.as_view(usecase=lu)),
    path('records/<int:record_id>/nice/',NiceView.as_view({"post": "create", "delete": "destroy","get": "list"}))
]+router.urls