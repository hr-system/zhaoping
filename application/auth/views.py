

from flask import redirect, render_template, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from ..models import User

from .forms import LoginForm
from .forms import UserRegister
from . import bp_auth


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_or_none(User.username == form.username.data)

        if user is None:
            flash('用户名或密码错误')
            return render_template('auth/login.html', form=form)

        if not check_password_hash(user.password, form.password.data):
            flash('用户名或密码错误')
            return render_template('auth/login.html', form=form)

        login_user(user)
        return redirect(url_for('bp_welcome.welcome'))

    return render_template('auth/login.html', form=form)


@bp_auth.route('/login', methods=['GET', 'POST'])
def register():
    form = UserRegister()
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            password=generate_password_hash(form.password.data),
            nickname=form.nickname.data,
            gender=form.gender.data,
            role=form.role.data,
            mail=form.mail.data
        )
        flash('注册成功')
        return redirect(url_for('auth/login'))
    return render_template('auth/register.html', form=form)


@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    return '成功退出系统'


