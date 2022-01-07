from api.MoorseMessageAPI import MoorseMessageAPI
from database.repositories.ItemRepo import ItemRepo
from database.repositories.ProductRepo import ProductRepo
from database.repositories.UserRepo import UserRepo
from database.repositories.MenuRepo import MenuRepo
from utils.DefaultMessages import *

class BotService:

    @staticmethod
    def handleMessage(**dictMessage):

        userName = dictMessage["contactUser"]["name"]
        userNumber = dictMessage["from"]
        messageContent = dictMessage["content"]

        user = UserRepo.findByNumber(userNumber)
        heWasAtDatabase = len(user) > 0

        welcomeMessage.format(userName)
        availableMenusMessage = BotService.createAvailableMenusMessage()

        if not heWasAtDatabase:

            newUser = {"name":userName,"number":userNumber}
            UserRepo.save(**newUser)
            MoorseMessageAPI.sendMessage(userNumber, welcomeMessage + availableMenusMessage)

        else:

            if not messageContent.isdecimal():
                MoorseMessageAPI.sendMessage(userNumber, chooseOption)
                MoorseMessageAPI.sendMessage(userNumber, availableMenusMessage)
                return

            if user[0]["selectedMenu"] != -1:
                
                selectedMenu = user[0]["selectedMenu"]
                userId = user[0]["id"]
                menu = MenuRepo.findMenuById(selectedMenu)

                selectedItem = int(messageContent)

                item = ItemRepo.findItemByItemPositionAndMenuId(selectedItem, selectedMenu)

                isSelectedItemAnItemPosition = len(item) > 0

                if not isSelectedItemAnItemPosition:
                    MoorseMessageAPI.sendMessage(userNumber, chooseOption)
                    MoorseMessageAPI.sendMessage(userNumber, availableMenusMessage)
                    return

                itemId = item[0]["id"]

                UserRepo.updateSelectedMenu(-1, userId)
                ProductRepo.save(**{
                    "status":False,
                    "userId":userId,
                    "itemId":itemId
                })

                MoorseMessageAPI.sendMessage(userNumber, addedProduct)
                MoorseMessageAPI.sendMessage(userNumber, availableMenusMessage)

            else:

                menu = MenuRepo.findMenuById(int(messageContent))
                isNumberAValidMenu = len(menu) > 0

                if (not isNumberAValidMenu) and int(messageContent) != 0:
                    MoorseMessageAPI.sendMessage(userNumber, chooseOption)
                    return
                
                if int(messageContent) == 0:
                    BotService.completeOrder(**dictMessage)
                    return

                menuId = int(messageContent)
                newMenuMessage = BotService.createAvailableMenuItemMessage(menuId, user, menu)
                MoorseMessageAPI.sendMessage(userNumber, newMenuMessage)

    @staticmethod
    def createAvailableMenusMessage():
        menus = MenuRepo.findAll()
        availableMenusMessage = "🍟 MENU PRINCIPAL 🍔\n"
        for i in range(len(menus)):
            availableMenusMessage += "[" + str(menus[i]["id"]) + "] " + menus[i]["name"] + ".\n"
        availableMenusMessage += "[0] FINALIZAR O PEDIDO ✅ .\n"
        return availableMenusMessage


    def createAvailableMenuItemMessage(menuId, user, menu):
        items = ItemRepo.findByMenuId(menuId)
        UserRepo.updateSelectedMenu(menuId, user[0]["id"])
        newMenuMessage = "🍟 MENU " + menu[0]["name"] + " 🍔\n"
        for i in range(len(items)):
            newMenuMessage += "[" + str(items[i]["position"]) + "] " + items[i]["name"] + ".\n" 
        return newMenuMessage

    @staticmethod
    def completeOrder(**dictMessage):
        
        userNumber = dictMessage["from"]
        user = UserRepo.findByNumber(userNumber)
        userId = user[0]["id"]

        products = UserRepo.findProductsNotCompletedByUserId(userId)

        if len(products) == 0:
            MoorseMessageAPI.sendMessage(userNumber, emptyOrder)
            MoorseMessageAPI.sendMessage(userNumber, BotService.createAvailableMenusMessage())
            return

        ProductRepo.finishNotCompletedOrders(userId)

        foodNames = []

        for i in range(len(products)):
            itemId = products[i]["itemId"]
            item = ItemRepo.findItemById(itemId)
            foodNames.append(item["name"])

        finalMessage = completedOrder
        
        for i in range(len(foodNames)):
            finalMessage += foodNames[i]
            if i!=len(foodNames)-1:
                finalMessage += ", "

        finalMessage += "]"
        MoorseMessageAPI.sendMessage(userNumber, finalMessage)
        finalMessage = BotService.createAvailableMenusMessage()
        MoorseMessageAPI.sendMessage(userNumber, finalMessage)
