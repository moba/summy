from flask.ext.wtf import Form
from wtforms import TextField, DecimalField
from wtforms.validators import Required

class ProjectForm(Form):
    name = TextField('name', validators = [Required()])

class EntryForm(Form):
    name = TextField('name', validators = [Required()])
    value = DecimalField('value', validators = [Required()])
