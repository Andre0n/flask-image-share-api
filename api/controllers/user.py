from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from flask import jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import BadRequest
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema
from database import db


class UserApi(MethodView):
    init_every_request = False

    def get(self, id):
        user = UserModel.get_row_by_id(id)
        if not user:
            return jsonify({"message": "User not found!"}), 404
        return user_schema.jsonify(user), 302

    def put(self, id):
        try:
            json_data = request.get_json(force=True)
            if not json_data:
                raise BadRequest
            query = UserModel.query_by_id(id)
            query.update(json_data)
            db.session.commit()
        except BadRequest:
            return jsonify({"message": "Input data can't be loaded!"}), 400
        except IntegrityError:
            user = query.first()

            provided_email = json_data["email"] if "email" in json_data.keys() else None
            provided_username = json_data["username"] if "username" in json_data.keys() else None
            db.session.rollback()

            if UserModel.query.filter((UserModel.id != user.id) & (UserModel.email == provided_email)).first():
                return jsonify({"message": f"email {provided_email} alredy in use"}), 409
            return jsonify({"message": f"username {provided_username} alredy in use"}), 409

        return user_schema.jsonify(query.first()), 201

    def delete(self, id):
        user = UserModel.query_by_id(id)
        if not user.first():
            return jsonify({"message": "User not found!"}), 404
        user.delete()
        db.session.commit()
        return jsonify({}), 200


class UsersApi(MethodView):
    init_every_request = False

    def get(self):
        all_users = UserModel.query.all()
        response_model = {
            'users': users_schema.dump(all_users)
        }
        return jsonify(response_model), 200

    def post(self):
        try:
            json_data = request.get_json(force=True)
            if not json_data:
                raise BadRequest
            user = user_schema.load(json_data)
            db.session.add(user)
            db.session.commit()
        except ValidationError as e:
            return jsonify(e.messages), 400
        except BadRequest:
            return jsonify({"message": "Input data can't be loaded!"}), 400
        except IntegrityError:
            db.session.rollback()
            if UserModel.query.filter(UserModel.email == user.email).first():
                return jsonify({"message": f"email {user.email} alredy in use"}), 409
            return jsonify({"message": f"username {user.username} alredy in use"}), 409

        return user_schema.jsonify(user), 201
