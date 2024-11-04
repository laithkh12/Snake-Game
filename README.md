# Snake Game

This project is a classic Snake game implemented in Python using the Turtle graphics library. Control the snake to navigate the screen, grow, and avoid colliding with walls or itself.

## Table of Contents
- [Features](#features)
- [Code Overview](#code-overview)
  - [main.py](#mainpy)
  - [snake.py](#snakepy)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [License](#license)

## Features
- **Snake Movement** - Control the snake's direction with the arrow keys.
- **Screen Boundaries** - The game screen is set to 600x600 pixels with a black background.
- **Growth Mechanism** - Snake grows each time it moves successfully.

## Code Overview

### main.py
This file initializes the game environment and manages the main game loop.

- **Screen Setup**: A 600x600 pixel screen is created, with a black background.
- **Snake Creation**: An instance of the `Snake` class is created to initialize the snake's starting position.
- **Key Bindings**: Arrow keys (`Up`, `Down`, `Left`, `Right`) are used to control the snake's movement.
- **Game Loop**: The loop updates the screen and moves the snake, maintaining a delay for smooth gameplay.

```python
from turtle import Turtle, Screen
import time
from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
```

## snake.py
This file defines the Snake class, which manages the snake's attributes and behaviors.
- Starting Positions: The snake starts as three white squares aligned horizontally.
- Movement: The snake moves forward by a set distance. Each segment follows the position of the segment in front of it.
- Direction Control: Arrow key functions set the direction of the snake’s head without allowing a 180-degree reversal.
```python
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for position in STARTING_POSITIONS:
            newSegment = Turtle("square")
            newSegment.color("white")
            newSegment.penup()
            newSegment.goto(position)
            self.segments.append(newSegment)

    def move(self):
        for segNum in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segNum - 1].xcor()
            newY = self.segments[segNum - 1].ycor()
            self.segments[segNum].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
  ```

## Requirements
- Python 3.x
- Turtle graphics library (included with Python)

## How to Run
1. Clone the repository or download the script files.
2. Run main.py to start the game:
```bash
python main.py
```
3. Use the arrow keys (Up, Down, Left, Right) to control the snake’s direction.

## License
This project is open-source and available under the MIT License.



Enjoy playing the classic Snake game in Python!
