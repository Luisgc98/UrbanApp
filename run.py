from app import create_app, login_manager
from flask import redirect, url_for
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.byID(user_id)

app = create_app()

@app.route('/')
def index():

    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)