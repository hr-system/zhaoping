from flask import render_template, flash, redirect, url_for
from playhouse.flask_utils import PaginatedQuery, get_object_or_404
from werkzeug.security import generate_password_hash


from ..models import RecruitInfo


from .forms import AddRecruitInfo
from .forms import EditRecruitInfo
from . import bp_recruitinfo


@bp_recruitinfo.route('/list_recruitinfos')
def list_recruitinfos():
    query = RecruitInfo.select().order_by(RecruitInfo.name)
    pg = PaginatedQuery(query, paginate_by=10, page_var='page', check_bounds=True)
    page = pg.get_page()
    page_count = pg.get_page_count()
    recruitinfos = pg.get_object_list()
    return render_template('recruitinfo/list_recruitinfos.html', recruitinfos=recruitinfos, page=page, page_count=page_count)


@bp_recruitinfo.route('/profile/<int:id>')
def profile(id):
    recruitinfos = get_object_or_404(RecruitInfo, (RecruitInfo.id == id))
    return render_template('recruitinfo/profile.html', recruitinfos=recruitinfos)


@bp_recruitinfo.route('/delete_recruitinfos/<int:id>')
def delete_recruitinfos(id):
    recruitinfos = RecruitInfo.select().where(RecruitInfo.id == id).get()
    recruitinfos.delete_instance()
    flash('删除成功')
    return redirect(url_for('bp_recruitinfo.list_recruitinfos'))


@bp_recruitinfo.route('/edit_recruitinfos/<int:id>', methods=['GET', 'POST'])
def edit_recruitinfos(id):
    recruitinfos = get_object_or_404(RecruitInfo, (RecruitInfo.id == id))
    form = EditRecruitInfo()
    if form.validate_on_submit():
        recruitinfos.name = form.name.data
        recruitinfos.position = form.position.data
        recruitinfos.email = form.email.data
        recruitinfos.tel = form.tel.data
        recruitinfos.data = form.data.data
        recruitinfos.save()
        flash('修改成功')
        return redirect(url_for('bp_recruitinfo.profile', id=recruitinfos.id))
    return render_template('recruitinfo/edit_recruitinfos.html', form=form, recruitinfos=recruitinfos)


@bp_recruitinfo.route('/add_recruitinfos', methods=['GET', 'POST'])
def add_recruitinfos():
    form = AddRecruitInfo()
    if form.validate_on_submit():
        RecruitInfo.create(
            name=form.name.data,
            position=form.position.data,
            email=form.email.data,
            tel=form.tel.data,
            data=form.data.data
        )
        flash('添加成功')
        return redirect(url_for('bp_recruitinfo.list_recruitinfos'))
    return render_template('recruitinfo/add_recruitinfos.html', form=form)

