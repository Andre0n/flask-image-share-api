from sys import prefix
from flask import Blueprint
from api.controllers.user import UserApi, UsersApi

user_bp = Blueprint('user', __name__, url_prefix='/user')

user_bp.add_url_rule("/<int:id>", view_func=UserApi.as_view("user"))
user_bp.add_url_rule("/", view_func=UsersApi.as_view("users"))
