#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games.progression_game import progress


def main():
    run_game(progress, 'What number is missing in the progression?')


if __name__ == '__main__':
    main()
