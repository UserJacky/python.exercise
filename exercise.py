a = input("a = ") 
b = input("b = ")
print(a, b)
a,b = b,a
print(a, b)
x = {"a","b"}
type(x)
y = ("a","b")
type(y)

sum = 0 
i = 1
while i <= 10:
    print(i)
    sum = sum + i
    i = i + 1
print("sum = ",sum)

sum = 0 
i = 1
for i in range(11):
    print(i)
    sum = sum + i
    i = i + 1
print("sum = ",sum)

L = [1,2,3]
len(L)
print(len(L))
type(L)

print(dir(L))
help(L.append)
help(input)
dir(L)

L1 = [True, True, True]
L2 = [True, False, True]
print(all(L1))
print(all(L2))
print(any(L1))
print(any(L2))

x1 = 11
x2 = 22
def foo(x1 = 111, x2 = 222):
    x1 = 1111
    x3 = 3333
    print("Inner globals: ",globals())
    print("Inner locals: ",locals()) 
    return sum
foo()

word = 'Python'
word[:2] + word[2:]

a,b = 0,1
while a < 10:
    print(a,b)
    a, b = b, a+b

a,b = 0,1
while a < 1000:
    print(a,end = ",")
    a, b = b, a+b

x = object()
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
'This is a string with a backslash:'

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))

print("My name is {0} and I am {1} years old.".format(name, age))

age = input("What is your age? ")
age = int(age)
print("You will be " + str(age+1) + " years old next year.")

my_string = " Hello, World! "
print(len(my_string))         # 15
print(my_string.strip())     # "Hello, World!"
print(my_string.lower())     # " hello, world! "
print(my_string.upper())     # " HELLO, WORLD! "
print(my_string.replace("H","J"))  # " Jello, World
print(my_string.split(","))  # [" Hello", " World!"]

sentence = "Hello, world! How are you?"
words = sentence.split()
print(words)

sentence = "apple,banana,orange"
fruits = sentence.split(",")
print(fruits)

message = "Hello, World!"
pos = message.find("World")
print(pos)

words = ["Hello", "world", "!"]
sentence = " ".join(words)

astring = "Hello world!"
print(astring[3:7:2])
print(astring[3:7:1])

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)
  
txt = "The best things in life are free!"
print("free" in txt)  
  
txt = "The best things in life are free!"
print("expensive" not in txt)
  
  
my_list = [1, 2, 3, 'hello', True, [4, 5, 6], 'world']
print(my_list[1:4])     # [2, 3, 'hello']
print(my_list[3:])      # ['hello', True, [4, 5, 6], 'world']
print(my_list[:5:2])    # [1, 3, True]

fruits = ['apple', 'banana', 'orange']
fruits.append('pear')
print(fruits) # ['apple', 'banana', 'orange', 'pear']

list1 = [1, 2, 3]
list2 = (4, 5, 6)
list1.append(list2);len(list1)
list1.extend(list2);len(list1)
print(list1) # [1, 2, 3, 4, 5, 6]
type(list1[3])

a = [('apple', 3), ('banana', 2), ('orange', 4)]
a_sorted = sorted(a, key=lambda x: x[1])
sorted(a)
help(sorted)

a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    print(a[i])
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

a = [1, 2, 3, 4, 5]
it = iter(a)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


help(list.append) 
help(list.extend) 

a = [1, 2, 3, 4, 5]
a[::-1]
list.reverse(a)
a

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
L.insert(len(L),L.pop(L.index(1)))
s = L
print(s) # [9, 1, 2, 3, 4, 5, 6, 7, 8]

my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}

# 遍歷字典中的所有項目
for key, value in my_dict.items():print(key, ':', value)

# 創建一個集合
my_set = {1, 2, 3}
my_set.add(4)
print(my_set) # 輸出 {1, 2, 3, 4}

# 創建一個集合
my_set = {1, 2, 3}
my_set[1]
my_set.remove(2)
print(my_set) # 輸出 {1, 3}

my_tuple = (1,) # 正確的創建方式
my_tuple2 = (1) # 會被認為是一個整數而不是元組

d = (1,2,3)
d + (4,)

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:print(key, my_dict[key])
my_dict["a"] = my_dict["a"] + 2

text = "This is a very big and red apple."
statistic = {}

for word in text:
    print(word)
    statistic[word] = statistic.get(word,0) + 1
for key in sorted(statistic):
    print(key, statistic[key])


L = [1, 1, 3, 9, 7, 8, 8, 8]
L = sorted(set(L),reverse=True)
print(L) # [9, 8, 7, 3, 1]

a = True
b = False

# 且
print(a and b)  # False
# 或
print(a or b)  # True
# 非
print(not a)  # False

print(a & b)  # False
# 或
print(a | b)  # True
# 非
print(not a)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for x in row:
        print(x)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for col in row:
        print(col)
        
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')
            
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger",
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# 枚舉列表中的元素
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i, fruit)
list(enumerate(fruits))
# 枚舉字典中的鍵值對
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for i, (key, value) in enumerate(person.items()):
    print(i, key, value)

# 將兩個列表組合成一個元組序列
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'green']
for fruit, color in zip(fruits, colors):
    print(fruit, color)

