from game_logic.game import init_game, play_round

if __name__ == "__main__":
    game_obj = init_game()
    rounds = 1
    while len(game_obj["player_1"]["hand"])>0 and len(game_obj["player_2"]["hand"])>0:
        print(f"round num: {rounds}")
        play_round(game_obj["player_1"],game_obj["player_2"])
        rounds+=1
    print("game over!")
    print(f"player 1 total: {len(game_obj["player_1"]["won_pile"])}")
    print(f"player 2 total: {len(game_obj["player_2"]["won_pile"])}")
    if len(game_obj["player_1"]["won_pile"]) > len(game_obj["player_2"]["won_pile"]):
        print("player 1 wins!")
    elif len(game_obj["player_2"]["won_pile"]) > len(game_obj["player_1"]["won_pile"]): 
        print("player 2 wins!")
    else:
        print("draw")