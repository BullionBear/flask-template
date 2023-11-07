from flask import Blueprint, jsonify, request
from flasgger import swag_from

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/multiply', methods=['GET'])
@swag_from('specs/multiply_specs.yml', methods=['GET'])
def multiply():
    # Example function for API
    x = request.args.get('x', type=int, default=1)
    y = request.args.get('y', type=int, default=1)
    return jsonify({'result': x * y})