#!/usr/bin/python3
#
#
# M.OKUNO
# ３の倍数、１の位が３、１０の位が３の数チェック
#

# 2021-05-21
# メッセージ表示
print("１〜５０までの整数のうち３の関連数を調べる")
print("該当数 = ", end="")

# ３の倍数をカウントする変数 cnt の初期化
cnt = 0

# １〜５０までの整数をチェックする
for i in range(1, 51):
if i % 3 == 0: # ３の倍数チェック
cnt += 1
print(i, end=" ")
elif i % 10 == 3: # １の位が３かチェック
cnt += 1
print(i, end=" ")
elif i // 10 == 3: # １０の位が３かチェック
cnt += 1
print(i, end=" ")

# 改行
print()
print("count = ", cnt)
