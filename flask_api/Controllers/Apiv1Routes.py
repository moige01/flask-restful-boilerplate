from flask import Blueprint, render_template, request, jsonify
from ..Models.Database import db
from ..Models.User import User, UserSchema

bp = Blueprint('api_v1', __name__)
user_schema = UserSchema()

@bp.route('/')
def root():
    return render_template('index.html')

@bp.route('/user', methods=['POST'])
def user_add():
    user = User(username=request.args.get('username'), email=request.args.get('email'))
    user.password = bytes(request.args.get('password'), 'utf-8')
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)

@bp.route('/user/', defaults={'id': None}, methods=['GET'])
@bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    if id is None:
        users = User.query.all()
        return user_schema.jsonify(users, many=True)
    
    user = User.query.get(id)
    if not user:
        return jsonify(success=False, message='User not found'), 404

    return user_schema.jsonify(user)

@bp.route('/user/<int:id>', methods=['DELETE'])
def del_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify(success=False, message='User not found'), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify(success=True, message=f'User {user.username} deleted')

@bp.route('/user/<int:id>', methods=['PUT'])
def mod_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify(success=False, message='User not found'), 404

    username = request.args.get('username', None)
    email = request.args.get('email', None)
    password = request.args.get('password', None)

    if not any([username, email, password]):
        return jsonify(success=True, message='Nothing to update')

    # TODO: Maybe need refactoring
    if username:
        user.username = username

    if email:
        user.email = email

    if password:
        user.password = password

    db.session.commit()

    return jsonify(sucess=True, message=f'User {user.username} updated')

