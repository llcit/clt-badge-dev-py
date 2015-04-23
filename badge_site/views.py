# badge_site/views.py
import datetime

from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from braces.views import StaffuserRequiredMixin

from .models import Award, Issuer, Badge, Revocation
from .forms import CreateIssuerForm, CreateBadgeForm, CreateAwardForm, ClaimCodeSubmitForm, RevokeAwardForm
from .mixins import ClassNameMixin

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['issuer_list'] = Issuer.objects.all()
        context['badge_list'] = Badge.objects.all().order_by('created')
        return context

class IndexView(StaffuserRequiredMixin, TemplateView):
    template_name = 'badge_index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['issuer_list'] = Issuer.objects.all()
        context['badge_list'] = Badge.objects.all().order_by('created')
        return context


class BadgeClaimView(FormView):
    template_name = 'badge_claim_view.html'
    form_class = ClaimCodeSubmitForm

    def get_success_url(self):
        return reverse('claim_badge_with_code', args=[self.claim_code])

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.claim_code = form.cleaned_data['claim_code'].strip()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(BadgeClaimView, self).get_context_data(**kwargs)
        return context


class BadgeClaimCodeView(TemplateView):
    template_name = 'badge_claim_view.html'

    def get_context_data(self, **kwargs):
        context = super(BadgeClaimCodeView, self).get_context_data(**kwargs)
        code = self.kwargs['claim_code']
        try:
            context['award'] = Award.objects.get(claimCode=code)
        except:
            context['bad_code'] = 'Code was not found. Try again'
        return context


class SendAwardNotificationView(StaffuserRequiredMixin, DetailView):
    model = Award
    template_name = 'badge_email_confirm.html'

    def get_context_data(self, **kwargs):
        context = super(
            SendAwardNotificationView, self).get_context_data(**kwargs)

        award = self.get_object()
        claim_url = award.getClaimUrl()
        subject = award.badge.notify_email_subject
        text_message = 'Hi %s, You have been awarded the -- %s -- badge by the %s. Please visit \r\r %s \r\r to claim your badge!' % (
            award.firstname, award.badge.name, award.badge.issuer.name, claim_url)

        html_message = '<p>Hi %s,</p> <p>You have been awarded the <strong>%s</strong> badge by the %s. Please visit the following link to claim your badge!</p><p><a href="%s">%s</a></p>' % (award.firstname, award.badge.name, award.badge.issuer.name, claim_url, claim_url)

        text_message += '\r\rSincerely, \rThe %s' % award.badge.issuer.name
        html_message += '<p>Sincerely,</p> <p>The %s</p>' % award.badge.issuer.name

        sender = '(CLT Technology Office) llcit@hawaii.edu'
        recipient = award.email

        try:
            msg = EmailMultiAlternatives(
                subject, text_message, sender, [recipient])
            msg.attach_alternative(html_message, "text/html")
            msg.send()
            award.notification_status = datetime.datetime.now()
            award.save()
        except:
            pass

        context['award'] = award
        return context


class IssuerListView(StaffuserRequiredMixin, ListView):
    model = Issuer
    template_name = 'badge_list_view.html'


class IssuerCreateView(StaffuserRequiredMixin, CreateView):
    model = Issuer
    template_name = 'issuer_create_view.html'
    form_class = CreateIssuerForm
    success_url = reverse_lazy('badge_home')

    def get_context_data(self, **kwargs):
        context = super(IssuerCreateView, self).get_context_data(**kwargs)
        context['current_objects'] = Issuer.objects.all()
        return context

class IssuerUpdateView(StaffuserRequiredMixin, ClassNameMixin, UpdateView):
    model = Issuer
    template_name = 'badge_update_view.html'
    success_url = reverse_lazy('badge_home')
    class_name = 'Issuer'
    fields = ['name', 'initials', 'url',
              'doc_path', 'desc', 'image', 'contact']


class BadgeListView(StaffuserRequiredMixin, ClassNameMixin, ListView):
    model = Badge
    template_name = 'badge_list_view.html'
    class_name = 'Badge'


