"""
練習問題

「math.floor」を利用して、リストの各数値を小数点を切り捨てて、
以下のように表示する処理を作成してください

2
4
6
3
1
"""

import math

numbers = [2.5, 4.7, 6.9, 3.1, 1.8]

for n in numbers:
    print(math.floor(n))
