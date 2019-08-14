from flask import(
	Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort
from werkzeug import secure_filename

bp = Blueprint('cm', __name__, url_prefix='/cm')

@bp.route('/')
def index():
	return render_template('cm.html')

@bp.route('/image', methods=['POST'])
def image():
	f = request.files['file']
	# f.save(secure_filename('../../test.png'))
	return secure_filename(f.filename)
