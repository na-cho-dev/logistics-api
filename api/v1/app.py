from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv
from models import storage
from api.v1.auth.auth import auth
from api.v1.views import views

PORT = getenv('PORT')
load_dotenv()

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(views)


@app.teardown_appcontext
def close_db(error):
    """
    Close Storage
    """
    storage.close()


@app.errorhandler(403)
def forbidden(error):
    """
    404 Error

    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'Error': "Forbidden"}), 403)


@app.errorhandler(404)
def not_found(error):
    """
    404 Error

    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'Error': "Not Found"}), 404)


@app.route('/', methods=['GET'])
def home():
    """
    Home Route
    """
    return jsonify({"Hello": "World!"})


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
