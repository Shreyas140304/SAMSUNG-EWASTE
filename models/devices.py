from config import db

class Device(db.Model):
    __tablename__ = 'Devices'

    DeviceID = db.Column(db.Integer, primary_key=True)
    SerialNumber = db.Column(db.String(255))
    DeviceType = db.Column(db.String(100))
    Brand = db.Column(db.String(100))
    Model = db.Column(db.String(100))
    ManufactureDate = db.Column(db.Date)
    CollectionPointID = db.Column(db.Integer, db.ForeignKey('CollectionPoints.CollectionPointID'))
    StatusID = db.Column(db.Integer, db.ForeignKey('DeviceStatus.StatusID'))
    ReceivedDate = db.Column(db.Date)

    sorting_results = db.relationship('SortingResult', backref='device', lazy=True)
    refurbishment_jobs = db.relationship('RefurbishmentJob', backref='device', lazy=True)
    parts = db.relationship('Part', backref='device', lazy=True)
    dismantling_logs = db.relationship('DismantlingLog', backref='device', lazy=True)
    material_recovery_logs = db.relationship('MaterialRecoveryLog', backref='device', lazy=True)
    disposal_records = db.relationship('DisposalRecord', backref='device', lazy=True)