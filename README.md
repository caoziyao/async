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

- virtualenv
在 /var/www 目录下建立一个 myflask 的文件夹(你的项目目录)，然后用 chmod 改一下权限
mkdir /var/www/iV2EX
chmod 777 /var/www/iV2EX
virtualenv --no-site-packages venv
source venv/bin/activate


- 安装 Gunicorn
Gunicorn 应该装在你的 virtualenv 环境下。安装前记得激活 venv
(venv) $ pip3 install gunicorn

运行 Gunicorn
(venv) $  nohup gunicorn -w4 -b0.0.0.0:80 appcorn:application &


- 项目地址
45.76.101.36
或 www.zycode.cc


- 附
pip uninstall gunicorn
pip3 install gunicorn

source venv/bin/activate
退出当前的venv环境，使用deactivate命令：

ps ax|grep gunicorn
pkill gunicorn