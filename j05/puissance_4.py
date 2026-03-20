def player_col_input(player):
    while True:
        col = input(f"joueur {player}, où veux-tu jouer 1-7) ")
        if len(col)== 1 and col in "1234567":
            break
        print("Mauvaise entrée, recommencez")

    print("Colonne ", col)
    return col

def print_game(game):
    pass


def puissance_4():
    # for turn in range(6 * 7):
    #     print(turn)
    player = 0
    game = ""

    
    while True:
        col = player_col_input(player + 1)
        # if has_someone_won():
        #     break
        print_game(game)
        player = (player + 1) % 2

def test_player_col_input():
    pass

def test():
    test_player_col_input()

if __name__ == "__main__":
    puissance_4()
    test()
