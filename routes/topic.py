from routes import *

from models.topic import Topic
from models.node import Node

# 蓝图
main = Blueprint('topic', __name__)

Model = Topic

@main.route('/')
def topic():
    """
    技术话题
    """
    # 获取 http://127.0.0.1:3000/topic?id=1 中的 id
    node_id = request.args.get('node_id')
    ts = Node.query.filter_by(id=node_id).first()
    print('ts', ts.topics)
    return render_template('topic_index.html', topic_list=ts.topics)
