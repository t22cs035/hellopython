import random

# じゃんけんの手を表示するための辞書
hand_dict = {0: 'グー', 1: 'チョキ', 2: 'パー'}

# 勝敗を判定する関数
def judge_winner(hand_A, hand_B, hand_C):
    if (hand_A == hand_B == hand_C) or (hand_A == 1 and hand_B == 2 and hand_C == 3) or (hand_A == 1 and hand_B == 3 and hand_C == 2) or (hand_A == 2 and hand_B == 1 and hand_C == 3) or (hand_A == 2 and hand_B == 3 and hand_C == 1) or (hand_A == 3 and hand_B == 1 and hand_C == 2) or (hand_A == 3 and hand_B == 2 and hand_C == 1):
        return "引き分け"
    elif (hand_A == 0 and hand_B == 1 and hand_C == 1) or (hand_A == 1 and hand_B == 2 and hand_C == 2) or (hand_A == 2 and hand_B == 0 and hand_C == 0):
        return "Aの勝ち"
    elif (hand_A == 0 and hand_B == 1 and hand_C == 0) or (hand_A == 1 and hand_B == 2 and hand_C == 1) or (hand_A == 2 and hand_B == 0 and hand_C == 2):
        return "Bの勝ち"
    else:
        return "Cの勝ち"

# メイン関数
def play_janken():
    # プレイヤーAとBの手をランダムに選択
    hand_A = random.randint(0, 2)
    hand_B = random.randint(0, 2)
    hand_C = random.randint(0, 2)

    # じゃんけんの手を表示
    print(f"Aの手: {hand_dict[hand_A]} v.s. Bの手: {hand_dict[hand_B]} v.s. Cの手: {hand_dict[hand_C]} → {judge_winner(hand_A, hand_B, hand_C)}")

# 実行
if __name__ == "__main__":
    play_janken()
