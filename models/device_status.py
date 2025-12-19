from config import db

class DeviceStatus(db.Model):
    __tablename__ = 'DeviceStatus'

    StatusID = db.Column(db.Integer, primary_key=True)
    StatusName = db.Column(db.String(100), nullable=False)