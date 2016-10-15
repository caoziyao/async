from . import ModelMixin
from . import db
from . import timestamp

import json


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

    def json(self):
        d = dict(
            id=self.id,
            created_time=self.created_time,
            comment=self.comment,
            
            replys=self.replys,
            topic_id=self.topic_id,
            user_id=self.user_id,
            # 外键
            user_img_url=self.user.img_url,
            username=self.user.username,
        )
        return d