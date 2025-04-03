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