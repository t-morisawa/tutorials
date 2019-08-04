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

