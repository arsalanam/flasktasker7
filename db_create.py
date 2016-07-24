# db_create.py
import datetime
from datetime import date
from project import db
from project.models import  Task , User,  Sprint

first_user = User(name='Admin' , password='Admin123', email='Admin@admin')


my_sprint = Sprint(name='Semester6')

myTask = Task(name='Test' , due_date= datetime.date(2008, 6, 24) ,status=10,posted_date= datetime.date(2008, 6, 24),   priority=1)
first_user.tasks.append(myTask)
my_sprint.tasks.append(myTask)

db.session.add(first_user )
db.session.add(my_sprint)
db.session.add(myTask)

# create the database and the db table
db.create_all()


# commit the changes
db.session.commit()
