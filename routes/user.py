from routes import *

from models.user import User

main = Blueprint('user', __name__)

@main.route('/')
def user():
    return render_template('user.html')


@main.route('/login', methods=['POST'])
def login():
    """
    登录
    """
    form = request.form
    # print('user', u)
    u = User(form)
    # 检查 u 是否存在于数据库中并且 密码用户 都验证合格
    user = User.query.filter_by(username=u.username).first()
    if u.valid_login(user):
        print('登录成功')
        # 设置 session
        session['user_id'] = user.id
        return redirect(url_for('node.index'))
    else:
        print('登录失败')
        return redirect(url_for('.user'))


@main.route('/register', methods=['POST'])
def register():
    """
    注册
    """
    form = request.form
    # print('user', u)
    u = User(form)
    u.save()
    print('注册成功')
    
    return redirect(url_for('.user'))

