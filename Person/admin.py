from django.contrib import admin

from Person.models import Person

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=('username','cin','mail')
    list_per_page=2
    list_filter=('cin','mail','username')
    search_fields = ['username']
    fieldsets=[
        ('Donneés confidentielles',{
        "fields":(
        'first_name',
        'last_name',
        'mail',
        'cin',
        'username',
        'password'
        )
        }),
        ('Permissions',{
         "fields":(
         'groups',
         'user_permissions',
         'is_staff',
         'is_active',
         'is_superuser',
         ) 
        }),
         ('Dates',{
         "fields":(
         'last_login',
         'date_joined',
         ) 
        }),
    ]


