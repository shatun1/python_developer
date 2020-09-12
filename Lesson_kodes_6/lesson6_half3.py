# with open('bytes.txt', 'wb') as f:
#     f.write(b'Hello Bytes')
#
# with open('bytes.txt', 'r', encoding='ascii') as f:
#     print(f.read())
#
# with open('bytes.txt', 'wb') as f:
#     str = 'Hello World'
#     f.write(str.encode('utf-8'))
#
#
# # with open('bytes.txt', 'rb') as f:
# #     pass
#
# with open('bytes.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
with open('bytes.txt', 'wb') as f:
    str = 'Привет Мир'
    f.write(str.encode('utf-8'))

    with open('bytes.txt', 'w', encoding='utf-8') as f:
        f.write('Привет Мир')

with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))
    s = result.decode('utf - 8')
    print(s)















