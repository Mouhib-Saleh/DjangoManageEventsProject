from django.contrib import admin
from.models import *
# Register your models here.

class ParticipationAdmin(admin.TabularInline):
    model=Participation
    extra=1
class DateListFilter(admin.SimpleListFilter):
    title="Event Date"
    parameter_name='evt_date'
    def lookups(self,request,model_admin):
        return(
            ('Past Event',('Past Event')),
            ('Incoming Events',('Incoming Events')),
            ('Today Events',('Today Events'))
            # key value
        )
    def queryset(self, request, queryset):
        if self.value()=='Past Event':
            return queryset.filter(evt_date__lt=datetime.now())
        if self.value()=='Incoming Events':
            return queryset.filter(evt_date__gt=datetime.now())
        if self.value()=='Today Events':
            return queryset.filter(evt_date__exact=datetime.now())
class ParticipantsFilter(admin.SimpleListFilter):
    title="Participants Number"
    parameter_name='nbe_participant'
    def lookups(self,request,model_admin):
        return(
            ('Superieur a 2',('Superieur a 2')),
            ('Superieur a 5',('Superieur a 5')),
            ('Superieur a 10',('Superieur a 10')),
            ('Pas de participants',('Pas de participants'))
        )
    def queryset(self, request, queryset):
        if self.value()=='Superieur a 2':
            return queryset.filter(nbe_participant__gte=2)
        if self.value()=='Superieur a 5':
            return queryset.filter(nbe_participant__gte=5)
        if self.value()=='Superieur a 10':
            return queryset.filter(nbe_participant__gte=10)
        if self.value()=='Pas de participants':
            return queryset.filter(nbe_participant__exact=0)

   

@admin.register(Event) 
class EventAdmin(admin.ModelAdmin):
    list_display=('title','description','nbe_participant','state','evt_date','update_date','organizer','evet_participants')
# admin.site.register(Event,EventAdmin)
    def evet_participants (self,obj):
        return obj.participations.count()
    
    list_per_page=2
    list_filter=('title',DateListFilter,ParticipantsFilter)
    fieldsets=[
        ('A propos', {
        "fields":(
        'title',
        'description',
        'image',
        'state',
        'nbe_participant'
        )
        }),
        ('Date',{
        "fields":(
        "evt_date",
        "creation_date",
        "update_date",
        )
        }),
        ('Personnel',{
        "fields":(
        "organizer",
        )
        })
    ]
    readonly_fields=["creation_date","update_date"]
    inlines=(ParticipationAdmin,)
    autocomplete_fields = ['organizer']

