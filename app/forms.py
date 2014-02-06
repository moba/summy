from flask.ext.wtf import Form
from wtforms import TextField, DecimalField, HiddenField
from wtforms.validators import Required

class ProjectForm(Form):
    name = TextField('name', validators = [Required()])

class EntryForm(Form):
    name = TextField('name', validators = [Required()])
    value = DecimalField('value', validators = [Required()])
    project_id = HiddenField('project_id', validators = [Required()])
