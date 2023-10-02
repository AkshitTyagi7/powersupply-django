from django.contrib import admin

from summary.models import DelhiGeneration, DiscomDrawl, StateDrawl, Summary

# Register your models here.

class SummaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'summary')


class DiscomDrawlAdmin(admin.ModelAdmin):
    list_display = ('id', 'discom', 'schedule', 'drawl', 'OD')

class DelhiGenerationAdmin(admin.ModelAdmin):
    list_display = ('id', 'GENCO', 'schedule', 'actual', 'UI')

class StateDrawlAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'schedule', 'drawl', 'OD')






admin.site.register(Summary, SummaryAdmin)
admin.site.register(DiscomDrawl, DiscomDrawlAdmin)
admin.site.register(DelhiGeneration, DelhiGenerationAdmin)
admin.site.register(StateDrawl, StateDrawlAdmin)
