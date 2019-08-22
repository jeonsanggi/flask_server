import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.module import dbModule

# creates Blueprint named 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        print('----username: ',username)
        db_class = dbModule.Database()

        if not username:
            error = "Username is required."
        elif not password:
        	error = 'Password is required.'
        elif db_class.execute(
        	# execute query and return first row
        	# fetchone은 query의 하나의 row를 반환
        	"SELECT id FROM user WHERE username='" + username +"'"
        	) is not None:
            print('-----------row-------- : ', row)
            error = 'User {} is already registered.'.format(username)
        if error is None:
            print('-----------sql execute--------')
            db_class.execute(
            	'INSERT INTO user (username, password) VALUES (%s,%s)', (username, generate_password_hash(password))
            )
            db_class.commit()
            return redirect(url_for('auth.login'))

        flash(error)
    return render_template('register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db_class = dbModule.Database()
        error = None
        sql = "SELECT * FROM user WHERE username='"+username+"'"
        print(sql)
        user = db_class.executeOne(sql)
        if user is None:
        	error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password ):
        	error = 'Incorrect password.'
        if error is None:
        	session.clear()
        	session['user_id'] = user['id']
        	return redirect(url_for('index'))

        flash(error)

    return render_template('login.html')

# view function 실행전에 실행된다.
# session에 사용자 ID가 저장되어 있는지 확인 후 database에서 user data를 가져옴
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    db_class = dbModule.Database()
    if user_id is None:
        g.user = None
    else:
        g.user = db_class.execute(
        	'SELECT * FROM user WHERE id = %s', (user_id)
        )

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
    	if g.user is None:
    		return redirect(url_for('auth.login'))

    	return view(**kwargs)
    return wrapped_view
