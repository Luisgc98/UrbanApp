from app import db
from flask_login import UserMixin

class UserRole(db.Model):
    __tablename__ = 'user_role_tat'
    role_id_tat = db.Column(db.Integer, primary_key=True)
    role_tat = db.Column(db.String(length=5))

class User(db.Model, UserMixin):
    __tablename__ = 'user_tat'
    id = db.Column(db.Integer, primary_key=True)
    user_name_tat = db.Column(db.String(length=200), unique=True)
    user_first_name_tat = db.Column(db.String(length=100))
    user_last_name_tat = db.Column(db.String(length=100))
    user_email_tat = db.Column(db.String(length=200))
    user_password_tat = db.Column(db.String(length=200))
    user_role_id = db.Column(db.Integer, db.ForeignKey('user_role_tat.role_id_tat'))

    @staticmethod
    def byID(user_id, all=False):
        if all:
            return User.query.all()
        else:
            return User.query.filter_by(id=user_id).first()

    @staticmethod
    def byUserName(user_name):
        return User.query.filter_by(user_name_tat=user_name).first()

    @staticmethod
    def byEmail(email):
        return User.query.filter_by(user_email_tat=email).first()

    def Add(self, user):
        try:
            db.session.add(user)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return 'Error: No se pudo agregar el usuario, vuelva a intentar'