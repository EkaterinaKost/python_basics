# реализовать дескрипторы для любых двух классов
class NonNegative:
    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError(f' {self.my_attr} - должно быть чило!')
        elif value <= 0:
            raise ValueError(f' {self.my_attr} - значение должно быть больше 0!')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    kg_square_meter = 25
    thickness = 0.05
    length = NonNegative()
    width = NonNegative()

    def asphalt_mass(self, length, width):
        self.lengh = length
        self.width = width

        print(
            f'{length * width * Road.kg_square_meter * Road.thickness} кг,'
            f'{(length * width * Road.kg_square_meter * Road.thickness) / 1000} т')


a = Road()
# a.asphalt_mass(20, 'fdg')  # TypeError:  width должно быть чило!
# a.asphalt_mass(20, -2000)  # ValueError:  width значение должно быть больше 0!
a.asphalt_mass(20, 2000)


class IsString:
    def __set__(self, instance, value):
        if type(value) != str:
            raise TypeError(f'тип данных {self.my_attr}  должен быть! str')

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = IsString()
    surname = IsString()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


ekaterina = Position(123, 'Костылева', 'Программист', 100000,
                     20000)  # TypeError: тип данных name  должен быть! str
print(ekaterina.get_full_name())
print(ekaterina.position)
print(ekaterina.get_total_income())
