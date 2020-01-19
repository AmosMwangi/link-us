from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('', views.index, name='Index'),
    path('my-profile/',views.my_profile, name='my-profile'),
    url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    path('create/profile/',views.create_profile, name='create-profile'),
    path('update/profile/',views.update_profile, name='update-profile'),
    path('blog/', views.BlogPageView.as_view(), name='blog'),
    path('new/blogpost/',views.new_blogpost, name='new-blogpost'),
    path('businesses/', views.BusinessView.as_view(), name='businesses'),
    path('new/business/',views.new_business, name='new-business'), 
    path('education/', views.EducationView.as_view(), name='education'),
    path('new/education/',views.new_education, name='new-education'),
    path('authorities/', views.AuthorityView.as_view(), name='authorities'),
    path('new/authorities/',views.new_authority, name='new-authorities'),
    path('search/',views.search_results, name='search_results'), 
    path('dashboard', views.user_dashboard, name='user_dashboard'),
    path('register/', views.SignUp.as_view(), name='register'),
    path('users', views.registered_users, name='system_users'),
    path('activate/user/<int:user_id>', views.user_activate, name='activate_user'),
    path('deactivate/user/<int:user_id>', views.user_deactivate, name='deactivate_user'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    