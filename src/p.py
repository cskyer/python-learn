import datetime

def print_long_line():
    print("The door bursts open. A MAN and WOMAN enter, drunk and giggling,\
horny as hell.No sooner is the door shut than they're all over each other,\
ripping at clothes, pawing at flesh, mouths locked together.")





print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
print_long_line()

for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{text:*{align}20}'.format(align=align, text=text))

width = 5
for num in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

print("repr() shows quotes: {!r}; str() does't: {!s}".format('test1', 'test2'))