class Animal:

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Dog(Animal):

    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()
dog.sleep()
dog.bark()


class vehicle:

    def start(self):
        print("\nStarting")

    def stop(self):
        print("Stoping")

class Car(vehicle):

    def drive(self):
        print("Driving")

car = Car()

car.start()
car.stop()
car.drive()