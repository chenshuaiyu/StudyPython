# 掷骰子
from random import randint

face = randint(1, 6)
if face == 1:
    result = 'one'
elif face == 2:
    result = 'two'
elif face == 3:
    result = 'three'
elif face == 4:
    result = 'four'
elif face == 5:
    result = 'five'
else:
    result = 'six'
print(result)
