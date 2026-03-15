from rest_framework import generics
from jfootball_record.model_definition.picture_models import Picture
from jfootball_record.serializer.picture_serializer import UploadedPictureSerializer
# Create your views here.
class PictureView(generics.CreateAPIView,generics.RetrieveAPIView):
    serializer_class = UploadedPictureSerializer
    queryset = Picture.objects.all()
    lookup_field = 'record_id'
    #TODO:user_idの取得方法
    user_id=1
    def perform_create(self, serializer):
        record_id = self.kwargs['record_id']
        serializer.check_create(data={"record_id":record_id,"user_id":self.user_id})
        serializer.save(record_id=record_id)
