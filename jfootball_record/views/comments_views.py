from rest_framework import generics
from jfootball_record.serializer.comments_serializer import CommentsSerializer
# Create your views here.
class CommentsView(generics.CreateAPIView):
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        match_records_id = self.kwargs['match_records_id']
        serializer.save(record_id=match_records_id,comment_by_id=1)
