from flask import Blueprint, render_template, request, redirect, url_for, flash
from config import db
from models import Device
from forms import DeviceForm
from datetime import date

admin_bp = Blueprint('admin', __name__)


# Dummy admin credentials (replace with DB later)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

@admin_bp.route('/')
def home():
    return render_template("base.html")
# -------------------------
# -------------------------
# LOGIN PAGE (GET + POST)
# -------------------------
@admin_bp.route('/admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect(url_for('admin.dashboard'))

        flash("Invalid username or password", "error")

    return render_template("login.html")


# -------------------------
# DASHBOARD PAGE
# -------------------------
@admin_bp.route('/admin/dashboard')
def dashboard():
    return render_template("adminDashboard.html")


# -------------------------
# RESET PASSWORD
# -------------------------
@admin_bp.route('/admin/reset-password', methods=['POST'])
def reset_password():
    username = request.form.get("resetUsername")
    new_password = request.form.get("newPassword")
    confirm_password = request.form.get("confirmPassword")

    if new_password != confirm_password:
        flash("Passwords do not match", "error")
        return redirect(url_for('admin.login'))

   
    flash("Password updated successfully", "success")
    return redirect(url_for('admin.login'))

@admin_bp.route('/register-device', methods=['GET', 'POST'])
def register_device():
    form = DeviceForm()

    if form.validate_on_submit():
        new_device = Device(
            SerialNumber=form.serial_number.data,
            DeviceType=form.device_type.data,
            Brand=form.brand.data,
            Model=form.model.data,
            DeviceCondition=form.device_condition.data,
            Center=form.center.data,
            ManufactureDate=form.manufacture_date.data,
            ReceivedDate=date.today(),
            Notes=form.notes.data
        )

        db.session.add(new_device)
        db.session.commit()

        flash("Device registered successfully!", "success")
        return redirect(url_for('admin.register_device'))

    return render_template("register.html", form=form)

