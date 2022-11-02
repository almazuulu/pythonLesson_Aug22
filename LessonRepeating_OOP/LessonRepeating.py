class Conditioner:
    def __init__(self,model, brand, temperature, mode) -> None:
        self.model=model
        self.brand=brand
        self.temperature=temperature
        self.mode=mode
    def nwTemp(self,newTemp):
        self.newTemp=newTemp
        self.temperature=newTemp
        print(self.temperature)
    def Mode(self):
        if 30>self.temperature>20:
            self.mode="тепло"
        elif self.temperature>30:
            self.mode="жарко"
        elif 0<self.temperature<20:
            self.mode="норма"
        elif self.temperature<0:
            self.mode="холодно"
    def off(self):
        self.temperature=0
    def on(self):
        self.newTemperature=int(input("Какую температуру хотите задать"))
        if 30>self.newTemperature>20:
            self.mode="тепло"
        elif self.newTemperature>30:
            self.mode="жарко"
        elif 0<self.newTemperature<20:
            self.mode="норма"
        elif self.newTemperature<0:
            self.mode="холодно"
    def display(self):
        print(f"Кондиционер {self.model}  в данной времени стоит в температуре {self.temperature} и состояние {self.mode}")

class MusicPlayer:
    def playMusic(self, songName):
        print(f'Проигрыватель играет песню {songName}')

class Car(Conditioner, MusicPlayer):
    def __init__(self, brandAuto, modelCar, yearProduction, model, brand, temperature, mode):
        super().__init__(model, brand, temperature, mode)
        self.brandAuto = brandAuto
        self.modelCar = modelCar
        self.yearProd = yearProduction




if __name__ == '__main__':
    # k1=Conditioner("X3","MAC",23,"тепло")
    # k1.nwTemp(15)
    # k1.Mode()
    # k1.display()
    # k1.nwTemp(35)
    # k1.display()
    # k1.off()
    # k1.display()

    car1 = Car('Toyota', 'Corolla', 2015, 'toyotaConditioner', 'toyota', 18, 'teplo')

    car1.display()
    car1.playMusic('Gimn KR')


