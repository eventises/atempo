from django.conf.urls import url
from atempoapp import views

urlpatterns = [
    url(r'^$', views.AtempoViewAll.as_view(), name='msg-list'),
    url(r'new$', views.AtempoNewMsg.as_view(), name='msg-new'),
    url(r'save$', views.AtempoSave.as_view(), name='msg-save'),
]