from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True, unique = True)
    entries = db.relationship('Entry', backref='project', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.Float)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __init__(self, name, value, project_id):
        self.name = name
        self.value = value
        self.project_id = project_id

    def __repr__(self):
        return self.name + "+" + str(self.value)
