from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    autocomplete_fields = ["country"]


admin.site.register(Company, CompanyAdmin)
