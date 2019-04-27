from module1 import foo

foo()

from module2 import foo

foo()

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()

from module1 import foo
from module2 import foo

foo() # goodbye world!

from module2 import foo
from module1 import foo

foo() # hello world!

import module3
# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
