from models.BaseModel import *
from peewee import PostgresqlDatabase, Model, CharField, DateTimeField, IntegerField

class MyUser(BaseModel):
    user_id = PrimaryKeyField
    username = CharField(20)
    password = CharField(10)
    email = CharField(30)


if __name__ == '__main__':
	MyUser.create_table(fail_silently=True)

	new_user = MyUser(username = "ethomas", password = "secret", email = "elohor.thomas@meltwater.org")
	new_user.save()

	for my_user in MyUser.select():
		print ("email {0} at {1}".format(my_user.username, my_user.email))

