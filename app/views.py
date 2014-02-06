from flask import render_template
from flask import request
from flask import redirect, url_for
from app import app

projects = [ 'sample', 'doing', 'naaga' ]

@app.route('/')
def index():
    return render_template("index.html",
            title = 'Index',
            projects = projects)

@app.route('/addproject', methods=['POST'])
def add_project():
    projects.append(request.form['project'])
    return redirect(url_for('index'))

@app.route('/project/<project>')
def view_project(project):
    return "Oi: " + project
