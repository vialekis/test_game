import random
NUMBERS = [1, 2, 3]
SYMBOLS = ["DIAMOND", "SQUIGGLE", "OVAL"]
SHADINGS = ["STRIPED", "SOLID", "OPEN"]
COLORS = ["RED", "GREEN", "PURPLE"]


class Card:
    def __init__(self, number, symbol, shading, color):
        if any([
            number not in NUMBERS,
            symbol not in SYMBOLS,
            shading not in SHADINGS,
            color not in COLORS
        ]):
            raise ValueError("Неправильные параметры карты")

        self.number = number
        self.symbol = symbol
        self.shading = shading
        self.color = color

def check_set(cards): #Проверка на "сет"
    if len(cards)!=3:
        return False
    set_cards = [[1,3,3,3],[3,1,3,3],[3,3,1,3],[3,3,3,1],[3,3,3,3],[1,1,1,1],[1,1,1,3],[1,1,3,1],[1,3,1,1],[3,1,1,1]]
    set_NUMBERS=set()
    set_SYMBOLS = set()
    set_SHADINGS=set()
    set_COLORS=set()
    set_card=[]
    for card in cards:
        set_NUMBERS.add(card.number)
        set_SYMBOLS.add(card.symbol)
        set_SHADINGS.add(card.shading)
        set_COLORS.add(card.color)

    set_card.append(len(set_NUMBERS))
    set_card.append(len(set_SYMBOLS))
    set_card.append(len(set_SHADINGS))
    set_card.append(len(set_COLORS))
    if set_card in set_cards:
        return True
    return False


def generator_cards(NUMBERS,SYMBOLS,SHADINGS,COLORS): #генератор 3-х карт
    if len(set(NUMBERS))==3 and len(set(SYMBOLS))==3 and len(set(SHADINGS))==3 and len(set(COLORS))==3:
        cards = [Card(random.choice(NUMBERS),random.choice(SYMBOLS),random.choice(SHADINGS),random.choice(COLORS)),
             Card(random.choice(NUMBERS),random.choice(SYMBOLS),random.choice(SHADINGS),random.choice(COLORS)),
             Card(random.choice(NUMBERS), random.choice(SYMBOLS), random.choice(SHADINGS), random.choice(COLORS))]
        if len(set(cards))==3:
            return cards
    return False


def check_set_true(): #Генерируем три варианта, для которых «сет» есть, и три варианта, для которых которых «сета» нет.
    set_true=0
    set_cards=[]
    flag = True
    while flag:
        cards = generator_cards(NUMBERS, SYMBOLS, SHADINGS, COLORS)
        if cards!= False:
            if check_set(cards):
                if set_true<3:
                    set_true +=1
                    set_cards.append(cards)
        if set_true == 3:
            flag = False
    return set_cards

def check_set_false(): #Генерируем три варианта, для которых «сет» есть, и три варианта, для которых которых «сета» нет.
    set_false=0
    set_cards=[]
    flag = True
    while flag:
        cards = generator_cards(NUMBERS, SYMBOLS, SHADINGS, COLORS)
        if cards!= False:
            if not check_set(cards):
                if set_false<3:
                    set_false +=1
                    set_cards.append(cards)
        if set_false == 3:
            flag = False
    return set_cards

# def check_set(cards):
#     set_cards = [[1,3,3,3],[3,1,3,3],[3,3,1,3],[3,3,3,1],[3,3,3,3],[1,1,1,1],[1,1,1,3],[1,1,3,1],[1,3,1,1],[3,1,1,1]]
#     set_NUMBERS=set()
#     set_SYMBOLS = set()
#     set_SHADINGS=set()
#     set_COLORS=set()
#     set_card=[]
#     for card in cards:
#         if card != type(card):
#             print("ca не card")
#             return False
#
#         set_NUMBERS.add(card[0])
#         set_SYMBOLS.add(card[1])
#         set_SHADINGS.add(card[2])
#         set_COLORS.add(card[3])
#
#     set_card.append(len(set_NUMBERS))
#     set_card.append(len(set_SYMBOLS))
#     set_card.append(len(set_SHADINGS))
#     set_card.append(len(set_COLORS))
#     if set_card in set_cards:
#         return True
#     return False

