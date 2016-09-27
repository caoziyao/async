from . import ModelMixin
from . import db
from . import timestamp

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

    # 定义一个关系
    # foreign_keys 有时候可以省略, 比如现在...
    #comments_user = db.relationship('Comment', backref='user')
    # topics = db.relationship('Topic', backref='user')

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.created_time = timestamp()

    def valid_login(self, u):
        """
        校验登陆
        """
        return u is not None and u.username == self.username and u.password == self.password
