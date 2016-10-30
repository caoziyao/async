from . import ModelMixin
from . import db
from . import timestamp

from flask import flash

class Permission:
    """
    用户权限
    0b0000 0001 关注用户
    0b0000 0010 可以评论
    0b0000 0100 写文章
    0b0000 1000 管理他人的评论
    0b1000 0000 管理员  
    """
    FOLLOW = 0x1
    COMMENT = 0x2
    WRITE_ARITICLES = 0x4
    MODERATE_COMMENTS = 0x8
    ADMINISTER = 0x80


class User(db.Model, ModelMixin):
    """
    用户信息
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    created_time = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())
    signed = db.Column(db.String())
    brief = db.Column(db.String())
    img_url = db.Column(db.String())
    permissions = db.Column(db.Integer)

    # 定义一个关系
    # foreign_keys 有时候可以省略, 比如现在...
    #comments_user = db.relationship('Comment', backref='user')
    # topics = db.relationship('Topic', backref='user')

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.created_time = timestamp()
        self.permissions = 0x7      # 默认是普通用户

    def valid_login(self, u):
        """
        校验登陆
        """
        return u is not None and u.username == self.username and u.password == self.password

    def valid_register(self):
        """
        校验注册
        """
        if len(self.username) < 3 or len(self.password) < 3:
            print('用户名/密码太短，小于2个字符')
            return False
        else:
            return True

        u = User.query.filter_by(username = self.username).first()
        if u is not None:
            print('已经存在用户')
            return True
        else:
            return False
        

