from routes import *

from models.user import User


main = Blueprint('user', __name__)


def current_user():
    """
    当前用户
    session 获得 user_id
    """
    uid = session.get('user_id')
    if uid is not None:
        u = User.query.get(uid)
        return u


@main.route('/')
def user():
    u = current_user()
    return render_template('user.html', user=u)


def save_setting(u, form):
    """
    设置用户信息
    """
    u.email = form.get('email', '')
    u.signed = form.get('signed', '')
    u.brief = form.get('brief', '')
    u.save()


@main.route('/setting', methods=['GET', 'POST'])
def setting():
    """
    设置用户信息
    """
    u = current_user()
    if request.method == 'GET':
        return render_template('user_setting.html', user=u)
    else:
        # 获得数据
        form = request.form
        save_setting(u, form)
        return render_template('user_setting.html', user=u)


@main.route('/update_img', methods=['POST'])
def update_img():
    """
    更新头像
    """
    u = current_user()
    form = request.form
    # print(form)
    img = form.get('file', '')
    img_url = '/static/img/avatar/' + img
    u.img_url = img_url
    u.save()
    return render_template('user_setting.html', user=u)



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
    u.img_url = url_for('static', filename='img/avatar/default.png')
    print(u.img_url)
    u.save()
    print('注册成功')
    
    return redirect(url_for('.user'))

@main.route('/signout')
def signout():
    """
    登出
    """
    pass
