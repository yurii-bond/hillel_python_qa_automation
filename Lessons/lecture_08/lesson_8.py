# functions

# def print_hi(name):
#     print(f'Hi, {name}')
# if __name__== '__main__':
#     print_hi('PyCharm')
#
# import main
# print_hi('Rymma')
# name = "Rymma"
# surname = "Loranets"
# age = 30
# def print_hi(name, surname, age):     # 1 variant
#     print(name)
#     print(surname)
#     print(age)
#     print(f'{name} {surname} is {age} years old')
#     if age >= 60:
#         message = "You are a senior person"
#     elif age >= 18:
#         message = "You an adult"
#     else:
#         message = "You are a kid"
#     print(message)
#     print('=' * 30)
#
# print_hi("Rymma", "Loranets", 30)
#
# print_hi(name='Rymma', surname='Loranets', age=30)
# print_hi(age=30, name='Rymma', surname='Loranets')
# print('='*30)

_name = "Rymma"
_surname = "Loranets"
_age = 30
def print_hi(name, surname, age = 25):    # 2 variant
    print(name)
    print(surname)
    print(age)
    print(f'{name} {surname} is {age} years old')
    if age >= 60:
       message = "You are a senior person"
    elif age >= 18:
         message = "You an adult"
    else:
         message = "You are a kid"
    print(message)
    print('=' * 30)

print_hi('Rymma', 'Loranets', 30)
print_hi('Rymma', 'Loranets')
print_hi(_name, _surname, _age)

print_hi(name='Rymma', surname='Loranets', age=30)
print_hi(age=30, name='Rymma', surname='Loranets')
print_hi(surname=_surname, name=_name, age=_age)

print('_'*30)
def print_multiple_arguments(*args, name, group):
    print(args)
    for a in args:
        print(a)
print_multiple_arguments(1, 2, 3, 4, 5, 6, 7, 8, name='Rymma', group='LA-51')


def print_multiple_args(name, *args, group):
    print(args)
    for a in args:
        print(a)
print_multiple_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, group='LA-51')


def kwords_print(**kwargs):
    print(kwargs)
#   print(kwargs['name'])
    _keys = kwargs.keys()
    if 'name' in _keys:
        print(kwargs['name'])

kwords_print(name=_name, surname=_surname, age=_age)


def args_and_kwargs(*args, **kwargs):
#   pass
   print(args)
   print(kwargs)

args_and_kwargs(1, 2, 3, 4, 5, name=_name)
print('\n'*2)

# scope
_x = 5
def scope():
    _x = 10
    print(_x)

    def scope_2():
        print('inner scope: {}' .format(_x))
    scope_2()

print('global: {}' .format(_x))
scope()
print('\n'*2)

#recursion
def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n -1)
print(factorial(11))
#11*10*9*8*7*6*5*4*3*2*1
print('\n'*2)

# for Homework
def get_some_data_from_user(m=None):
    name = input('name yourself: ')
    surname = input('Type your surname, please: ')
    age = input('How old are you?: ')
    m.print_hi(name, surname, int(age))
get_some_data_from_user()