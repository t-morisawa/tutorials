"""
第5章

第1級関数

第1級オブジェクト（生成・代入・演算ができるオブジェクト）として扱える関数のことをさす。
"""

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(fruits)

# yrrebwarts
print(fruits[0][::-1])

# 単語を逆にしたもので名前順に並べる
# lambdaについては、lambda 引数: 返り値
reverse = sorted(fruits, key=lambda word: word[::-1])
print(reverse)

def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()

upper_case_name.short_description = 'Customer name'

# 普通のインスタンスには存在しない関数の属性を取得
class C: pass
obj = C()
def func(): pass
print(sorted(set(dir(func)) - set(dir(obj))))

# キーワードオンリー引数
def f(a, *, b):
    return a, b

print(f(1, b=2))

# 階乗計算
from functools import reduce
from operator import mul

def fact(n):
    """階乗計算をする関数"""
    return reduce(mul, range(1, n+1))

print(fact.__name__)
print(fact.__doc__)
print(fact(3))

# itemgetter
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(1,0)
for city in metro_data:
    print(cc_name(city))

print(itemgetter(1)(('a', 'b', 'c')))
