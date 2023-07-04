# # lambda
# def multiply(x, y):
#     return print(x * y)
#
#
# multiply(2, 2)
# multiply(3, 3)
#
# (lambda x, y: print(x * y))(2, 2)  # lambda variant
#
# mult = lambda x, y: print(x * y)
#
# mult(3, 3)
#
# print("\n"*2)
#
# lamb_da = lambda x, func: func(x)
#
# lamb_da(2, print)
#
# print("\n"*2)
#
# lamb_da = lambda x, y, func: func(x, y)
#
# lamb_da(2, 3, mult)
#
# print("\n"*2)
#
# _lambda = lambda x, y: print(f'My full name is: {x} {y}')
#
# _lambda('Rymma', 'Loranets')
#
# print("\n"*2)
#
# format_numeric = lambda num: f'{num:e}' if isinstance(num, int) else f'{num:,.2f}'   #number formating + lambda
#
# print("Int formatting:", format_numeric(1000000))
# print('float formatting:', format_numeric(999999.7895412345))
#
# print("\n"*2)
#
# axb = multiply
#
# axb(5,4)
# print("\n"*2)
#
# # list comprehension
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def get_sorted(_list):
#     empty_list = []
#     for i in _list:
#         if i < 5:
#             print(i)
#
# get_sorted(a)
#
# print("\n"*2)
# def get_sorted(_list):
#     empty_list = []
#     for i in _list:
#         if i < 5:
#             empty_list.append(i)
#             print(i)
#     print('Filtered list: {}' .format(empty_list))
#
# get_sorted(a)
#
# print("\n"*2)
# def get_sorted(_list):
#     empty_list = []
#     for i in _list:
#         if i < 5:
#             empty_list.append(i)
#             print(i)
#     print('Filtered list: {}' .format(empty_list))
#     # return empty_list
#
# v = [x if x < 5 else '' for x in a ]
# b = [x for x in a if x < 5]
#
# x = [x for x in range(10) if x < 5]
# print(f'x: {x}')
# get_sorted(a)
# # print(get_sorted(a))
# print(v)
# print(b)
#
# print("\n"*2)
# # variant 1
# message = input('Input:')
# vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U', 'y', 'Y']
# formatted_message_list = ['' if ch in vowels else ch for ch in message]
# print(formatted_message_list)
# joined_list = '' .join(formatted_message_list)
# print(joined_list)
# print('Output: {}' .format(joined_list))
# #print('Output: {}' .format('' .join(['' if ch in vowels else ch for ch in message])))
#
# print('\n')
# # variant 2
# message = input('Input:')
# vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U', 'y', 'Y']
# formatted_message_list = ['' if ch in vowels else ch for ch in message]
# joined_list = '' .join(formatted_message_list)
# print('Output: {}' .format(joined_list))
# print('Output: {}' .format('' .join(['' if ch in vowels else ch for ch in message])))
#
# print('\n' * 2)

# decorators

from datetime import datetime


def my_decorator(func):
    def wrapper():
        print('start of the decorator')
        func()
        print('end of the decorator')

    return wrapper


@my_decorator
def say_yuppi():
    print('Yuppi!')


say_yuppi()


# say_yuppi = my_decorator(say_yuppi) # variant without decorator

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour <= 22:
            func()
        else:
            print('Tsss!!!')
    return wrapper


def do_twise(func):
    def wrapper():
        func()
        func()

    return wrapper

@not_during_the_night
@do_twise
@my_decoratords
def say_yuppi():
    print('Yuppi!')


say_yuppi()

