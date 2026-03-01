from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from jfootball_record.model_definition.nice_models import Nice
from jfootball_record.model_definition.match_records_models import MatchRecords
from jfootball_record.serializer.nice_serializer import NiceSerializer
# Create your views here.
class NiceView(generics.UpdateAPIView):
    serializer_class = NiceSerializer
    
    def update(self, request, *args, **kwargs):
        match_records_id = self.kwargs['match_records_id']
        user_id = 1
        get_object_or_404(MatchRecords,id=match_records_id)
        partial = kwargs.pop('partial', False)
        request_data={"record":match_records_id,"post_by":user_id}
        serializer = self.get_serializer(data=request_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        return self.perform_update(serializer,match_records_id,user_id)
    
    def get_object(self,match_records_id,user_id):
        exist=Nice.objects.filter(record_id=match_records_id,post_by=user_id).exists()
        return exist
    
    def perform_update(self, serializer,match_records_id,user_id):
        if self.get_object(match_records_id,user_id):
            #すでに対戦記録に「いいね」がある場合は削除
            Nice.objects.filter(record_id=match_records_id,post_by=user_id).delete()
            return Response("いいね削除")
        else:
            #対戦記録に「いいね」がない場合は新規登録
            serializer.save()
            return Response("いいね登録")
