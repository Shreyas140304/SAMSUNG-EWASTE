from flask import Blueprint, request, jsonify
from config import db
from models import DismantlingLog, MaterialRecoveryLog, DisposalRecord

lifecycle_bp = Blueprint('lifecycle_bp', __name__)

# -----------------------------
# Dismantling Log
# -----------------------------
@lifecycle_bp.route('/dismantle', methods=['POST'])
def log_dismantle():
    data = request.json
    log = DismantlingLog(**data)
    db.session.add(log)
    db.session.commit()
    return jsonify({'message': 'Dismantling logged successfully'}), 201

# -----------------------------
# Material Recovery Log
# -----------------------------
@lifecycle_bp.route('/recover', methods=['POST'])
def log_recovery():
    data = request.json
    recovery = MaterialRecoveryLog(**data)
    db.session.add(recovery)
    db.session.commit()
    return jsonify({'message': 'Material recovery logged successfully'}), 201

# -----------------------------
# Disposal Record
# -----------------------------
@lifecycle_bp.route('/dispose', methods=['POST'])
def log_disposal():
    data = request.json
    disposal = DisposalRecord(**data)
    db.session.add(disposal)
    db.session.commit()
    return jsonify({'message': 'Disposal record logged successfully'}), 201