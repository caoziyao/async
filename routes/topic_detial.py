from routes import *

from models.topic import Topic
from models.comment import Comment
from models.user import User

main = Blueprint('detail', __name__)


@main.route('/')
def detail():
    """
    id 唯一标识一个 Topic
    """
    topic_id = int(request.args.get('topic_id'))
    ts = Topic.query.get(topic_id)
    # print('topic_detail', ts)
    # 自动关联 不用手动查询就有数据
    cs = ts.comments
    # print(cs)
    # 查找用户
    # us = []
    # for c in cs:
        # u = User.query.get(c.user_id)
        # c.append(u.username)
    # print('user', cs)
    return render_template('topic_detail.html', t=ts, comment_list=cs)


@main.route('/add/<int:topic_id>', methods=['POST'])
def comment_add(topic_id):
    """
    增加评论功能, topic_id 唯一标识一个 Topic
    """
    # print('comment_add id', topic_id)
    form = request.form
    c = Comment(form)
    # 外键
    c.topic_id = topic_id
    
    c.save()
    return redirect(url_for('.detail', topic_id=topic_id))