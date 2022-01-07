import datetime
from database.db import db

class Item(db.Model):

    __tablename__ = "item"
    id       = db.Column("id"      , db.Integer, primary_key=True, autoincrement=True)
    name     = db.Column("name"    , db.String)
    position = db.Column("position", db.Integer)
    created  = db.Column("created" , db.DateTime(timezone=True), default=datetime.datetime.now())
    updated  = db.Column("updated" , db.DateTime(timezone=True), default=datetime.datetime.now())

    def __init__(self, **kwargs):
        self.id       = kwargs.get("id")
        self.name     = kwargs.get("name")
        self.position = kwargs.get("position")

    def toJson(self):
        return {
            "id":self.id,
            "name":self.name,
            "position":self.position,
            "created":self.created,
            "updated":self.updated
        }

