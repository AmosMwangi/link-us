from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile);
admin.site.register(neighbourhood);
admin.site.register(BlogPost);
admin.site.register(Business);
admin.site.register(Education);
admin.site.register(educationservices);
admin.site.register(Authorities);
admin.site.register(notifications);