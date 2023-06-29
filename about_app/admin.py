from django.contrib import admin
from .models import About, library, Experience, Education, Contact_me, Recieve_massage

# Register your models here.

admin.site.register(About)
admin.site.register(library)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Contact_me)
admin.site.register(Recieve_massage)
