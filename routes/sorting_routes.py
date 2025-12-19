from flask import Blueprint, render_template, request, redirect, url_for, flash
from config import db
from models import Device, SortingResult
from datetime import datetime

sorting_bp = Blueprint('sorting_bp', __name__)

@sorting_bp.route('/sorting', methods=['GET'])
def show_sorting_page():
    devices = Device.query.all()
    return render_template('sorting.html', devices=devices)

@sorting_bp.route('/sorting/save', methods=['POST'])
def save_sorting():
    device_id = request.form.get('device_id')
    sorting_date = request.form.get('sorting_date')
    sorted_by = request.form.get('sorted_by')
    category = request.form.get('category')
    remarks = request.form.get('remarks')

    new_sorting = SortingResult(
        DeviceID=device_id,
        SortingDate=datetime.strptime(sorting_date, '%Y-%m-%d'),
        SortedBy=sorted_by,
        Category=category,
        Remarks=remarks
    )

    db.session.add(new_sorting)
    db.session.commit()

    flash("Sorting data saved successfully!", "success")
    return redirect(url_for('sorting_bp.show_sorting_page'))