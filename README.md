# Python 入门

## 1. Python 环境变量
Python语言是一种动态的脚本语言, 需要动态解析, 当前分为主流的**Python2**和**Python3**版本, 它们的语法是不安全兼容的, 也即**Python3**通常无法直接执行**Python2**版本的`.py`文件.

所以在安装之前需要确定需要安装的Python版本. 由于不同的应用转件需要不同的Python开发环境, 可能需要同时安装多个Python版本, 那么防止冲突, 可以使用`virtualenv`实现安装环境的隔离.

### 1.1 简单安装
这里以**Ubuntu**为例, 安装命令异常简单:
```shell
sudo apt-get install python3.6
```

安装后通过查看版本验证环境是否安装成功:
```shell
python3.6 --version
```
与此同时**Python**的转简报包管理器**pip**也被一同安装了:
```shell
pip -V
```
通过**pip**安装的软件包将放置到`/usr/local/lib/python3.6/dist-packages`下

直接使用`apt-get install`安装多个版本的**Python**可能导致**pip**包管理混乱: 此时会出现多个以pip开发的命名, 例如**pip2**, **pip3**. 但是这并不意味着他们就分别对应着**Python2**和**Python3**, 通过执行`pip -V`查看它对应的**python**解释器版本, 这样使用`pip install`就会安装到对应版本解释器的**dist-packages**文件夹下.

### 1.2 多版本安装
### 1.3 pip 管理软件包
#### 1.3.1 pip安装软件包
pip安装python软件包非常方便, 首先通过`pip -V`查看是否是我们要安装的python环境. 如果不是,这要安装多版本方式重新安装,或是对pip重命名. 如果所有用户都可以使用该开发环境, 那么需要再安装命令前使用`sudo`安装
```shell
whereis pip
```
**`whereis`**命令查看pip命令. pip通常通常是一个软连接

```shell
pip install numpy
```

如果我们想更新已有软件包, 命令为:
```shell
# 或者 pip install -U numpy
pip install --upgrade numpy
```

#### 1.3.2 pip卸载软件包
卸载与安装相对应, 使用`uninstall`命令, 例如:
```shell
pip uninstall numpy
```
#### 1.3.3 pip查看软件包
查看所有通过当前pip安装的软件包:
```shell
pip list
```
**pip show**查看单个软件包信息, 包含版本, 官网, 作者, 发布协议, 安装路径和对其他软件包的依赖关系:
```shell
pip show
```

#### 1.3.4 查看pip帮助
普通的linux命令使用`man cmd`查看帮助信息, 但是pip是python脚本, 查看帮助信息方式为
```shell
# 或是 pip --help
pip -h
```

## 2. 打印输出和格式化
### 2.1 直接打印输出
```shell
print(value, ..., sep='', end='\n', file=sys.stdout, flush=False)
```
`print()`内置函数用于打印输出, 默认打印到标准输出`sys.stdout`
```python
print('Hello %s: %d' % ('world', 100))
print('end')
```
`print()`函数会自动在输出行后添加换行符.

### 2.2 不换行打印输出
```python
strs = '123'
for i in strs:
    print(i),
print('end')
```
通过在`print()`语句后添加**`,`**, 可以不换行, 但会在输出后添加一个空格.

`print()`函数支持`end`参数, 默认为换行符, 如果句尾有**逗号**, 则默认为空格, 可以指定end参数为空字符, 来避免输出空格
```python
strs = '123'
print(strs, end='')
print('end')
# 123end
```

使用`sys.stdout`模块中的`write()`函数可以实现直接输出.
```python
import sys
strs = '123'
for i in strs:
    sys.stdout.write(i)
print('end')
```

### 2.3 分割符打印多个字符串
`print()`函数支持一次输入多个打印字符串, 默认是以空格分割, 可以通过`sep`参数指定分割符号.
```python
str0 = '123'
str1 = '456%s' # 字符串中的%s不会被解释为格式化字符串

# 含有%s的格式化字符串只能有一个, 且位于最后
print(str0, str1, '%s%s' %('end', '!'))
print(str0, str1, '%s%s' %('end', '!'), sep='*')
print('%s*%s*end!' %(str0, str1)) # 手动指定分隔符
# 123 456%s end!
# 123*456%s*end!
# 123*456%s*end!
```

### 2.4 格式化输出到变量
```python
tmpstr = ('Number is: %d' % 100)
print(tmpstr)

hexlist = [('%02x' % ord(x))for x in tmpstr]
print(''.join(hexlist))
print('end')
```
通过打印字符串的ascii码, 可以看到换行符是`print()`函数在打印时追加的, 而并没有格式化到变量中.

### 2.5 长行打印输出
```python
def print_long_line():
    print("The door bursts open. A MAN and WOMAN enter, drunk and giggling,\
horny as hell.No sooner is the door shut than they're all over each other,\
ripping at clothes, pawing at flesh, mouths locked together.")

print_long_line()
#The door bursts open. A MAN and WOMAN enter, drunk and giggling,horny as hell.No sooner is the door shut than they're all over each other,ripping at clothes, pawing at flesh, mouths locked together.
```
如果`print()`函数要打印很长的数据, 则可使用右斜杠将一行的语句分为多行进行编辑, 编译器在执行时, 将它们作为一行解释, 注意右斜杠后不可有空格, 且其后的行必须定格, 否则头部空格将被打印.

```python
def print_long_line():
    print('''The door bursts open. A MAN and WOMAN enter. drunk and giggling,
horny as hell.No sooner is the door shut than they're all over each other,
ripping at clothes, pawing at flesh, mouths locked together.''')
```
使用一对三引号和上述代码是等价的, 以上写法每一行字符串必须定格, 否则对齐空格将作为字符串内容被打印, 这影响了代码的美观. 可以为每行添加引号来解决这个问题.

```python
def print_long_line():
    print("The door bursts open. A MAN and WOMAN enter. drunk and giggling,"
          "horny as hell.No sooner is the door shut than they're all over each other,"
          "ripping at clothes, pawing at flesh, mouths locked together.")
print_long_line()
```

### 2.6 打印含有引号的字符串
Python使用单引号或者双引号来表示字符, 那么当打印含有单双引号的行时如何处理呢?
```python
print("It's a dog!") # It's a dog!
print('It is a "Gentleman" dog!') # It is a "Gentleman" dog!
print('''It's a "Gentleman" dog!''') # It's a "Gentleman" dog!
```

