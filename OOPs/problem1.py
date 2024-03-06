# create class - brand
# attributes - brand, color
# behaviour - BrandName car is accelarating

class Brand:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    # defining behaviour - method
    def accelarate(self):
        print(f"{self.brand} car is accelarating")

car1 = Brand("Lambourghini", "Black")

car1.accelarate()