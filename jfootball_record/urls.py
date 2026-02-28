from django.urls import path
from jfootball_record.views.user_views import UserView
from jfootball_record.views.team_views import TeamListView
from jfootball_record.views.match_records_views import MatchRecordsView
from jfootball_record.views.comments_views import CommentsView
urlpatterns = [
    path('create/user', UserView.as_view()),
    path('create/match_records', MatchRecordsView.as_view()),
    path('create/comments/<int:match_records_id>', CommentsView.as_view()),
    path('teams/<int:league_id>', TeamListView.as_view()),
]