### 2.7 打印输出到文件
```shell
print(value, ..., sep='', end='n', file=sys.stdout, flush=False)
```
`print()`函数支持`file`参数来指定输出文件的描述符, 默认值是标准输出`sys.stdout`, 与此对应, 标准的错误输出是`sys.stderr`, 当然也可以指定普通文件描述符.
输出到磁盘文件时, 为了保证实时性, 根据实际情况可能需要把`flush`参数设置为`True`.
```python
logf = open('logfile.log', 'a+')
print('123', file=logf, flush=True)
```

### 2.8 对齐输出(左中右对齐)
通过`print()`函数可以直接实现左对齐输出. `print()`函数不能动态置顶对齐的字符数, 也不能指定其他填充字符, 智能使用默认的空格进行填充.
```python
man=[['Name', 'John'], ['Age', '25'], ['Address', 'Beijing China']]
for i in man:
    print('%-10s: %s' % (i[0], i[1]))
#Name      : John
#Age       : 25
#Address   : BeiJing China
```
Python中字符串处理函数`ljust()`, `rjust()`和`center()`提供了更强大的对齐输出功能.
```python
print('123'.ljust(5) == "123  ")
print('123'.rjust(5) == '  123')
print('123'.center(5) == ' 123 ')

print('123'.ljust(5, '*'))
print('123'.rjust(5, '*'))
print('123'.center(5, '*'))
#True
#True
#True
#123**
#**123
#*123*
```
左对齐`ljust()`示例, 计算特征量的长度, 决定动态便宜的字符数.
```python
man=[['Name', 'John'], ['Age', '25'], ['Address', 'Beijing China']]
len_list = [len(x[0])for x in man]
offset = max(len_list) + 5
for i in man:
    print('%s: %s' % (i[0].ljust(offset), i[1]))
#Name        : John
#Age         : 25
#Address     : BeiJing China
```
居中对齐示例, 这里以字符`~`填充.
```python
lines = ['GNU GENERAL PUBLIC LICENSE', 'Version 3, 29 June 2007']
len_list = [len(x) for x in lines]
center_num = max(len_list) + 30
for i in lines:
    print(i.center(center_num, '~'))

#~~~~~~~~~~~~~~~GNU GENERAL PUBLIC LICENSE~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~Version 3, 29 June 2007~~~~~~~~~~~~~~~~~
```

### 2.9 格式化输出
更多格式化输出请参考[字符串格式化]()

#### 2.9.1 百分号格式化
与C语言类似, python 支持百分号格式化, 并且基本保持了一致.

##### 2.9.1.1 数值格式化
整数格式化符号可以指定不同进制:

| 符号    | 含义         |
|-------|------------|
| %o    | oct八进制     |
| %d    | dec十进制     |
| %x    | hex十六进制    |
| %X    | hex十六进制大写  |

```python
print('%o %d %x %X' % (10, 10, 10, 10))

# 12 10 a A
```
浮点数可以指定保留的小数位数,或使用科学计数法:

| 符号 | 含义                                             |
|----|------------------------------------------------|
| %f | 保留小数点后面6位有效数字, `%.2f`, 保留2位小数位                 |
| %e | 保留小数点后面6位有效数字, 指数形式输出, `%.2`, 保留2位小数位, 使用科学计数法 |

```python
print('%f' % 1.23)

print('%.2f' %1.23456)

print('%e' % 1.23)

print('%.3e' % 1.23)
```

##### 2.9.1.2 字符串格式化
| 符号     | 含义             |
|--------|----------------|
| %s     | 格式化字符串         |
| %10s   | 右对齐, 空格占位符10位  |
| %-10s  | 左对齐, 空格占位符10位  |
| %.2s   | 截取2个字符串        |
| %10.2s | 10位占位符, 截取两个字符 |
```python
print('%s' % 'hello world')

print('%20s' % 'hello world')

print('%-20s' % 'hello world')

print('%.2s' % 'hello world')

print('%10.2s' % 'hello world')

print('%-10.2s' % 'hello world')
```

#### 2.9.2 format 格式化
`format()`是字符串对象的内置对象, 它提供了比百分号格式化更强大的功能, 例如调整参数顺序, 支持字典关键字等. 它该函数吧字符串当成一个模版, 通过传入的参数惊醒格式化, 并且使用大括号`{}`作为特殊字符代替`%`
##### 2.9.2.1 未知匹配
未知匹配有以下几种方式:
- 不带编码, 即`{}`, 此时按顺序匹配
- 带数字编号, 可调整顺序, 即`{1}`、`{2}`按编号匹配
- 带关键字, 即`{name}`、`{name1}`, 按字典键匹配
- 通过对象属性匹配, 例如: `obj.x`
- 通过下标索引匹配, 例如: `a[0]`、`a[1]`
```python
# 默认从左到右匹配
print('{} {}'.format('hello', 'world')) # hello world

# 按数字编号匹配
print('{0} {1}'.format('hello', 'world')) # hello world
print('{0} {1} {1}'.format('hello', 'world')) # hello world world

# 关键字匹配
print('{w} {h}'.format(h='hello', w='world')) # world hello
```
通过对象属性匹配, 可以方便地实现对象的`str`方法:
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    # 通过对象属性匹配
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)
```
对于元组, 列表, 字典等支持索引的对象, 支持使用索引匹配位置
```python
point = (0, 1)
print('X: {0[0]}, Y: {0[1]}'.format(point))

m = { 'a': 'a', 'b': 'b' }
print('A: {0[a]}, B: {0[b]}'.format(m))
```

##### 2.9.2.2 数值格式转换
| 符号  | 含义                                                   |
|-----|------------------------------------------------------|
| 'b' | 二进制. 将数字以2为基数进行输出.                                   |
| 'c' | 字符. 在打印之前将整数转换成对应的unicode字符串.                        |
| 'd' | 十进制整数. 将数字以10为基数进行输出                                 |
| 'o' | 八进制. 将数字以8为基数进行输出                                    |
| 'x' | 十六进制.将数字以16为基数进行输出, 9以上的位数进行输出                       |
| 'e' | 幂符号. 用科学技术服打印数字.用'e'表示幂                              |
| 'g' | 一般格式. 将数值以fixed-point格式输出. 当数值特别大的时候, 用幂形式打印.        |
| 'n' | 数字. 当值为整数时和'd'相同, 值为浮点数时和'g'相同. 不同的是它会根据区域设置插入数字分隔符. |
| '%' | 百分数. 将数值乘以100然后以fixed-point('f')格式打印, 值后面会有一个百分号.    |
```python
# 整数格式化
print('{0:b}'.format(3))
print('{:c}'.format(97))
print('{:d}'.format(20))
print('{:o}'.format(20))
print('{:x}, {:X}'.format(0xab, 0xab))

