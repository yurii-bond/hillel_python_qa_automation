import unittests

unittests.throw_import_clause_function()


def new_func(a: int, b: str, c: bool, d: float = 2.0) -> None:
    print(a, b, c, d)


print(new_func(a=1.0, b=True, c='True'))
