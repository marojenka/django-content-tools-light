from django.db import models
from django.urls import reverse


class Page(models.Model):
    """ Simple container for web page.  """
    title = models.CharField(
        max_length=255, default='')
    h1 = models.CharField(
        max_length=255, default='')
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('page-update', kwargs={'pk': self.pk})
