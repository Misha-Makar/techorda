class Person:
    fullName: str
    age: int

    def __init__(self, fullName, age):
        self.fullName = fullName
        self.age = age

    def __str__(self):
        return self.fullName, self.age


class Driver(Person):
    experience: int

    def __init__(self, fullName, age, experience):
        super().__init__(fullName, age)
        self.experience = experience

    def __str__(self):
        return Person.__str__(self), self.experience


class Engine:
    power: int
    company: str

    def __init__(self, power, company):
        self.power = power
        self.company = company

    def __str__(self):
        return self.power, self.company


class Lorry():
    carrying: int

    def __init__(self, carrying):
        self.carrying = carrying

    def __str__(self):
        return self.carrying


class SportCar():
    speed: int

    def __init__(self, speed):
        self.speed = speed

    def __str__(self):
        return self.speed


class Car(Driver, Engine, SportCar, Lorry):
    carClass: str
    engine: Engine
    driver: Driver
    mark: str
    speed: SportCar
    carrying: Lorry

    def __init__(self, carClass, mark, fullName, age, experience, speed, carrying, power, company):
        self.carClass = carClass
        self.mark = mark
        Driver.__init__(self, fullName, age, experience)
        SportCar.__init__(self, speed)
        Lorry.__init__(self, carrying)
        Engine.__init__(self, power, company)

    @staticmethod
    def start():
        print("Поехали")

    @staticmethod
    def stop():
        print("Останавливаемся")

    @staticmethod
    def turnRight():
        print("Поворот на право")

    @staticmethod
    def turnLeft():
        print("Поворот на лево")

    def __str__(self):  # выводит полную информацию об автомобиле, ее водителе и моторе
        return {self.carClass}, \
               {self.mark}, \
               {self.fullName}, \
               {self.age}, \
               {self.experience},\
               {self.speed},\
               {self.carrying}, \
               {self.power},\
               {self.company}


# x = Car('PREMIUM',
#         'MERCEDES',
#         "TIMUR BAKIROV",
#         '31 years old',
#         '12 driving experience',
#         '200 km/h',
#         '200 kg',
#         '220 horse power',
#         'MERCEDES')
# print(x.__str__())


# Car.turnRight()
# Car.turnLeft()
# Car.start()
# Car.stop()






