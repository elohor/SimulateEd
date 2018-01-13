from BaseModel import *
from peewee import PostgresqlDatabase, Model, CharField, DateTimeField, IntegerField

class DailyTasks(BaseModel):
    task_id = PrimaryKeyField
    day_number = IntegerField 
    course_id =  ForeignKeyField(Courses)
    task_title = CharField(70)
    task_description = CharField(100)
    resources_link = CharField(100)
    


if __name__ == '__main__':
    Courses.create_table(fail_silently=True)
