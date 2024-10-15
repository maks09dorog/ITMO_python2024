def kwargs(**kwargs):
    print(kwargs)

x = kwargs(age=130, name = "Peter")

def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

fn = counter()
fn_ = counter()
print(fn)


print(fn())
print(fn())
print(fn_())

#поле чудес

from random import randint as ri
