import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

app = Flask(__name__)
# setup_db(app)
CORS(app)

# Define a route and a view function
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

