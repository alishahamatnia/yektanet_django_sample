from django.contrib import admin
from .models import Ad, Advertiser, BaseAdvertising, Click, Seen
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class AdvertisingAdAdmin(UserAdmin):
    list_display = ('ad_owner', 'title', 'link', 'img_url', 'is_approved')
    search_fields = ('title',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ('is_approved',)
    fieldsets = ()
    ordering = ('id', 'title')


admin.site.register(Ad, AdvertisingAdAdmin)
admin.site.register(Advertiser)
admin.site.register(BaseAdvertising)
admin.site.register(Click)
admin.site.register(Seen)
