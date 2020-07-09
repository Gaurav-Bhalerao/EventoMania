from django.contrib import admin
from . models import HomeSlide,Feature,Team
from . models import Gold_Plan, Platinum_Plan
from . models import EventsImage,EventStat
from . models import Contact
# Register your models here.

admin.site.register(HomeSlide)
admin.site.register(Feature)

admin.site.register(Gold_Plan)
admin.site.register(Platinum_Plan)

admin.site.register(Team)

admin.site.register(EventsImage)
admin.site.register(EventStat)

admin.site.register(Contact)
