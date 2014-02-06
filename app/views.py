from flask import render_template, request, redirect, url_for
from app import app, db
from forms import ProjectForm, EntryForm
from models import Project, Entry
from wtforms.ext.sqlalchemy.orm import model_form
from sqlalchemy.sql import func

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
    entrysum = db.session.query(func.sum(Entry.value)).filter_by(project_id=project.id).first()[0]
    form = EntryForm(obj=entry)
    return render_template("project.html",
            project = project.name,
            entries = project.entries,
            entrysum = entrysum,
            form = form)

@app.route('/addproject', methods=['POST'])
def add_project():
    form = ProjectForm(request.form)
    if not form.validate():
        return str(form.errors)
    project = Project(form.name.data)
    db.session.add(project)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/<project>/addentry', methods=['POST'])
def add_entry(project):
    form = EntryForm(request.form)
    if not form.validate():
        return str(form.errors)
    name = form.name.data
    value = form.value.data
    project_id = form.project_id.data

    entry = Entry(name, value, project_id)
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for('view_project',name=project))
