from typing import List


class Driver:

    def __init__(self, rating: int):
        self.rating = rating

    def can_cook(self):
        print('I can cook!!!')

    def can_drive(self) -> None:
        print('I can drive!!!')


class Builder:

    def __init__(self, equipments: List[str]):
        self.equipments = equipments

    def can_build(self) -> None:
        print('I can build!!!')

    def can_cook(self):
        print('I can cook also!!!')


class Person(Driver, Builder):

    def __init__(self, rating: int, equipments: List[str], name: str, surname: str):
        Driver.__init__(self, rating)
        Builder.__init__(self, equipments)
        self.name = name
        self.surname = surname

    def can_cook(self):
        Driver.can_cook(self)
        Builder.can_cook(self)
        print('I can cook so amazing!')


person = Person(rating=5, equipments=['Молоток', 'Каска'], name='Aibar', surname='Bek')
# person.can_cook()
# person.can_drive()
# person.can_build()
print(person.rating)
print(person.equipments)
print(person.name)
print(person.surname)