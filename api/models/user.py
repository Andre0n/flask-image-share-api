from database import db
from datetime import datetime, timezone
from sqlalchemy import Integer, String, DateTime
from werkzeug.security import generate_password_hash

Column = db.Column
Model = db.Model


class UserModel(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    username = Column(String(80), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    register_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)

    def __init__(self, first_name, last_name, username, email, password) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    @staticmethod
    def get_row_by_id(id):
        return UserModel.query.filter(UserModel.id == id).first()

    @staticmethod
    def query_by_id(id):
        return UserModel.query.filter(UserModel.id == id)

    def __repr__(self) -> str:
        return f"<User(fullname='{self.first_name + ' ' + self.last_name}', username='{self.username}')>"
