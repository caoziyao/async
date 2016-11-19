# iV2EX
仿V2EX论坛

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![platform](https://img.shields.io/badge/python-3.4-green.svg)]()

* 主页：[https://github.com/caoziyao/iV2EX](https://github.com/caoziyao/iV2EX)
* 联系邮箱：wyzycao@gmail.com

> * 项目地址
> * python 配置环境
> * 运行
> * 开发日记

![iV2EX](https://github.com/caoziyao/iV2EX/blob/master/static/img/v2ex.png)  

## 项目地址

> http://45.76.101.36
或
http://www.zycode.cc

## 开发日记
- [x] 搭建框架
- [x] 发布、编辑、删除文章功能
- [x] 添加富文本编辑器
- [x] 个人信息修改
- [x] 图片上传
- [x] 分页功能
- 完善个人主页：显示发布过的文章
- [x] 添加权限系统
- [x] 安全问题、密码加密 hashlib
- 爬虫获取内容

## 优化

## 部署方案
- nginx + Gunicorn + supervisord
- virtualenv

## python 配置环境
- 后台基于flask开发，可以用Python环境直接运行。 
1. pip环境下安装在/下的package pip3 install -r requirements.txt
2. python3 app.py server
3. 访问 http://localhost:80/








