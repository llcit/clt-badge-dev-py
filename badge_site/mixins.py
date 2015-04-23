# mixins.py

from django.core.exceptions import ImproperlyConfigured


class ClassNameMixin(object):

    def get_context_data(self, **kwargs):
        context = super(ClassNameMixin, self).get_context_data(**kwargs)
        try:
            context['object_type'] = self.class_name
        except AttributeError:
            raise ImproperlyConfigured(
                'Please set class_name to appropriate string.')

        return context
