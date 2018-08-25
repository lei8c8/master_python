class Car:

    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.val)

cars = [Car(3), Car(5), Car(1), Car(2)]
sortedCars = sorted(cars, key = lambda car: car.val)
print(cars)
print(sortedCars)
print()