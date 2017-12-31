import sys, os
sys.path.append(os.getcwd())

from flask import Flask, render_template, redirect, session, request, flash, url_for
from models.BaseModel import DBSingelton
from models.Courses import Courses
from models.MyUser import MyUser
from models.UserCourses import UserCourses
from twilio import twiml
from flask_rq2 import RQ


app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
rq = RQ(app)


@app.before_first_request
def initialize_tables() :
    connect_db()
    if not MyUser.table_exists() :
        MyUser.create_table()

    if not Courses.table_exists() :
        Courses.create_table()

    if not UserCourses.table_exists() :
        UserCourses.create_table()

    disconnect_db()


@app.before_request
def connect_db() :
    DBSingelton.getInstance().connect()


@app.teardown_request
def disconnect_db(err = None) :
    DBSingelton.getInstance().close()

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    resp = twiml.Response()
    resp.message('Hello {},: {}'.format(number, message_body))
    return str(resp)

@rq.job
def add_jobs():
    add.cron('0 0 12 * * ?', 'add-one-two', 1, 2)

@app.route('/')
def course_level():
    # completed = []
    # uncompleted = []
    # for user_id in UserCourses:
    #     if completion_rate < 100:
    #         uncompleted.append(user_id)
    #     else:
    #         completed.append(user_id)
  

