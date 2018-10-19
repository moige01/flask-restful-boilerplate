from flask import Blueprint, jsonify

bp = Blueprint('error_routes', __name__)

@bp.app_errorhandler(404)
def error404(e):
  return jsonify(message="404 NOT FOUND", code=404)


@bp.app_errorhandler(505)
def error505(e):
    return jsonify(message="505 HTTP VERSION NOT SUPPORTED", code=505)

