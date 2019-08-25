from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from flask import current_app as current_app

from flaskr.module import dbModule
from flaskr.module import Userlog

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/log', methods=['GET'])
def log():
    userlog = Userlog.UserLog()
    db_class = dbModule.Database()
    
    recommend = userlog.recommend(session['user_id'])
    print("-------------사용자 추천--------")
    data=[]
    for color in recommend:
        sql = "SELECT Brand, Product, Color, Price, Image FROM deepstick.products WHERE Color='" + color + "'"
        row = db_class.executeOne(sql)
        if not row:
            continue
        data.append(row)

    return render_template('/user.html',
							resultData=data,
							size=len(data))
