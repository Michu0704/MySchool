from django.contrib import admin

from my_schools.models import Catalog, Training

#admin.site.register(Catalog)
#admin.site.register(Training)


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'level')


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'catalog', 'limit', 'auditorium', 'date')
