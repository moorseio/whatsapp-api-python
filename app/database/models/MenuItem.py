from database.db import db

class MenuItem(db.Model):

    __tablename__ = "menuitem"
    id      = db.Column("id"     ,db.Integer,primary_key=True,autoincrement=True)
    item_id = db.Column("item_id",db.ForeignKey("item.id"))
    menu_id = db.Column("menu_id",db.ForeignKey("menu.id"))

    def __init__(self, **kwargs):
        self.item_id = kwargs.get("itemId")
        self.menu_id = kwargs.get("menuId")

    def toJson(self):
        return {
            "id":self.id,
            "itemId":self.item_id,
            "menuId":self.menu_id
        }
