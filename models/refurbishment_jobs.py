from config import db

class RefurbishmentJob(db.Model):
    __tablename__ = 'RefurbishmentJobs'

    JobID = db.Column(db.Integer, primary_key=True)
    DeviceID = db.Column(db.Integer, db.ForeignKey('Devices.DeviceID'))
    StartDate = db.Column(db.Date)
    EndDate = db.Column(db.Date)
    TechnicianID = db.Column(db.String(255))
    JobStatus = db.Column(db.String(100))
    Notes = db.Column(db.Text)