from routes import *

from models.topic import Topic
from models.node import Node
from routes.user import current_user

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
    # print('ts', ts.topics)
    return render_template('topic_index.html', topic_list=ts.topics)


@main.route('/new', methods=[ 'GET', 'POST'])
def topic_new():
    """
    创作新主题
    """
    if request.method == 'GET':
        u = current_user()
        if u is not None:
            return render_template('topic_new.html')
        else:
            # 如果没有登录
            return redirect(url_for('node.index'))
    else:
        form = request.form
        print('new', form)
        t = Topic(form)
        t.node_id = int(form.get('note_id', '1'))
        t.save()
        return redirect(url_for('.topic', node_id=t.node_id))
