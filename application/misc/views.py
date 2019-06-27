from werkzeug.security import generate_password_hash

from ..extensions import flask_db
from ..models import User, CorpSum, CorpInfo, RecruitInfo, CVInfo

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


@bp_misc.route('/generate_date1')
def generate_date1():
    flask_db.database.create_tables([CorpSum], safe=True)
    data1 = [
        {'name': '同方', 'type': 'M', 'date': '2016-12-12'},
        {'name': '华为', 'type': 'M', 'date': '2016-12-12'},
        {'name': '三星', 'type': 'M', 'date': '2016-12-12'},
        {'name': '三星', 'type': 'M', 'date': '2019-06-15'}
    ]
    CorpSum.insert_many(data1).execute()
    return '初始化数据成功1'


@bp_misc.route('/generate_date2')
def generate_date2():
    flask_db.database.create_tables([CorpInfo], safe=True)
    data2 = [
        {'name': '刘顺', 'address': '云南省昆明市', 'tel': '15087441352', 'biography': 'M'},
        {'name': '小王', 'address': '云南省昆明市', 'tel': '15087441352', 'biography': 'M'},
        {'name': '王五', 'address': '云南省昆明市', 'tel': '15087441352', 'biography': 'M'}
    ]
    CorpInfo.insert_many(data2).execute()
    return '初始化数据成功2'


@bp_misc.route('/generate_date3')
def generate_date3():
    flask_db.database.create_tables([RecruitInfo], safe=True)
    data3 = [
        {'name': '王五', 'position': '网络工程师', 'type': '医学', 'tel': '15087441352', 'email': '2523892104@qq.com', 'date': '2019-9-25'},
        {'name': '张三', 'position': '网络工程师', 'type': '医学', 'tel': '15087441352', 'email': '2523892104@qq.com', 'date': '2019-9-25'},
        {'name': '李四', 'position': '网络工程师', 'type': '医学', 'tel': '15087441352', 'email': '2523892104@qq.com', 'date': '2019-9-25'}
    ]
    RecruitInfo.insert_many(data3).execute()
    return '初始化数据成功3'


@bp_misc.route('/generate_date4')
def generate_date4():
    flask_db.database.create_tables([CVInfo], safe=True)
    data4 = [
        {'name': '同方', 'email': '2523892104@qq.com', 'address': '云南省昆明市', 'tel': '15087441352', 'gender': 'F', 'birthday': '2019-6-25'},
        {'name': '同方', 'email': '2523892104@qq.com', 'address': '云南省昆明市', 'tel': '15087441352', 'gender': 'M', 'birthday': '2019-6-25'},
        {'name': '同方', 'email': '2523892104@qq.com', 'address': '云南省昆明市', 'tel': '15087441352', 'gender': 'M', 'birthday': '2019-6-25'}
    ]
    CVInfo.insert_many(data4).execute()
    return '初始化数据成功4'


