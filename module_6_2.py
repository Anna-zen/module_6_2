"""Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
Цели: Применить сокрытие атрибутов и повторить наследование. Рассмотреть на примере объекта из реального мира.

Задача "Изменять нельзя получать":
В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет, мощность двигателя и прочие свойства, т.к. в реальной жизни это чаще всего делается не владельцем, а в специальных сервисах. Да, узнать значения этих свойств мы сможем, но вот изменить - нет.

Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса Vehicle.

I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:

    Атрибут owner(str) - владелец транспорта. (владелец может меняться)
    Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
    Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
    Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)

А так же атрибут класса:

    Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)

Каждый объект Vehicle должен содержать следующий методы:

    Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
    Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
    Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
    Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color; а так же владельца в конце в формате "Владелец: <имя>"
    Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".

Взаимосвязь методов и скрытых атрибутов:

    Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами: __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
    Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
    Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').

II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:

    Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)
"""


class Vehicle:
    # Список допустимых цветов
    __COLOR_VARIANTS = ['синий', 'красный', 'зеленый', 'черный', 'белый']

    def __init__(self, owner,__model, __color, __engine_power):
        self.owner = owner   # владелец может смениться
        self.model = __model   # остальные параметры с__  - не меняются
        self.color = __color
        self.engine_power = __engine_power

    def get_model(self):
        return (f"Модель авто: {self.model}")

    def get_horsepower(self):
        return (f"Мощность двигателя: {self.engine_power}")

    def get_color(self):
        return (f"Цвет авто: {self.color}")

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print("Владелец:", self.owner)

    def set_color(self, new_color):       # метод изменения цвета
        # переводим название цвета в нижний регистр и сравниваем со список допустимых цветов

        if new_color.lower() in self.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['синий', 'красный', 'зеленый', 'черный', 'белый']
vehicle1 = Sedan('Федор', 'Toyota Mark II', 'синий', 500)

# Изначальные свойства
print('Изначальные свойства: ')
vehicle1.print_info()
#print('Максимальное число пассажиров',__PASSENGERS_LIMIT)
print() # пустая строка


# Меняем свойства (в т.ч. вызывая методы)
print('Меняем свойства: ')
__PASSENGERS_LIMIT = 7
__model = "cybertrack"
__engine_power = 600
vehicle1.set_color('красный')

# Проверяем что поменялось
vehicle1.print_info()
print('Максимальное число пассажиров',__PASSENGERS_LIMIT)
print() # пустая строка

# Меняем свойства (в т.ч. вызывая методы)
print('Меняем свойства еще раз: ')
vehicle1.set_color('РОЗОВЫЙ')
vehicle1.owner = 'Андрей'

# Проверяем что поменялось
vehicle1.print_info()
print('Максимальное число пассажиров',__PASSENGERS_LIMIT)