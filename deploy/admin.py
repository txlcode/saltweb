from django.contrib import admin
from deploy.models import SaltGroup,SaltHost
# Register your models here.
admin.site.register([SaltHost,SaltGroup])
