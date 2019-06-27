from flask import Blueprint

bp_recruitinfo = Blueprint('bp_recruitinfo', __name__)

from . import views