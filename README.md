# iV2EX
伪V2EX

- python 配置环境
apt-get update
apt-get install python-dev python-pip python-virtualenv

apt-get install python3-pip
pip3 install virtualenv
pip3 install flask flask-sqlalchemy
pip3 install flask-migrate flask-script

- 安装 nginx
apt-get install nginx

- 在 /var/www 目录下建立一个 myflask 的文件夹(你的项目目录)，然后用 chmod 改一下权限
mkdir /var/www/iV2EX
chmod 777 /var/www/iV2EX


安装 Gunicorn
Gunicorn 应该装在你的 virtualenv 环境下。安装前记得激活 venv
virtualenv --no-site-packages venv
source venv/bin/activate
(venv) $ pip3 install gunicorn

运行 Gunicorn
(venv) $ gunicorn -w 4 -b 0.0.0.0:80 wsgi:application

- 运行 python3 app.py server

- 项目地址
45.76.101.36:3000
或 www.zycode.cc:3000


- 后续
下步部署 Nginx + Gunicore



http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000