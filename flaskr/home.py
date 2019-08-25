from flask import(
	Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from werkzeug import secure_filename
from flaskr.module import dbModule
from flaskr.module import CosSimilarity
from flaskr.module import ReviewCount
from flaskr.auth import login_required
# from flaskr.module import WordCloud
import pandas as pd

bp = Blueprint('home', __name__ )

@bp.route('/')
def index():
	return render_template('home.html',
							g=session)
@bp.route('/image', methods=['POST'])
def image():
	f = request.files['file']
	# f.save(secure_filename('../../test.png'))
	return secure_filename(f.filename)

@bp.route('/single/<data>')
def single(data):
	print('----single----')
	# print('-----',request.args.get('product'),'------')
	db_class = dbModule.Database()
	sql = "SELECT Brand, Product, Color, Price, Image, R, G, B, colorpower, spread, keep, moisture \
		   FROM deepstick.products \
		   WHERE Color='" + data + "'"

	row = db_class.executeOne(sql)
	print("-----row-----",row)
	sql = "SELECT Brand, Color, remonth, Product, Review \
		   FROM deepstick.review \
		   WHERE Color='" + row['Color'] + "'"

	row_review = db_class.executeAll(sql)
	print('----row_review------',row_review)
	if row_review and row_review[0]['remonth'] is not None:
		review = pd.DataFrame(row_review)
		re_class = ReviewCount.ReviewCnt()
		re_class.draw(review, row['Color'])

		Countpath = '../static/images/'+row['Color']+'.png'
		WCpath = '../static/images/wordcloud/'+row['Product']+'.png'
	else:
		Countpath = False
		WCpath = False
	print("wcpath------", WCpath)
	return render_template('/single.html',
							resultData=row,
							resultFigPath=Countpath,
							resultWCPath=WCpath)

@bp.route('/search', methods=['POST'])
def search():
	print('--------search---------')
	result = request.form
	color_name = result['color_name']

	db_class = dbModule.Database()
	sql = "SELECT Color, label_one, label_two \
		   FROM deepstick.products \
		   WHERE Color='" + color_name + "'"

	row = db_class.executeOne(sql)
	label_one = str(row['label_one'])
	label_two = str(int(row['label_two']))

	sql = "SELECT Brand, Product, Color, Price, Image, colorpower, spread, keep, moisture \
		   FROM deepstick.products \
		   WHERE label_one='" + label_one + "' AND label_two='" + label_two +"'"
	row = db_class.executeAll(sql)

	CosSim = CosSimilarity.CosSimilarity(row)

	row = CosSim.get_recommendations(color_name)

	data =[]
	for i in range(0,7):
		data.append(dict(row.iloc[i]))

	return render_template('/product.html',
							resultData=data,
							size=len(data))
