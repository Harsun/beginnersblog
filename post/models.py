from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    pubdate = models.DateTimeField(auto_now_add=True, verbose_name='publishing date')
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

