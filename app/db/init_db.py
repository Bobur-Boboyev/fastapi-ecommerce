from .session import engine
from .base import Base

from ..models.user import User
from ..models.category import Category
from ..models.product import Product


def create_all():
    Base.metadata.create_all(engine)


def delete_all():
    Base.metadata.drop_all(engine)
