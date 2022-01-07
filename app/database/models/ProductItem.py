from database.db import db

class ProductItem(db.Model):

    __tablename__ = "productitem"
    id         = db.Column("id"        ,db.Integer,primary_key=True,autoincrement=True)
    item_id    = db.Column("item_id"   ,db.ForeignKey("item.id"))
    product_id = db.Column("product_id",db.ForeignKey("product.id"))

    def __init__(self, **kwargs):
        self.id         = kwargs.get("id")
        self.item_id    = kwargs.get("itemId")
        self.product_id = kwargs.get("productId")

    def toJson(self):
        return {
            "id":self.id,
            "itemId":self.item_id,
            "productId":self.product_id
        }

