
import os, random, string, json

from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from .utils import hashEmailAddress, genGuid


def getRandomString(size=12, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))





class Issuer(models.Model):
    # Issuing organization (e.g. CLT, NFLRC, etc.)
    guid = models.CharField(
        max_length=24, unique=True, blank=True, help_text="This is auto generated and cannot be edited.")
    name = models.CharField(max_length=128)
    initials = models.CharField(max_length=32)
    url = models.CharField(max_length=128)
    doc_path = models.CharField(max_length=512)
    desc = models.CharField(max_length=512)
    image = models.CharField(max_length=128)
    contact = models.CharField(max_length=128)
    jsonfile = models.URLField(max_length=1024, blank=True)

    def getJsonFilename(self):
        return 'issuer-assert-' + self.guid + '.json'

    def getIssuerUrl(self):
        return os.path.join(self.url, settings.ISSUER_REPO, self.getJsonFilename())

    def getIssuerPath(self):
        return os.path.join(self.doc_path, settings.ISSUER_REPO, self.getJsonFilename())

    def writeIssuerFile(self):
        data = json.dumps(self.serialize())
        f = open(self.getIssuerPath(), 'w')
        localFile = File(f)
        localFile.write(data)
        localFile.closed
        f.closed

    def deleteIssuerFile(self):
        # Remove the file from the filesystem.
        f = open(self.getIssuerPath(), 'w')
        localFile = File(f)
        if os.path.isfile(localFile.name):
            os.remove(localFile.name)

    def serialize(self, request=None):
        """Produce an Open Badge Infrastructure serialization of this Issuer"""
        data = {
            "name": self.name,
            "url": self.url,
            "image": self.image,
            "email": self.contact
        }
        return data

    def save(self, *args, **kwargs):
        if not self.guid:
            self.guid = genGuid()
        if not self.jsonfile:
            self.jsonfile = self.getIssuerUrl()

        super(Issuer, self).save(*args, **kwargs) # Call the "real" save()
        self.writeIssuerFile()

    def __unicode__(self):
        return self.name


class Badge(models.Model):
    guid = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=1024)
    image = models.URLField()
    description = models.CharField(max_length=128)
    criteria = models.URLField()
    issuer = models.ForeignKey(Issuer, related_name='badges')
    created = models.DateField(auto_now=True, blank=False)
    jsonfile = models.URLField(max_length=1024, blank=True)
    notify_email_message = models.TextField(blank=True, default='')
    notify_email_subject = models.CharField(max_length=256, blank=True, default='')


    def getJsonFilename(self):
        return 'badge-assert-' + self.guid + '.json'

    def getBadgeUrl(self):
        return os.path.join(self.issuer.url, settings.BADGES_REPO, self.getJsonFilename())

    def getBadgePath(self):
        return os.path.join(self.issuer.doc_path, settings.BADGES_REPO, self.getJsonFilename())

    def writeBadgeFile(self):
        data = json.dumps(self.serialize())
        f = open(self.getBadgePath(), 'w')
        localFile = File(f)
        localFile.write(data)
        localFile.closed
        f.closed

    def deleteBadgeFile(self):
        # Remove the file from the filesystem.
        f = open(self.getBadgePath(), 'w')
        localFile = File(f)
        if os.path.isfile(localFile.name):
            os.remove(localFile.name)

    def serialize(self, request=None):
        """Produce an Open Badge Infrastructure serialization of this Badge"""
        data = {
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "criteria": self.criteria,
            "issuer": self.issuer.getIssuerUrl()
        }
        return data

    def save(self, *args, **kwargs):
        if not self.guid:
            self.guid = genGuid()
        if not self.jsonfile:
            self.jsonfile = self.getBadgeUrl()
        super(Badge, self).save(*args, **kwargs) # Call the "real" save()
        self.writeBadgeFile()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-created']

