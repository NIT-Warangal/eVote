from django.contrib import admin
from vote.models import Students, Invigilators, Contestants, Campaigning

# Register your models here.

admin.site.register(Students)
admin.site.register(Invigilators)
admin.site.register(Contestants)
admin.site.register(Campaigning)
