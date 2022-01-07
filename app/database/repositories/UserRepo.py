from database.models.Product import Product
from database.models.User import User
from database.db import db

class UserRepo:

    @staticmethod
    def save(**kwargs):
        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()
        return user.toJson()

    @staticmethod
    def findById(userId):
        data = db.session.query(User).filter(User.id==userId).all()
        if len(data) == 0:
            return []
        return data[0].toJson()

    @staticmethod
    def findByNumber(userNumber):
        data = db.session.query(User).filter(User.number==userNumber).all()
        if len(data) == 0:
            return []
        exit = []
        for i in range(len(data)):
            exit.append(data[i].toJson())
        return exit

    @staticmethod
    def findProductsNotCompletedByUserId(userId):
        data = db.session.query(Product).filter(Product.user_id==userId).filter(Product.status==False).all()
        if len(data) == 0:
            return []
        exit = []
        for i in range(len(data)):
            exit.append(data[i].toJson())
        return exit

    @staticmethod
    def updateSelectedMenu(selectedMenu, userId):
        db.session.query(User).filter(User.id == userId).update({"selected_menu":selectedMenu})
        db.session.commit()

