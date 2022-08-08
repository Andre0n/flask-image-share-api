from api.models.user import UserModel
from database import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        ordered = True
        fields = ("id", "first_name", "last_name", "username", "email", "password")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