print('{:e}'.format(20))
print('{:g}'.format(20.1))
print('{:f}'.format(20))
print('{:n}'.format(20))
print('{:%}'.format(20))
```
各种进制转换
```python
print('int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}'.format(42))

# 在前面价`#`, 自动添加进制前缀
print('int: {0:#d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}'.format(42))
```
##### 2.9.2.3 位数对齐和补全
- `<`(默认)左对齐、`>`右对齐、`^`中间对齐、`=`(只用于数字)在小数点后进行补齐
- 取字符数或者位数`{:4s}`、`{:.2f}`
```python
# 默认左对齐
print('{} and {}'.format('hello', 'world'))

#取10位左对齐, 取10位右对齐
print('{:10s} and {:>10s}'.format('hello', 'world')) # hello      and      world

# 取10位中间对齐
print('{:^10s} and {:^10s}'.format('hello', 'world')) #  hello    and   world

# 使用`*`填充
print(':*^30s'.format('center'))

# `=`只能应用于数字, 这种方法可用`>`代替
print('{:0=30}'.format(30))
```

##### 2.9.2.4 正负号和百分显示
正负号显示通过`%+f`, `%-f`和`%f`实现:
```python
# 总显示符号
print('{:+f}; {:+f}'.format(3.14, -3.14)) # '+3.140000; -3.140000'
# 若是+数, 则在前面留空格
print('{: f}; {: f}'.format(3.14, -3.14)) # ' 3.140000; -3.140000'
# 负数时显示`-`, 与`{:f}; {:f}` 一致
print('{:-f}; {:-f}'.format(3.14, -3.14))
```
打印百分号, 注意会自动计算百分数:
```python
print('Correct answers: {:.2%}'.format(1/2.1)) # 'Correct answers: 47.62%'
# 以上代码等价于
print('Correct answers: {:.2f}%'.format(1/2.1 * 100))
```

##### 2.9.2.5 千位分割数字
用`,`分割数字, 每一千进位:
```python
print('{:,}'.format(1234567890)) # 1,234,567,890
```

##### 2.9.2.6 时间格式化
```python
import datetime

d = datetime.datetime.now()
print('{:%Y-%m-%d %H:%M:%S}'.format(d)) # 2025-04-03 18:30:22
```

##### 2.9.2.7 占位符嵌套
```python
for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{text:*{align}20}'.format(align=align, text=text))

# left****************
# *******center*******
# ***************right
```
```python
width = 5
for num in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111 
#     8     8    10  1000 
#     9     9    11  1001 
#    10     A    12  1010 
#    11     B    13  1011
```

##### 2.9.2.7 repr 和 str 占位符
- `repr()`: `{!r}` 带引号
- `str()`: `{!s}` 不带引号
```python
print("repr() shows quotes: {!r}; str() does't: {!s}".format('test1', 'test2'))
# repr() shows quotes: 'test1'; str() does't: test2
```

##### 2.9.2.9 format缩写形式
可在格式化字符串前加`f`以达到格式化的目的, 在`{}`里加入对象, 这是`format`的缩写形式:

```python
a = 'hello'
b = 'world'
print(f"{a} {b}") # hello world
```

## 3. 调试和性能优化
### 3.1 定制调试信息
#### 3.1.1 打印文件名和行号
借助`sys.exc_info`模块自己捕获异常, 来打印调试者信息, 同时打印当前调试信息.
```python
import sys


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
#to do
#/Users/.../python-learn/src/p.py[36]: 
#to do
#c/Users/.../python-learn/src/p.py[37]: 10 hello
```

#### 3.1.2 异常时打印函数调用栈
异常时, Python默认处理方式将中断程序的运行, 有时我们希望程序继续进行. 我们可以通过`try`语句结合`sys.exc_info()`和`traceback`模块抛出异常, 并给出提示信息.
```python
import traceback
import sys


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
```
`xtry()`函数接受一个字符串作为表达式, 与`xprint()`函数类似, 在异常出现时打印文件名和行号, 并且借助`traceback`模块格式化调用栈信息. 同时返回是否出现异常和表达式的结果. `status`为`True`表示可以正常执行, 否则出现异常.

### 3.2 断言和测试框架
#### 3.2.1 assert语句
`0`和`False`是等价的, `1`和`True`是等价的. 当表达式为假时抛出异常.


断言语句assert在表达式为假时抛出断言异常语句`AssertionError`并终止程序执行. 这在调试和测试代码时非常有用.
```python
assert isinstance('str', str)
assert 1 == 2
# assert 0
# assert False
```
断言语句还支持一个格式化字符串参数, 以逗号区分, 用于提供更明确的断言信息.
```python
oct_num = -1
assert oct_num in range(10), 'Oct number must be in (%d - %d)' % (0, 9)
```
专门的测试框架通常工具通常会对Python自带的断言功能进行扩展, 已提供更强大的测试和诊断功能.

#### 3.2.2 单元测试模块 unittest
单元测试主要针对最基础的代码可测单元进行测试, 比如一个表达式, 一个变量值的合法性, 一个函数的入参和出参规格直至一个模块的功能. 著名的极限编程中的测试驱动开发(TDD: Test-Driven Development)就是以单元测试为基础的开发方式, 单元测试代码在编写功能代码时同时进行, 每次对代码的增删和缺陷修复都要进行单元测试, 以保证代码是符合预期的. 这很像在修路的同时, 同时修筑了足够高的防护栏, 而在赛车选手变换各类驾驶技巧时, 不会冲出赛道.


可以这样说, 只要单元测试没有漏洞, 编码者就有底气说问题已经彻底修复了.

##### 3.2.2.1 unittest测试用例
Python自带单元测试框架`unittest`, 它将测试用例定义为`TestCase`类. 编写单元测试时, 首先需要编写一个测试类, 并继承`unittest.TestCase`, 类中的方法必须以`test`开头:
```python
import unittest


class test_suit1(unittest.TestSuite):
    def test1(self):
        """test suit 2""" # 测试用例描述, 同用例标题一并显示测试报告里
        self.assertEqual(1, 1) # 测试用例断言, 期望`1 == 1`, 否则抛出异常
