class GeographyTeacher:
    def __init__(self, country):
        self.__teacher_type = 'Учитель Географии'
        self.country = country

    def get_teacher_type(self):
        return self.__teacher_type

    def findCapitalcity(self):

        someCity = ' '
        if self.country == 'Russia':
            someCity = 'Moscow'

        elif self.country == 'Kyrgyzstan':
            someCity = 'Bishkek'

        elif self.country == 'Sweden':
            someCity = 'Vienna'

        return someCity

    def display(self):

        print(f'Capital of {self.country} is {self.findCapitalcity()}')

class MathTeacher:
    def __init__(self, num1, num2, num3):
        self.__teacher_type = 'Учитель Математики'
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def get_teacher_type(self):
        return self.__teacher_type

    def display(self):
        print(f'{(self.num1 + self.num2 + self.num3) / 3}')


class Teacher(GeographyTeacher, MathTeacher):
    def __init__(self, name, experience, numStudent, country, num1, num2, num3):
        super().__init__(country)
        MathTeacher.__init__(self, num1, num2, num3)
        self.name = name
        self.experience = experience
        self.numStudent = numStudent

    def display(self):
        print(f'Teacher: {self.name}'
              f'\nExperience: {self.experience}'
              f'\nStudent`s quantity: {self.numStudent}')
        super(Teacher, self).display()
        MathTeacher.display(self)

    def introducing(self):
        print(f'Меня зовут {self.name} и я '
              f'{super().get_teacher_type()} и {MathTeacher.get_teacher_type(self)}')


t1 = Teacher('Вася Пупкин', 10, 100, 'Kyrgyzstan', 10, 20, 30)
t1.display()
t1.introducing()