# 將多個列表組合成一個元組序列
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
names = ['John', 'Mary', 'Tom']
for num, letter, name in zip(numbers, letters, names):
    print(num, letter, name)

# 使用 break 終止循環
for i in range(10):
    if i == 5:
        break
    print(i)

# 使用 continue 跳過當前迭代
for i in range(10):
    if i == 5:
        continue
    print(i)

def my_func():
    pass

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


x = -6
y = -6
print(x == y) # Prints out True
print(x is y) # Prints out False
id(x)
id(y)

number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

globals()

class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i

dir(int)
help(int.bit_length)


class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
        
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                # unexpectedly shared by all dogs
d.name

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
filtered_data

help(math.isnan)

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
         else:
             print(n, 'is a prime number')
             
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    "#12453453"
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok("Do you really want to quit?")
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2,'Come on, only yes or no!')

list(range(3, 6))            # normal call with separate arguments
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
list(range(args))  
print(ask_ok.__doc__)
dir(ask_ok)

def f(ham: str, eggs: str = 'eggs') -> str:
     print("Annotations:", f.__annotations__)
     print("Arguments:", ham, eggs)
     return ham + ' and ' + eggs
f("12")
ask_ok.__annotations__

squares = [x**2 for x in range(1, 11)]
print(squares)

squares = [x**2 for x in range(1, 11)]
print(squares)


numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
unique_numbers = {x for x in numbers}
print(unique_numbers)
# output: {1, 2, 3, 4, 5}


ascii_dict = {x: x for x in range(97, 123)}
print(ascii_dict)
# output: {'a': 97, 'b': 98, 'c': 99, ..., 'x': 120, 'y': 121, 'z': 122}

squares = (x**2 for x in range(1, 11))
print(squares)
squares = [x**2 for x in range(1, 11)]
print(squares)
squares = (x**2 for x in range(1, 11))
for square in squares:
    print(square,end=(","))

flag = False
for i in range(5):
    if i == 5:
        flag = True
        break
    if not flag:
        print('Loop finished')
        
        
        
import random
num = random.randint(1, 100)
guess = 0
while guess != num:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > num:
        print("Too high, try again!")
    elif guess < num:
        print("Too low, try again!")
    else:
        print("Congratulations, you guessed it!")
        
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print()
    
    
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
    
string = "hello world"
reverse = ""
index = len(string) - 1
while index >= 0:
    reverse += string[index]
    index -= 1
print(reverse)


x = input() # 4
x = int(x)
n = 1
f = 0
for i in range(1,x+1):
    n = n * i
    f = f + n
print(f) # 33

x = int(input("輸入一個正整數："))
x = int(input("輸入一個正整數："))
result = 0
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
for i in range(1,x+1):
  result += factorial(i)
print(f"1! + 2! + ⋯⋯ + {x}! = {result}")


x = input() # Hello World
f = {a:x.count(a) for a in x}
print(f) # {‘H’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ’:1, ‘W’: 1, ‘r’: 1, ‘d’: 1}

x = input() # Hello World
f = dict()
for char in x:
    f[char] = f.get(char,0) + 1
print(f)

def greet(name):
    """
    這個函式會印出一個歡迎訊息
    :param name: 字串，要歡迎的名字
    """
    print("Hello, " + name + "!")
help(greet)
greet.__annotations__

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
f100 = fib2(100)    # call it
f100 


def f(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(f(1, 2, 3)) # 6
print(f(1, 2, 3, 4, 5)) # 15

#練習：定義一個計算質數的函數。


def isPrime(n):
    choose = "是"
    logit = 1
    for i in range(2,n):
        if (n % i) == 0:
            choose = "不是"
            logit = 0
    return(f"{n}{choose}質數",logit)
def primes(n):
    result = []
    for i in range(2,n): #2:n-1
        # sum = 1
        # for j in range(1,i):
        #     if (j == 1):
        #          continue
        #     sum = sum * (i % j)
        # if (sum > 0):
        #     result.append(i)
        if isPrime(i)[1] == 1:
            result.append(i)
    return(result)
x = int(input("請輸入一個數字: ")) # 20
f = primes(x)
print(f) # 2, 3, 5, 7, 11, 13, 17, 19


try:
    a = int("hello")
except ValueError:
    print("不能把字串轉換為整數")

try:
    f = open("file.txt", "r")
    # 一些代碼
except:
    print("出現了一個例外")
finally:
     print("執行一些清理代碼")

class MyException(Exception):
    pass

try:
    raise MyException("這是自定義的例外")
except MyException as e:
    print(e)
    
import logging

# 配置日誌格式和級別
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

try:
    # 在這裡執行一些代碼
    f = open("file.txt", "r")
except Exception as e:
    # 記錄日誌
    logging.error("出現了一個錯誤: %s", e)
    
    
    
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)
    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()




for x in range(10):
    for y in range(10):
        try:
            result = x / y
            # print(x, y,result)
        except ZeroDivisionError:
            print("division by zero!")
        else:
            print("result is", result)
        finally:
            print("executing finally clause")
    

try:
    5/0
    # raise Exception('spam', 'eggs')
except Exception as e:
    print(e)
finally:
    print('done')


try:
    raise KeyboardInterrupt

finally:
    print('Goodbye, world!')


