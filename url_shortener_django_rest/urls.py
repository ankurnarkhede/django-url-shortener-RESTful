from django.urls import re_path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from shorten import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.url_list.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
