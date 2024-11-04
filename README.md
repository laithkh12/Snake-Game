# 🐍 Snake Game

A classic Snake game implemented in Python using the Turtle graphics library. Guide the snake to eat food, grow, and avoid obstacles! 🕹️

## 📋 Table of Contents
- [✨ Features](#-features)
- [📂 Code Overview](#-code-overview)
  - [main.py](#mainpy)
  - [snake.py](#snakepy)
  - [food.py](#foodpy)
  - [scoreboard.py](#scoreboardpy)
- [⚙️ Requirements](#️-requirements)
- [▶️ How to Run](#️-how-to-run)
- [📄 License](#-license)

## ✨ Features
- **Snake Movement** - Control the snake's direction using the arrow keys.
- **Screen Boundaries** - Play within a 600x600 pixel game screen with a sleek black background.
- **Growth Mechanism** - The snake grows every time it eats food.
- **Score Tracking** - The scoreboard keeps track of the player’s score.
- **Game Over Condition** - The game ends if the snake collides with walls or itself.

## 📂 Code Overview

### main.py
The main game file that initializes the game environment and manages the primary game loop.

- **Screen Setup**: Creates a 600x600 pixel game screen with a black background.
- **Game Elements**: Initializes instances of `Snake`, `Food`, and `ScoreBoard`.
- **Key Bindings**: Uses arrow keys (`Up`, `Down`, `Left`, `Right`) to control snake movement.
- **Game Loop**: Continuously updates the screen, manages snake movement, handles collisions with food, and checks for game-over conditions.

```python
from turtle import Screen
import time
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increaseScore()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameIsOn = False
        score.gameOver()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameIsOn = False
            score.gameOver()

screen.exitonclick()
```

### Snake.py
Defines the Snake class, which manages the snake’s attributes and behaviors.
- Starting Positions: The snake begins with three segments aligned horizontally.
- Movement: Each segment follows the one ahead, allowing the snake to move fluidly.
- Direction Control: Functions set the snake's direction while preventing it from reversing into itself.
- Extend Snake: The extend() method adds a segment to the snake each time it eats food.
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
            self.addSegment(position)

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

    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)

    def extend(self):
        # add a new seg t the snake
        self.addSegment(self.segments[-1].position())
```

### food.py
Defines the Food class, which manages the food object.
- Food Initialization: Generates a small blue circle as food at random positions on the screen.
- Food Refresh: Moves the food to a new random position each time it's eaten by the snake.
```python
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomX = random.randint(-280, 280)
        randomY = random.randint(-280, 280)
        self.goto(x=randomX, y=randomY)
```

### scoreboard.py
Defines the ScoreBoard class, which tracks and displays the score.
- Score Tracking: Starts at 0 and increases each time the snake eats food.
- Game Over: Displays "GAME OVER" at the end of the game.
```python
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
```

## ⚙️ Requirements
- Python 3.x
- Turtle graphics library (included with Python)

## ▶️ How to Run
1. Clone the repository or download the script files.
2. Run main.py to start the game:
```bash
python main.py
```
3. Use the arrow keys (Up, Down, Left, Right) to control the snake’s direction and enjoy!

## 📄 License
This project is open-source and available under the MIT License.



Enjoy playing the classic Snake game in Python! 🐍✨
