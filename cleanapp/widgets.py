from django import forms
from django.utils.safestring import mark_safe
from django.forms.widgets import Widget
from django.template import loader


class AdminImageWidget(forms.FileInput):
    """A ImageField Widget for admin that shows a thumbnail."""

    def __init__(self, attrs={}):   # pylint: disable=E1002,W0102
        super(AdminImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):  # pylint: disable=E1002
        output = []
        output.append(super(AdminImageWidget, self).render(name, value))

        return mark_safe(u''.join(output))




class MyWidget(Widget):
    template_name = 'cleanapp/my_widget.html'

    def get_context(self, name, value, attrs=None):
        return {'widget': {
            'name': name,
            'value': value,
        }}

    def render(self, name, value, attrs=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)
