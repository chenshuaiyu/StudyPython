# 作用域问题

# 局部作用域
def foo1():
    a = 5


foo1()
# print(a) # name 'a' is not defined

# 全局作用域
b = 10


def foo2():
    print(b)


foo2()


def foo3():
    b = 100  # 局部变量
    print(b)


foo3()
print(b)


def foo4():
    global b  # global关键字来指示foo函数中的变量b来自于全局作用域，如果全局作用域中没有b，那么下面一行的代码就会定义变量b并将其置于全局作用域
    b = 200  # 全局变量
    print(b)


foo4()
print(b)

# 函数内部的函数能够修改嵌套作用域中的变量，可以使用nonlocal关键字来指示变量来自于嵌套作用域