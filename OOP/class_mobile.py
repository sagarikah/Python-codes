class Mobile:

    def __init__(self,brand,price):
        self.brand= brand
        self.price= price

    def purchase(self):
        print("Purchasing a mobile")
        print("This mobile is of brand ", self.brand, " and price ", self.price)



mob1= Mobile("Samsung",12000)

mob2= Mobile("Vivo",20000)


mob2.purchase()

