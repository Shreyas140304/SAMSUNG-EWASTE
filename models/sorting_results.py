from config import db

class SortingResult(db.Model):
    __tablename__ = 'SortingResults'

    SortingID = db.Column(db.Integer, primary_key=True)
    DeviceID = db.Column(db.Integer, db.ForeignKey('Devices.DeviceID'))
    SortingDate = db.Column(db.Date)
    Category = db.Column(db.String(100))
    SortedBy = db.Column(db.String(255))
    Remarks = db.Column(db.Text)