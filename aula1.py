from flask import Flask, url_for, render_template, request
from markupsafe import escape
import sqlite3 as db

app = Flask(__name__)



@app.route('/')
def index():
    return 'hello dick'
#as rotas devem ser em "cascata"

#rotas podem receber argumentos, atraves do "< >"
@app.route('/<name>')
def names(name):
    return f'hello {escape(name)}'

@app.route('/post/<int:post_id>')
def post(post_id):
    return f'post {post_id}'

#o conversor path e basicamente uma string que aceita barra
@app.route('/path/<path:subpath>')
def pathsite(subpath):
    return f'Subpath {escape(subpath)}'

# eh possivel criar urls sem usar o decorador, usando o url_for()
#funcao que retorna qual a url daquela funcao especifica
with app.test_request_context():
    print(url_for('index', next='/'))
    print(url_for('post', post_id=2))
    print(url_for('names', name='daniel'))
    print(url_for('pathsite', subpath='cock'))
    print(url_for('static', filename='styles.css'))

# metodos http, só permite algum metodo especifico http

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        #poderia ser uma funcao do_login(), para realizar o login
#        return 'Login feito'
#    else:
#        # poderia ser uma funcao show_login_page()
#        return 'login nao feito'
    
#outra forma de fazer o código acima seria com outro decorador
#@app.get('/login')
#def login_get():
#    return 'loginget feito'

#@app.post('/login')
#def login_post():
#    return 'loginpost feito'

#parei no renderring templates
# https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application

@app.route('/html')
def htmlpage():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        return 'cock'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug='on')