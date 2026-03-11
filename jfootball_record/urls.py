
from django.urls import path
from jfootball_record.adaptor.team_adaptor import Team_Adaptor
from jfootball_record.usecase.team_usecase import Team_Usecase
from jfootball_record.views.user_views import UserView
from jfootball_record.views.team_views import TeamDetailView, TeamListView
from jfootball_record.views.match_records_views import MatchRecordsView
from jfootball_record.views.comments_views import CommentsView
from jfootball_record.views.nice_views import NiceView
from rest_framework.routers import DefaultRouter

au=Team_Adaptor()
tu = Team_Usecase(au)
router=DefaultRouter()
router.register('nice',NiceView)
urlpatterns = [
    path('user', UserView.as_view()),
    path('match_records', MatchRecordsView.as_view()),
    path('comments/<int:match_records_id>', CommentsView.as_view()),
    path('teams/<int:league_id>', TeamListView.as_view()),
    path('teams/detail/<int:team_id>', TeamDetailView.as_view(usecase=tu)),
]+router.urls