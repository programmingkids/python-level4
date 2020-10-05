"""
練習問題

以下のファイルから文章を読み込み、実行結果のように表示する処理を作成してください

■ファイル名
python-level4/chapter05/data/data10.txt

縄文時代
弥生時代
古墳時代
飛鳥時代
奈良時代
平安時代
鎌倉時代
南北朝時代
室町時代
戦国時代
安土桃山時代
江戸時代
"""

with open("python-level4/chapter05/data/data10.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line, end="")
