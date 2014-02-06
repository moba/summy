from flask.ext.wtf import Form
from wtforms import TextField, DecimalField
from wtforms.validators import Required

class ProjectForm(Form):
    project = TextField('project', validators = [Required()])

class EntryForm(Form):
    entry = TextField('entry', validators = [Required()])
    value = DecimalField('value', validators = [Required()])
