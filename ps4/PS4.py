# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 18:40:18 2021

@author: Jonas
"""
Helpers


def getWordScore(w, n):
    return sum(SCRABBLE_LETTER_VALUES[c] for c in w) * len(w) + 50 * (n == len(w))


def updateHand(hand, word):
    return {k: v - word.count(k) for k, v in hand.items()}


def isValidWord(w, h, wordList):
    return all(h.get(c, 0) >= w.count(c) for c in w) and w in wordList


def calculateHandlen(hand):
    return sum(hand.values())


PS 4 - 6


def playGame(wordList):
    while True:
        choice = input('Enter n for a new hand, r to replay, e to end: ')
        if choice == 'n':
            hand = dealHand(HAND_SIZE)
        elif choice == 'e':
            break
        elif choice != 'r':
            print('Invalid command.')
            continue
        try:
            playHand(hand, wordList, HAND_SIZE)
        except NameError:
            print('You have not played yet. Please play a new hand first!\n')


PS 4 - 7


def playGame(wordList):
    ans = hand = ''
    while ans != 'e':
        who = ans = input('Enter n for a new hand, r to replay, e to end: ')
        if ans == 'n' or (ans == 'r' and hand):
            hand = hand if ans == 'r' else dealHand(HAND_SIZE)
            while who not in 'uc':
                who = input('Enter u to play, c for the computer to play: ')
                playHand(hand, wordList, HAND_SIZE) if who == 'u' else \
                    compPlayHand(hand, wordList, HAND_SIZE) if who == 'c' else \
                    print('Invalid command.')
        elif ans == 'r':
            print('You have not played yet. Please play a new hand first!')
        elif ans != 'e':
            print('Invalid command.')
