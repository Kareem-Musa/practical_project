from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class State(models.Model):
    name = models.CharField(verbose_name='الولاية', max_length=50)
    slug = models.SlugField(blank=True, null=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('locations:state_list')


class Locality(models.Model):
    name = models.CharField(verbose_name='المحلية', max_length=50)
    state = models.ForeignKey(
        State, verbose_name='الولاية', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('locations:locality_list')
