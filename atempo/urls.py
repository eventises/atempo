from django.conf.urls import url
from atempoapp import views

urlpatterns = [
    url(r'^$', views.AtempoViewAll.as_view(), name='msg-list'),
    url(r'new$', views.AtempoNewMsg.as_view(), name='msg-new'),
    url(r'save$', views.AtempoSave.as_view(), name='msg-save'),
    url(
        r'^details/(?P<message_id>\d+)/$',
        views.AtempoDetails.as_view(),
        name='msg-details'
    ),
url(
        r'^remove/(?P<message_id>\d+)/$',
        views.AtempoRemove.as_view(),
        name='msg-remove'
    ),
]