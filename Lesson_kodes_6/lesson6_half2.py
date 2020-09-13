s = 'hello world'
# sb = b'Hello world'
# print(s)
# print(type(s))
# print(s[1])
# print(type(sb))
# print(sb)
# print(sb[1])

# print(s[1:3])
# print(sb[1:3])
# for item in sb:
#     print(item)
# sb = b"Ad"
# print(sb[0])
# print(sb[1])
s = 'Hello Nik Ник'
# sb = s.encode('ascii')
sb = s.encode('utf-8')
# print(type(sb))
# print(sb)

s = sb.decode('utf-8')

print(s)
print(type(s))


