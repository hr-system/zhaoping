from flask import render_template, flash, redirect, url_for
from playhouse.flask_utils import PaginatedQuery, get_object_or_404
from werkzeug.security import generate_password_hash

from application.models import CorpSum

from .forms import AddCorSum
from .forms import EditCorSum
from . import bp_corpsum


@bp_corpsum.route('/list_corpsums')
def list_corpsums():
    query = CorpSum.select().order_by(CorpSum.name)
    pg = PaginatedQuery(query, paginate_by=10, page_var='page', check_bounds=True)
    page = pg.get_page()
    page_count = pg.get_page_count()
    corpsums = pg.get_object_list()
    return render_template('corpsum/list_corpsums.html', corpsums=corpsums, page=page, page_count=page_count)


@bp_corpsum.route('/profile/<int:id>')
def profile(id):
    corpsums = get_object_or_404(CorpSum, (CorpSum.id == id))
    return render_template('corpsum/profile.html', corpsums=corpsums)


@bp_corpsum.route('/delete_corpsums/<int:id>')
def delete_corpsums(id):
    corpsums = CorpSum.select().where(CorpSum.id == id).get()
    corpsums.delete_instance()
    flash('删除成功')
    return redirect(url_for('bp_corpsum.list_corpsums'))


@bp_corpsum.route('/edit_corpsums/<int:id>', methods=['GET', 'POST'])
def edit_corpsums(id):
    corpsums = get_object_or_404(CorpSum, (CorpSum.id == id))
    form = EditCorSum()
    if form.validate_on_submit():
        corpsums.name = form.name.data
        corpsums.type = form.type.data
        corpsums.data = form.gender.data
        corpsums.save()
        flash('修改成功')
        return redirect(url_for('bp_corpsum.profile', id=corpsums.id))
    return render_template('corpsum/edit_corpsums.html', form=form, corpsums=corpsums)


@bp_corpsum.route('/add_corpsums', methods=['GET', 'POST'])
def add_corpsums():
    form = AddCorSum()
    if form.validate_on_submit():
        CorpSum.create(
            name=form.name.data,
            type=form.type.data,
            data=form.data.data
        )
        flash('添加成功')
        return redirect(url_for('bp_corpsum.list_corpsums'))
    return render_template('corpsum/add_corpsums.html', form=form)

