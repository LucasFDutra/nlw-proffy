from flask import Flask, request, jsonify
from dotenv import load_dotenv
from src.controllers.classes_controller import Classes
from src.controllers.connections_controller import ConnectionsController
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

classes = Classes()
connections = ConnectionsController()


@app.route('/classes', methods=['GET', 'POST'])
def classes_route():
    if (request.method == 'POST'):
        return classes.create(request)
    elif (request.method == 'GET'):
        return classes.index(request)


@app.route('/connections', methods=['GET', 'POST'])
def connections_route():
    if (request.method == 'POST'):
        return connections.create(request)
    elif (request.method == 'GET'):
        return connections.index(request)


if __name__ == "__main__":
    os.environ['FLASK_ENV'] = "development"
    app.run()
