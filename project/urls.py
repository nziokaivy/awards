from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),   
    url(r'^profile', views.profile, name = 'profile'),
    url(r'^project(\d+)', views.project, name='project'),
    url(r'^newproject$', views.new_project, name='new_project'),    
    url(r'^search/', views.search_projects, name='search_projects'),
    url(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    
 

]    
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
