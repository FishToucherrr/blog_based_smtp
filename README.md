# blog_test

## 要求

信息管理系统

https://fduxuan.github.io/IntroDB-Spring-2021/

## 实现

### Django + Bootstrap

## 相关信息

### 概要

post + 用户注册 + 登录 + 注销 + 评论 + 分类 + 归档 + 标签 + 搜索 + 统计阅读量

上方搜索栏可以搜索文章中的关键字

主页按发布时间将文章排序 同时有分页功能

左侧第一栏显示 近期阅读量最高的文章

归档 将 文章按年月归档

分类右侧数字为分类下文章数量

标签与分类类似

用户个人主页显示个人信息和自己发布的文章

每个用户都可以删除或者修改自己发布的文章 

每个用户都可以在文章下发布评论

发布文章时若未填写摘要，则自动生成摘要

文章正文支持md格式 同时在左侧生成大纲

### 数据库：

python 自带的 SQLite3

### 模型设计：

符合BCNF，详见文件   **\blog\models.py**

#### User

1. id
2. username
3. email
4. password
5. is_staff                   是否为工作人员
6. is_superuser          是否为admin

#### Category

文章分类

每个文章只属于一个分类，一个分类可以有多个文章

1. id
2. name

#### Tag

文章标签

每个文章可以有多个标签，一个标签下可以有多个文章

1. id
2. name

#### Post

1. id
2. title 文章标题
3. body 文章正文
4. excerpt 文章摘要
5. created_time
6. modified_time
7. views 阅读量
8. **category_id  外键**
9. **author  （user_id） 外键**

#### Post_tag

文章-标签的 拥有 关系

1. <u>**tag_id 外键**</u>
2. <u>**post_id 外键**</u>

#### Comment

每个文章可以有多个评论，每个评论属于一个用户，一个用户可以评论多个文章

1. id
2. text 内容
3. created_time
4. **user_id 外键**
5. **post_id 外键**

### 关于用户权限

#### 未登录：

查看文章

#### 普通用户：

查看文章  发布文章 修改自己的文章 删除自己的文章

在所有文章下发表评论

#### staff:

在普通用户基础上 + 删除文章/删除评论  （不能修改）

#### superuser：所有权限

如增加分类 增加标签



### 

## 环境配置

建议：Ubuntu/windows

### 更新python版本

```shell
$ sudo apt-get update
$ sudo apt-get install python3.8
```

### 安装pipenv

```shell
$ sudo pip3 install pipenv
```

### 安装django

```shell
$ sudo pip3 install django
```

### 创建文件夹

```shell
$ mkdir test
$ cd test
```

### 拉取代码文件

```shell
$ git clone https://github.com/GOODChives/blog_test.git
```

### 进入项目根目录 安装依赖

```shell
$ cd blog_test
$ pipenv install --deploy --ignore-pipfile
```

### 更新数据库信息

```shell
$ pipenv run python manage.py makemigrations
$ pipenv run phthon manage.py migrate
```

### 启动服务器

```shell
$ pipenv run phthon manage.py runserver
```

### 访问首页

如果上述步骤没有问题，访问 http://127.0.0.1:8000/ 可以看到首页

## 仓库结构

### blog

views.py  视图

urls.py 路由

models.py 模型

admin.py    admin界面

#### blog/static 

静态文件，如 .css文件、.js文件

#### blog/templatetags

自定义模板标签 相关文件

### templates

各页面的html文件

### blogproject

主要是settings.py

### scripts

生成数据的脚本