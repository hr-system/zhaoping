

from flask import redirect, render_template, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from ..models import User

from .forms import LoginForm
from .forms import UserRegister
from . import bp_auth


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    log = LoginForm()
    if log.validate_on_submit():
        user = User.get_or_none(User.username == log.username.data)

        if user is None:
            flash('用户名或密码错误')
            return render_template('auth/login.html', form=log)

        if not check_password_hash(user.password, log.password.data):
            flash('用户名或密码错误')
            return render_template('auth/login.html', form=log)

        login_user(user)
        return redirect(url_for('bp_welcome.welcome'))

    return render_template('auth/login.html', form=log)


@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    re = UserRegister()
    if re.validate_on_submit():
        User.create(
            username=re.username.data,
            password=generate_password_hash(re.password.data),
            nickname=re.nickname.data,
            gender=re.gender.data,
            role=re.role.data,
            mail=re.mail.data,
            address=re.address.data
        )
        flash('注册成功')
        return redirect(url_for('bp_auth.login'))
    return render_template('auth/register1.html', form=re)


@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    return '成功退出系统'


