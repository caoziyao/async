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
    u = current_user()
    node_id = int(request.args.get('node_id'))
    print('node id', node_id)
    # 获得 nodes
    ns = Node.query.filter_by(id=node_id).first()
    if ns is None:
        # print('t is None', ts)
        return render_template('topic_index.html', topic_list=[], user=u)
    # print('ts', ts.topics)
    # print('t isnot None', ts)
    return render_template('topic_index.html', topic_list=ns.topics, user=u)


@main.route('/new', methods=[ 'GET', 'POST'])
def topic_new():
    """
    创作新主题
    """
    u = current_user()
    if request.method == 'GET':
        if u is not None:
            return render_template('topic_new.html')
        else:
            # 如果没有登录
            return redirect(url_for('node.index'))
    else:
        form = request.form
        print('new', form)
        t = Topic(form)
        t.node_id = int(form.get('note_id'))
        # 外键
        t.user_id = u.id
        print('new save')
        t.save()
        return redirect(url_for('.topic', node_id=t.node_id))
