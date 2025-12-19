from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp

class DeviceForm(FlaskForm):
    serial_number = StringField("Serial Number", validators=[DataRequired()])
    device_type = StringField("Device Type", validators=[DataRequired()])
    brand = StringField("Brand", default="Samsung")
    model = StringField("Model", validators=[DataRequired()])
    device_condition = SelectField(
        "Device Condition",
        choices=[('', 'Select Condition'), 
                 ('Working','Working'), 
                 ('Partially Working','Partially Working'), 
                 ('Not Working','Not Working')],
        validators=[DataRequired()]
    )
    center = SelectField(
        "Select Nearby Samsung E‑Waste Center",
        choices=[('', 'Select Center'),
                 ('Andheri','Samsung Service Center – Andheri'),
                 ('Bandra','Samsung E‑Waste Hub – Bandra'),
                 ('Navi Mumbai','Samsung Authorized Center – Navi Mumbai')],
        validators=[DataRequired()]
    )
    manufacture_date = DateField("Manufacture Date", validators=[DataRequired()])
    received_date = DateField("Received Date")
    notes = TextAreaField("Additional Notes")
    submit = SubmitField("Register Device")