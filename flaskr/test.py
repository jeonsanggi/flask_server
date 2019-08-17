from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

from flaskr.module import dbModule

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route('/', methods=['GET'])
def index():
    return render_template('/testDB.html',
                            result=None,
                            resultData=None,
                            resultUPDATE=None)



# INSERT 함수 예제
@bp.route('/insert', methods=['GET'])
def insert():
    db_class = dbModule.Database()

    sql      = "INSERT INTO testDB.testTable(test) \
                VALUES('%s')" % ('testData')
    db_class.execute(sql)
    db_class.commit()

    return render_template('/testDB.html',
                           result='insert is done!',
                           resultData=None,
                           resultUPDATE=None)



# SELECT 함수 예제
@bp.route('/select', methods=['GET'])
def select():
    db_class = dbModule.Database()

    sql = "SELECT Brand, Product, Color, Price, Image \
		   FROM deepstick.products \
		   WHERE Product='" + "루쥬 쀠르 꾸뛰르" + "'"
    row      = db_class.executeAll(sql)

    print(row)

    return render_template('/testDB.html',
                            result=None,
                            resultData=row[0],
                            resultUPDATE=None)



# UPDATE 함수 예제
@bp.route('/update', methods=['GET'])
def update():
    db_class = dbModule.Database()

    sql      = "UPDATE testDB.testTable \
                SET test='%s' \
                WHERE test='testData'" % ('update_Data')
    db_class.execute(sql)
    db_class.commit()

    sql      = "SELECT idx, test \
                FROM testDB.testTable"
    row      = db_class.executeAll(sql)

    return render_template('/testDB.html',
                            result=None,
                            resultData=None,
                            resultUPDATE=row[0])
