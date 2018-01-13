from BaseModel import *
from peewee import PostgresqlDatabase, Model, CharField, DateTimeField, IntegerField
import timeline

class MyUser(BaseModel):
    user_id = PrimaryKeyField
    username = CharField(20)
    password = CharField(10)
    email = CharField(30)
    phone_number = IntegerField
    course = CharField(100)
    date_started = DateTimeField(default=datetime.datetime.now)

    # active_users = MyUser.select(username).join(DailyTasks).where(MyUser.user_id = DailyTasks.user_id and Timeline.date_started = NOT NULL)
        


if __name__ == '__main__':
	MyUser.create_table(fail_silently=True)

	new_user = MyUser(username = "ethomas", password = "secret", email = "elohor.thomas@meltwater.org, phone_number = 07034891929, course = Customer Service")
	new_user.save()

	for my_user in MyUser.select():
		print ("email {0} at {1}".format(MyUser.username, MyUser.email))

