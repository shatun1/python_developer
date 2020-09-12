# a = open('first file.txt', 'w')
a = open('first file.txt', 'r')
# a.write('Hello\n')
# a.write('World\n')
# a.writelines(['Hello\n', 'Python\n'])
# print(a.read())
for line in a:
    print(line.replace('\n', ''))
# print(a.readlines())
a.close()
with open('first file.txt', 'r') as a:
    for line in a:
        print(line.replace('\n', ''))
print('file closed')












