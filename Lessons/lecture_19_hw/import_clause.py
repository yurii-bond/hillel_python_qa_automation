def print_smth():
    print('Hello, I\'m from import clause')


print(f'This is what we get at importing import clause file: {__name__}')


if __name__ == '__main__':
    print_smth()

    print(f'This is import clause file: {__name__}')
