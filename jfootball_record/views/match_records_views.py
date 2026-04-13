from rest_framework import filters, viewsets,status
from rest_framework.response import Response
from jfootball_record.exception.exception_handler import hundle_exception
from jfootball_record.model_definition.match_records_models import MatchRecords
from jfootball_record.serializer.match_records_serializer import MatchRecordsSerializer
from rest_framework.pagination import PageNumberPagination
import django_filters

from django_filters.rest_framework import DjangoFilterBackend

class MyPagination(PageNumberPagination):
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 100
    }
    page_size = 5
    def get_paginated_response(self, data):
        return Response({
            'current' :self.page.number,              # 現在のページ
            'count': self.page.paginator.count,       # 項目数の合計
            'final': self. page.paginator.num_pages,  # 全体のページ数
            'next': self.get_next_link(),             # 次のページネーションへのリンク
            'previous': self.get_previous_link(),  # 前のページネーションへのリンク
            'results': data,                       # 結果データ　（page_size個のデータ）
        })

class MatchRecordsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = MatchRecords
        fields = ["title"]
    
# Create your views here.
class MatchRecordsViewSet(viewsets.ModelViewSet):
    serializer_class = MatchRecordsSerializer
    queryset = MatchRecords.objects.all()
    #TODO:user_idの取得方法
    user_id=2
    #pagenation設定
    pagination_class = MyPagination
    #filtering設定
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_class = MatchRecordsFilter
    ordering_fields = ['round']
    def perform_create(self, serializer):
        serializer.save(created_by_id=self.user_id)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception as e:
            return hundle_exception(e)
        created_by_id=instance.__getattribute__("created_by_id")
        if created_by_id==self.user_id:
            self.perform_destroy(instance)
        else:
            return Response("権限がありません",status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        
        try:
            instance = self.get_object()
        except Exception as e:
            return hundle_exception(e)
        created_by_id=instance.__getattribute__("created_by_id")
        
        if created_by_id==self.user_id:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
        else:
            return Response("権限がありません",status=status.HTTP_403_FORBIDDEN)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    #後ほどhome_team_idとaway_team_idからチーム名を取得するため,listメソッドを定義
    def list(self, request, *args, **kwargs):
        return super().list(self,request, *args, **kwargs)
                #TODO superで継承元のlistメソッド呼び出し後の取得結果を加工
