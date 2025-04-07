import datetime
import sys
import traceback
import unittest


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


def xprint(msg=''):
    try:
        print('to do')
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    print('%s[%s]: %s' % (f.f_code.co_filename, str(f.f_lineno), msg))


def test_xprint(msg=''):
    xprint()
    xprint("%d %s" % (10, "hello"))


test_xprint()


def xtry(runstr):
    ret, status = None, True
    try:
        ret = eval(runstr)
    except:
        info = traceback.format_exc()

        try:
            raise Exception
        except:
            f = sys.exc_info()[2].tb_frame.f_back
        print('%s[%s]: %s' % (f.f_code.co_filename, str(f.f_lineno), info))
        status = False
    return status, ret

class test_suit(unittest.TestSuite):
    def test1(self):
        """test suit 1"""
        self.assertEqual(1, 1)

unittest.main()

str0 = '0123456789'
str1 = str0[:]