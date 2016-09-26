from . import ModelMixin
from . import db
from . import timestamp


class Topic(db.Model, ModelMixin):
    """
    Topic 和 Node 关联
    """
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    created_time = db.Column(db.String())
    content = db.Column(db.String())

    # 这里要定义外键
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))

    # 定义一个关系
    # foreign_keys 有时候可以省略, 比如现在...
    comments = db.relationship('Comment', backref='topic')

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.created_time = timestamp()