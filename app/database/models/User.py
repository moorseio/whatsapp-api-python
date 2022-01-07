import datetime
from database.db import db

class User(db.Model):

    __tablename__     = "user"
    id                = db.Column("id"               , db.Integer, primary_key=True, autoincrement=True)
    name              = db.Column("name"             , db.String)
    number            = db.Column("number"           , db.String)
    profile_image_url = db.Column("profile_image_url", db.String)
    created           = db.Column("created"          , db.DateTime(timezone=True), default=datetime.datetime.now())
    updated           = db.Column("updated"          , db.DateTime(timezone=True), default=datetime.datetime.now())
    selected_menu     = db.Column("selected_menu", db.Integer, default=-1)

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.number = kwargs.get("number")
        self.profile_image_url = kwargs.get("profileImageUrl")

    def toJson(self):
        return {
            "id":self.id,
            "name":self.name,
            "number":self.number,
            "profileImageUrl":self.profile_image_url,
            "created":str(self.created),
            "updated":str(self.updated),
            "selectedMenu":self.selected_menu
        }
