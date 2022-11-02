class A:
    def displayA(self):
        print('I am class A')

class B:
    def displayB(self):
        print('I am class B')

class C:
    def displayC(self):
        print('I am class C')

class D(C, B, A):
    pass

d = D()
d.displayA()
d.displayB()
d.displayC()
# print(D.mro())

class Doctor:
    def __init__(self, postion, typedoctor):
        self.position = postion
        self.typedoctor = typedoctor

    def can_cure(self):
        print('Я доктор и я могу лечить!')

    def display(self):
        print(f'\nЗвание докторантуры: {self.position}'
              f'\nТип врачевания: {self.typedoctor}')

class Army:
    def __init__(self, positionArmy, numberPolk):
        self.positionArmy =  positionArmy
        self.numberPolk = numberPolk

    def can_shoot(self):
        print('Я военный и я могу стрелять!')

    def display(self):
        print(f'\nОфицерское звание: {self.positionArmy}'
        f'\nНомер полка: {self.numberPolk}')

class Instructor:
    def __init__(self, numberStudent):
        self.numStudent = numberStudent

    def can_teach(self):
        print('Я могу обучать людей!')

    def display(self):
        print(f'\nКол-во обучаемых студентов: {self.numStudent}')


class Person(Doctor, Army, Instructor):
    def __init__(self, position, typeDoctor,positionArmy, numPolk, numStudent, name, age):
        self.name = name
        self.age = age
        super().__init__(position, typeDoctor)
        Army.__init__(self, positionArmy, numPolk)
        Instructor.__init__(self, numStudent)

    def display(self):
        print(f'Имя человека: {self.name}'
              f'\nВозраст человека: {self.age}')
        super().display()
        Army.display(self)
        Instructor.display(self)

p1 = Person('Главрач', 'Терапевт', 'Майор', 65, 100, 'Иван Иванов', 54)
p1.can_cure()
p1.can_shoot()
p1.can_teach()
p1.display()





