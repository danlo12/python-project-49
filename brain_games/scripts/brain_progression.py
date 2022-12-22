#!/usr/bin/env python3
from brain_games.game_engine import engine
from brain_games.game.progression_game import progress


def main():
    engine(progress, 'What number is missing in the progression?')


if __name__ == '__main__':
    main()
