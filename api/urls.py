from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^books/(?P<pk>[0-9]+)/$', GetView.as_view(), name="details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
