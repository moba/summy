from flask import render_template, request, redirect, url_for
from app import app, db
from forms import ProjectForm, EntryForm
from models import Project, Entry
from wtforms.ext.sqlalchemy.orm import model_form

@app.route('/')
def index():
    projects = Project.query.all()
    form = ProjectForm()
    return render_template("index.html",
            title = 'Index',
            projects = projects,
            form = form)

@app.route('/<name>')
def view_project(name):
    project = Project.query.filter_by(name=name).first()
    entry = Entry("",10,project.id)
    form = EntryForm(obj=entry)
    return render_template("project.html",
            project = project.name,
            entries = project.entries,
            form = form)

@app.route('/addproject', methods=['POST'])
def add_project():
    project = Project(request.form['name'])
    db.session.add(project)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/<project>/addentry', methods=['POST'])
def add_entry(project):
    name = request.form['name']
    value = request.form['value']
    project_id = request.form['project_id']

    entry = Entry(name, value, project_id)
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for('view_project',name=project))
