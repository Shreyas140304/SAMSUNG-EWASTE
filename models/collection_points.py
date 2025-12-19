from config import db

class CollectionPoint(db.Model):
    __tablename__ = 'CollectionPoints'

    CollectionPointID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Location = db.Column(db.String(255), nullable=False)
    ManagerName = db.Column(db.String(255), nullable=False)
    ContactNumber = db.Column(db.String(50), nullable=False)
    Capacity = db.Column(db.Integer, nullable=False)