# a raise travelling through many statement-position calls is linear, not exponential
def f0():
    raise Exception(5)
def f1():
    f0()
def f2():
    f1()
def f3():
    f2()
def f4():
    f3()
def f5():
    f4()
def f6():
    f5()
def f7():
    f6()
def f8():
    f7()
def f9():
    f8()
def f10():
    f9()
def f11():
    f10()
def f12():
    f11()
n = 0
try:
    n = 1
    f12()
    n = 2
except Exception as e:
    print(n)
    print(e)
