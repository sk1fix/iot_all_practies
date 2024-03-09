class Human():
    default_name = 'Cristiano'
    default_age = 39

    def __init__(self, name=default_name, age=default_age) -> None:
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.name, self.age, self.__house, self.__money)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, arg):
        self.__money += arg

    def buy_house(self, house, discount):
        if self.__money-house.final_price(discount)>=0:
            self.__make_deal(house, house.final_price(discount))
        else:
            print("You don't have money")


class House():
    def __init__(self, area, price) -> None:
        self._area = area
        self._price = price
    

    def final_price(self, discount):
        return self._price-self._price*0.01*discount
    

class SmallHouse(House):
    def __init__(self, area, price) -> None:
        super().__init__(area, price)
        self._area='40м^2'


Human.default_info()

man=Human("Danek", 20)
man.info()

domik=SmallHouse(None, 10000000)

man.buy_house(domik,0.05)

man.earn_money(100000000)
man.buy_house(domik,0.05)
man.info()