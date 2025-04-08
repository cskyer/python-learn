import re

str0 = 'spam' 'eggs'
str1 = 'spam''eggs'
print(str0, str1)

str2 = r"123\"\'456"
str3 = R"123\"\'456"
print(str2, str3)

str4 = '0123456789'
print(str4[1:3])  # 12
print(str4[1::2])  # 13579
print(str4[3:])  # 3456789
print(str4[3:-1])  # 345678
print(str4[100:])  # 返回空字符串

str5 = 'abcde'
print(str5[::-1])  # edcba
print(str5[::-2])  # eca


def doslice(instr, start, stop, step):
    newstr = ''

    for i in range(start, stop, step):
        newstr += instr[i]
    return newstr


print(doslice(str5, 3, 0, -2))

iterable = filter(lambda i: int(i) % 2 == 0, str4)
print(''.join(iterable))

list0 = list(str5)
print(list0)
list0[0] = 'A'
print(list0)
str5 = ''.join(list0)
print(str5)

print("name: {name}, age: {age}".format(name="John", age=18))
man = {'name': 'John', 'age': 18}
print("name: {name}, age: {age}".format(**man))
man_list = ['John', 18]
print("name: {0[0]}, age: {0[1]}".format(man_list))


class testobj(object):
    def __init__(self, value):
        self.value = value


testval = testobj(100)
print('value: {0.value}'.format(testval))

print("{:.0f}".format(2.5))  # 2

print("{:.2e}".format(1000000000))  # 1.00e+09

print('123' in str4)  # True
print('1232' in str4)  # False
if '123' in str4:
    print('123')

if '1232' not in str4:
    print('1232')

print(str4.find('78'))  # 7
print(str4.find('1232'))  # -1

print(set(str4))
for i in set(str4):
    print("%s count %d" % (i, str4.count(i)))

str6 = "abcdef \n12345 \nxyz"
print(str6.split())  # ['abcdef', '12345', 'xyz']
print(str6.split(' ', 1))  # ['abcdef', '\n12345 \nxyz']
print(str6.split('A'))  # ['abcdef \n12345 \nxyz']

str7 = 'str1\n\nstr2\n\rstr3\rstr4\r\n\r\n'
print(str7.splitlines())  # ['str1', '', 'str2', '', 'str3', 'str4', '']
print(str7.splitlines(True))  # ['str1\n', '\n', 'str2\n', '\r', 'str3\r', 'str4\r\n', '\r\n']

str8 = 's\te'
print(str8)  # s	e
print(str8.expandtabs())  # s       e
print(str8.expandtabs(4))  # s   e

str9 = 'old old old old old'
print(str9.replace('old', 'new'))  # new new new new new
print(str9.replace('old', 'new', 3))  # new new new old old

str10 = '\r\nhello 1213 \nworld'
print(re.sub('[\r\n]', '', str10))  # hello 1213 world

str11 = 'hello'
str_list = list(str11)
str_list.sort()
print(''.join(str_list)) # ehllo

str12 = 'ABCD'
tuple0 = ('a', 'b', 'c')
list1 = ['1', '2', '3']
print('--'.join(str12)) # A--B--C--D
print('--'.join(tuple0)) # a--b--c
print('--'.join(list1)) # 1--2--3
print(''.join(list1)) # 123


# print('\n'.join([' '.join(['%sx%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

print('\n'.join(' '.join(['%s * %s = %-3s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)))

bytes0 = b'abc'
print(type(bytes0).__name__)

print('abc'.encode('utf-8'))

bytes1 = bytes('abc', 'utf-8')
print(type(bytes1).__name__, bytes1) # bytes b'abc'

ba = bytearray(3)
print(ba)
ba[0] = 255 # 2 ** 8
print(ba)

bytes2 = bytes('中文', 'utf-8')
print(bytes2) # b'\xe4\xb8\xad\xe6\x96\x87'
print(bytes2.hex()) # e4b8ade69687

int0 = 0xefefefef
hexstr = hex(int0)
print(hexstr) # 0xefefefef
bytes3 = bytes.fromhex(hexstr[2:])
print(bytes3) # b'\xef\xef\xef\xef'