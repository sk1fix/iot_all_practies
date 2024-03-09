class Dog():
    def __init__(self,name,age) -> None:
        self._name = name
        self._age = age
    

    def sit(self):
        print(f"{self._name} сел/села")


    def roll_over(self):
        print(f"{self._name} перекатвается")


my_dog=Dog("Sharik",6)
my_dog.sit()
my_dog.roll_over()


his_dog=Dog("Karusel", 3)
his_dog.sit()
his_dog.roll_over()