#Task 2
class Alphabet:
    def __init__(self, lang, letters):
        self.language = lang
        self.letts = letters

    def displayLetters(self):
        for c in self.letts:
            print(c, end=' ')

        print()

    def countLetts(self):
        # print(len(self.letts))
        return len(self.letts)

rus = Alphabet('Ru', 'абвгде')
eng  = Alphabet('En', 'abcdefgh')

rus.displayLetters()
eng.displayLetters()

print(rus.countLetts())
print(eng.countLetts())


