from BaseModel import *
from peewee import PostgresqlDatabase, Model, CharField, DateTimeField, IntegerField

class UserCourses(BaseModel):
    userCourse_id = PrimaryKeyField
    user_id = ForeignKeyField(MyUser)
    course_id = ForeignKeyField(Courses)
    date_started = DateTimeField(default=datetime.datetime.now)
    completion_rate = CharField(20)

if __name__ == '__main__':
    UserCourses.create_table(fail_silently=True)

