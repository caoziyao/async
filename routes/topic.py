from routes import *

from models.topic import Topic
from models.node import Node
from models.comment import Comment
from routes.user import current_user

# 蓝图
main = Blueprint('topic', __name__)

Model = Topic
HOT_TOPIC = 9
ALL_TOPIC = 10

# sorted(data, cmp=None, key=None, reverse=False)  
def hot_topic():
    """
    最热
    node_id = 9
    """
    tp = Topic.query.all()
    # for t in tp:
    #     print('len', len(t.comments))
    # 排序
    s = sorted(tp, key=lambda t: len(t.comments))
    # print(tp)
    return s

def all_topic():
    """
    全部
    node_id = 10
    """
    # comm = Comment.query.all()
    tp = Topic.query.all()
    print('ns', tp)
    return tp


def normal_topic(node_id):
    """
    普通 topic
    """
    ns = Node.query.filter_by(id=node_id).first()
    tp = ns.topics if ns is not None else []
    return tp


@main.route('/')
def topic():
    """
    技术话题
    """
    # 获取 http://127.0.0.1:3000/topic?id=1 中的 id
    u = current_user()
    node_id = int(request.args.get('node_id', -1))
    if node_id == ALL_TOPIC:
        tp = all_topic()    # 获得 nodes
    elif node_id == HOT_TOPIC:
        tp = hot_topic()
    else:
        tp = normal_topic(node_id)

    return render_template('topic_index.html', topic_list=tp, user=u)




@main.route('/new', methods=[ 'GET', 'POST'])
def topic_new():
    """
    创作新主题
    """
    u = current_user()
    if request.method == 'GET':
        if u is not None:
            # return redirect(url_for('topic.topic'))
            return render_template('topic_new.html', user=u)
        else:
            # 如果没有登录
            return redirect(url_for('node.index'))
    else:

        r = {
            'data': []
        }


        form = request.form
        print('new', form)
        t = Topic(form)
        t.node_id = int(form.get('note_id'))
        # 外键
        t.user_id = u.id
        # print('new save')
        t.save()
        # 返回数据给后端
        r['success'] = True
        r['data'] = t.json()

        return json.dumps(r, ensure_ascii=False)





# @main.route('/new', methods=[ 'GET', 'POST'])
# def topic_new():
#     """
#     创作新主题
#     """
#     u = current_user()
#     if request.method == 'GET':
#         if u is not None:
#             # return redirect(url_for('topic.topic'))
#             return render_template('topic_new.html', user=u)
#         else:
#             # 如果没有登录
#             return redirect(url_for('node.index'))
#     else:
#         form = request.form
#         print('new', form)
#         t = Topic(form)
#         t.node_id = int(form.get('note_id'))
#         # 外键
#         t.user_id = u.id
#         # print('new save')
#         t.save()
#         return redirect(url_for('.topic', node_id=t.node_id))
