from django import template
from django.db.models.aggregates import Count

from ..models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('blog/inclusions/_most_viewed.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'most_viewed_list': Post.objects.all().order_by('-views')[:num],
    }

@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }

@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'category_list': category_list,
    }

@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    tag_list = Tag.objects.all()
    return {
        'tag_list': tag_list,
    }