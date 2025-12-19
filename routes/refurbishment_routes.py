from flask import Blueprint, request, jsonify,render_template,url_for,redirect
from config import db
from models import RefurbishmentJob

refurbishment_bp = Blueprint('refurbishment_bp', __name__)

@refurbishment_bp.route('/refurbishment', methods=['GET'])
def show_jobs():
    jobs = RefurbishmentJob.query.all()
    return render_template('refurbishment.html', jobs=jobs)

# Add a new job
@refurbishment_bp.route('/refurbishment', methods=['POST'])
def add_job():
    data = request.form

    new_job = RefurbishmentJob(
        DeviceID=data.get('deviceId'),
        StartDate=data.get('startDate'),
        EndDate=data.get('endDate'),
        TechnicianID=data.get('technicianId'),
        JobStatus=data.get('jobStatus'),
        Notes=data.get('notes')
    )

    db.session.add(new_job)
    db.session.commit()

    return redirect(url_for('refurbishment_bp.show_jobs'))
