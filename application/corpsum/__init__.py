from flask import Blueprint

bp_corpsum = Blueprint('bp_corpsum', __name__)

from . import views