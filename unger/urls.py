from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    # Example:
    # (r'^web/', include('web.foo.urls')),
    url(r'expenses/(?P<year>\d{4})/(?P<month>\d{1,2})/$', expenses, name="month_expenses"),
    url(r'expenses/$', expenses, name = "expenses"),
    url(r'login/$', user_login, name = "login"),
    url(r'logout/$', logout_user, name = "logout"),
    url(r'targets/$', spending_target, name = "spending_target"),
    url(r'profile/$', edit_profile, name = 'profile'),
)
