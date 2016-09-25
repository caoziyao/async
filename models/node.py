from . import ModelMixin
from . import db
from . import timestamp

'''
Node:
    id


Topic:
    id
    created_time
    title
    content
    user_id(外键)
    node_id(外键)

Comment:
    id
    created_time
    content
    user_id(外键)
    topic_id(外键)

User:
    id
    created_time
    sex

Message:
    id
    created_time
    sender_id
    recv_id

'''


class Node(db.Model, ModelMixin):
    """
    model 数据
    """
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    # 定义一个关系
    # foreign_keys 有时候可以省略, 比如现在...
    topics = db.relationship('Topic', backref='node')

    def __init__(self, name):
        self.name = name
