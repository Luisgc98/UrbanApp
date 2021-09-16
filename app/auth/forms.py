from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

validators = [DataRequired()]
class LoginForm(FlaskForm):
    user_name = StringField(' ', validators=validators)
    password = PasswordField(' ', validators=validators)
    login = SubmitField('Conectar')

    def validateUser(self):
        user = User.byUserName(self.user_name.data)
        if user is None:
            user = User.byEmail(self.user_name.data)

        if user is not None:
            if check_password_hash(user.user_password_tat, self.password.data):
                return (True, user)
            else: 
                return 'Contraseña incorrecta'
        else:
            return 'Nombre de usuario o Correo incorrecto'
            

class RegisterForm(FlaskForm):
    n_user_name = StringField(' ', validators=validators)
    n_email = StringField(' ', validators=validators)
    n_password = PasswordField(' ', validators=validators)
    repeat_psswd = PasswordField(' ', validators=validators)
    register = SubmitField('Registrar')

    def validateUser(self):
        user = User.byUserName(self.n_user_name.data)
        if user is None:
            user = User.byEmail(self.n_email.data)
        
        if user is not None:
            return 'Usuario ya existente'
        else:
            return True

    def addUser(self):
        new_user = User(
            user_name_tat = self.n_user_name.data.strip(),
            user_email_tat = self.n_email.data.strip(),
            user_password_tat = generate_password_hash(self.n_password.data),
            user_role_id = 1
        )
        return new_user.Add(new_user)