
class Item:
#     name = ""
#     cost = 0
#     price = 0
#     shelfLife = -1
#     dateEntered = ""
    def __init__(self, idNum, itemName, itemCost, itemPrice, itemShelfLife, itemDateEntered):
        self.id = idNum
        self.name = itemName
        self.cost = itemCost
        self.price = itemPrice
        self.shelfLife = itemShelfLife
        self.dateEntered = itemDateEntered

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getCost(self):
        return self.cost

    def getPrice(self):
        return self.price

    def getShelfLife(self):
        return self.shelfLife

    def getDateEntered(self):
        return self.dateEntered
