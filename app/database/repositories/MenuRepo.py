from database.models.Menu import Menu
from database.db import db

class MenuRepo:

    @staticmethod
    def save(**kwargs):
        menu = Menu(**kwargs)
        db.session.add(menu)
        db.session.commit()
        return menu.toJson()

    @staticmethod
    def findAll():
        data = db.session.query(Menu).all()
        menus = []
        for i in range (len(data)):
            menus.append(data[i].toJson())
        return menus

    @staticmethod
    def findMenuById(menuId):
        data = db.session.query(Menu).filter(Menu.id==menuId).all()
        if len(data)==0:
            return []
        return [data[0].toJson()]

