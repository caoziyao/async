from routes import *

from models.node import Node
from models.topic import Topic
from models.comment import Comment
from models.user import User
from routes.user import current_user

# 蓝图
main = Blueprint('node', __name__)

Model = Node

def test_data():
    """
    测试数据库
    """
    n = Node('name1')
    n.save()
    t = Topic('title')
    # t.node_id = n.id
    t.node = n
    t.save()

    data = Node.query.filter_by(name='name1').first()
    print('data', data)
    print('topic', data.topics)



@main.route('/')
def index():
    # test_data()
    ms = Model.query.all()
    # 获得当前用户
    u = current_user()
    return render_template('node_index.html', node_list=ms, user=u)
    # return render_template('base.html')



    
