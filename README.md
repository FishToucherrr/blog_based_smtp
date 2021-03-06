# blog_based_smtp

> reference：
>
> https://github.com/GOODChives/blog_test 
>
> https://docs.python.org/3/library/ssl.html

+ 基于blog图形界面的socket_based smtp  
+ 存在bug 但是不改了  
+ 核心功能见blog/sklab.py  
+ socket_based_smtp
+ 从隔壁blog改过来的 所以一大堆多余的文件没删
+ `TLS/SSL wrapper for socket objects` are used.

## 环境配置

建议：Ubuntu/windows

### 更新python版本

```shell
$ sudo apt-get update
$ sudo apt-get install python3.9
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
$ git clone https://github.com/GOODChives/blog_based_smtp.git
```

### 进入项目根目录 安装依赖

```shell
$ cd blog_based_smtp
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
