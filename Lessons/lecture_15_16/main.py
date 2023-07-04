class Bus:
    def one(self):
        pass

    def two(self):
        pass

    def three(self):
        pass


class Car:
    def one(self):
        pass

    def two(self):
        pass


bus = Bus()
car = Car()

for obj in (bus, car):
    obj.one()
    obj.two()
