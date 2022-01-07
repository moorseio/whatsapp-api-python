import datetime
from database.db import db

class Menu(db.Model):

    __tablename__ = "menu"
    id      = db.Column("id"      , db.Integer, primary_key=True)
    name    = db.Column("name"    , db.String)
    created = db.Column("created" , db.DateTime(timezone=True), default=datetime.datetime.now())
    updated = db.Column("updated" , db.DateTime(timezone=True), default=datetime.datetime.now())

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.id   = kwargs.get("id")

    def toJson(self):
        return {
            "id":self.id,
            "name":self.name,
            "created":self.created,
            "updated":self.updated
        }

