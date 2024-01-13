# define a class person with instance object variables name and age. Set instance object variables
#  in __init__() method. Also define show() method to display name and age of a person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name} is {self.age} years old.\n")


admin = Person("Mohammad Arsalan Rather", 20)
victor = Person("Victor", 69)
andy = Person("Andy", 45)

admin.show()
victor.show()
andy.show()