class BadgeCreateView(StaffuserRequiredMixin, ClassNameMixin, CreateView):
    model = Badge
    template_name = 'badge_create_badge_view.html'
    form_class = CreateBadgeForm
    class_name = 'Badge'
    badge_issuer = None

    def get_success_url(self):
        return reverse_lazy('create_badge_by_issuer', args=[self.badge_issuer.id])

    def get_initial(self):
        self.badge_issuer = get_object_or_404(Issuer, pk=self.kwargs['issuer'])
        initial = self.initial.copy()
        initial['issuer'] = self.badge_issuer
        initial['creator'] = self.request.user
        return initial

    def get_context_data(self, **kwargs):
        context = super(BadgeCreateView, self).get_context_data(**kwargs)
        context['current_objects'] = Badge.objects.filter(
            issuer=self.badge_issuer)
        context['parent_object'] = self.badge_issuer
        return context


class BadgeUpdateView(StaffuserRequiredMixin, ClassNameMixin, UpdateView):
    model = Badge
    template_name = 'badge_update_view.html'
    class_name = 'Badge'
    fields = ['name', 'image', 'description', 'criteria',
              'issuer']

    def get_success_url(self):
        return reverse_lazy('create_badge_by_issuer', args=[self.get_object().issuer.id])


class AwardListView(StaffuserRequiredMixin, ClassNameMixin, ListView):
    model = Award
    template_name = 'badge_list_view.html'
    class_name = 'Award'

    def get_queryset(self):
        try:
            badge_id = self.kwargs['pk']
            self.queryset = Award.objects.filter(badge__id=badge_id)
        except:
            pass

        return super(AwardListView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super(AwardListView, self).get_context_data(**kwargs)
        try:
            context['obj_filter'] = Badge.objects.get(pk=self.kwargs['pk'])
        except:
            pass
        return context


class AwardCreateView(StaffuserRequiredMixin, ClassNameMixin, CreateView):
    model = Award
    template_name = 'badge_create_award_view.html'
    form_class = CreateAwardForm
    class_name = 'Award'
    badge_to_award = None

    def get_success_url(self):
        return reverse_lazy('create_award_by_badge', args=[self.badge_to_award.id])

    def get_initial(self):
        self.badge_to_award = get_object_or_404(Badge, pk=self.kwargs['badge'])
        initial = self.initial.copy()
        initial['badge'] = self.badge_to_award
        initial['creator'] = self.request.user
        return initial

    def get_context_data(self, **kwargs):
        context = super(AwardCreateView, self).get_context_data(**kwargs)
        context['current_objects'] = Award.objects.filter(
            badge=self.badge_to_award)
        context['parent_object'] = self.badge_to_award
        return context


class AwardUpdateView(StaffuserRequiredMixin, ClassNameMixin, UpdateView):
    model = Award
    template_name = 'badge_update_view.html'
    class_name = 'Award'
    fields = ['email', 'firstname', 'lastname',
              'badge', 'creator', 'evidence', 'expires']

    def get_success_url(self):
        return reverse_lazy('create_award_by_badge', args=[self.get_object().badge.id])


class RevokeAwardView(StaffuserRequiredMixin, ClassNameMixin, CreateView):
    model = Revocation
    template_name = 'badge_revoke_award_view.html'
    award_to_revoke = None
    form_class = RevokeAwardForm
    class_name = 'Revocation'

    def get_success_url(self):
        return reverse_lazy('revoke_award', args=[self.award_to_revoke.id])

    def get_initial(self):
        self.award_to_revoke = get_object_or_404(
            Award, pk=self.kwargs['award_to_revoke'])
        initial = self.initial.copy()
        initial['issuer'] = self.award_to_revoke.badge.issuer
        initial['award'] = self.award_to_revoke

        return initial

    def get_context_data(self, **kwargs):
        context = super(RevokeAwardView, self).get_context_data(**kwargs)
        context['form'].fields[
            'award'].label = '%s -- %s' % (self.award_to_revoke.badge, self.award_to_revoke)
        context['current_objects'] = Revocation.objects.all().order_by(
            'issuer')
        context['parent_object'] = 'Revocation'
        return context
