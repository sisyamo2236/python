import random
#----------------------------------------------- define
_GAME_CONTINUE  = 0
_GAME_HUMAN_WIN = 1
_GAME_PC_WIN    = 2
_GAME_DRAW      = 4

_HUMAN_MARK     = 'O'
_PC_MARK        = 'X'
#----------------------------------------------- class
class TicTacToe:
    # 各種リスト（配列）や変数の初期化
    # 人間あなたの打った場所　：self.value[] =  1
    # コンピュータの打った場所：self.value[] = -1
    def __init__(self):
        self.number = ['1','2','3', '4','5','6', '7','8','9']
        self.value  = [0,0,0, 0,0,0, 0,0,0]
        self.imax   = len(self.number)
        self.vPattern = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 横・勝利判定パターン
                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 縦・勝利判定パターン
                [0, 4, 8], [2, 4, 6]              # 斜め・勝利判定パターン
        ]

    #---------------------------------------------- 盤面表示
    def dispBoard(self):
        for i in range(self.imax):
            if self.value[i] < 0:
                self.number[i] = _PC_MARK
            elif self.value[i] > 0:
                self.number[i] = _HUMAN_MARK

        print()
        print(_HUMAN_MARK, ':あなた')
        print(_PC_MARK,    ':コンピュータ')
        print('+---+---+---+')
        print('| {0} | {1} | {2} |'.format(self.number[0], self.number[1], self.number[2]))
        print('+---+---+---+')
        print('| {0} | {1} | {2} |'.format(self.number[3], self.number[4], self.number[5]))
        print('+---+---+---+')
        print('| {0} | {1} | {2} |'.format(self.number[6], self.number[7], self.number[8]))
        print('+---+---+---+')

        return
#---------------------------------------------- 打ち手の入力
    def hitBoard(self):
        while True:
            self.no = int(input('1-9までの番号を入力してください：'))
            if self.no >= 1 and self.no <= self.imax:
                if self.value[self.no - 1] == 0:
                    self.value[self.no - 1] = 1
                    return
                else:
                    print('\n## その場所には打てません ##\n')
                    continue
            else:
                print('\n## 指定できるのは 1-9 までの数字です ##\n')
                continue
        return
    #---------------------------------------------- コンピュータ思考ルーチン
    def processing(self):
        self.iy = 0
        # 後一手で勝てる場合
        for ix in self.vPattern:
            s = self.value[ix[0]] + self.value[ix[1]] + self.value[ix[2]]
            if s == -2:
                if self.value[ix[0]] == 0:
                    self.iy = ix[0]
                elif self.value[ix[1]] == 0:
                    self.iy = ix[1]
                elif self.value[ix[2]] == 0:
                    self.iy = ix[2]

                self.value[self.iy] = -1
                print('コンピュータの指し手：', self.iy + 1)
                return

        # 後一手で負ける場合
        for ix in self.vPattern:
            s = self.value[ix[0]] + self.value[ix[1]] + self.value[ix[2]]
            if s == 2:
                if self.value[ix[0]] == 0:
                    self.iy = ix[0]
                elif self.value[ix[1]] == 0:
                    self.iy = ix[1]
                elif self.value[ix[2]] == 0:
                    self.iy = ix[2]

                self.value[self.iy] = -1
                print('コンピュータの指し手：', self.iy + 1)
                return

        # 適当な空き箇所に打つ
        for self.iy in range(self.imax):
            if self.value[self.iy] == 0:
                print('コンピュータの指し手：', self.iy + 1)
                self.value[self.iy] = -1
                break
        return
    #---------------------------------------------- 勝敗判定ルーチン
    # 縦・横・斜めのいずれかのマス目（self.value[]）の合計が +3 になったら、あなたの勝ち
    # 縦・横・斜めのいずれかのマス目（self.value[]）の合計が -3 になったら、コンピュータの勝ち
    # 戻り値 = _GAME_CONTINUE = 0 ：勝敗未定
    # 戻り値 = _HUMAN_WIN     = 1 ：あなたの勝ち
    # 戻り値 = _PC_WIN        = 2 ：コンピュータの勝ち
    # 戻り値 = _GAME_DRAW     = 4 ：引き分け
    #
    def judgement(self):
        #
        # 勝ち負け判定処理
        #
        for ix in self.vPattern:
            s = self.value[ix[0]] + self.value[ix[1]] + self.value[ix[2]]
            if s == 3:
                return _GAME_HUMAN_WIN
            elif s == -3:
                return _GAME_PC_WIN

        # 終了判定（全盤面選択済みのチェック）
        if self.value.count(0) == 0:
            return _GAME_DRAW

        # まだ選択されていない盤面があるので、試合続行
        return _GAME_CONTINUE
#----------------------------------------------- main
if __name__ == '__main__':
    # 常に先攻（o）は「あなた」
    ttt = TicTacToe()               # インスタンスの生成
    ttt.dispBoard()                 # 盤面の表示

    # TicTacToeの勝負
    while True:
        ttt.hitBoard()              # あなたの打ち手を入力する
        ttt.dispBoard()
        judge = ttt.judgement()
        if judge == _GAME_HUMAN_WIN:
            print('あなたの勝ち')
            break
        elif judge == _GAME_DRAW:
            print('引き分け')
            break

        ttt.processing()            # コンピュータの打ち手を考える
        ttt.dispBoard()
        judge = ttt.judgement()
        if judge == _GAME_PC_WIN:
            print('コンピュータの勝ち')
            break
        elif judge == _GAME_DRAW:
            print('引き分け')
            break
