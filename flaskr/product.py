from flask import(
	Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('prodcut', __name__, url_prefix='/product' )

@bp.route('/')
def home():
	return render_template('product.html')
