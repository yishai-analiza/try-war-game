from utils.deck import create_deck,shuffle, compare_cards

def create_player(name:str="AI") -> dict:
    return {"name":name, "hand":[],"won_pile": [], "num_of_hearts":0}

def init_game()->dict:
    deck = create_deck()
    deck = shuffle(deck)
    player_1 = create_player("yishai")
    player_2 = create_player()
    player_1["hand"] = deck[0:26]
    player_2["hand"] = deck[26:]
    print(len(player_1["hand"]))
    print(len(player_2["hand"]))
    return {
        "deck":deck,
        "player_1":player_1,
        "player_2":player_2
    }

def play_round(player_1: dict, player_2: dict):
    p1_card =  player_1["hand"].pop()
    p2_card =  player_2["hand"].pop()
    print(f"player 1 played: {p1_card["rank"]}-{p1_card["suite"]}")
    print(f"player 2 played: {p2_card["rank"]}-{p2_card["suite"]}")
    res = compare_cards(p1_card,p2_card)
    match res:
        case "p1":
            print("player 1 card is better!")
            player_1["won_pile"].append(p1_card)    
            player_1["won_pile"].append(p2_card)    
        case "p2":
            print("player 2 card is better!")
            player_2["won_pile"].append(p1_card)    
            player_2["won_pile"].append(p2_card)
        case "WAR":
            print("war! doing nothing")    
    print("round done")