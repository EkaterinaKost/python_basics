# реализовать метакласс. позволяющий создавать всегда один и тот же
# объект класса (см. урок)



class TypeMeta(type):
    a = None

    def __call__(self):
        if self.a is None:
            self.a = super().__call__()
        return self.a


class MyClass(metaclass=TypeMeta):
    pass


obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()

print(obj_1 is obj_2)
print(obj_2 is obj_3)
print(obj_3 is obj_1)
