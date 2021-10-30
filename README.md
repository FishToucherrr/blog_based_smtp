# blog_based_smtp
基于blog图形界面的socket_based smtp  
reference:https://github.com/GOODChives/blog_test  

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
$ git clone https://github.com/GOODChives/blog_based_smtp.git
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
