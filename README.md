# Graphical-python-drawing
This repository features a graphical drawing application built using the pygame library, allowing users to interactively draw points and squares on the screen. It implements basic drawing features like adding color, resizing squares, and positioning objects using mouse and keyboard inputs.

## Features:
-Draw a Point: Left-click on the screen after pressing the "A" key to place a point at the clicked position.

-Draw a Square: Left-click on the screen after pressing the "S" key to place a square at the clicked position.

-Change Colors: Use the following key combinations to change the colors of the point and square:

-**"QA"**: Red

-**"WA"**: Green

-**"EA"**: Blue

-**"QS"**: Red (for square)

-**"WS"**: Green (for square)

-**"ES"**: Blue (for square)

-Resize Square: Press **"F1"** to increase the square size and **"F2"** to decrease it.

-Real-Time Drawing: Points and squares are immediately updated as you move them around the screen or change their properties.

## Files
-**main.py**: The main entry point of the application. It initializes the pygame window, sets up the game loop, and handles user inputs to update and render graphical objects. The objects (point and square) are drawn on the screen, and their properties can be modified interactively.

-**classes.py**: Contains the *Point* and *Square* classes. The *Point* class represents a simple pixel, while the *Square* class represents a square shape made up of multiple pixels. Both classes support various methods for altering their position, color, and size.

-**event_key_handler.py**: Handles user inputs. The *eventhandler* function processes mouse clicks and keyboard events to move the *Point* and *Square*, as well as change their color or size. The *keyhandler* function listens for key presses to modify the drawing.

## Planned Enhancements
Adding additional shapes, such as circles, squares, and lines.
Ability to dynamically change shape sizes etc.
Expanding interactive control options and real-time parameter adjustments.

## Requirements:
[Pygame](https://www.pygame.org/wiki/GettingStarted)

[Python 3.x](https://www.python.org/downloads/)

## Installation:
1. Clone this repository:
```bash
git clone https://github.com/Treechcer/Graphical-python-drawing.git
```

2. Install the necessary dependencies:
 ```bash
pip install pygame
 ```

3. Run the application:
 ```bash
python main.py
 ```

## License:
This project is licensed under the MIT License - see the LICENSE file for details.
