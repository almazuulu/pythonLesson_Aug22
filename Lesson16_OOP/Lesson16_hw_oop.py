#Task 2
"""
Создайте класс Vehicle, где в качестве атрибута принимаются
следующие переменные в конструктор – brandCar, nameCar,
maxSpeed, color

Создайте следующие методы:
• Метод, который отображает все информации о том или
ином автомобиле
• Метод, возвращает тип автомобиля в зависимости от
скорости автомобиля при следующих условиях:
- Метод должен возвращать «Семейный», если
максимальная скорость не достигает 150 км/ч.
- Метод возвращает «Школьный», если скорость
не достигает 80 км/ч
- Метод возвращает «Спортивный», если скорость
автомобиля превышает 150 км/ч
• Метод при вызове, которой меняет цвет автомобиля
"""

class Vehicle:
    def __init__(self, brandCar, nameCar, maxSpeed, color):
        self.brandCar = brandCar
        self.nameCar = nameCar
        self.speedMax = maxSpeed
        self.colorCar = color

    def display(self):
        print(f'Бренд автомобиля:  {self.brandCar}'
              f'\nМодель автомобиля:  {self.nameCar}'
              f'\nМаксимальную скорость:  {self.speedMax}'
              f'\nЦвет автомобиля:  {self.colorCar}')
        print()

    def changeColor(self, newColor):
        self.colorCar = newColor

    def typeCar(self) -> str:
        carType = str()

        if self.speedMax <= 80:
            carType = 'School type'
        elif self.speedMax > 81 and self.speedMax < 150:
            carType = 'Family type'
        elif self.speedMax >= 150:
            carType = 'Sport type'

        return f'{self.brandCar} {self.nameCar} is {carType} car'


car1 = Vehicle('Tyota', 'Camry 35', 100, 'black')
car2 = Vehicle('Ferrari', 'F1', 350, 'red')

car1.display()
car2.display()

car1.changeColor('pink')
car1.display()

print(car1.typeCar())
print(car2.typeCar())






