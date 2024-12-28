# Tic Tac Toe Game

A simple tic-tac-toe game written in Python, allowing you to play against the computer.

---

## Table of Contents
- [Required Dependencies](#required-dependencies)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [Game Rules](#game-rules)
- [Difficulty Levels](#difficulty-levels)
- [Results and Leaderboard](#results-and-leaderboard)
- [License](#license)
- [Author](#author)

---

## Required Dependencies
To run this game, you need to install the following libraries:

- `pygame`: A set of Python modules designed for writing video games, including sound playback.
- `windows-curses` (only on Windows): A compatibility library to enable `curses` on Windows.

You can install them automatically by running:

```bash
python install_requirements.py
```

Alternatively, install them manually:

```bash
pip install pygame==2.5.2
```
```bash
pip install windows-curses  # Only for Windows users
```

---

## Installation Instructions

1. **Ensure you have Python installed**:
   - Download and install Python 3.10+ from [python.org](https://www.python.org/).

2. **Clone the repository**:
   ```bash
   git clone https://github.com/Matsunaru/TicTacToe-Akill.git
   cd TicTacToe-Akill
   ```

3. **Install dependencies**:
   Run the provided script to install required packages:
   ```bash
   python install_requirements.py
   ```

4. **Run the game**:
   Start the game using the following command:
   ```bash
   python Start_Menu.py
   ```

---

## Usage Instructions

1. **Navigate the menu**:
   - Use **Up/Down arrow keys** or **W/S** to move between options.
   - Press **Enter** to confirm your selection.

2. **Start a new game**:
   - Select **Start** in the menu to play.

3. **Control the game**:
   - Use keys `1-9` to place your "X" on the board. The positions correspond to the numeric keypad:
     ```
     1 | 2 | 3
     ---------
     4 | 5 | 6
     ---------
     7 | 8 | 9
     ```

4. **Adjust difficulty**:
   - Select **Poziom Trudności** to choose between:
     - `KidBot(Łatwy)` – Random moves by the computer.
     - `TopBot(Trudny)` – Computer uses the minimax algorithm.

5. **View results**:
   - Select **Wyniki** to see the top scores.

6. **Exit the game**:
   - Select **Wyjdz** to quit.

---

## Game Rules

- The player ("X") starts the game.
- Players take turns placing their symbols on the board.
- The objective is to align three symbols in a row (horizontal, vertical, or diagonal).
- The game ends when:
  - A player wins.
  - The board is full (resulting in a draw).

---

## Difficulty Levels

1. **KidBot(Łatwy)**:
   - The computer plays randomly, making it easier to win.

2. **TopBot(Trudny)**:
   - The computer uses the minimax algorithm, providing a real challenge.

---

## Results and Leaderboard

- The game saves your top 10 scores in a file called `scores.txt`.
- You can check your rank in the **Wyniki** menu.
- If your score is in the top 10, you will be prompted to enter your name.

---

## License

### Sound and Music Credits:
- **Enter Sound**: [LTSoundEffects](https://www.youtube.com/watch?v=X-aU6-cSRdA&ab_channel=LTSoundEffects)
- **Up/Down Sound**: [FreeSoundEffectsFesliyanStudios](https://www.youtube.com/watch?v=_vs49MJwwSw&ab_channel=FreeSoundEffectsFesliyanStudios)
- **Game Music for KidBot**: [Sean Phillips Music](https://www.youtube.com/watch?v=bsF4MLRE1vU&ab_channel=SeanPhillipsMusic)
- **Game Music for TopBot**: [Leviathan_Music](https://www.youtube.com/watch?v=kHQ9Ey-enmU&ab_channel=Leviathan_Music)

---

## Author

- Creator: [Matsunaru](https://github.com/Matsunaru)

Feel free to contribute to this project by submitting Pull Requests or reporting issues!

