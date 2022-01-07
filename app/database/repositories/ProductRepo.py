from database.models.Product import Product
from database.db import db

class ProductRepo:

    @staticmethod
    def save(**kwargs):
        product = Product(**kwargs)
        db.session.add(product)
        db.session.commit()
        return product.toJson()

    @staticmethod
    def findById(productId):
        data = db.session.query(Product).filter(Product.id==productId).all()
        if len(data) == 0:
            return []
        return data[0].toJson()

    @staticmethod
    def finishNotCompletedOrders(userId):
        db.session.query(Product).filter(Product.user_id == userId).update({"status":True})
        db.session.commit()



