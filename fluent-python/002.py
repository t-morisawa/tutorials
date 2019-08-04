"""
第7章 関数デコレータとクロージャ

クロージャとは、関数内部で定義されていないが内部で参照されている非グローバルな変数を含む、拡張されたスコープをもつ関数のこと。
"""

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target()

"""
targetはinnerへの参照が上書きされる

実行結果:
<function deco.<locals>.inner at 0x10d0e5950>
"""
print(target)

"""
Pythonの変数スコープ

関数内で代入が行われた変数はローカル変数だと見なされる。
それを防ぐにはglobal宣言をする
"""
b = 6
def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f3(3)
print(b)

"""
クロージャの例
関数averagerと変数seriesのセットがクロージャ

averger内では、seriesのことは自由変数と呼ぶ
"""
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

print(avg.__code__.co_varnames) # new_value, total
print(avg.__code__.co_freevars) # series

"""
seriesのバインディングはavgの__closure__属性に保持される。

実行結果
(<cell at 0x1029ea4c8: list object at 0x102c3f388>,)
"""
print(avg.__closure__)
print(avg.__closure__[0].cell_contents) # [10, 11, 12]

import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked
