"""
第7章 関数デコレータとクロージャ
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
