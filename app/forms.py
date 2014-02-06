from flask.ext.wtf import Form
from wtforms import TextField, DecimalField, HiddenField
from wtforms.validators import InputRequired,Required

class ProjectForm(Form):
    name = TextField('name', validators = [Required()])

class EntryForm(Form):
    name = TextField('name', validators = [InputRequired()])
    value = DecimalField('value', validators = [InputRequired()])
    project_id = HiddenField('project_id', validators = [InputRequired()])
