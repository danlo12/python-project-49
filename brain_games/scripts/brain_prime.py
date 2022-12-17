#!/usr/bin/env python3
from brain_games.game.game_engine import engine
from brain_games.game.even_numbers import quest

def main():
    print('Welcome to the Brain Games!')
    engine(5, 'Answer "yes" if given number is prime. Otherwise answer "no".')

if __name__ == '__main__':
    main()
