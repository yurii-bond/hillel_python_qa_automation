# This is a sample Rython script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def  print_hi(name) :
# Use a breakpoint in the code line below to debug your script.
     print(f'Hi, {name}') #Press Ctrl+F8 to toggle the breakpoint


# Press the green button in the gutter to run the script.
if __name__ == '__main__' :
    print_hi('PyCharm')
    print_hi('Rymma')

# See PyCharm help at https"//www.jetbrains.com/help/pycharm

# int -> 1, 2, 3, 4..

# float ->

# bool ->

print(len("Rymma"))

# list
_list = [2, 3, 4, "Eggs", "Apple"]
print(_list)
print(_list[0])
print(_list[1])
print(_list[2])
print(_list[3])
print(_list[4])
# Display the length of the list
print("Length of the list " + str(len(_list)))

print(_list[::-1])

reversed_list = _list.reverse()
print(reversed_list)