```
测试结果的第一行给出所有测试用例的结果, `.`和 `F` 分别表示测试通过或失败, 每一个测试用例对应一个字符.


接着给出出错所用例的类名和描述, 并附上对应出错的文件和行号等信息. 最后给出总的运行用例数和测试耗时.


上面的示例直接通过`unittest.main()`函数运行, 也可以在命令中调用`unittest`模块, 注意要注释掉`unittest.main()`
```shell
python3 -m unittest unit_sample.py
```
`unittest`目前支持如下断言函数:

| 名称                          | 等价                     |
|-----------------------------|------------------------|
| `assertEqual(a, b)`         | `a == b`               |
| `assertTrue(x)`             | `bool(x)` is `True`    |
| `assertFalse(x)`            | `bool(x)` is `False`   |
| `assertIs(a, b)`            | `a` is `b`             |
| `assertIsNot(a, b)`         | `a` is not `b`         |
| `assertIsNone(x)`           | `x` is `None`          |
| `assertIsNotNone(x)`        | `x` is not `None`      |
| `assertIn(a, b)`            | `a in b`               |
| `assertNotIn(a, b)`         | `a not in b`           |
| `assertIsInstance(a, b)`    | `isinstance(a, b)`     |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` |

## 4. 字符串处理
字符串(`str`)是Python中最常用的数据类型, 可以使用单引号或双引号来创建字符串. 注意:
- Python不支持单字符类型(对应C语言中的`char`), 单字符在Python中也是字符串类型.
- 字符串是不可变类型, 即无法直接修改字符串的某一索引对应的字符, 需要转换为列表处理. 可以认为字符串是特殊元组类型.
### 4.1 创建字符串变量
#### 4.1.1 直接赋值创建字符串
Python中通过各类引号(**单引号**、**双引号**和**三引号**)标识字符串.
```python
str0 = 'hello'
str1 = "hello"
str2 = '''hello'''
str3 = """hello"""

# 多行
str4 = "hello"\
" world"
str5 = """hello\
 world"""

for i in range(6):
    print(eval('str' + str(i)))
```

#### 4.1.2 由字符串组合生成新字符串
- `+`运算符实现字符串的拼接
```python
str0 = "Name:"
str1 = "john"
str2 = str0 + ' ' + str1
str3 = 'Age:' + ' ' + str(18)
```
- `*`运算符实现字符串重复
```python
str0 = '~' * 10
```
操作符必须作用在`str`类型上, 如果为其他类型必须使用`str()`函数进行转换, 例如这里的`str(18)`


新字符串可以通过**字符串合并**, **转换**, 切片, 分割和替换等方式得到.

#### 4.1.3 复制字符换
复制字符串是护理字符串的常用操作, 通过切片实现.
```python
str0 = ["0123456789"]
str1 = str0[:]
```

#### 4.1.4 其他类型转换为字符串
`str()`内建函数可以将多种其他数据类型转化为字符串.
```python
print(str(1)) # 1
print(str(1.0)) # 1.0
print(str(1+1j)) # (1+1j)
print(str(['12', 'anc'])) # [12, 'abc']
print(str((12, 'abc'))) # (12, 'abc')
print(str({'Name': 'John', 'Age': '18'})) # {'Name': 'John', 'Age': '18'}
```
可以注意到, 将复杂数据类型转化为字符串时会保留其语法格式, 若要进行个细致的操作, 需要相应函数帮助, 比如`str.format()`, 它们提供了异常强大的转换功能.

### 4.2 特殊字符的转义处理
所谓特殊字符, 有些字符是不显示的, 比如回车换行符, 有些是用来做特殊控制的, 比如单引号在代码中表示字符的开始或结束, 这些字符必须用可见的字符来表示, 但是可见字符已经表示了自身, 解决方案就是通过在普通字符前添加前缀, 实现对普通字符的转义, `\`被称为转义符.

#### 4.2.1 ASCII码值转义
`\yyy`和`\xyy`分别表示三位八进制数和二位十六进制数ascii码对应的字符, 8进制如果不够3位, 前面必须补`0`, 比如`099`
```python
str0 = "A"
print(ord(str0[0]))
print('0x%02x' % (ord(str0[0])))
print('%o' % ord(str0[0]))
```

#### 4.2.2 Unicode码值转义
在字符串中, 我们可以使用`\x0d`和`\r`表示回车符号, 那么对于中文字符来说, 也同样有两种表示方式:
```python
str0 = '\u4f60'
str1 = '你'
print(str0, str1)
```
`0x46f0`是中文字符你的Unicode码值, 可以采用`'\u'`前缀加Unicode码值的方式表示一个中文字符, 它和'你'是等价的. 注意Unicode码值和`UTF-8`编码的区别, 参考[常见的编码方式]()

#### 4.2.3 引号转义
对于字符串中的单双引号可以进行转义处理, 也可以互斥使用单双引号:
```python
str0 = '123"456'
str1 = "123'456"
str2 = """123'''456"""
print(str0, str1, str2)
```
既有单引号又有双引号, 可以使用转义, 或者三引号处理.
```python
str0 = "123\"\'456"
str1 = """123'''456"""
```
可以指定多个字符串, 字符串中间的空格被忽略
```python
str0 = 'spam' 'eggs'
str1 = 'spam''eggs'
print(str0, str1) #spameggs spameggs
```

#### 4.2.4 原生字符
使用原生(**raw**)字符串输入标志`r`或`R`可以免除大量转义, 直接原样输出.
```python
str2 = r"123\"\'456"
str3 = R"123\"\'456"
print(str2, str3) #123\"\'456 123\"\'456
```
**注意:** 原生字符串必须保证代码行符合编码逻辑, 也即起止标志(引号)必须配对, 比如字符串`r"\"`是不能被解析的, 右斜杠和引号同时存在令解析器认为字符串没有结束符. 将提示"SyntaxError: EOL while scanning string"错误

### 4.3 访问字符串中的值
要理解下标和切片访问方式, 必须理解字符串的索引. 和C语言类似, 字符串中每一个字符都有一个唯一的自然数和它对应, 从`0`开始.

#### 4.3.1 负数索引编号
与C语言不通, Python语言提供了负数下标, 方便从字符串尾部进行访问.下标从`-1`向前依次递减.

#### 4.3.2 下标直接访问
```python
str0 = 'Python'
print(str0[0], str0[-1])
```

#### 4.3.3 切片取子字符串
通过提供起止索引来访问子字符串的方式称为**切片**. 下标超出最大索引, 或者起始索引大于终止索引, 返回空字符串.


