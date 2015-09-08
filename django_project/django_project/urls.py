from django.conf.urls import include, url
from django.contrib import admin

from quiz import urls as quiz_urls
from quiz.views import Profile

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/(?P<pk>[0-9]+)/$', Profile.as_view()),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include(quiz_urls)),
]
