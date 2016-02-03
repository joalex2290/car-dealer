from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()
import apps.manager.urls
import apps.inventory.urls
import apps.sales.urls
from views import Home

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}, name='login'),
    url(r'^change-password/$','django.contrib.auth.views.password_change', 
    	{
    	'template_name': 'change-password.html',
        },
        name='change-password'),
    url(r'change-password-done/$','django.contrib.auth.views.password_change_done',
    	{
    	'template_name': 'login.html',
        },
        name='password_change_done'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^home/$', login_required(Home.as_view()),name='home'),

    url(r'^manager/', include(apps.manager.urls)),

    url(r'^inventory/', include(apps.inventory.urls)),

    url(r'^sales/', include(apps.sales.urls)),
)