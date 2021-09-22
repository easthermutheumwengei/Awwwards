from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    url('^$', views.index, name='index'),
    url('auth/login/', views.login_user, name='login'),
    url('auth/register/', views.register_user, name='register'),
    url('accounts/logout/', views.logout_user, name='logout'),
    url('profile/<int:id>', views.profile, name='profile'),
    url('project/<int:id>', views.project, name='project'),
    url('api/profiles/', views.ProfileList.as_view()),
    url('api/projects/', views.ProjectsList.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)