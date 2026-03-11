from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from jfootball_record.model_definition.nice_models import Nice
from jfootball_record.model_definition.match_records_models import MatchRecords
from jfootball_record.serializer.nice_serializer import NiceSerializer
from rest_framework import viewsets
from rest_framework import mixins
# Create your views here.
class NiceView(mixins.CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = NiceSerializer
    queryset = Nice.objects.all()
    def perform_create(self, serializer):
        serializer.save(record_id=1,post_by_id=1)
