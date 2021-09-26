from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/login/', views.login_user, name='login'),
    path('auth/register/', views.register_user, name='register'),
    path('accounts/logout/', views.logout_user, name='logout'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('project/<int:id>/', views.project, name='project'),
    path('api/profiles/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectsList.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)