切片操作支持指定步长, 格式为`[start:stop:step]`, 前两个索引和普通切片一样.
```python
str4 = '0123456789'
print(str4[1:3]) # 12
print(str4[1::2]) # 13579
print(str4[3:]) # 3456789
print(str4[3:-1]) # 345678
print(str4[100:]) # 返回空字符串
```
切片操作的步长可以为负数, 通常用于翻转字符串, 此时如果不通过默认值start和stop则默认为尾部和头部索引:
```python
str5 = 'abcde'
print(str5[::-1]) # edcba
print(str5[::-2]) # eca
```
切片操作等价于:
```python
str5 = 'abcde'
def doslice(instr, start, stop, step):
    newstr = ''

    for i in range(start, stop, step):
        newstr += instr[i]
    return newstr
print(doslice(str5, 3, 0, -2))
```

#### 4.3.4 过滤特定的字符
`filter(function or None, iterable) -> filter object`

内建函数`filter()`可以对迭代数据类型执行特定的过滤操作. 返回迭代对象.

取数字组成的字符串中的偶数字符, 并得到新字符串
```python
str4 = '0123456789'
iterable = filter(lambda i: int(i) % 2 == 0, str4)
print(''.join(iterable))
```

### 4.4 更新字符串中的值
字符串不允许直接修改, 只能转换成其他类型更新后再转回字符串.

#### 4.4.1 转换为列表再转回
字符串转换为列表后, 每一个字符串称为列表中的一个元素, 此时通过索引就可以更新每一个字符, 然后在通过`join()`函数换回字符串.
```python
str5 = 'abcde'
list0 = list(str5)
print(list0)
list0[0] = 'A'
print(list0)
str5 = ''.join(list0)
print(str5)
# ['a', 'b', 'c', 'd', 'e']
# ['A', 'b', 'c', 'd', 'e']
# Abcde
```

### 4.5 字符串格式化
更多格式化输出请参考[格式化输出]()

#### 4.5.1 常用格式化符号
| 符号   | 描述                    |
|------|-----------------------|
| `%c` | 格式化字符及其ASCII码         |
| `%s` | 格式化字符串                |
| `%d` | 格式化整数                 |
| `%u` | 格式化无符号整型              |
| `%o` | 格式化无符号八进制数            |
| `%x` | 格式化无符号十六进制数           |
| `%X` | 格式化无符号十六进制数(大写)       |
| `%f` | 格式化浮点数字, 可指定小数点后的精度   |
| `%e` | 用科学计数法格式化浮点数          |
| `%E` | 作用同`%e`, 用科学计数法格式化浮点数 |
| `%g` | `%d`和`%e`的简写          |
| `%G` | `%d`和`%E`的简写          |
| `%`  | 直接输出`%`               |

### 4.5.2 转换符格式化
转换符格式化(conversion specifier)可以引用字典变量. 转换符的格式为:`%(mapping_key)flags`, `mapping_key`指明引用变量的名称, `flags`指明转换格式.
```python
print('%(language)s has %(number)01d quote types.' % { 'language': 'Python', 'number': 2 })
```
更复杂的格式化使用`str.format()`更便捷.

#### 4.5.3 format函数格式化
Python2.6开始, 新增了一种格式化字符串的函数`str.format()`, 它增强了字符串格式化的功能. 基本语法是通过`{}`和`:`来代替以前`%`. `format`函数可以接收不限个参数, 未知可以不按顺序.

##### 4.5.3.1 为格式化参数指定顺序
```python
print("{} {}".format("abc", "123"))
print("{0} {1}".format("abc", "123"))
print("{1} {0} {1}".format("abc", "123"))
```

##### 4.5.3.2 通过名称或索引指定参数
直接通过名称引用, 或者可以通过字典和列表传递参数.

```python
print("name: {name}, age: {age}".format(name="John", age=18))
man = {'name': 'John', 'age': 18}
print("name: {name}, age: {age}".format(**man))
man_list = ['John', 18]
print("name: {0[0]}, age: {0[1]}".format(man_list))
```

##### 4.5.3.3 直接传递对象
```python
class testobj(object):
    def __init__(self, value):
        self.value = value

testval = testobj(100)
print('value: {0.value}'.format(testval))
```

##### 4.5.3.4 数字格式化
`str.format()`提供了强大的数字格式化方法.
- `^`,`<`,`>`分别是句号左对齐,右对齐, 后面带宽度
- `:`好后面带填充的字符, 只能是一个字符, 不指定则默认用空格填充
- `+`表示在正数前显示`+`号, 负数前显示`-`,(空格)表示在正数前加空格
- `b`、`d`、`o`、`x/X`分别表示二进制、十进制、八进制、十六进制

