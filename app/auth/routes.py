from flask.helpers import url_for
from werkzeug.utils import redirect
from . import auth
from flask import render_template, request, flash
from .forms import LoginForm, RegisterForm
from flask_login import login_required, logout_user, login_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    register_form = RegisterForm()
    
    if request.method == 'POST':
        request_form = list(request.form)
        if 'login' in request_form:
            validation = login_form.validateUser()
            if validation[0] == True:
                login_user(validation[1])
                flash('Bienvenido '+login_form.user_name.data)
                return redirect(url_for('main.home'))
            else:
                flash(validation)
        elif 'register' in request_form:
            validation = register_form.validateUser()
            if validation == True:
                msg = register_form.addUser()
                if msg == True:
                    flash('Registrado con éxito')
                else:
                    flash(msg)
                return redirect(url_for('auth.login'))
            else:
                flash(validation)
    
    return render_template('auth/login.html',
                                            login_form=login_form,
                                            register_form=register_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))