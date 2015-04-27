# forms.py
from django.forms import ModelForm
from django import forms

from badge_site.models import Issuer, Badge, Award, Revocation

class CreateIssuerForm(ModelForm):
    class Meta:
        model = Issuer
        fields = ['name', 'initials', 'url', 'doc_path', 'desc', 'image', 'contact']


class CreateBadgeForm(ModelForm):
    class Meta:
        model = Badge
        fields = ['name', 'image', 'description', 'criteria', 'issuer', 'notify_email_subject']


class CreateAwardForm(ModelForm):
    class Meta:
        model = Award
        fields = ['email', 'firstname', 'lastname', 'badge', 'creator', 'evidence', 'expires']
        widgets = {'expires': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'datepicker'})}
        help_texts = {'expires': 'Eg: 2015-01-01 for January 1, 2015'}


class RevokeAwardForm(ModelForm):
    class Meta:
        model = Revocation
        fields = ['issuer', 'award', 'reason']
        readonly_fields = ['award']
        # labels = ['award': '']


class UnRevokeAwardForm(ModelForm):
    class Meta:
        model = Revocation
        fields = ['issuer', 'award', 'reason']
        readonly_fields = ['award']



class ClaimCodeSubmitForm(forms.Form):
    claim_code = forms.CharField(label='Your claim code?', max_length=100)
