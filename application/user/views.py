from flask import render_template, flash, redirect, url_for
from playhouse.flask_utils import PaginatedQuery, get_object_or_404
from werkzeug.security import generate_password_hash

from ..models import User

from .forms import AddUser
from .forms import EditUser
from . import bp_user


@bp_user.route('/list_users')
def list_users():
    query = User.select().order_by(User.username)
    pg = PaginatedQuery(query, paginate_by=10, page_var='page', check_bounds=True)
    page = pg.get_page()
    page_count = pg.get_page_count()
    users = pg.get_object_list()
    return render_template('user/list_users.html', users=users, page=page, page_count=page_count)


@bp_user.route('/profile/<int:id>')
def profile(id):
    user = get_object_or_404(User, (User.id == id))
    return render_template('user/profile.html', user=user)


@bp_user.route('/delete_user/<int:id>')
def delete_user(id):
    user = User.select().where(User.id == id).get()
    user.delete_instance()
    flash('删除成功')
    return redirect(url_for('bp_user.list_users'))


@bp_user.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = get_object_or_404(User, (User.id == id))
    form = EditUser()
    if form.validate_on_submit():
        user.username = form.username.data
        user.nickname = form.nickname.data
        user.gender = form.gender.data
        user.save()
        flash('修改成功')
        return redirect(url_for('bp_user.profile', id=user.id))
    return render_template('user/edit_user.html', form=form, user=user)


@bp_user.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = AddUser()
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            password=generate_password_hash(form.password.data),
            nickname=form.nickname.data,
            gender=form.gender.data,
            role=form.role.data
        )
        flash('添加成功')
        return redirect(url_for('bp_user.list_users'))
    return render_template('user/add_user.html', form=form)