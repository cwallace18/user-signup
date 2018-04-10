from flask import Flask, request, redirect, render_template
import os
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = 'Please enter a valid username'
        username = ''
    
    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'Please enter a valid password'
        password = ''
    
    if password != verify_password:
        verify_error = 'Password does not match'
        password = ''
    else:
        password = password

    if email != '': 
        if email.count('.') != 1 or email.count('@') != 1 or ' ' in email:
            email_error = 'Invalid email'
            email = ''
    
    if not username_error and not password_error and not verify_error and not email_error:
        return redirect("/welcome?username={0}".format(username))
    else:
        return render_template('signup_form.html', username=username, username_error=username_error, password_error=password_error,
        verify_error=verify_error, email=email, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()
    

