# String formatting
import datetime
name = "Rymma"
surname = 'Loranets'
digit = 0.125478
print('Name' + name) # concatenation
print(f'Name: {name}, {surname}') # analog format
print('Name: {}'. format(name))
print('Full Name: {} {}'. format(name, surname))
print('Full Name: {1} {0}' .format(name, surname)) # set the order
print(r'Raw string')
print("Show number: {}" .format(digit))
print("Show number: {:.2f}" .format(digit)) # rounds up
print("Show number: {}" .format(digit.__round__(3))) # the same rounds up

print(datetime.datetime.now()) # import datetime
print("What time is now: {:DD:MM:YYYY}".format(datetime.datetime.now())) # import datetime

print(name[1]) # show the second letter in the name

# list formatting
list = list()
print('List initiated via list(): {}' .format(list))
_list = []
print("List initiates via []: {}" .format(_list))

number_list = [1, 2, 3, 4]
print(number_list)
string_list = ["a", "b", "banana"]
print(string_list)
mixed_list = [1, 2, 3, "apple"]
print(mixed_list)

# copy list
new_number_list = number_list
print("New list after assigning: {}" .format(new_number_list))

new_number_list.append(5) # change the list
print("New list after appending 5: {}" .format(new_number_list))
print("Old list: {}" .format(number_list))

new_new_number_list = number_list.copy() # doesn`t change the list
new_new_number_list.append(6)
print(new_new_number_list)
print(number_list)

number = 5
string = "AAa"
string_st = "aaaa"
string_str = "Gdmdfe ewkrjfh wgddhgdd"
string_string = "Gdmdfe, ewkrjfh, wgddhgdd"

print(string.lower())
print(string_st.upper())
print(string_str.split())
print(string_string.split(sep=","))
print(string_st.capitalize())

number_list = [1,2,3,4,5,6]
pop_item = number_list.pop(1)
print("Pop item {}" .format(pop_item))
print("Old list after .pop(1): {}" .format(number_list))
print(number_list.index(3))
print(number_list[0])
number_list[0] = 9
print(number_list[0])
print(number_list)

# slices
subset_list = number_list[1::]
print(subset_list)

subset_list_1 = number_list[1:4]
print(subset_list_1)

list_of_numbers = number_list.copy()
list_of_numbers.extend(number_list)
list_of_numbers.append(10)
print(list_of_numbers)

subset_list_1 = list_of_numbers[3::2]
subset_list_1 = list_of_numbers[::-1] #reverse

print(subset_list_1)