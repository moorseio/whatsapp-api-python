from database.models.MenuItem import MenuItem
from database.db import db

class MenuItemRepo:

    @staticmethod
    def save(**kwargs):
        menuItem = MenuItem(**kwargs)
        db.session.add(menuItem)
        db.session.commit()
        return menuItem.toJson()

    @staticmethod
    def findAll():
        return db.session.query(MenuItem).all()
    