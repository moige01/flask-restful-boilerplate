from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property
from .Database import *

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, p):
        self._password = generate_password_hash(p)

    def chck_psswd(self, p):
        return check_password_hash(self._password, p)

    def __repr__(self):
        return f'<Username {self.username}>'


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

