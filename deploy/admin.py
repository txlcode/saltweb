# encoding:utf-8
from django.contrib import admin
from deploy.models import SaltGroup,SaltHost,FileUpload,ProjectRollback
# Register your models here.
admin.site.site_header = '成都商报运维管理后台'



class SaltHostAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main', {
            'fields': ('hostname', 'alive'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('alive_time_now',),
        }]
    )
    list_display=('hostname', 'alive','alive_time_last')
    search_fields = ('hostname',)
admin.site.register(SaltHost,SaltHostAdmin)
admin.site.register(FileUpload)
admin.site.register(ProjectRollback)
