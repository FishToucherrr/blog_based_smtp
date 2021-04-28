from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

import markdown
from django.utils.html import strip_tags


class Category(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)


class Tag(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)




class Post(models.Model):


    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        if not self.excerpt:
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 标题
    title = models.CharField(max_length=70)

    # TextField。
    body = models.TextField()

    # DateTimeField 类型。
    created_time = models.DateTimeField('创建时间',default=timezone.now)
    modified_time = models.DateTimeField()

    # 文章摘要
    # 指定 CharField 的 blank=True 参数值后可以允许空值。
    excerpt = models.CharField(max_length=200, blank=True)


    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # 文章作者 User 从 django.contrib.auth.models 导入

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0, editable=False)
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
class Post_tag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('blog.Post', verbose_name='文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])