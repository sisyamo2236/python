
import csv

#----------------------------------------------- class
class Atend:

    # 初期化
    def __init__(self, row):
        # row ... 0:名前、1:ユーザーメール、2:期間の合計（分）、3:ゲスト
        self.items = row[0].split('_')
        if len(self.items) >= 4:
            self.min   = int(row[2])
            if self.items[0][0:1] == '\'':
                self.items[0] = self.items[0][1:]
            # items ... 0:氏名、1:クラス名、2:出席番号、3:学籍番号
            self.line  = ''
            self.line += self.items[1] + ','
            self.line += self.items[2] + ','
            self.line += self.items[3] + ','
            self.line += self.items[0] + ','
            self.line += row[2]
        else:
            self.line = ',,,' + row[0] + ',' + row[2]

    # 成形後データの取得
    def getData(self):
        return self.line

#----------------------------------------------- main
# CSVファイル名
csvFile = 'zoomChat.csv'

# 先頭の情報行数
dummyLines = 4

# 処理中の行番号
rowNo = 0

# 読み込んだCSVデータのクラスリスト（配列）
data = []
with open(csvFile) as f:
    lines = csv.reader(f)
    for row in lines:
        rowNo += 1
        if rowNo > dummyLines:
            # row ... 0:名前、1:ユーザーメール、2:期間の合計（分）、3:参加者
            if row[3] == 'はい':
#                print(row)
                data.append(Atend(row))

# 成形後データをリスト（配列）として data2[] に格納する
data2 = []
for dt in data:
#    print(dt.getData())
    data2.append(dt.getData())

# data2リストの昇順ソートを行う
data2.sort()

# 文字列項目の両端に " を付けて、成形データを表示する
for dt in data2:
    wk   = dt.split(',')
    wk2  = '"' + wk[0] + '",'
    wk2 += '"' + wk[1] + '",'
    wk2 += '"' + wk[2] + '",'
    wk2 += '"' + wk[3] + '",'
    wk2 += wk[4] + '\r\n'
    print(wk2, end='')
