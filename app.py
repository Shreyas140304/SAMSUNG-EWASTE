from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from config import Config, db
from flask_wtf.csrf import CSRFProtect
from datetime import date, datetime

from models import (
    Device,
    CollectionEvent,
    CollectionPoint,
    SortingResult,
    RefurbishmentJob,
    DismantlingLog,
    MaterialRecoveryLog,
    DisposalRecord,
)
from forms import DeviceForm

app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)

# Initialize DB with the app
db.init_app(app)


# -------------------------
# HOME / LANDING
# -------------------------
@app.route("/")
def home():
    return render_template("base.html")


# -------------------------
# ADMIN AUTH + DASHBOARD
# -------------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


@app.route("/admin/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect(url_for("dashboard"))

        flash("Invalid username or password", "error")

    return render_template("login.html")


@app.route("/admin/dashboard")
def dashboard():
    return render_template("adminDashboard.html")


@app.route("/admin/reset-password", methods=["POST"])
def reset_password():
    username = request.form.get("resetUsername")
    new_password = request.form.get("newPassword")
    confirm_password = request.form.get("confirmPassword")

    if new_password != confirm_password:
        flash("Passwords do not match", "error")
        return redirect(url_for("login"))

    # Password reset persistence would go here in a real app
    flash("Password updated successfully", "success")
    return redirect(url_for("login"))


@app.route("/register-device", methods=["GET", "POST"])
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
            Notes=form.notes.data,
        )

        db.session.add(new_device)
        db.session.commit()

        flash("Device registered successfully!", "success")
        return redirect(url_for("register_device"))

    return render_template("register.html", form=form)


# -------------------------
# COLLECTION EVENTS + POINTS
# -------------------------
@app.route("/collection-events", methods=["GET"])
def show_collection_events():
    events = CollectionEvent.query.all()
    return render_template("collection.html", events=events)


@app.route("/events", methods=["POST", "GET"])
def add_event():
    data = request.form

    new_event = CollectionEvent(
        CollectionPointID=data.get("collection_point_id"),
        EventDate=data.get("event_date"),
        CollectedBy=data.get("collected_by"),
        DeviceCount=data.get("device_count"),
        Notes=data.get("notes"),
    )

    db.session.add(new_event)
    db.session.commit()

    return redirect(url_for("show_collection_events"))


@app.route("/collection-points", methods=["GET"])
def show_collection_points():
    points = CollectionPoint.query.all()
    return render_template("collectionPoints.html", collection_points=points)


@app.route("/collection-points", methods=["POST"])
def add_collection_point():
    data = request.form

    new_point = CollectionPoint(
        Name=data.get("name"),
        Location=data.get("location"),
        ManagerName=data.get("manager_name"),
        ContactNumber=data.get("contact"),
        Capacity=data.get("capacity"),
    )

    db.session.add(new_point)
    db.session.commit()

    return redirect(url_for("show_collection_points"))


# -------------------------
# SORTING / INSPECTION
# -------------------------
@app.route("/sorting", methods=["GET"])
def show_sorting_page():
    devices = Device.query.all()
    return render_template("sorting.html", devices=devices)


@app.route("/sorting/save", methods=["POST"])
def save_sorting():
    device_id = request.form.get("device_id")
    sorting_date = request.form.get("sorting_date")
    sorted_by = request.form.get("sorted_by")
    category = request.form.get("category")
    remarks = request.form.get("remarks")

    new_sorting = SortingResult(
        DeviceID=device_id,
        SortingDate=datetime.strptime(sorting_date, "%Y-%m-%d"),
        SortedBy=sorted_by,
        Category=category,
        Remarks=remarks,
    )

    db.session.add(new_sorting)
    db.session.commit()

    flash("Sorting data saved successfully!", "success")
    return redirect(url_for("show_sorting_page"))


# -------------------------
# REFURBISHMENT JOBS
# -------------------------
@app.route("/refurbishment", methods=["GET"])
def show_jobs():
    jobs = RefurbishmentJob.query.all()
    return render_template("refurbishment.html", jobs=jobs)


@app.route("/refurbishment", methods=["POST"])
def add_job():
    data = request.form

    new_job = RefurbishmentJob(
        DeviceID=data.get("deviceId"),
        StartDate=data.get("startDate"),
        EndDate=data.get("endDate"),
        TechnicianID=data.get("technicianId"),
        JobStatus=data.get("jobStatus"),
        Notes=data.get("notes"),
    )

    db.session.add(new_job)
    db.session.commit()

    return redirect(url_for("show_jobs"))


# -------------------------
# LIFECYCLE API (JSON)
# -------------------------
@app.route("/dismantle", methods=["POST"])
def log_dismantle():
    data = request.json or {}
    log = DismantlingLog(**data)
    db.session.add(log)
    db.session.commit()
    return jsonify({"message": "Dismantling logged successfully"}), 201


@app.route("/recover", methods=["POST"])
def log_recovery():
    data = request.json or {}
    recovery = MaterialRecoveryLog(**data)
    db.session.add(recovery)
    db.session.commit()
    return jsonify({"message": "Material recovery logged successfully"}), 201


@app.route("/dispose", methods=["POST"])
def log_disposal():
    data = request.json or {}
    disposal = DisposalRecord(**data)
    db.session.add(disposal)
    db.session.commit()
    return jsonify({"message": "Disposal record logged successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)