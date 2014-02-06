from flask import render_template, request, redirect, url_for
from app import app, db
from forms import EntryForm
from models import Project, Entry

@app.route('/')
def index():
    projects = Project.query.all()
#    return str(len(projects))
#    projects = [ Project('bla'), Project('blupp') ]
    return render_template("index.html",
            title = 'Index',
            projects = projects)

@app.route('/addproject', methods=['POST'])
def add_project():
    project = Project(request.form['project'])
    db.session.add(project)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/<name>')
def view_project(name):
    project = Project.query.filter_by(name=name).first()
    return project.name
