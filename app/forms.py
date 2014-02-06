from flask.ext.wtf import Form
from wtforms import TextField, DecimalField
from wtforms.validators import Required

class EntryForm(Form):
    entry = TextField('entry', validators = [Required()]
    value = DecimalField('value', validators = [Required()}

