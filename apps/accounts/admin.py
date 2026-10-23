from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Добавляем поле role в форму редактирования
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('role', 'phone')}),
    )
    # Добавляем поле role в форму создания (Add User)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {'fields': ('role', 'phone')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.site_header = "Панель управления Электронным дневником"