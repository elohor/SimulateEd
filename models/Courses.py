from BaseModel import *
from peewee import PostgresqlDatabase, Model, CharField, DateTimeField, IntegerField

class Courses(BaseModel):
    course_id = PrimaryKeyField
    task_id = IntegerField(50)
    course_title = CharField(70)
    course_description = CharField

if __name__ == '__main__':
    Courses.create_table(fail_silently=True)
