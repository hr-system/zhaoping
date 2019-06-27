from flask import render_template, flash, redirect, url_for
from playhouse.flask_utils import PaginatedQuery, get_object_or_404
from werkzeug.security import generate_password_hash


from ..models import CVInfo


from .forms import AddCVInfo
from .forms import EditCVInfo
from . import bp_cvinfo


@bp_cvinfo.route('/list_cvinfos')
def list_cvinfos():
    query = CVInfo.select().order_by(CVInfo.name)
    pg = PaginatedQuery(query, paginate_by=10, page_var='page', check_bounds=True)
    page = pg.get_page()
    page_count = pg.get_page_count()
    cvinfos = pg.get_object_list()
    return render_template('cvinfo/list_cvinfos.html', cvinfos=cvinfos, page=page, page_count=page_count)


@bp_cvinfo.route('/profile/<int:id>')
def profile(id):
    cvinfos = get_object_or_404(CVInfo, (CVInfo.id == id))
    return render_template('cvinfo/profile.html', cvinfos=cvinfos)


@bp_cvinfo.route('/delete_cvinfos/<int:id>')
def delete_cvinfos(id):
    cvinfos = CVInfo.select().where(CVInfo.id == id).get()
    cvinfos.delete_instance()
    flash('删除成功')
    return redirect(url_for('bp_cvinfo.list_cvinfos'))


@bp_cvinfo.route('/edit_cvinfos/<int:id>', methods=['GET', 'POST'])
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