class Award(models.Model):

    """
    Stores a record of an awarded badge, related to :model:`badge.Badge`

    """
    guid = models.CharField(
        max_length=24, unique=True, help_text="This is auto generated.")
    email = models.CharField(max_length=1024,
                             help_text="Email for the recipient (use the email the user intends to use with their Mozilla Backpack account).")
    firstname = models.CharField(max_length=1024)
    lastname = models.CharField(max_length=1024)
    badge = models.ForeignKey(Badge, related_name='awards')
    creator = models.ForeignKey(
        User, related_name="award_creator", blank=True, null=True,
        help_text="Specify yourself.")
    issuedOn = models.DateTimeField(auto_now_add=True, blank=False)
    evidence = models.URLField(max_length=1024,
                               help_text="URL that points to a resource that provides evidence for this award.")
    modified = models.DateTimeField(auto_now=True, blank=False)
    claimCode = models.CharField(max_length=10, blank=True,
                                 help_text="This is auto generated. Send this to recipient so they may claim their badge.")
    salt = models.CharField(
        max_length=10, blank=True, help_text="This is auto generated.")
    jsonfile = models.URLField(max_length=1024, blank=True,
                               help_text="This is auto generated but is fully qualified url for the award assertion.")
    expires  = models.DateField(null=True, blank=True)
    notification_status = models.DateField(null=True, default=None)

    class Meta:
        unique_together = ('email', 'badge')

    def getJsonFilename(self):
        return 'award-assert-' + self.guid + '.json'

    def getAssertionUrl(self):
        return os.path.join(self.badge.issuer.url, settings.AWARDS_REPO, self.getJsonFilename())

    def getAssertionPath(self):
        return os.path.join(self.badge.issuer.doc_path, settings.AWARDS_REPO, self.getJsonFilename())

    def getClaimUrl(self):
        return settings.SITE_HOST + str(reverse_lazy('claim_badge_with_code', args=[self.claimCode]))

    def writeAssertionFile(self):
        data = json.dumps(self.serialize())
        f = open(self.getAssertionPath(), 'w')
        localFile = File(f)
        localFile.write(data)
        localFile.closed
        f.closed

    def deleteAssertionFile(self):
        # Remove the file from the filesystem.
        f = open(self.getAssertionPath(), 'w')
        localFile = File(f)
        if os.path.isfile(localFile.name):
            os.remove(localFile.name)

    def serialize(self, request=None):
        hashed = hashEmailAddress(self.email, self.salt)
        expiredate = ''
        try:
            expiredate = self.expires.strftime('%Y-%m-%d')
        except:
            expiredate = None

        identityObj = {
            "type": "email",
            "identity": hashed,
            "hashed": True,
            "salt": self.salt,
        }
        verifyObj = {
            "type": "hosted",
            "url": self.getAssertionUrl(),
        }
        assertion = {
            "uid": self.guid,
            "recipient": identityObj,
            "evidence": self.evidence,
            "issuedOn": self.issuedOn.strftime('%Y-%m-%d'),
            "badge": self.badge.getBadgeUrl(),
            "verify": verifyObj,
            "expires": expiredate,
        }
        return assertion

    def save(self, *args, **kwargs):
        if not self.guid:
            self.guid = genGuid()

        if not self.jsonfile:
            self.jsonfile = self.getAssertionUrl()
            self.claimCode = getRandomString(10)
            self.salt = getRandomString(10)
        super(Award, self).save(*args, **kwargs) # Call the "real" save()
        self.writeAssertionFile()

    def __unicode__(self):
        return self.email

class Revocation(models.Model):
    issuer = models.ForeignKey(Issuer, related_name='revoked_ist')
    award = models.ForeignKey(Award)
    reason = models.CharField(max_length=512, null=False)
    revoke_date = models.DateField(auto_now=True, blank=False)
    jsonfile = models.URLField(max_length=1024, blank=True,
                               help_text="This is auto generated but is fully qualified url for the revocation list.")

    class Meta:
        unique_together = ('issuer', 'award')

    def getJsonFilename(self):
        return 'revoked-award-' + self.award.guid + '.json'

    def getAssertionUrl(self):
        return os.path.join(self.issuer.url, settings.REVOKE_REPO, self.getJsonFilename())

    def getAssertionPath(self):
        return os.path.join(self.issuer.doc_path, settings.REVOKE_REPO, self.getJsonFilename())

    def writeAssertionFile(self):
        self.deleteAssertionFile()
        data = json.dumps(self.serialize())
        f = open(self.getAssertionPath(), 'w')
        localFile = File(f)
        localFile.write(data)
        localFile.closed
        f.closed

    def deleteAssertionFile(self):
        # Remove the file from the filesystem.
        try:
            f = open(self.getAssertionPath(), 'w')
            localFile = File(f)
            if os.path.isfile(localFile.name):
                os.remove(localFile.name)
            f.closed
        except:
            pass

    def serialize(self, request=None):
        """
            Serializes the entire table
            {
              "qp8g1s": "Issued in error",
              "2i9016k": "Issued in error",
              "1av09le": "Honor code violation"
            }
        """
        revocation_list = {}
        for i in Revocation.objects.all().order_by('issuer'):
            revocation_list[i.award.guid] = i.reason

        return revocation_list

    def save(self, *args, **kwargs):
        super(Revocation, self).save(*args, **kwargs) # Call the "real" save()

        if not self.jsonfile:
            self.jsonfile = self.getAssertionUrl()
            self.save()

        self.writeAssertionFile()


    def __unicode__(self):
        return '%s %s %s %s' % (self.issuer, self.award.badge, self.award, self.revoke_date)

