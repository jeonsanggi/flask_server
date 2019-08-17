from flask import(
	Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug import secure_filename

bp = Blueprint('home', __name__ )

@bp.route('/')
def home():
	return render_template('home.html')

@bp.route('/image', methods=['POST'])
def image():
	f = request.files['file']
	# f.save(secure_filename('../../test.png'))
	return secure_filename(f.filename)

@bp.route('/search', methods=['POST'])
def search():
	result = request.form
	product_name = result['product_name']

	
	return product_name
