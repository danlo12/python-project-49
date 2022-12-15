#!/usr/bin/env python3
from brain_games.game.game_engine import engine
from brain_games.game.even_numbers import quest

def main():
    print('Welcome to the Brain Games!')
    engine(4, 'What number is missing in the progression?')

if __name__ == '__main__':
    main()
