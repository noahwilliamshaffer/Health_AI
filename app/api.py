from flask import Blueprint, request, jsonify
from .models import predict_health_issue

api = Blueprint('api', __name__)

@api.route('/monitor', methods=['POST'])
def monitor_health():
    data = request.json
    prediction = predict_health_issue(data)
    return jsonify({'prediction': prediction})
