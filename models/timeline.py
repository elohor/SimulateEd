from BaseModel import *
from peewee import PostgresqlDatabase, Model, CharField, DateTimeField, IntegerField
from datetime import date
import MyUser
import Courses
import DailyTasks

class Timeline(BaseModel):
    timeline_id = PrimaryKeyField
    user_id = ForeignKeyField(MyUser)
    date_started = ForeignKeyField(MyUser)
    task_id = ForeignKeyField(Courses)
    day_number =  ForeignKeyField(DailyTasks)

    current_date = datetime.datetime.now
    timeline_day = date_started - current_date
    


if __name__ == '__main__':
    UserCourses.create_table(fail_silently=True)

