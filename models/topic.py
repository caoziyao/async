from . import ModelMixin
from . import db
from . import timestamp

import json

class Topic(db.Model, ModelMixin):
    """
    Topic 和 Node 关联
    """
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    created_time = db.Column(db.String())
    content = db.Column(db.String())
    # avatar = db.Column(db.String())

    # 这里要定义外键
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    # 定义一个关系
    # foreign_keys 有时候可以省略, 比如现在...
    # 自动关联 不用手动查询就有数据
    # 通过topic查找comment：c = t.comments
    # 也可以通过comment查找topic： t = c.topic
    comments = db.relationship('Comment', backref='topic')
    user = db.relationship('User', backref='topic')

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.created_time = timestamp()

    def json(self):
        d = dict(
            id = self.id,
            title = self.title,
            content = self.content,
            created_time = self.created_time,
            node_id = self.node_id,
            user_id = self.user_id,
        )
        return d