from werkzeug.security import generate_password_hash

from ..extensions import flask_db
from ..models import User

from . import bp_misc


@bp_misc.route('/generate_date')
def generate_date():
    flask_db.database.create_tables([User], safe=True)
    users = [
        {'username': '2017001', 'password': generate_password_hash('2017001'), 'nickname': '张三', 'gender': 'M', 'role': 'student'},
        {'username': '2017002', 'password': generate_password_hash('2017002'), 'nickname': '李四', 'gender': 'M', 'role': 'student'},
        {'username': '2017003', 'password': generate_password_hash('2017003'), 'nickname': '小红', 'gender': 'M', 'role': 'student'},
        {'username': '2017004', 'password': generate_password_hash('2017004'), 'nickname': '韩梅梅', 'gender': 'M', 'role': 'student'},
        {'username': '101', 'password': generate_password_hash('101'), 'nickname': '张老师', 'gender': 'M', 'role': 'teacher'},
        {'username': '102', 'password': generate_password_hash('102'), 'nickname': '王老师', 'gender': 'M', 'role': 'teacher'}
    ]
    User.insert_many(users).execute()
    return '初始化用户数据成功'
