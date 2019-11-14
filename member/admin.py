from django.contrib import admin
from .models import University, Profile
# Register your models here.

admin.site.register(University)


class ProfileAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['first_name']}),
    #     ('University', {'fields': ['student_num'], 'classes': ['collapse']}),
    # ]
    # 목록 항목
    list_display = ('university', 'student_num')

    list_filter = ['university']

admin.site.register(Profile, ProfileAdmin)

