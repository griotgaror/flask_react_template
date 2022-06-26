from flask import Flask, render_template
import json

def create_app():
    app = Flask(__name__)
    app.template_folder = '../client/build'
    app.static_folder = '../client/build/static'
    
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'this_is_a_secret_key'

    host = '0.0.0.0'
    port = 5050

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')

    return app.run(host, port)
