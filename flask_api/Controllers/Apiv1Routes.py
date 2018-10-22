from http import HTTPStatus
from flask import Blueprint, render_template, request, jsonify
from sqlalchemy.exc import IntegrityError, DBAPIError
from ..Models.Database import db
from ..Models.User import User, UserSchema

bp = Blueprint('api_v1', __name__)
user_schema = UserSchema()

@bp.route('/')
def root():
    return render_template('index.html')

@bp.route('/user', methods=['POST'])
def user_add():
    request_body = request.get_json()
    if not all(request_body.values()):
        return jsonify(sucess=False,
                    message="All fields are required",
                    status=HTTPStatus.BAD_REQUEST.value,
                    detial=HTTPStatus.BAD_REQUEST.description
                    ), HTTPStatus.BAD_REQUEST

    user = User(username=request_body['username'], email=request_body['email'])
    user.password = bytes(request_body['password'], 'utf-8')

    db.session.add(user)
    try:
        db.session.commit() 
    except IntegrityError as err:
        return jsonify(sucess=False,
                    message=str(err.orig),
                    status=HTTPStatus.BAD_REQUEST.value,
                    detatil=HTTPStatus.BAD_REQUEST.description,
                    ), HTTPStatus.BAD_REQUEST

    return user_schema.jsonify(user), HTTPStatus.CREATED

@bp.route('/user/<int:id>', methods=['PUT'])
def mod_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify(success=False,
                message='User not found',
                status=HTTPStatus.NOT_FOUND.value,
                detail=HTTPStatus.NOT_FOUND.description,
                ), HTTPStatus.NOT_FOUND

    old = user.username

    request_body = request.get_json()
    if not any(request_body.values()):
        return jsonify(success=True, message='Nothing to update')

    # TODO: Maybe need refactoring
    if request_body['username']:
        user.username = request_body['username']

    if request_body['email']:
        user.email = request_body['email']

    if request_body['password']:
        user.password = request_body['password']

    db.session.commit()

    return jsonify(sucess=True, message=f'User {old} updated')

@bp.route('/user/', defaults={'id': None}, methods=['GET'])
@bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    if id is None:
        users = User.query.all()
        return user_schema.jsonify(users, many=True)
    
    user = User.query.get(id)
    if not user:
        return jsonify(success=False,
                message='User not found',
                status=HTTPStatus.NOT_FOUND.value,
                detail=HTTPStatus.NOT_FOUND.description,
                ), HTTPStatus.NOT_FOUND


    return user_schema.jsonify(user)

@bp.route('/user/<int:id>', methods=['DELETE'])
def del_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify(success=False,
                message='User not found',
                status=HTTPStatus.NOT_FOUND.value,
                detail=HTTPStatus.NOT_FOUND.description,
                ), HTTPStatus.NOT_FOUND

    db.session.delete(user)
    db.session.commit()
    return jsonify(success=True, message=f'User {user.username} deleted')

