from django.contrib import admin
from payments_app.models import pay_method

# Register your models here.
class pay_method_admin(admin.ModelAdmin):
    list_display = ('id', 'pay_id', 'pay_option', 'min_pay')
admin.site.register(pay_method, pay_method_admin)
