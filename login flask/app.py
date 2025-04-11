from flask import Flask, request, jsonify, session, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ajinkya%402025@localhost/aeroed'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if not name or not email or not password:
            return jsonify({"status": "error", "message": "Missing fields!"}), 400
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"status": "error", "message": "Email already registered!"}), 409
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['user_email'] = user.email  # Store email for profile
            return redirect(url_for('home'))
        else:
            return jsonify({"status": "error", "message": "Invalid email or password"}), 401
    return render_template('login.html')

@app.route('/')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_email', None)
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    if 'user_id' in session:
        return render_template('profile.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5005)