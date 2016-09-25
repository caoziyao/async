from flask import Flask
from flask import render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db
from routes.node import main as route_node
from routes.topic import main as route_topic
from routes.topic_detial import main as route_topic_detial
from routes.user import main as route_user

app = Flask(__name__)
db_path = 'todo.sqlite'
manager = Manager(app)


# 自定义的命令行命令用来运行服务器
@manager.command
def server():
    print('server run')
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


def register_route(app):
    """
    蓝图注册
    """
    # url_prefix='/node'
    app.register_blueprint(route_node)
    app.register_blueprint(route_topic, url_prefix='/topic')
    app.register_blueprint(route_topic_detial, url_prefix='/detail')
    app.register_blueprint(route_user, url_prefix='/user')


def configure_app():
    """
    套路
    """
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 设置 secret_key 来使用 flask 自带的 session
    app.secret_key = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    # 蓝图注册
    register_route(app)


def configure_manager():
    """
    这个函数用来配置命令行选项
    """
    # 数据库迁移
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


@app.errorhandler(404)
def error404(e):
    """
    自定义 404 界面
    """
    return render_template('404.html')


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()       # 命令行