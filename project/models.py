# project/models.py


from project import db


class Task(db.Model):

    import datetime

    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    posted_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprints.id'))

    def __init__(self, name = None, due_date= None, priority = None, posted_date = None, status =None, user_id = None , sprint_id = None):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.posted_date = posted_date
        self.status = status
        self.user_id = user_id
        self.sprint_id = sprint_id


    def __repr__(self):
        return '<name %r>' % (self.name)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    tasks = db.relationship('Task', backref='poster')
    role = db.Column(db.String, default='user')

    def __init__(self, name=None, email=None, password=None, role=None):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % (self.name)


class Sprint(db.Model):

    __tablename__ = 'sprints'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    tasks = db.relationship('Task', backref='current_sprint')
    def __init__(self, name =None ):
        self.name = name

    def __repr__(self):
        return '<Sprint {0} >'.format(self.name)

    @staticmethod
    def get_sprints():
        retval = []
        sprints = db.session.query(Sprint).all()
        index = 0
        for sprint in sprints:
            row = (str(sprint.id), sprint.name)
            retval.append(row)
        return tuple(retval)