| 数字         | 格式        | 输出        | 描述                      |
|------------|-----------|-----------|-------------------------|
| 3.1415926  | `{:.2f}`  | 3.14      | 保留小数点后两位                |
| 3.1415926  | `{:+.2f}` | +3.14     | 带符号保留小数点后两位             |
| -1         | `{+.2f}`  | -1.00     | 带符号保留小数点后两位             |
| 2.71828    | `{:.0f}`  | 3         | 不带小数, `<=0.5`舍, `>0.5`入 |
| 5          | `{:0>2d}` | 05        | 数字补零(填充左边, 宽度为2         |
| 5          | `{:x<4d}` | 5xxx      | 数字补x(填充右边, 宽度为4         |
| 10         | `{:x<4d}` | 10xx      | 数字补x(填充右边, 宽度为4)        |
| 1000000    | `{:,}`    | 1,000,000 | 以逗号分割的数字格式              |
| 0.25       | `{:.2%}`  | 25.00%    | 百分比格式                   |
| 1000000000 | `{:.2e}`  | 1.00e+09  | 指数记发                    |
| 10         | `{:10d}`  | 13        | 右对齐(默认, 宽度10)           |
| 10         | `{:<10d}` | 13        | 左对齐(宽度为10)              |
| 10         | `{:^10d}` | 13        | 中间对齐(宽度为10)             |
针对不同的进制, `str.format()`提供了以下格式化方法:

```python
print('{:b}'.format(11))  # 二进制 1011
print('0b{:0>5b}'.format(11)) # 二进制, 数字补零(填充左边, 宽度为5) 0b01011
print('{:d}'.format(11))     # 十进制
print('{:o}'.format(11))     # 八进制
print('{:x}'.format(11))     # 16进制
print('{:#x}'.format(11))    # 16进制带0x前缀
print('{:#X}'.format(11))    # 16进制带0X前缀
```

##### 4.5.3.5 转义大括号
由于大括号在`format()`函数作为参数引用的特殊用途, 如果要在字符串中输出大括号, 则使用大括号`{}`来转义大括号.

```python
print("{0} is {{0}}".format('value'))
print("{0} is ".format('value') + '{0}')
```
应采用字符串连接的方式来组合含有大括号的字符串, 这样更清晰.

### 4.6 字符串查找和统计
#### 4.6.1 判断字符串存在
使用`in`和`not in`判定字符串是否存在
```python
str4 = '0123456789'
print('123' in str4) # True
print('1232' in str4) # False
if '123' in str4:
    print('123')

if '1232' not in str4:
    print('1232')
```

#### 4.6.2 指定范围查找字符串
本小结主要针对`find()`、`index()`和`rindex()`函数的使用.

- `S.find(sub, [,start, [,end]]) -> int`

    `find()`在`[start, end)`索引范围内查找`sub`字符串, 如果存在返回第一个的索引, 否则返回`-1`
- `S.index(sub, [,start [, end]]) -> int`

    `index()`函数与`find()`函数非常类似, 找不到时会抛出ValueError异常
- `S.rindex(sub [,start [,end]]) -> int`

    `rindex()`与`index()`作用类似, 从右侧开始查找
```python
str4 = '0123456789'

print(str4.find('78')) # 7
print(str4.find('1232')) # -1
```

#### 4.6.3 字符是否以子串开始或结束
- `S.endswith(suffix [,start [, end]]) -> bool`
    `endswith()`函数返回`True`或`False`, start和end指定查找返回, 可选
- `S.startwith(prefix [,start [, end]]) -> bool`
    与`endswith()`类似, 判断字符串是否以`prefix`子串开始

```python
str4 = '0123456789'
print(str4.endswith('89', 0, 9))
print(str4.startswith('01'))
```

#### 4.6.4 字符串最大最小值
`max()`和`min()`用于获取字符串中的最大ASCII码和最小ASCII码的字符.
```python
str4 = '0123456789'

print(min(str4), max(str4))
```

#### 4.6.5 统计字符串出现的次数
`S.count(sub, [, start [, end]]) -> int`

`count()`返回str在string里面出现的次数, 如果start或者end指定则返回指定范围内str出现的次数

```python
str4 = '0123456789'
print(str4.count('0', 0, 9))
print(str4.count('0', 1, 9))
print(str4.count('abc'))
```

#### 4.6.6 统计字符串不同字符数
`set()`函数可以对字符串进行归一化处理. 需要注意的, `set()`函数返回的字符集合是无序的.

```python
str4 = '0123456789'

print(set(str4))

for i in set(str4):
    print("%s count %d" %(i, str4.count(i)))
```

### 4.7 字符串大小写转换
#### 4.7.1 首字母转化为大写
`S.capitalize() -> string`

`capitalize()`将字符串的第一个字母变成大写, 其他字母变小写.

#### 4.7.2 转为大写或小写
`S.upper() -> string`

`S.lower() -> string`

`upper()`和`lower()`分别对字符串进行大写和小写转换.

```python
str0 = 'Hello World'
print(str0.upper())
print(str0.lower())
```

#### 4.7.3 大小写反转
`S.swapcase() -> string`

大写变小写, 小写变大写, 非字符字符保持不变

```python
str0 = 'Hello World'
print(str0.swapcase())
```

#### 4.7.4 标题化字符串
`S.title() -> string`

`title()`返回'标题化'的字符串, 即所有单词都是以大写开始, 其余字母均为小写.

```python
str0 = 'HI world'
print(str0.title())
```

### 4.8 字符串对齐和填充
关于字符串对齐参考 [打印输出到文件]()

`S.zfill(width) -> string`

`zfill()`函数返回指定长度的字符串, 原字符串右对齐, 前面填充字符`0`

```python
str0 = 'Hello world'
print(str0.zfill(20))
print(str0.rjust(30, '0'))
```
由示例可以得知`zfill(width)`和`rjust(width, '0')`是等价的.

### 4.9 字符串strip和分割
#### 4.9.1 strip字符串
`S.strip([chars]) -> string or unicode`

`strip()`函数默认将字符串头部和尾部的空白符(whitespace)移除. **注意:** 该函数不删除中间部分的空白符.

也可以通过chars参数指定出的字符集.

**PoSIX**标准给出空白符包括如下几种:

| 符号      | 描述                    |
|---------|-----------------------|
| `space` | 空格                    |
| `\f`    | 换页(form feed)         |
| `\n`    | 换行(newline)           |
| `\r`    | 回车(carriage return)   |
| `\t`    | 水平制表符(horizontal tab) |
| `\v`    | 垂直制表符(vertical tab)   |

```python
str0 = "  hello  \r\n\t\v\f"
str1 = "00000hell10o10000"

print(str0.strip())  # 去除首尾空白符号
print(str1.strip('01')) # 去除首尾符号 1 和 0
```

如果参数chars为unicode类型, 则首先将要处理的字符串S转换为unicode类型

`S.lstrip([chars]) -> string or unicode`

`S.rstrip([chars]) -> string or unicode`

`lstrip()`和`rstrip()`方法和`strip()`类似, 只是只去除头部或者尾部的空白符, 或指定的字符集中的字符.

#### 4.9.2 单次分割
`S.partition(sep) -> (head, sep, tail)`

`partition()方法用来根据指定的分隔符将字符串进行分割, sep若包含多个字符, 则作为一个整体分割.`

`rpatition()`方法从右侧开始分割.

如果字符串包含指定的分隔符, 则返回一个3元的元组, 第一个为分隔符左边的子串, 第二个为分隔符本身, 第三个为分隔符右边的子串.

```python
str0 = "www.google.com"
print(str0.partition('.')) # ('www', '.', 'google.com')
str0.rpartition('.') # ('www.google', '.', 'com')
str0.partition('1') # ('', '', 'www.google.com')
str0.partition('google') # ('www.','google', '.com')
```

#### 4.9.3 字符串切片
`S.split([sep [, maxsplit]]) -> list of strings`

`split()`通过指定分隔符对字符串进行切片, 默认使用所有空白符, 如果参数maxsplit有指定值, 则进分割maxsplit个字字符串.

**注意:** `split()`返回的是一个字符串列表.

```python
str6 = "abcdef \n12345 \nxyz"
print(str6.split()) # ['abcdef', '12345', 'xyz']
print(str6.split(' ', 1)) # ['abcdef', '\n12345 \nxyz']
print(str6.split('A')) # ['abcdef \n12345 \nxyz']
```

#### 4.9.4 按换行符切割
`S.splitlines(keepends=False) -> list of strings`

`splitlines()`按照换行符(`\r`、`\r\n`、`\n`)分割, 返回一个包含各行作为元素的列表, 如果参数keepends位`False`, 不包含换行符, 如果为`True`, 则保留换行符.
```python
str7 = 'str1\n\nstr2\n\rstr3\rstr4\r\n\r\n'
print(str7.splitlines()) # ['str1', '', 'str2', '', 'str3', 'str4', '']
print(str7.splitlines(True)) # ['str1\n', '\n', 'str2\n', '\r', 'str3\r', 'str4\r\n', '\r\n']
```

### 4.10 字符串替换
#### 4.10.1 制表符替换为空格
`S.expandtabs(tabsize) -> string`

`expandtabs()`方法把字符串中的水平制表符(`\t`)转为空格, 默认的空格数是8.
```python
str8 = 's\te'
print(str8) # s	e
print(str8.expandtabs()) # s       e
print(str8.expandtabs(4)) # s   e
```

#### 4.10.2 新子串替换旧子串
`S.replace(old, new [, count]) -> string`

`replace()`方法把字符串中的旧字符串old替换成新字符串new, 如果指定第三个参数count, 则替换不超过count次.
```python
str9 = 'old old old old old'
print(str9.replace('old', 'new')) # new new new new new
print(str9.replace('old', 'new', 3)) # new new new old old
```

`replace()`方法只能把参数作为一个整体进行替换, 如果我们要替换字符串中的过个字符, 可以借助`re`正则表达式模块.

```python
import re

str10 = '\r\nhello 1213 \nworld'
print(re.sub('[\r\n]', '', str10)) # hello 1213 world
```

#### 4.10.3 字符映射替换
```shell
S.translate(table [, deleterchars]) -> string [Python 2.x]
S.translate(table) -> str [Python 3.x]
```
`translate()`函数根据参数table给出的转换表(它是一个长度为256的字符串)转换字符串的单个字符, 要过滤掉的字符通过deletechars参数传入
```python
# 引用 maketrans 函数生成转换表
from string import maketrans

# intab 和 outtab 长度必须相同
intab  = "aeiou+"
outtab = "12345-"
trantab = maketrans(intab, outtab)

str0 = "aeiou+r1m"
# print(str0.translate(trantab, "rm"))

# Python 3.x 版本不支持 deletechars
print(str0.translate(trantab))
```

#### 4.10.4 字符串映射替换
为了解决`translate()`方法单字符映射的限制, 使用`re`功能可以无副作用的替换多个字符串.
```python
# count 表示替换的次数，默认替换所有
def replace_strs(instr, map_dict, count=0):
    import re

    # escape all key strings
    re_dict = dict((re.escape(i), j) for i, j in map_dict.items())
    pattern = re.compile('|'.join(re_dict.keys()))

    return pattern.sub(lambda x: re_dict[re.escape(x.group(0))], instr, count)

str0 = "This and That."
map_dict = {'This' : 'That', 'That' : 'This'}

print(replace_strs(str0, map_dict))

# 注意重复调用 replace() 方法带来的副作用
newstr = str0.replace('This', 'That').replace('That', 'This')
print(newstr)
```

### 4.11 字符串排序
对于一个字符串排序, 通常有两种方式:
- 转换为列表, 使用列表的`sort()`方法.
- 使用内建函数`sorted()`, 它可以为任何迭代对象进行排序, 还可以指定key来忽略大小写排序.参考[sorted]().

这两种方式都需要把排序后的列表转换
```python
str11 = 'hello'
str_list = list(str11)
str_list.sort()
print(''.join(str_list)) # ehllo
```

### 4.12 字符串合并
如同`int`类一样, 字符串重载了 `+ `运算符, 使用`+`运算符合并两个子串是最简洁的.

`S.join(iterable) -> str`

`join()`方法用于将可迭代类型中的元素以指定的字符连接生成一个新的字符串.
```python
str12 = 'ABCD'
tuple0 = ('a', 'b', 'c')
list1 = ['1', '2', '3']
print('--'.join(str12)) # A--B--C--D
print('--'.join(tuple0)) # a--b--c
print('--'.join(list1)) # 1--2--3
print(''.join(list1)) # 123
```

使用`join()`函数打印乘法表:
```python
print('\n'.join(' '.join(['%s * %s = %-3s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)))
```

### 4.13 字符串特征类型判定
判定函数均返回布尔值. 非空表示如果字符串为空字符则返回`False`

为何更好的理解字符类型特征, 请参考[Unicode的字符集分类](https://www.fileformat.info/info/unicode/category/index.htm)

| 方法                     | 描述                                                                                                                                               |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `string.isalnum()`     | - 非空, 全为字母或者数字(alphanumeric character)<br/> - 等价于`isalpha()` or `isdecimal()` or `isnumeric()`                                                   |
| `string.isalpha()`     | - 非空, 全为字母(alphabetic character)<br/> - Unicode “Letter”字符集，包含 Lm, Lt, Lu, Ll 和 Lo                                                               |
| `string.isdigit()`     | - 非空, 全为十进制数字(0-9)<br/> - Unicode “Decimal, Digit”字符集 Nd                                                                                         |
| `string.isspace()`     | - 非空, 全为空白符(whitespace), 参考[strip字符串]()<br/> - Unicode “Separator” 字符集，包含 ZI, Zp 和 Zs                                                            |
| `string.istitle()`     | - 非空，是否为标题化字符串，至少包含一个区分大小写的字符<br/> - 区分大小写的字符称为 cased characters<br/> - 包含 Lu (Letter, uppercase) Ll (Letter, lowercase)和Lt (Letter, titlecase). |
| `string.isupper()`     | 非空，至少包含一个区分大小写的字符，且全为大写                                                                                                                          |
| `string.lower()`       | 非空，至少包含一个区分大小写的字符，且全为小写                                                                                                                          |
| `ustring.isnumeric()`  | - 非空，全为数字，只存在于unicode对象<br/> - Unicode “Digit, Decimal, Numeric”字符集, 包含 Nd, Ni 和 No                                                              |
| `ustring.isdecimal()`  | 非空，全为数字，只存在于unicode对象，包含 Nd                                                                                                                      |
| `string.isascii()`     | 空，或者全为ASCII码字符，U+0000-U+007F 3.7版本引入                                                                                                             |
| `string.isprintable()` | - 空，或全为可打印字符<br/> - 不可打印字符 Unicode “Separator” 字符集，包含 ZI, Zp 和 Zs<br/> - 例外：空格是可打印字符                                                             |

### 4.14 字符编解码
世界上存在着各种各样的编码, 有数学符号, 有语言符号, 为了在计算机中统一表达, 制定了统一编码规范, 被称为Unicode编码. 它让计算机具有了跨语言、跨平台的文本和符号的处理能力.

[细说编码](https://blog.csdn.net/zhouguoqionghai/article/details/79733525)和[彻底理解字符编码](https://www.cnblogs.com/leesf456/p/5317574.html)是两篇了解字符编码比较深入浅出的文章. 这里只做简单的总结性介绍.

#### 4.14.1 常见的编码方式
- ASCII编码: 美国指定, 单字节棉麻, 只用了8位的后7位, 第一位总是0, 一共128个字节
- ISO-8859-1(Latin1): ISO组织制定, 单字节编码, 扩展了Ascii编码的最高位, 一共256字节
- GB2312: 分区编码, 针对简体中文, 2字节编码, 高字节表示区, 低字节表示位, 共收录6763个中文字符
- BIG5(cp950)：针对繁体中文，2字节编码，共收录13060个中文字符
- GBK(cp936)：“国标”、“扩展”汉语拼音的第一个字母缩写，2字节编码。扩展了GB2312编码，完全兼容GB2312，包含繁体字符，但是不兼容BIG5 (所以BIG5编码的文档采用GBK打开是乱码，GB2312采用GBK打开可以正常浏览)
- Unicode(统一码/万国码/单一码)：全球通用的单一字符集，包含人类迄今使用的所有字符，但只规定了符号的编码值，没有规定计算机如何编码和存储，针对Unicode有两种编码方案。

### 4.15 字节序列化 Bytes
Python3中明确区分了字符串类型(`str`)和字节序列类型(`bytes`), 这成为字节流. 内存, 磁盘中均是以字节流的形式保存数据, 它是一个一个的字节(byte, 8bit)顺序构成, 然而人们并不习惯直接使用字节, 即读不懂, 操作起来也很麻烦, 人们容易看懂的是字符串.

所以字符串和字节流需要进行转化, 字节流转换为人们可以读懂得过程叫做解码, 于此相反, 将字符串转换为字节流的过程叫做编码. 我们已经了解对于值在0-128之间的字符, 可以使用ASCII编码, 而对于多字节的中文, 则需要GBK或者utf-8编码.

当我们读取文件时, 如果打开模式是文本模式, 就会自动进行解码的转换, 当我们写出字符串时, 也会进行编码转码, 不需要显式的进行编码, 如果要进行网络传输, 那么就要手动进行编解码.

Python对于bytes类型的数据用带`b`前缀加字符串(如果字节值在ascii码值内则显示对应的ascii字符, 否则显示\x表示的16进制字节值)表示.

- 我们可以通过**b'xxx'**显式定义一个bytes类型对象, 例如:
```python
bytes0 = b'abc'
print(type(bytes0).__name__) # bytes
```
- 同样也可以使用字符串对象的encode函数得到bytes对象:
```python
print('abc'.encode('utf-8')) # b'abc'
```
- 也可以通过bytes类名把字符串类型转换为bytes对象:
```python
bytes1 = bytes('abc', 'utf-8')
print(type(bytes1).__name__, bytes1) # bytes b'abc'
```
`utf-8`是一种适用于全世界各种语言文字符号进行编码的编码格式. 默认在编写Python代码时也使用该编码格式. 可以看到一个中文字符, 在`utf-8`中通常使用3个字节进行编码

字节流类型具有只读属性, 字节流中的每个字节都是int型, 可以通过下标访问, 但不可更改字节值

#### 4.15.1 bytes
`bytes()`类支持一下参数来实例化一个字节流对象:
1. 不提供参数, 生成一个空对象, 值为`b''`
2. 字符串参数, 必须提供编码参数encoding, 此时可以传入`errors='ignore'`忽略错误的字节.
3. 正整数n, 返回含n个`\x00`字节的对象
4. `bytearray`对象, 将可读写的bytearray对象转换为只读的bytes对象
5. 整数型可迭代对象, 比如`[1, 2, 3]`, 每个元素必须在\[0-255\]之间.
```python
print(bytes())  # 等价于 bytes(0) b''

print('string'.encode('utf-8'))
print(bytes('string', 'utf-8'))

print(bytes(3))

print(bytes(bytearray([1, 2, 3])))

print(bytes([1, 2, 3]))
```
bytes对象具有`decode()`方法, 将自己流转换回字符串:
```python
print('中文'.encode('utf-8').decode('utf-8'))
```

#### 4.15.2 bytearray
`bytearray()`创建一个可读可写的字节流对象. 其他参数和属性与bytes()一致.
```python
ba = bytearray(3)
print(ba)
ba[0] = 256 # 2 ** 8
print(ba)
```

#### 4.15.3 hex
`bytes.hex()`方法可以以16进制字符串方式显示字节流对象:
```python
bytes2 = bytes('中文', 'utf-8')
print(bytes2) # b'\xe4\xb8\xad\xe6\x96\x87'
print(bytes2.hex()) # e4b8ade69687
```
当然使用`bytes.formathex()`方法也可以将一个16进制字符串转换为bytes对象:
```python
int0 = 0xefefefef
hexstr = hex(int0)
print(hexstr) # 0xefefefef
bytes3 = bytes.fromhex(hexstr[2:])
print(bytes3) # b'\xef\xef\xef\xef'
```
#### 4.15.4 bytes和字符串转换
str 对象编码后变为 bytes 对象，bytes 对象解码后对应 str 对象
```python
bytes0 = bytes('中文', 'utf-8')
bytes1 = '中文'.encode('utf-8')
print(bytes0, bytes1)

str0 = bytes0.decode('utf-8')
str1 = str(bytes1, 'utf-8')
print(str0, str1)
```

#### 4.15.5 类字符串操作
字节流对象类似str, 所以定义了很多类似字符串的放的, 比如转换其中ascii字符的大小写, 查找等
```python
bytes0 = bytes('string', encoding='utf-8')
print(bytes0.find(b't')) # 参数必须也是 bytes 类型
print(bytes0.swapcase())
```