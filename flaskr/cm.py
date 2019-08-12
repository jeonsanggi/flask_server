from flask import(
	Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('cm', __name__, url_prefix='/cm')

@bp.route('/')
def index():
	return render_template('cm.html')

@bp.route('/image', methods=('POST',))
def image():
	bp.logger.info('what')
	return json.dumps(response)
