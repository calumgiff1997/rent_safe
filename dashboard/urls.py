from django.conf.urls import url
from dashboard import views
urlpatterns = [
    #temporary url for testing templates
    url(r'^test', views.templateTest, name='templateTest'),
]
