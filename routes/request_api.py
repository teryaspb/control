from flask import Blueprint

REQUEST_API = Blueprint('request_api', __name__)
def get_blueprint():
    return REQUEST_API