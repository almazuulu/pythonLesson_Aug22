#Task 1
def find_sum_text(fun):
    def wrapper(lst):
        textTowrite = 'Все элементы списка'
        with open('task1.txt', 'w') as f:
            for n in lst:
                textTowrite += f'\n{n}'

            textTowrite += '\n'
            textTowrite += '-' * 50
            textTowrite += '\nСумма всех значений в списке: \n'
            textTowrite += '-' * 50
            textTowrite += f'\n{sum(lst)}\n'
            textTowrite += '-' * 50
            f.write(textTowrite)

        print('Saved!')
    return wrapper

# @find_sum_text
def showList(lst):
    return lst

if __name__ == '__main__':
    showList([12,43,34,54,6])