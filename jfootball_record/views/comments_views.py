from rest_framework import generics
from jfootball_record.serializer.comments_serializer import CommentsSerializer
# Create your views here.
class CommentsView(generics.CreateAPIView):
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        record_id = self.kwargs['record_id']
        serializer.save(record_id=record_id,comment_by_id=1)
