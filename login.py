from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,redirect
)

import time
from homepage import Homepage
from logging import FileHandler, WARNING    



class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='ODE', password='ode2020'))

server = Flask(__name__)



app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

if not app.debug:
    file_handler = FileHandler('errorlog.txt')
    file_handler.setLevel(WARNING)
    app.logger.addHandler(file_handler)




@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        if session['user_id']==None and request.endpoint != 'login':
            return redirect(url_for('login'))
        user = [x for x in users if x.id == session['user_id']]
        if user != []:
        	g.user = user[0]
    else:
        if request.endpoint == '/app1/_dash-update-component':
            return '404'


@app.route('/login', methods=['GET', 'POST'])
def login():
    session['user_id']=None
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        user = [x for x in users if x.username == username]
        if user != []:
        	user = user[0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('/app1/'))

        return redirect(url_for('login'))

    return render_template('login.html')



@app.route('/app1/')
def app1():
    if not g.user:
        return redirect(url_for('login'))
    #time.sleep(3)
    print('vamo ver2')
    return redirect(url_for('/app1/_dash-update-component'))



@app.route('/')
def inicio():
    print('vamover3',flush=True)
    return redirect(url_for('login'))


if __name__ == '__main__':
	server.run(port=1019)




