import import_clause

print(f'This is unittest when we ran it file {__name__}')


def throw_import_clause_function():
    import_clause.print_smth()


if __name__ == '__main__':
    import_clause.print_smth()

    print(f'This is unittest file {__name__}')