from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('admin/', admin.site.urls),
    path('',include('hood.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

]
