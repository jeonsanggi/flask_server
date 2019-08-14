import os
from flask import Flask


def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True) # creates the flask instance

	if test_config is None:
		# load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

	from . import home
    # home에서 정의한 bluepoint를 등록
	app.register_blueprint(home.bp)

	from . import product
	# home에서 정의한 bluepoint를 등록
	app.register_blueprint(product.bp)

	from . import test
    # home에서 정의한 bluepoint를 등록
	app.register_blueprint(test.bp)

	from . import cm
	# home에서 정의한 bluepoint를 등록
	app.register_blueprint(cm.bp)

	app.add_url_rule('/', endpoint='index')

	return app
