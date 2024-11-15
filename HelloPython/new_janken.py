import random

# じゃんけんの手を表示するための辞書
hand_dict = {0: 'グー', 1: 'チョキ', 2: 'パー'}

# 勝敗を判定する関数
def judge_winner(hands):
    unique_hands = set(hands)  # ユニークな手をセットにする

    # もし全員が同じ手なら引き分け
    if len(unique_hands) == 1:
        return "引き分け"

    # 各手の出現回数をカウント
    counts = {0: hands.count(0), 1: hands.count(1), 2: hands.count(2)}

    # 勝利条件のチェック
    if counts[0] > 0 and counts[1] > 0 and counts[2] == 0:
        return "グーを出したプレイヤーの勝ち"
    elif counts[1] > 0 and counts[2] > 0 and counts[0] == 0:
        return "チョキを出したプレイヤーの勝ち"
    elif counts[2] > 0 and counts[0] > 0 and counts[1] == 0:
        return "パーを出したプレイヤーの勝ち"
    
    return "引き分け"

# メイン関数
def play_janken(num_players):
    hands = []

    # 各プレイヤーの手をランダムに選択
    for i in range(num_players):
        hand = random.randint(0, 2)
        hands.append(hand)
        print(f"プレイヤー{i+1}の手: {hand_dict[hand]}")

    # 勝敗の判定
    result = judge_winner(hands)
    print(f"→ {result}")

# 実行
if __name__ == "__main__":
    #num_players = int(input("プレイヤーの数を入力してください: "))
    num_players = 3
    play_janken(num_players)
