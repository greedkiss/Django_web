# Django登陆界面
## 介绍
本次项目使用Django开发登陆界面，用户输入用户名密码进行登陆（默认用户名为root,密码为admin）  
若输入正确的用户名和密码页面跳转显示恭喜你！登陆成功！字样  
如果输入错误的用户名或者密码，界面返回用户名或密码错误字样
## 使用方式
- 安装python
- 安装Django
- 配置好环境后，进入login目录下后，输入以下命令启动本地web服务
```shell
python manage.py runserver 127.0.0.1:8000
#or
python3 manage.py runserver 127.0.0.1:8000
```
- 之后在浏览器中打开127.0.0.1:8000即可看到登陆界面
## 结果演示
用户登陆界面,用户名是root,密码是admin  
![login](https://github.com/greedkiss/markdown_picture/blob/master/login.png)  
登陆成功  
![home](https://github.com/greedkiss/markdown_picture/blob/master/home.png)  
登陆失败  
![error](https://github.com/greedkiss/markdown_picture/blob/master/login_error.png)
