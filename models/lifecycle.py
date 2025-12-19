from config import db

class DismantlingLog(db.Model):
    __tablename__ = 'DismantlingLogs'

    LogID = db.Column(db.Integer, primary_key=True)
    DeviceID = db.Column(db.Integer, db.ForeignKey('Devices.DeviceID'))
    DismantleDate = db.Column(db.Date)
    TechnicianID = db.Column(db.String(255))
    RecoveredPartsCount = db.Column(db.Integer)
    HazardousMaterialFlag = db.Column(db.Boolean)
    Notes = db.Column(db.Text)

class MaterialRecoveryLog(db.Model):
    __tablename__ = 'MaterialRecoveryLogs'

    RecoveryID = db.Column(db.Integer, primary_key=True)
    DeviceID = db.Column(db.Integer, db.ForeignKey('Devices.DeviceID'))
    MaterialType = db.Column(db.String(100))
    Quantity = db.Column(db.Numeric(10, 3))
    RecoveryDate = db.Column(db.Date)
    RecoveredBy = db.Column(db.String(255))
    Destination = db.Column(db.String(255))

class DisposalRecord(db.Model):
    __tablename__ = 'DisposalRecords'

    DisposalID = db.Column(db.Integer, primary_key=True)
    DeviceID = db.Column(db.Integer, db.ForeignKey('Devices.DeviceID'))
    DisposalDate = db.Column(db.Date)
    Method = db.Column(db.String(100))
    DisposedBy = db.Column(db.String(255))
    ComplianceCertificate = db.Column(db.Boolean)
    Notes = db.Column(db.Text)