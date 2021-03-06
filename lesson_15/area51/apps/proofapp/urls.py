from django.conf.urls import url
from apps.proofapp.views import hello
from apps.proofapp.views import root
from apps.proofapp.views import current_time
from apps.proofapp.views import time_ahead, find_form, find

urlpatterns = [
    url(r'^$', root),
    url(r'^hello/$', hello),
    url(r'^time/$', current_time),
    url(r'^time/(\d{1,2})/$', time_ahead),
    url(r'^find-form/$', find_form),
    url(r'^find/$', find),
]

