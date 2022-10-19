class Car:
    def __init__(self, brand, model, speed, places):
        self.brandCar = brand
        self.modelCar = model
        self.speedCar = speed
        self.placesCar = places

    def display(self):
        print(self.brandCar, self.modelCar, self.speedCar, self.placesCar)

    def breakCar(self):
        print(f'{self.modelCar} затормозил!')

class Bus(Car):
    def __init__(self, brand, model, speed, places, typeBus):
        # Car.__init__(self, brand, model, speed, places)
        super().__init__(brand, model, speed, places)
        self.busType = typeBus

    def whichBus(self):
        if self.busType == 'School bus':
            print('Это школьный автобус')
        elif self.busType == 'Army':
            print('Военный автобус и у него ' + str(self.placesCar) + ' мест')
        else:
            print('Общественный автобус')

    def display(self):
        super().display()
        print(self.busType)

        # print(self.brandCar, self.modelCar, self.speedCar, self.placesCar, self.busType)

        # print(self.brandCar)

class SportCar(Car):
    def __init__(self, brand, model, speed, places, speepLimit, raceCar):
        self.speepLimit = speepLimit
        self.raceCar = raceCar
        Car.__init__(self,brand, model, speed, places)

    def raceType(self):
        if self.speepLimit > 350:
            print('Участвует в Формуле 1')
        else:
            print('Не участвует в Формуле 1')

    def display(self):
        super().display()
        print(self.speepLimit, self.raceCar)


bus1 = Bus('Mercedes', 'Sprinter 123', 80, 20, 'Army')
bus1.display()
# bus1.whichBus()
# bus1.breakCar()
#
sportCar = SportCar('Ferrari', 'F1', 420, 1, 1200, True)
sportCar.display()
# sportCar.breakCar()











