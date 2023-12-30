# Tic Tac Toe Game

A simple tic-tac-toe game written in Python, allowing you to play against the computer.

## Required Dependencies
To run this game, you need to install the following libraries:

- `keyboard`: a library for non-blocking keyboard input.
- `pygame`: a set of Python modules designed for writing video games, including sound playback.

You can install them using the following commands:

```bash
pip install keyboard==0.13.5
```
```bash
pip install pygame==2.5.2
```

## Installation Instructions

1. Ensure that you have Python installed.
2. Clone this project to your computer.
3. Run the game using the command python Start_Menu.py

## Usage Instructions
1. Control is done with arrow keys Up/Down, and Enter is used to confirm a selection(outside of the game).
2. Place your "X" on the board using keys 1 to 9 (preferably using the numeric keypad).
3. Choose the "Start" option to begin a new game.
5. The "Poziom Trudności" option allows you to select the game's difficulty level.
6. The "Wyniki" option lets you check the best scores.
7. Select "Wyjdz" to end the game.

## Game Rules

- The player marked as "X" starts the game.
- The player chooses a square on the board to place an "X".
- The goal is to align three of your symbols in a row.
- The game ends when one of the players wins or the board is filled.

## Difficulty Levels

- "KidBot(Łatwy)": The computer makes random moves.
- "TopBot(Trudny)": The computer uses the minimax algorithm for challenging moves.

## Results

- The game saves the best 10 scores in the scores.txt file.
- Check your place in the top 10 results!

## Authors

- Creator: [Matsunaru]

## License
Coppyright free sound/music
- https://www.youtube.com/watch?v=X-aU6-cSRdA&ab_channel=LTSoundEffects (Enter Sound)
- https://www.youtube.com/watch?v=_vs49MJwwSw&ab_channel=FreeSoundEffectsFesliyanStudios (Up/Down)
- Sean Phillips - www.seanphillipsmusic.co.uk - https://www.youtube.com/watch?v=bsF4MLRE1vU&ab_channel=SeanPhillipsMusic (GameMusic for Kidbot)
- https://www.youtube.com/watch?v=kHQ9Ey-enmU&ab_channel=Leviathan_Music (GameMusic for Topbot)
