"""
練習問題

メソッド「math.ceil」を利用して、リストの各数値を小数点を切り上げて
以下のように表示する処理を作成してください

3
5
7
4
2
"""

import math

numbers = [2.5, 4.7, 6.9, 3.1, 1.8]

for n in numbers:
    print(math.ceil(n))
