from flask import render_template, flash, redirect, url_for
from playhouse.flask_utils import PaginatedQuery, get_object_or_404
from werkzeug.security import generate_password_hash


from ..models import CorpInfo


from .forms import AddCorpInfo
from .forms import EditCorpInfo
from . import bp_corpinfo


@bp_corpinfo.route('/list_corpinfos')
def list_corpinfos():
    query = CorpInfo.select().order_by(CorpInfo.name)
    pg = PaginatedQuery(query, paginate_by=10, page_var='page', check_bounds=True)
    page = pg.get_page()
    page_count = pg.get_page_count()
    corpinfos = pg.get_object_list()
    return render_template('corpinfo/list_corpinfos.html', corpinfos=corpinfos, page=page, page_count=page_count)


@bp_corpinfo.route('/profile/<int:id>')
def profile(id):
    corpinfos = get_object_or_404(CorpInfo, (CorpInfo.id == id))
    return render_template('corpinfo/profile.html', corpinfos=corpinfos)


@bp_corpinfo.route('/delete_corpinfos/<int:id>')
def delete_corpinfos(id):
    corpinfos = CorpInfo.select().where(CorpInfo.id == id).get()
    corpinfos.delete_instance()
    flash('删除成功')
    return redirect(url_for('bp_corpinfo.list_corpinfos'))


@bp_corpinfo.route('/edit_corpinfos/<int:id>', methods=['GET', 'POST'])
def edit_corpinfos(id):
    corpinfos = get_object_or_404(CorpInfo, (CorpInfo.id == id))
    form = EditCorpInfo()
    if form.validate_on_submit():
        corpinfos.name = form.name.data
        corpinfos.biography = form.biography.data
        corpinfos.address = form.address.data
        corpinfos.email = form.email.data
        corpinfos.tel = form.tel.data
        corpinfos.save()
        flash('修改成功')
        return redirect(url_for('bp_corpinfo.profile', id=corpinfos.id))
    return render_template('corpinfo/edit_corpinfos.html', form=form, corpinfos=corpinfos)


@bp_corpinfo.route('/add_corpinfos', methods=['GET', 'POST'])
def add_corpinfos():
    form = AddCorpInfo()
    if form.validate_on_submit():
        CorpInfo.create(
            name=form.name.data,
            biography=form.biography.data,
            address=form.address.data,
            email=form.email.data,
            tel=form.tel.data
        )
        flash('添加成功')
        return redirect(url_for('bp_corpinfo.list_corpinfos'))
    return render_template('corpinfo/add_corpinfos.html', form=form)

