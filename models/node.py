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



def create_node():
    """
    创建 node 

    """
    n1 = Node('tech')
    n2 = Node('activity')
    n3 = Node('play')
    n4 = Node('apple')
    n5 = Node('jobs')
    n6 = Node('deals')
    n7 = Node('city')
    n8 = Node('qna')
    n9 = Node('hot')
    n10 = Node('all')
    n11 = Node('r2')
    n12 = Node('nodess')
    n13 = Node('members')
    n1.save()
    n2.save()
    n3.save()
    n4.save()
    n5.save()
    n6.save()
    n7.save()
    n8.save()
    n9.save()
    n10.save()
    n11.save()
    n12.save()
    n13.save()
