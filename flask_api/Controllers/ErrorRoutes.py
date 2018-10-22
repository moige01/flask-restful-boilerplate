from http import HTTPStatus
from flask import Blueprint, jsonify

bp = Blueprint('error_routes', __name__)

@bp.app_errorhandler(404)
def error404(e):
    return jsonify(detail=HTTPStatus.NOT_FOUND.phrase,
            code=HTTPStatus.NOT_FOUND.value,
            message="Oops! Wrong way."
            )

