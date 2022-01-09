from django.contrib import admin
from .models import Ubezpieczenie
#from .models import Ubezpieczenie, DodatkoweInfo, Ocena, Obiekt_ubezpieczony
#admin.site.register(Ubezpieczenie)

@admin.register(Ubezpieczenie)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = ["opis"]
    list_display = ["tytul", "opis", "znizka"]
    list_filter = ("premiera", "znizka")
    search_fields = ("tytul", "opis")
'''
admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Obiekt_ubezpieczony)
'''