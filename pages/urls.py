from django.conf.urls import url

from .views import PageUpdate


urlpatterns = [
    url(r'^(?P<pk>[-\d]+)/$', PageUpdate.as_view(), name='page-update'),
]
