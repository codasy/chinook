from models import *
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired


EmployeesSelect = Employees.select(Employees.first_name, Employees.last_name)
EmployeesCount = Employees.select().count()
lesEmployes = [ 0 for _ in range(EmployeesCount)]
i = 0

for EmployeeSelect in Employees:
    lesEmployes[i] = EmployeeSelect.first_name +' '+ EmployeeSelect.last_name
    i = i+1


class CommandForm(Form):
    employe = SelectField(u'EmployeeField', choices = lesEmployes, validators=[InputRequired()])
    submit = SubmitField('Valider')
