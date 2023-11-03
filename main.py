import unittest

# Define the cards tuple
cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')


def check_straight(card1, card2, card3):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
              'A': 14}
    sorted_cards = sorted([card1[1:], card2[1:], card3[1:]], key=lambda x: values[x])
    if (values[sorted_cards[1]] == values[sorted_cards[0]] + 1) and (
            values[sorted_cards[2]] == values[sorted_cards[1]] + 1):
        return values[sorted_cards[2]]
    return 0


def check_3ofa_kind(card1, card2, card3):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
              'A': 14}
    sorted_cards = sorted([card1[1:], card2[1:], card3[1:]], key=lambda x: values[x])
    if (values[sorted_cards[0]] == values[sorted_cards[1]] == values[sorted_cards[2]]):
        return values[sorted_cards[0]]
    return 0


def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    return 0


def play_cards(left1, left2, left3, right1, right2, right3):
    left_straight = check_straight(left1, left2, left3)
    right_straight = check_straight(right1, right2, right3)
    left_3ofakind = check_3ofa_kind(left1, left2, left3)
    right_3ofakind = check_3ofa_kind(right1, right2, right3)

    if left_straight and right_straight:
        if left_straight > right_straight:
            return -1
        elif left_straight < right_straight:
            return 1
        else:
            return 0
    elif left_3ofakind and right_3ofakind:
        if left_3ofakind > right_3ofakind:
            return -1
        elif left_3ofakind < right_3ofakind:
            return 1
        else:
            return 0
    elif left_straight:
        return -1
    elif right_straight:
        return 1
    elif check_royal_flush(left1, left2, left3):
        return -1
    elif check_royal_flush(right1, right2, right3):
        return 1
    else:
        return 0



