from werkzeug.security import check_password_hash

from flask import redirect, render_template, url_for, flash
from flask_login import login_user, logout_user, login_required

from ..models import User

from .forms import LoginForm
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
        return redirect(url_for('bp_welcome.index'))

    return render_template('auth/login.html', form=form)


@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    return '成功退出系统'


