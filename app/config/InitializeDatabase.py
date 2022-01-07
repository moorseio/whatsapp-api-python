from database.models.Item import Item
from database.models.Menu import Menu
from database.models.MenuItem import MenuItem
from database.repositories.MenuItemRepo import MenuItemRepo

from database.repositories.MenuRepo import MenuRepo
from database.repositories.ItemRepo import ItemRepo

class InitializeDatabase:

    @staticmethod
    def initialize():

        sabor = {
            "name":"SABOR",
            "id":1
        }

        massa = {
            "name":"MASSA",
            "id":2
        }

        adicional = {
            "name":"ADICIONAL",
            "id":3
        }
        
        MenuRepo.save(**sabor)
        MenuRepo.save(**massa)
        MenuRepo.save(**adicional)

        saborFrango = {
            "name":"FRANGO",
            "position":1,
            "id":1
        }

        saborCalabresa = {
            "name":"CALABRESA",
            "position":2,
            "id":2
        }

        saborPortuguesa = {
            "name":"PORTUGUESA",
            "position":3,
            "id":3
        }

        ItemRepo.save(**saborFrango)
        ItemRepo.save(**saborCalabresa)
        ItemRepo.save(**saborPortuguesa)

        massaFina = {
            "name":"FINA",
            "position":1,
            "id":4
        }

        massaGrossa = {
            "name":"GROSSA",
            "position":2,
            "id":5
        }

        massaRecheada = {
            "name":"RECHEADA",
            "position":3,
            "id":6
        }

        ItemRepo.save(**massaFina)
        ItemRepo.save(**massaGrossa)
        ItemRepo.save(**massaRecheada)

        adicionalBacon = {
            "name":"BACON",
            "position":1,
            "id":7
        }

        adicionalQueijo = {
            "name":"QUEIJO",
            "position":2,
            "id":8
        }

        adicionalLegumes = {
            "name":"LEGUMES",
            "position":3,
            "id":9
        }

        ItemRepo.save(**adicionalBacon)
        ItemRepo.save(**adicionalQueijo)
        ItemRepo.save(**adicionalLegumes)

        #lembrar de inicializar os menuitem
        menuItemFrango = {
            "itemId":1,
            "menuId":1
        }
        menuItemCalabresa = {
            "itemId":2,
            "menuId":1
        }
        menuItemPortuguesa = {
            "itemId":3,
            "menuId":1
        }

        MenuItemRepo.save(**menuItemFrango)
        MenuItemRepo.save(**menuItemCalabresa)
        MenuItemRepo.save(**menuItemPortuguesa)

        menuItemGrossa = {
            "itemId":4,
            "menuId":2
        }
        menuItemFina = {
            "itemId":5,
            "menuId":2
        }
        menuItemRecheada = {
            "itemId":6,
            "menuId":2
        }

        MenuItemRepo.save(**menuItemGrossa)
        MenuItemRepo.save(**menuItemFina)
        MenuItemRepo.save(**menuItemRecheada)

        menuItemBacon = {
            "itemId":7,
            "menuId":3
        }
        menuItemQueijo = {
            "itemId":8,
            "menuId":3
        }
        menuItemLegumes = {
            "itemId":9,
            "menuId":3
        }

        MenuItemRepo.save(**menuItemBacon)
        MenuItemRepo.save(**menuItemQueijo)
        MenuItemRepo.save(**menuItemLegumes)
        