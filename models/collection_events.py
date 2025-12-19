from config import db

class CollectionEvent(db.Model):
    __tablename__ = 'CollectionEvents'

    EventID = db.Column(db.Integer, primary_key=True)
    CollectionPointID = db.Column(db.Integer, db.ForeignKey('CollectionPoints.CollectionPointID'))
    EventDate = db.Column(db.Date)
    CollectedBy = db.Column(db.String(255))
    DeviceCount = db.Column(db.Integer)
    Notes = db.Column(db.Text)