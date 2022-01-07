from database.db import db

class Product(db.Model):

    __tablename__ = "product"
    id            = db.Column("id"      , db.Integer, primary_key=True, autoincrement=True)
    status        = db.Column("status"  , db.Boolean)
    user_id       = db.Column("user_id" , db.ForeignKey("user.id"))
    item_id       = db.Column("item_id" , db.ForeignKey("item.id"))

    def __init__(self, **kwargs):
        self.status  = kwargs.get("status")
        self.user_id = kwargs.get("userId")
        self.item_id = kwargs.get("itemId")

    def toJson(self):
        return {
            "id":self.id,
            "status":self.status,
            "userId":self.user_id,
            "itemId":self.item_id
        }
