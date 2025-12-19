from config import db

class Part(db.Model):
    __tablename__ = 'PartsInventory'

    PartID = db.Column(db.Integer, primary_key=True)
    PartName = db.Column(db.String(255))
    PartType = db.Column(db.String(100))
    Condition = db.Column(db.String(100))
    Quantity = db.Column(db.Integer)
    Location = db.Column(db.String(255))
    DeviceID = db.Column(db.Integer, db.ForeignKey('Devices.DeviceID'))