from datetime import datetime

import peewee

from app.v1.utils.db import db
from .user_model import User


class Todo(peewee.Model):
    """ToDo Model

    Args:
        peewee (class): Peewee Model
    """
    title = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.now)
    is_done = peewee.BooleanField(default=False)
    user = peewee.ForeignKeyField(User, backref="todos")

    class Meta:
        database = db
