# -*- coding:utf-8 -*-

# 編集したいファイル（元ファイル）を開く
file = open("result.csv","r")
# 書き出し用のファイルを開く
out_file = open("seikei.csv","w")

# 書き出し用ファイルのヘッダーを記述
out_file.write("image1,image2,answer\n")

# 元ファイルのヘッダーをreadlineメソッドで１行飛ばす
file.readline()
# 元ファイルのレコード部分をreadlinesメソッドで全行を読み取る
lines = file.readlines()

# for文で1行ずつ取得
for line in lines:
    # 改行コードをブランクに置換
    line = line.replace("\n","")
    # カンマ区切りでリストに変換する
    line = line.split(",")

    # 変換後のカンマ区切りの雛形を作り、変換処理した値を入れ込む
    if line[4]=='TRUE':
        row="{},{},{}\n".format(
            line[0],
            line[1],
            1.0
        )
    elif line[4]=='FALSE':
        row="{},{},{}\n".format(
            line[0],
            line[1],
            0.0
        )
    # 書き出し用のファイルに出力
    out_file.write(row)

    if line[5]=='TRUE':
        row="{},{},{}\n".format(
            line[0],
            line[2],
            1.0
        )
    elif line[5]=='FALSE':
        row="{},{},{}\n".format(
            line[0],
            line[2],
            0.0
        )
    # 書き出し用のファイルに出力
    out_file.write(row)

    if line[6]=='TRUE':
        row="{},{},{}\n".format(
            line[0],
            line[3],
            1.0
        )
    elif line[6]=='FALSE':
        row="{},{},{}\n".format(
            line[0],
            line[3],
            0.0
        )

    # 書き出し用のファイルに出力
    out_file.write(row)

# ２つのファイルを閉じる
file.close()
out_file.close()
