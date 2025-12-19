from flask import Blueprint, request, jsonify,redirect,render_template,url_for
from config import db
from models import CollectionEvent,CollectionPoint

collection_bp = Blueprint('collection_bp', __name__)

@collection_bp.route('/collection-events', methods=['GET'])
def show_collection_events():
    events = CollectionEvent.query.all()
    return render_template('collection.html', events=events)

@collection_bp.route('/events', methods=['POST','GET'])
def add_event():
    data = request.form

    new_event = CollectionEvent(
        CollectionPointID=data.get('collection_point_id'),
        EventDate=data.get('event_date'),
        CollectedBy=data.get('collected_by'),
        DeviceCount=data.get('device_count'),
        Notes=data.get('notes')
    )

    db.session.add(new_event)
    db.session.commit()

    return redirect(url_for('collection_bp.show_collection_events'))

@collection_bp.route('/collection-points', methods=['GET'])
def show_collection_points():
    points = CollectionPoint.query.all()
    return render_template('collectionPoints.html', collection_points=points)

@collection_bp.route('/collection-points', methods=['POST'])
def add_collection_point():
    data = request.form

    new_point = CollectionPoint(
        Name=data.get('name'),
        Location=data.get('location'),
        ManagerName=data.get('manager_name'),
        ContactNumber=data.get('contact'),
        Capacity=data.get('capacity')
    )

    db.session.add(new_point)
    db.session.commit()

    return redirect(url_for('collection_bp.show_collection_points'))