from flask import Flask, jsonify
from flask_cors import CORS
from logic import format_number

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/format/<value>', methods=['GET'])
def format_call(value):
    return jsonify(format_number(value))

if __name__ == '__main__':
    app.run()