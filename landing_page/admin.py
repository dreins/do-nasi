from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Pengguna

class PenggunaAdmin(UserAdmin):
    list_display = ('email', 'username', 'name', 'role', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Pengguna, PenggunaAdmin)