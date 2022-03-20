from django.db import models
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL

MODULES = (
    (1844, 'Forecast'),
    (1418, 'Workorder')
)


class AMOSModule(models.Model):
    apn = models.IntegerField()
    name = models.CharField(max_length=155)

    def __str__(self):
        return f"{self.name} (APN{self.apn})"


def case_directory_path(instance, filename):
    try:
        id = instance.case.id
    except:
        id = instance.id
    # file will be uploaded to MEDIA_ROOT/user_<id>/documents/
    return f'case_{id}/documents/{filename}'

class Case(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # module = models.IntegerField(choices=MODULES)
    module = models.ForeignKey(AMOSModule, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to=case_directory_path, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_docfile = self.docfile
            self.docfile = None
            super(Case, self).save(*args, **kwargs)
            self.docfile = saved_docfile

        super(Case, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cases:detail', args=[str(self.id)])

    def timestamp(self):
        return self.created.strftime("%Y-%m-%d %H:%M:%S")



class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='comments')
    docfile = models.FileField(upload_to=case_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:30]

    def timestamp(self):
        return self.created.strftime("%Y-%m-%d %H:%M:%S")


