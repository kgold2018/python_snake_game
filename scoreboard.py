from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        # with open("data.txt") as file:
        #     self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
             self.high_score = self.score

             with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        set.score = 0
        self.update_scoreboard()


