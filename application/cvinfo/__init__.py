from flask import Blueprint

bp_cvinfo = Blueprint('bp_cvinfo', __name__)

from . import views