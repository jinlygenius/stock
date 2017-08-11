from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^records/$',
        views.RecordListCreateView.as_view(),
        name="record_list_create_view"),

    url(r'^records/(?P<pk>\d+)/$',
        views.RecordRetrieveDestroyView.as_view(),
        name="record_detail_view"),
]
