from django.conf.urls import url
from atempoapp import views

urlpatterns = [
    url(r'^$', views.AtempoViewAll.as_view(), name='msg-list'),
]