from django.contrib import admin
from core.models import TranslationModel

class TranslationModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    pass

# Register your models here.
admin.site.register(TranslationModel, TranslationModelAdmin)
