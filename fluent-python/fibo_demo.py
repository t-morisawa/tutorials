"""
第7章のサンプル、フィボナッチ数列

同じ計算を何度もしているので効率が悪い
"""
from clockdeco import clock

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    print(fibonacci(6))
