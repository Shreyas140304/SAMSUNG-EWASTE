from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from config import db
from models import Device
from forms import DeviceForm

device_bp = Blueprint('device_bp', __name__)

@device_bp.route('/register-device', methods=['GET', 'POST'])
def register_device():
    form = DeviceForm()

    if form.validate_on_submit():
        new_device = Device(
            SerialNumber=form.serial_number.data,
            DeviceType=form.device_type.data,
            Brand=form.brand.data,
            Model=form.model.data,
            ManufactureDate=form.manufacture_date.data,
            ReceivedDate=form.received_date.data
        )
        db.session.add(new_device)
        db.session.commit()

        return redirect(url_for('device_bp.success'))

    return render_template('register_device.html', form=form)

@device_bp.route('/success')
def success():
    return "Device Registered Successfully!"