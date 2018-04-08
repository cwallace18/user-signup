from flask import Flask, request, redirect, render_template
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('signup_form.html')
    return template.render()

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

    if not username:
        username_error = 'Enter a username'
    if not password:
        password_error = 'Enter a password'
    if not verify_password:
        verify_error = 'Retype your password'

    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = 'Please enter a valid username'
    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'Please enter a valid password'
        password = ''
    if password != verify_password:
        verify_error = 'Password does not must match'
        verfiy_password = ''
    if email != '': 
        if email.count('.') != 1 or email.count('@') != 1:
            email_error = 'Invalid email'
    
    if not username_error and not password_error and not verify_error:
        return redirect("/welcome?username={0}".format(username))
    else:
        template = jinja_env.get_template('signup_form.html')
        return template.render(username_error=username_error, password_error=password_error,
        verify_error=verify_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    template = jinja_env.get_template('welcome.html')
    return template.render(username=username)
app.run()
    

