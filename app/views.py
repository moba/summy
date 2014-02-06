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

@app.route('/addproject', methods=['POST'])
def add_project():
    project = Project(request.form['name'])
    db.session.add(project)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/<name>')
def view_project(name):
    project = Project.query.filter_by(name=name).first()
    return project.name
