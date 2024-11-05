from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highScore}")
        self.score = 0
        self.updateScoreBoard()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScoreBoard()
