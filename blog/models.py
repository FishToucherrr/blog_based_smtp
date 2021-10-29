from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from django.utils.html import strip_tags


class Category(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)


class Friends(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    email= models.CharField(max_length=100)



class Email(models.Model):


    def __str__(self):
        return self.title

    # 标题
    title = models.CharField(max_length=70)

    # TextField。
    body = models.TextField()

    # DateTimeField 类型。
    created_time = models.DateTimeField('创建时间',default=timezone.now)
    modified_time = models.DateTimeField()


    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:edit', kwargs={'pk': self.pk})
