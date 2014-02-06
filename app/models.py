from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    project = db.Column(db.String(120), index = True, unique = True)
    entries = db.relationship('Entry', backref='project', lazy='dynamic')

    def __repr__(self):
        return '<Project %r>' % (self.project)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.Float, db.ForeignKey('project.id'))
