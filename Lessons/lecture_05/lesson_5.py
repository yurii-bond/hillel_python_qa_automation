# tuple (cortege)
var_tuple = (1, 2, 3, 4, 5)
print(var_tuple)

new_tuple = (1, 2, 3,[1, 2])
print(new_tuple)

print(new_tuple[0])
nested_tuple = new_tuple[3]

new_tuple[3][0] = 10

print(new_tuple)
print(new_tuple[-2])
print(new_tuple[len(new_tuple) -1])

if 1 in new_tuple:
    print('1 is in the tuple: {}' .format(new_tuple))

print("_" * 12 )

# set
new_set = {1, 2, 3, 4, 5, 0, True, False}
print(new_set)

set2 = {1, 33, 2, 2, 3, 3}
print(set2)

print(int(True))
print(int(False))

empty_set = set()
empty_dict = {}
empty_dict2 = dict()

name_set = {"yurii", 'dariia', 'yuliia', 'liliia', 'denis'}
print(name_set)

set3 = {5.0, 4, 3.5, 2, 1}
print(set3)

# adding 1 element
set3.add("name")
print(set3)

set3.update(set2)
print(set3)

new_dictionary = {
    'name': 'Rymma',
    'age': 30,
    'occupation': 'QA'
}
set3.update(new_dictionary)

print(set3)

new_dictionary.get('name')
new_dictionary['name'] = 'Olga'
print(new_dictionary.get('name'))
set3.add('denis')
set3.union(name_set)
print('union {}' .format(set3))

# intersection
# set3.intersection_update(name_set)
# print(set3)

set4 = set3.intersection(name_set)
print('set4 {}' .format(set4))
print('set3 {}' .format(set3))
print('_' * 20)

_set1 = {1, 2, 3, 4, 5, 0}
_set2 = {4, 5, 6, 7, 8, 9}

_set3 = _set1.difference(_set2)
print(_set3)

_set4 = _set2.difference(_set1)
print('set4 {}' .format(_set4))
print('set2 {}' .format(_set2))

_set5 = _set1.symmetric_difference(_set2)
print(_set5)
_set1.symmetric_difference_update(_set2)


_set2.difference_update(_set1)
print(_set2)
print("")

superset = {1,2,3,4,5,6,7}
subset = {3,4,5}

disjointset = {8,9,0}

is_subset = subset.issubset(superset)
print(is_subset)

print(superset.issubset(subset))

print(superset.issuperset(subset))

print(superset.isdisjoint(disjointset))

_set2.add(4)
_set1.union(_set2)
_set2.update(_set3)

print(_set2)

_set2.remove(3)  #delete element
print(_set2)
#_set2.remove(3)
_set2.discard(2)  #delete element
print(_set2)

_set2.pop()
_set2.clear()
print(_set2) #delete all

#del _set2 #delete but give an error

print('')
#frozenset

_set8 = frozenset(_set1)
print(_set1)
print(_set8)

print('\n'*2)
# cycles (for_loop)
for i in range(1, 10):
    print(i)

print('')
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
print("")

_list = ['yurii', 'valeriia', 'taras']
for name in _list:
    print(name)
    for char in name:
        print(char)

print("")

_list9 = ['yurii', 'valeriia', 'taras', 1]
for name1 in _list9:
    print(name1)
    if type(name1) == str:
        for char1 in name1:
             print(char1)
    else:
        print('Variable name is not a string')

print('')

_list11 = ['yurii', 'valeriia', 'taras', 1]
index = None
for key, name2 in enumerate(_list11):
    print(key, name2)
    if name2 == "valeriia":
        index = key
        break #to stop operation
print('index {}' .format(index))
print(_list11[index])
print('')
for key, name2 in enumerate(_list11):
    print(key, name2)
    if type(name2) == str:
        continue
        print(type(name2))
    else:
        print(type(name2))
print('')
# for key, name2 in enumerate(_list11):
#     print(key, name2)
#     if 'a' not in name2:
#         continue
#     else:
#         print(name2)
print('')

_list111 = ['yurii', 'valeriia', 'taras', 1]
index = None

for key, name22 in enumerate(_list111):
    print(key, name22)

for name22 in _list111:
    print(name22)

for i in range(1, len(_list111)):
    print(_list111[i])

for i in range(0, len(_list111)):
    print(i)
    print(_list111[i])

print('\n' * 2)
# while loop
#while condition:
    #expression
#while True:
    #print("Hi") # endless prosses

_list12 = [1, 2, 3, 4, 5, 6, 7, 8]
index = 0
while _list12:
    x = _list12.pop()
    print((x))

while len(_list12) > 0:
    print(_list12.pop())
print(bool(_list12))
print(bool(list()))

# while len(_list12) > index:
#     print(_list12[index])
#     index += 1
# print('end of the loop')

print('\n'*2)
# match case
var = 'Yurii'
if var == '':
    pass
elif var == 'a':
    pass
else:
    print('Cannot do anything')

match var:
    case 1:
        print(f'Monday')
    case 2:
        pass
    case 3:
        pass
    case _:
        print("Can do nothing")

