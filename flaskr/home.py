from flask import(
	Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug import secure_filename
from flaskr.module import dbModule

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
	color_name = result['color_name']

	db_class = dbModule.Database()
	sql = "SELECT Brand, Product, Color, Price, Image \
		   FROM deepstick.products \
		   WHERE Product='" + color_name + "'"
	row = db_class.executeAll(sql)
	print(row)
	print("row 길이: " ,len(row))
	return render_template('/product.html',
							resultData=row,
							size=len(row))
