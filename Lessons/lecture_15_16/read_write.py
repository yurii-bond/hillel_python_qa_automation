import os

f = open('new_file.txt', mode='w')
f.writelines('Hello, world!\n')
f.close()

f = open('new_file.txt', mode='a')
f.write('Hello, there!')
f.close()

try:
    f = open('./folder/new_file.txt', mode='x')
except FileExistsError:
    os.remove('./folder/new_file.txt')
finally:
    f = open('./folder/new_file.txt', mode='x')
    f.write('Hello, there!\nThis is new file.')
    f.close()


f = open("new_file.txt", "r+")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
# print(f.read())
f.write('Bye')
f.close()

with open("new_file.txt", 'r') as f:
    print(f.readlines())

f = open("new_file.txt", 'r')
print(f.readlines())
f.close()

lines = ['Hello,', 'World!', '\n' 'Hi,', 'there!']
print(lines)
print(' '.join(lines))

with open('new_file.txt', 'a') as f:
    f.writelines(lines)

with open('new_file.txt', 'r') as f:
    print(f.readlines())



