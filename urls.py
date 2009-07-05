from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    # Example:
    # (r'^web/', include('web.foo.urls')),
    url(r'expenses/(?P<year>\d{4})/(?P<month>\d{1,2})/$', home),
    url(r'expenses/$', home, name = "home"),
    url(r'login/$', user_login, name = "login"),
    url(r'logout/$', logout_user, name = "logout"),
    url(r'targets/$', spending_target, name = "spending_target"),
)
