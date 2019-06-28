from flask import render_template, flash, redirect, url_for, abort
from playhouse.flask_utils import PaginatedQuery, get_object_or_404
from werkzeug.security import generate_password_hash
from flask_login import login_required, current_user
from ..utilities import name_required

from ..models import CVInfo
from ..models import User


from .forms import AddCVInfo
from .forms import EditCVInfo
from . import bp_cvinfo


@bp_cvinfo.route('/list_cvinfos')
@login_required
def list_cvinfos():
    query = CVInfo.select().order_by(CVInfo.name)
    pg = PaginatedQuery(query, paginate_by=10, page_var='page', check_bounds=True)
    page = pg.get_page()
    page_count = pg.get_page_count()
    cvinfos = pg.get_object_list()
    return render_template('cvinfo/list_cvinfos.html', cvinfos=cvinfos, page=page, page_count=page_count)


@bp_cvinfo.route('/profile/<int:id>')
@login_required
def profile(id):
    cvinfos = get_object_or_404(CVInfo, (CVInfo.id == id))
    return render_template('cvinfo/profile.html', cvinfos=cvinfos)


@bp_cvinfo.route('/delete_cvinfos/<string:name>')
@login_required
# @name_required('<string:name>')
def delete_cvinfos(name):
    me = current_user
    cvinfos = CVInfo.select().where(CVInfo.name == name).get()
    if me.nickname != cvinfos.name:
        abort(403)
    else:
        cvinfos.delete_instance()
        flash('删除成功')
        return redirect(url_for('bp_cvinfo.list_cvinfos'))


@bp_cvinfo.route('/edit_cvinfos/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_cvinfos(id):
    cvinfos = get_object_or_404(CVInfo, (CVInfo.id == id))
    form = EditCVInfo()
    if form.validate_on_submit():
        cvinfos.name = form.name.data
        cvinfos.gender = form.gender.data
        cvinfos.email = form.email.data
        cvinfos.tel = form.tel.data
        cvinfos.address = form.address.data
        cvinfos.birthday = form.birthday.data
        cvinfos.save()
        flash('修改成功')
        return redirect(url_for('bp_cvinfo.profile', id=cvinfos.id))
    return render_template('cvinfo/edit_cvinfos.html', form=form, cvinfos=cvinfos)


@bp_cvinfo.route('/add_cvinfos', methods=['GET', 'POST'])
@login_required
def add_cvinfos():
    form = AddCVInfo()
    if form.validate_on_submit():
        CVInfo.create(
            name=form.name.data,
            gender=form.gender.data,
            email=form.email.data,
            tel=form.tel.data,
            address=form.address.data,
            birthday=form.birthday.data
        )
        flash('添加成功')
        return redirect(url_for('bp_cvinfo.list_cvinfos'))
    return render_template('cvinfo/add_cvinfos.html', form=form)

