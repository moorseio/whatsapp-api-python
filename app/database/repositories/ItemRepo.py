from database.models.MenuItem import MenuItem
from database.models.Item import Item
from database.db import db

class ItemRepo:

    @staticmethod
    def save(**kwargs):
        item = Item(**kwargs)
        db.session.add(item)
        db.session.commit()
        return item.toJson()

    @staticmethod
    def findItemById(itemId):
        item = db.session.query(Item).filter(Item.id == itemId).all()
        if len(item)==0:
            return []
        return item[0].toJson()

    @staticmethod
    def findByMenuId(menuId):
        listMenuItem = db.session.query(MenuItem).filter(MenuItem.menu_id == menuId).all()
        listItems = []
        for i in range(len(listMenuItem)):
            item = ItemRepo.findItemById(listMenuItem[i].item_id)
            listItems.append(item)
        return listItems

    @staticmethod
    def findItemByItemPositionAndMenuId(itemPosition, menuId):
        menusItems = db.session.query(MenuItem).filter(MenuItem.menu_id==menuId).all()
        
        item = []

        for i in range(len(menusItems)):
            itemId = menusItems[i].toJson()["itemId"]
            position = ItemRepo.findItemById(itemId)["position"]
            if position == itemPosition:
                item.append(ItemRepo.findItemById(itemId))
                break

        if len(item) == 0:
            return []

        return item
        
