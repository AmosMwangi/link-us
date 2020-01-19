from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('', views.index, name='Index'),
    path('create/profile/',views.profile, name='create-profile'),
    path('update/profile/',views.update_profile, name='update-profile'),
    path('blog/', views.BlogPageView.as_view(), name='blog'),
    path('businesses/', views.BusinessView.as_view(), name='businesses'), 
    path('education/', views.EducationView.as_view(), name='education'), 
    path('activate/user/<int:user_id>', views.user_activate, name='activate_user'),
    path('deactivate/user/<int:user_id>', views.user_deactivate, name='deactivate_user'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    