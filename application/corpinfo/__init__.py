from flask import Blueprint

bp_corpinfo = Blueprint('bp_corpinfo', __name__)

from . import views