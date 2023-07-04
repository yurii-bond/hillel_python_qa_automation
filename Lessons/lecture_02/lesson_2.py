# print(self, *arg, sep='', end='/n', file=None): # known special case of print
"""
 Prints the values to a stream, or to sys.stdout by default.

  sep
    string inserted between values, default a space.
  end
    string appended after the last value, default a newline.
  file
    a file-like object (stream); defaults to the current sys.stdout.
  flush
    whether to forcibly flush the stream.
"""
# variables 1
print("Hello", end=' ')
print("  ", end="\n")
print("  ", end="\n\n")
print("element1 ", "element2", sep=",", end="\n\n")
print(1, 2, 3, sep="; ")

element1 = 1
element2 = 2
print(element1, element2)
print(element2, element1)

element_variable = 100
a = 100
b = 222
c = a + b
print(c)
print("-----")
print(a + b)
print(f"{a +b}")

print("a +' b")
print('a +\\\' b')

# variables_names

element = "element"
element_first = "1"
element_first_of_a_set = "123"
_element = "private" # for not to use
__element = "  " # for not to use

PI = 3.14 # constanta
ELEMENT = PI
print(ELEMENT)

# operators

a = 100.0
b = 200
print(a - b)
print(a + b)
print(a * b)
print(int(a * b))
print(a / b)
print(int(a / b))
print(a + b)
print(a + b * a / a)
print(a + b * a)
print(a + b * b / a)
print(a + (b * b) / a)
print((a + b) * b)

if a < b:
    print("a<b")
else:
    print("a>b")

if a > b:
    print("a<b")
else:
    print("a>b")

if a > b:
    print("a<b")
elif a == b:
    print("a == b")
else:
    print("a>b")

a = 9
b = 10
if a < b:
    print("a < b_1")
elif a == b:
    print("a == b")
elif a <= b:
    print("a <= b")
elif a >= b:
    print("a >= b")
else:
    print("a>b")

if a < b:
    print("You can buy it")
if a <= b:
    print("You need to buy it")

a, b, c = 9, 10, 11
print(a, b, c)

a, b = b, a
print(a, b, c)

a = 10
b = 10
a = b + 5
a += 5
print(b)
print(a)

b = b % 5
a %= 5
print(b)
print(a)

a = 11
b = 11
b = b ** 2
a **= 2
print(b)
print(a)

a = 11
b = 11
print(a)
print(b)
if a == 11 or b == 11:
    print("True")

a = 11
b = 11
print(a)
print(b)
if a == 11 or b == 11:
    print("True")
else:
    print("False")

print(b)
print(a)
if a != 11 or b != 11:
    print("True")
else:
    print("False")

_list = [1, 2, 3]
if 1 in _list:
   print("Yes")

_list = [1, 2, 3]
if 4 in _list:
    print("NO")


print("---------")

a, b, c = 9, 10, 11
a+b
print(a+b)

a = 11
b = 11
print(b)

b = b % 5
a %= 5
print(b)
print(a)
b = b ** 2
a **= 2
print(b)
print(a)

a = 11
b = 11
if a ==11 and b == 11:
    print("True")
else:
    print("False")

a = 11
b = 11
if a == 11 or b == 11:
    print("True")
else:
    print("False")

_list = [1, 2, 3]
if 4 in _list:
    print("Yes")
else:
    print("No")


