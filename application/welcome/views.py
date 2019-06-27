from flask import render_template
from flask_login import login_required
from playhouse.flask_utils import get_object_or_404
from flask import Flask, render_template, request, redirect, url_for, flash, abort


from ..models import User

from . import bp_welcome
from ..auth.forms import EditPerson


@bp_welcome.route('/welcome')
@login_required
def welcome():
    return render_template('welcome/page_news.html')


@bp_welcome.route('/we')
@login_required
def we():
    return render_template('page/WebBio.html')


@bp_welcome.route('/page_calendar')
@login_required
def page_calendar():
    return render_template('welcome/page_calendar.html')


@bp_welcome.route('/profile/<string:username>')
@login_required
def profile(username):
    user = get_object_or_404(User, (User.username == username))
    return render_template('welcome/profile.html', user=user)


@bp_welcome.route('/edit_user/<string:username>', methods=['GET', 'POST'])
@login_required
def edit_user(username):
    user = get_object_or_404(User, (User.username == username))
    form = EditPerson()
    if form.validate_on_submit():
        user.nickname = form.nickname.data
        user.gender = form.gender.data
        user.address = form.address.data
        user.mail = form.mail.data
        user.save()
        flash('修改成功')
        return redirect(url_for('bp_welcome.profile', username=user.username))
    return render_template('welcome/edit_user.html', form=form, user=user)