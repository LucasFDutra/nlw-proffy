from flask import Flask, request, jsonify
from dotenv import load_dotenv
from routes import route
import os


load_dotenv()

app = Flask(__name__)

route(app)

if __name__ == "__main__":
    os.environ['FLASK_ENV'] = "development"
    app.run()
