import os
import pathlib
import random
import sys
from datetime import timedelta

import django
import faker
from django.utils import timezone

# 将项目根目录添加到 Python 的模块搜索路径中
back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogproject.settings")
    django.setup()

    from blog.models import Category, Post, Tag,Comment,Post_tag

    from django.contrib.auth.models import User

    print('clean database')
    Post.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()
    Post_tag.objects.all().delete()
    Comment.objects.all().delete()

    print('create a blog user')

    category_list = ['Python', 'JAVA', 'C++', 'PHP', '笔记']
    tag_list = ['语言', '算法', '狗屁不通', '技术', 'markdown', 'test']
    a_year_ago = timezone.now() - timedelta(days=365)


    print('create categories and tags')

    for cate in category_list:
        Category.objects.create(name=cate)

    for tag in tag_list:
        Tag.objects.create(name=tag)
    
    print('create some faked posts published within the past year')
    fake = faker.Faker('zh_CN')  # English
    for _ in range(100):
        tags = Tag.objects.order_by('?')
        user = User.objects.order_by('?').first()
        tag1 = tags.first()
        tag2 = tags.last()
        cate = Category.objects.order_by('?').first()
        created_time = fake.date_time_between(start_date='-1y', end_date="now",
                                              tzinfo=timezone.get_current_timezone())
        post = Post.objects.create(
            title=fake.sentence().rstrip('.'),
            body='\n\n'.join(fake.paragraphs(10)),
            created_time=created_time,
            category=cate,
            author=user,
        )
        post.save()
    print('Create some tags and comments')

    post_list = Post.objects.all()
    for post in post_list:
        tags = Tag.objects.order_by('?')
        tag1 = tags.first()
        tag2 = tags.last()

        p_t = Post_tag.objects.create(
            post= post,
            tag=tag1,
        )

        p_t.save()

        p_t = Post_tag.objects.create(
            post= post,
            tag=tag2,
        )

        p_t.save()

        users = User.objects.order_by('?')
        user1 =users.first()
        user2 = users.last()

        comment = Comment.objects.create(
            post= post,
            name=user1,
            text=' '.join(fake.paragraphs(1)),
            created_time=fake.date_time_between(start_date='-1y', end_date="now",
                                              tzinfo=timezone.get_current_timezone())
        )

        comment.save()

        comment = Comment.objects.create(
            post= post,
            name=user2,
            text=' '.join(fake.paragraphs(1)),
            created_time=fake.date_time_between(start_date='-1y', end_date="now",
                                              tzinfo=timezone.get_current_timezone())
        )

        comment.save()
