# Tic-Tac-Toe Game

A simple implementation of the classic Tic-Tac-Toe game in Python. This game allows two players to take turns marking the spaces in a 3x3 grid with 'X' and 'O'. The game ends when one player wins by getting three of their marks in a row, column, or diagonal, or when there is a draw if all spaces are filled without a winner.

## Features
- Two-player mode: Play against a friend on the same device.
- Interactive game board displayed in the console.
- Option to restart the game after it ends.
- Simple and easy-to-understand gameplay.
  
1. Run the game:
   ```bash
   python tic_tac_toe.py
   ```

2. The game will display a grid, and players will be prompted to enter their moves (row and column).
   
3. The game alternates between player 'X' and player 'O' after each move.

4. After the game ends, you’ll be informed if there's a winner or if it's a draw. You can choose to restart the game.

## Game Rules
- The board is a 3x3 grid.
- Player 1 uses 'X', and Player 2 uses 'O'.
- Players take turns marking an empty cell.
- The game ends when a player has three of their marks in a row (horizontally, vertically, or diagonally).
- If all cells are filled and no player has won, it is a draw.

## Example Gameplay

```
Player 1 (X) | Player 2 (O)
  |   |  
--|---|---
  |   | 
--|---|---
  |   |   
```

- Player 1 enters `1 1` to place 'X' in the top-left corner.
- Player 2 enters `2 2` to place 'O' in the center.
- Continue until a winner or draw is determined.

## Contributing
Feel free to fork the repository and submit pull requests with improvements, bug fixes, or new features!

## License
This project is open-source and available under the MIT License.

---
