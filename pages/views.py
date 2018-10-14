import re

from django.views.generic import UpdateView

from .models import Page


# Regexp to strip away one uttermost HTML tag
STRIP_P = re.compile(r'<([\d\w]*)> *(.*)</\1>')


class PageUpdate(UpdateView):
    """
    Hached UpdateView which hadels data from contettools
    and saves it into model instance.
    Allows usage of fields that needs to be cleaned from html tags:
    for those fields html tag wrapper would be removed before form saving.
    Those one might use:
    section(data-editable, data-name='h1')
        h1 {{ object.h1 }}
    and it will be editable in contexttools as h1 element, but stored as
    a text with escaped html tags.

    Ordinary fields are expected to be inserted as safe:
    section(data-editable, data-name='content')
        {{object.content|safe}}
    """
    model = Page
    fields = ['content', 'h1']
    dirty_fields = ['h1']

    def form_valid(self, form):
        for field in self.dirty_fields:
            value = re.sub(STRIP_P, r'\2', form.cleaned_data[field])
            setattr(form.instance, field, value)
        return super().form_valid(form)
