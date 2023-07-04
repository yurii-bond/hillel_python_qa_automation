# ternary
name = "Rymma"
if name == "Rymma":
    print(name)

base = 4
new_var = None

if base % 2 == 0:
    new_var = True
else:
    new_var = False

print("The number {} is even: {}" .format(base, new_var))


base = 4
new_var = None

if base % 2 == 0:
    new_var = True
    if base < 5:
        print("base is less then 5")
    else:
        print("base is greater than 5")
else:
    new_var = False

print("The number {} is even: {}" .format(base, new_var))
# ternary
ternary_var = True if base % 2 == 0 else False   # elegance ternary
print("The number {} is even: {}" .format(base, ternary_var))


# string
string_var = 'value of a string'  # standart string1
print(string_var)

string_var2 = "value of a string2"  # standart string2
print(string_var2)

multiline_string = """
Lorem ipsum
Lorem ipsum
           Lorem ipsum
"""
print(multiline_string)            # formating

multiline_string2 = """
Lorem ipsum
Lorem ipsum
           Lorem ipsum
       Lorem ipsum
"""
print(multiline_string2)           # formating

multiline_string3 = 'jhrfgjkgjktjkjhhjhkthjhkjtkjhkjt' \
                    'jthjhtgjththhtkhkjtkjhtkjhktjhtk' \
                    'ghrkhrjhkrjkhrjkrjhkrjrkjhkhjrkjh'
print(multiline_string3)            # formating

multiline_string4 = 'jhrfgjkgjktjkjhhjhkthjhkjtkjhkjt\n' \
                    'jthjhtgjththhtkhkjtkjhtkjhktjhtk\n' \
                    'ghrkhrjhkrjkhrjkrjhkrjrkjhkhjrkjh'
print(multiline_string4)     # formating new raw

raw_string = r'Hello\n world'
print(raw_string)

raw_string2 = R'C:\Windows\Users'
print(raw_string2)

raw_string3 = 'C:\\Windows\\Users'
print(raw_string3)

linux_path = '//etc/root'
print(linux_path)
import copy

# list id
old_list = []
print(id("old list id"))

new_list = list()
print('new list id {}' .format(id(new_list)))
print('new list values {}' .format(new_list))

copy_list = new_list
print('new list id {}' .format(id(copy_list)))
print('new list values {}' .format(copy_list))


if id(new_list) == id(copy_list):
    print('The lists are identical')

shallow_copy = new_list.copy()
print('shallow_copy list id {}' .format(id(shallow_copy)))
print('shallow_copy list values {}' .format(shallow_copy))

if id(new_list) == id(shallow_copy):
    print('The lists are not identical')

copy_list.append(1)
print('_' * 15)

print('new list id {}' .format(id(new_list)))
print('new list values {}' .format(new_list))

copy_list = new_list
print('new list id {}' .format(id(copy_list)))
print('new list values {}' .format(copy_list))

# Shallow copy
print('shallow_copy list id {}' .format(id(shallow_copy)))
print('shallow_copy list values {}' .format(shallow_copy))

#nested list
import copy
# print('\n\n\n\n')
original_nested_list = [1,2,4,[0,1,2],5]
print("Nested list id {}" .format(id(original_nested_list)))
print("Nested list {}" .format(original_nested_list))

# Copy of a link
link_copy = original_nested_list
print("Link copied nested list id {}" .format(id(link_copy)))
print("Link copied nested list {}" .format(link_copy))

# Shallow copy
shallow_copy_nested_list = copy.copy(original_nested_list)
print("Shallow copied nested list id {}" .format(id(shallow_copy_nested_list)))
print("Shallow copied nested list {}" .format(shallow_copy_nested_list))

# Deep copy
deep_shallow_copy_nested_list = copy.deepcopy(original_nested_list)
print("Deep copied nested list id {}" .format(id(deep_shallow_copy_nested_list)))
print("Deep copied nested list {}" .format(deep_shallow_copy_nested_list))
print('\n\n\n')
print('_'*20)

shallow_copy_nested_list.append(9)
print("Shallow copied nested list id {}" .format(id(shallow_copy_nested_list)))
print("Shallow copied nested list {}" .format(shallow_copy_nested_list))
print("Nested list id {}" .format(id(original_nested_list)))
print("Nested list {}" .format(original_nested_list))

shallow_copy_nested_list[3].append(9)
new_nested_list = shallow_copy_nested_list[3]
print('new nested list', new_nested_list)
new_nested_list.append(9)
print('new nested list', new_nested_list)
shallow_copy_nested_list[3] = new_nested_list


print("Shallow copied nested list id {}" .format(id(shallow_copy_nested_list)))
print("Shallow copied nested list {}" .format(shallow_copy_nested_list))
print("Nested list id {}" .format(id(original_nested_list)))
print("Nested list {}" .format(original_nested_list))
print("Deep copied nested list id {}" .format(id(deep_shallow_copy_nested_list)))
print("Deep copied nested list {}" .format(deep_shallow_copy_nested_list))

print("id of a nested list from original list {}" .format(id(original_nested_list[3])))
print("id of a nested list from shallow copied list list {}" .format(id(shallow_copy_nested_list[3])))
print("id of a nested list from deep copied list {}" .format(id(deep_shallow_copy_nested_list[3])))
import copy

# dictionary

dictionary = {}
new_dictionary = dict()

new_dict = {
    'name': 'Rymma',
    'surname': 'Loranets',
    'city': 'Kyiv'
}
print(new_dict)

list_of_keys = new_dict.keys()
print(list_of_keys)

list_of_values = new_dict.values()
print(list_of_values)

list_of_items = new_dict.items()
print(list_of_items)

if 'name' in list_of_keys:
    print(new_dict['name'])

# print(new_dict['key'])
# add item to the dictionary option 1

new_dict['key'] = 'multilock'
print(new_dict['key'])
print(new_dict)

# option 2 add item to the dictionary

new_dict.update({'new_key': 'double multilock'})
print(new_dict['new_key'])
print(new_dict)

update_dict = {
    'car': 'toyota',
    'city': 'Wroclaw'
}
new_dict.update(update_dict)
print(new_dict)

# remove
popped_item = new_dict.pop('city')
print('popped_item {}' .format(popped_item))
print(new_dict)

link_copied_dict = new_dict
shallow_copy = new_dict.copy()
deep_copy = copy.deepcopy(new_dict)
print(id(link_copied_dict))
print(id(new_dict))
print(id(shallow_copy))
print(id(deep_copy))

# add nested dictionary
new_dict['nested_dict'] = update_dict
print(new_dict)