from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^profile/update/', views.update_profile, name='update_profile'),
    url(r'^new_hood/$',views.new_hood,name='add_neighborhood'),
    url(r'^new_business/$',views.new_business,name='add_business'),
    url(r'^alert/$',views.new_alert,name='new_alert'),
    url(r'^searched/', views.search_business, name='search'),
    url('^join/(?P<id>\d+)$',views.join_hood, name='join_hood'),
    url('^home/$',views.current_hood, name='current_hood'),
    url('^exit/(?P<id>\d+)$',views.exit_hood, name='exit_hood'),
    url(r'^comment/(?P<alert_id>\d+)', views.post_comment, name='comment'),
    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)