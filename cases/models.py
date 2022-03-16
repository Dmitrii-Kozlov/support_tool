from django.db import models
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL

MODULES = (
    (1844, 'Forecast'),
    (1418, 'Workorder')
)


class Case(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    module = models.IntegerField(choices=MODULES)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cases:detail', args=[str(self.id)])


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:30]


