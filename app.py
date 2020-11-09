from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from logic import format_number

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def create_app():
    # sanity check route
    @app.route('/format/<value>', methods=['GET'])
    def format_call(value):
        return jsonify(format_number(value))

    @app.route('/')
    def form():
        return render_template("/form.html")

    @app.route('/', methods=['POST'])
    def form_post():
        text = request.form['text']
        return jsonify(format_number(text))

    return app

if __name__ == '__main__':
    from app import create_app
    myapp = create_app()
    myapp.run()