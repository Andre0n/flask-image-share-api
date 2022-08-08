from flask import Blueprint, jsonify
from api.routes.user import user_bp

api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(user_bp)


@api_bp.route("/")
def index():
    response_model = {
        "routes": {
            "/api": "Api usage Reference",
            "/user": "User control api  (Create, Read, Update, Delete)"
        },
    }

    return jsonify(response_model), 200
