class Cart:
    def __init__(self,name):
        self.cago = []
        self.name = name
    def add_list(self,item):
        self.cago.append(item)
    # def sum_price(self):
    #     list_price = []
    #     for item in self.cago:
    #         list_price.append(item.price)
    #     return sum(list_price)
    def sum_price(self):
        sum = 0
        for item in self.cago:
            sum += item.price
        return sum

class Item:
    def __init__(self, name, price):
        self.name= name
        self.price = price

if __name__ == '__main__':
    cart1 = Cart('cart1')
    print(cart1.name) 
    apple = Item('apple',200)
    banana = Item('banana',100)      
    cart1.add_list(apple)
    cart1.add_list(banana)
    for i in cart1.cago:
        print(i.name)

    print(cart1.cago[0].price)
    print(cart1.sum_price())
    # print(cart1.sum_price(cart1.cago.price))

# list = [100,200,300]
# print(sum(list))

    
    