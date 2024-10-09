from django.contrib import admin
from .models import reviewer

# Register your models here.
class reviewer_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'email', 'password', 'confirm_password', 'review', 'age', 'cgpa', 'youtube')
admin.site.register(reviewer, reviewer_admin)