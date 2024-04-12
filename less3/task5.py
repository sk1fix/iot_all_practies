default_name="Николай"
class Nikola():
    def __init__(self,name,age):
        self.name=default_name
        self.age=age
        if name!="Николай":
            print("Я не ",name,", Я Николай",age)
        else:
            print(name, age)

person1 = Nikola('Иван', 31)
person2 = Nikola('Николай', 14)
print(person1.name)
print(person2.name)
person2.surname = 'Петров'