from django.contrib import admin

from .models import *
# this is admin file

admin.site.register([Blog,Email,Hvs])
