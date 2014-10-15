from django.contrib import admin
from mezzanine.core.admin import  TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from .models import HomePage, Slide, Portfolio


class AdminSlide(TabularDynamicInlineAdmin):
    model = Slide
    
class AdminHomePage(PageAdmin):
    inlines = [AdminSlide,]

admin.site.register(HomePage, AdminHomePage)
admin.site.register(Portfolio, PageAdmin)

