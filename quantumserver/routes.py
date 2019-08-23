from quantumserver import app, db, bcrypt
from quantumserver.forms import RegistrationForm, LoginForm
from quantumserver.models import User
from flask import render_template, flash, redirect, url_for
from quantumserver.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user
import time
'''
@app.route("/")
def dbcreate():
    db.create_all()
    #return render_template("intro.html")
'''



@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('intro'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        db.session.close()
        flash(f'Registration complete for {form.username.data}!','success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/", methods=['GET','POST'])
@app.route("/login", methods=['GET','POST'])
def login():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('intro'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('intro'))
        else:
            flash(f'Unsuccessful Login!. Check email and password','danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/net")
def net():
    return render_template('net.html')
    #return "hello net"

@app.route("/ai")
def ai():
    return render_template('ai.html')

@app.route("/material")
def material():
    return render_template('material.html')


@app.route("/tutorial")
def tutorial():
    return render_template('tutorial.html')

@app.route("/compute")
def compute():
    return render_template('compute.html')

@app.route("/tools")
def tools():
    return render_template('tools.html')

@app.route("/teleport")
def teleport():
    return render_template('teleport.html')

@app.route("/iot")
def iot():
    return render_template('iot.html')

@app.route("/crypto")
def crypto():
    return render_template('crypto.html')

#@app.route("/")
@app.route("/intro")
def intro():
    return render_template("intro.html")
