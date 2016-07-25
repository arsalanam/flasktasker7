# db_create.py
import datetime
from datetime import date
from project import db , bcrypt
from project.models import  Task , User,  Sprint

db.create_all()
db.session.commit()

first_user = User(name='Admin' , password= bcrypt.generate_password_hash('Admin123'), email='Admin@admin')


my_sprint = Sprint(name='Semester6')
my_sprint2 = Sprint(name='Semester7')

myTask = Task(name='Test' , due_date= datetime.date(2016, 12, 12) ,status=0,posted_date= datetime.date(2016, 7, 24),   priority=1)
myTask2 = Task(name='Test' , due_date= datetime.date(2016, 12, 12) ,status=1,posted_date= datetime.date(2016, 7, 24),   priority=1)
first_user.tasks.append(myTask)
first_user.tasks.append(myTask2)

my_sprint.tasks.append(myTask)
my_sprint.tasks.append(myTask2)

db.session.add(first_user )
db.session.add(my_sprint)
db.session.add(my_sprint2)
db.session.add(myTask)
db.session.add(myTask2)
# create the database and the db table



# commit the changes
db.session.commit()
