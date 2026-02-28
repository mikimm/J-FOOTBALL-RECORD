from rest_framework import generics
from jfootball_record.serializer.match_records_serializer import MatchRecordsSerializer
# Create your views here.
class MatchRecordsView(generics.CreateAPIView):
    serializer_class = MatchRecordsSerializer

    def perform_create(self, serializer):
        serializer.save(created_by_id=1)
