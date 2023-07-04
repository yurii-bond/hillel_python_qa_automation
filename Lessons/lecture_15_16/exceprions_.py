import os

new_list = []
new_dic = {}
file = None

try:
    new_dic['age']
    print(new_list[2])
    if os.path.exists('output.csv'):
        print('Raising an exception')
        raise FileExistsError("The file was created before")
    print('Open a file')
    file = open('output.csv', 'x')
except ZeroDivisionError as zde:
    print(f'This is zero division error: {zde}')
except KeyError as ke:
    print(ke.__doc__, ke)
except ArithmeticError as ae:
    print(f'Arithmetic Error {ae}')
except FileExistsError as fee:
    print(f'We are here {fee}')
    os.remove('output.csv')
    file = open('output.csv', 'x')
except Exception as ex:
    print(f'Something went wrong: {ex}')

else:
    file.write('Hello')

finally:
    # file.close()
    print('This block is always run')







