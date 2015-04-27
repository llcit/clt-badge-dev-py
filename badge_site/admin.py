from django.contrib import admin

from .models import Issuer, Badge, Award, Revocation
from .utils import genGuid, getRandomString


class IssuerAdmin(admin.ModelAdmin):
    list_display = ('initials', 'name', 'contact', 'jsonfile', 'jsonfile_name')
    list_filter = ['initials']
    readonly_fields = ('guid', 'jsonfile')

    # Override: Save the object, then over/write json file.
    def save_model(self, request, obj, form, change):
        if not change:
            # Set a one-time unique id
            obj.guid = genGuid()
            # Set url to the json file on intialization (first save)
            obj.jsonfile = obj.getIssuerUrl()

        obj.save()
        obj.writeIssuerFile()


class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'created', 'image', 'jsonfile', 'jsonfile_name', 'guid',)
    list_filter = ['issuer', ]
    readonly_fields = ('guid', 'jsonfile')

    # Override: Save the object, then over/write json file.
    def save_model(self, request, obj, form, change):
        if not change:
            # Set a one-time unique id
            obj.guid = genGuid()
            # Set url to the json file on intialization (first save)
            obj.jsonfile = obj.getBadgeUrl()

        obj.save()
        obj.writeBadgeFile()


class AwardAdmin(admin.ModelAdmin):
    list_display = ('email', 'lastname', 'firstname', 'guid',
                    'badge', 'issuedOn', 'claimCode', 'jsonfile', 'jsonfile_name')
    list_filter = ['email', 'badge', 'badge__issuer']
    readonly_fields = ('guid', 'salt', 'claimCode', 'jsonfile')
    save_as = True

    # Override: Save the object, then over/write json file.
    def save_model(self, request, obj, form, change):
        if not change:
            # Set a one-time unique id, claimCode, and salt for this badge to
            # random strings
            obj.guid = genGuid()
            obj.claimCode = getRandomString(size=10)
            obj.salt = getRandomString(size=10)
            obj.jsonfile = obj.getAssertionUrl()

        # Save the object, then over/write json file.
        obj.save()
        obj.writeAssertionFile()

    def delete_model(self, request, obj):
        obj.deleteAssertionFile()
        obj.delete()

admin.site.register(Issuer, IssuerAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Revocation)
