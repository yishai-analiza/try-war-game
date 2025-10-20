def create_card(rank:str,suite:str) -> dict:
    dict_card = {}
    dict_card["suite"] = suite
    dict_card["rank"] = rank
    non_num_ranks = ["a","k","q","j"]
    value = ""
    if rank.lower() in non_num_ranks:
        match rank.lower():
            case "a":
                value = 14
            case "k":
                value = 13
            case "q":
                value = 12
            case "j":
                value = 11
    else:
        try:
            value = int(rank)
        except:
            print("rank is not an int format")
            raise TypeError("rank is not int format")
    dict_card["value"] = value
        
    return dict_card

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card.get("value") is not None and  p2_card.get("value") is not None:
        if p1_card.get("value") > p2_card.get("value"):
            return "p1"
        elif p2_card.get("value") > p1_card.get("value"):
                return "p2"
        else:
            return "WAR"
    else:
        raise TypeError("missing values in card dict")


def create_deck() -> list[dict]:
    deck = []
    for rank in ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]:
        for suite in ["h","c","s","d"]:
            
            new_card = create_card(rank,suite.upper())
            deck.append(new_card)
    return deck

import random
def shuffle(deck:list[dict]) -> list[dict]:
    for _ in range(1000):
        index1 = random.randint(0,51)
        index2 = random.randint(0,51)
        while index1 == index2:
            index2 = random.randint(0,51)
        tmp = deck[index1]
        deck[index1] = deck[index2]
        deck[index2] = tmp
    return deck
