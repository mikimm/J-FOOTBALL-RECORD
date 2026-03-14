
from django.http import JsonResponse
from jfootball_record.exception.exception_handler import hundle_exception
from jfootball_record.model_definition.match_records_models import MatchRecords
from jfootball_record.model_definition.nice_models import Nice
from jfootball_record.serializer.nice_serializer import NiceSerializer
from rest_framework import viewsets,mixins
from rest_framework import status
# Create your views here.
class NiceView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = NiceSerializer
    lookup_url_kwarg = "record_id"
    lookup_field="record_id"
    #TODO:user_idの取得方法
    user_id=2
    queryset=Nice.objects.filter(post_by_id=user_id)
    def perform_create(self, serializer):
        record_id = self.kwargs.get(self.lookup_url_kwarg)
        serializer.check_create(data={"post_by_id":self.user_id,"record_id":record_id})
        serializer.save(record_id=record_id,post_by_id=self.user_id)
        
        
    def list(self, request, *args, **kwargs):
        record_id = self.kwargs.get(self.lookup_url_kwarg)
        try:
            mobj=MatchRecords.objects.get(id=record_id)
        except Exception as e:
            return hundle_exception(e)
        count=Nice.objects.filter(record=mobj).count()
        return JsonResponse({"いいね":count},status=status.HTTP_200_OK)
