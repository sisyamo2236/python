#----------------------------------------------- class
class Marking:

    # 初期化
    def __init__(self, row, border):
        self.item = []
        self.name = row[0]                                  # 氏名
        for i in range(1, len(row)):
            self.item.append(float(row[i]))                 # 科目ｉの得点
        self.total = sum(self.item)                         # ３科目の合計点
        self.judge = self.judgement(self.total, border)     # 合否判定

    # 合否判定
    def judgement(self, t, border):
        self.judge = '不合格'       # 合否
        if t >= border:
            self.judge = '合格'
        return self.judge

#----------------------------------------------- main
# CSVファイル名
csvFile = 'testResult.csv'

# 合格点
border = 180.0

# CSVファイルの読み込み
data = []
with open(csvFile) as f:
    lines = csv.reader(f)
    for row in lines:
        data.append(Marking(row, border))

# 個人データの表示
for dt in data:
    print(dt.name + ', ', end='')
    for t in dt.item:
        print(str(t) + ', ', end='')
    print(str(dt.total) + ', ', end='')
    print(dt.judge)
