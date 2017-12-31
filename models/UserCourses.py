from models.BaseModel import *
from peewee import PostgresqlDatabase, Model, CharField, DateTimeField, IntegerField

class UserCourses(BaseModel):
    user_id = ForeignKeyField(MyUser)
    course_id = ForeignKeyField(Courses)
    date_started = DateTimeField(default=datetime.datetime.now)
    Compleion_rate = CharField(20)

if __name__ == '__main__':
    UserCourses.create_table(fail_silently=True)

