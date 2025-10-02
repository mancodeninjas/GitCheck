class Order:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        self.price = 0
    def calcPrice(self):
        selectedSize = self.size
        match selectedSize:
            case 1:
                self.price = 7.99 * self.quantity
            case 2:
                self.price = 8.99 * self.quantity
            case 3:
                self.price = 9.99 * self.quantity
    def printReceipt(self):
        finalPrice = str(self.price)
        print("Your order of ", self.quantity, "pizzas is placed at ", finalPrice)

o1 = Order(2, 5)
o1.calcPrice()
o1.printReceipt()