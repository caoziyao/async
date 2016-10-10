from . import ModelMixin
from . import db
from . import timestamp


class Comment(db.Model, ModelMixin):
    """
    评论功能
    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.String())
    comment = db.Column(db.String())
    username = db.Column(db.String())
    replys = db.Column(db.Integer)

    # 这里要定义外键
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='comment')

    def __init__(self, form):
        self.comment = form.get('comment', '')
        self.created_time = timestamp()