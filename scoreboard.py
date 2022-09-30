from turtle import Turtle

SCORE_INCREMENT = 2
SCORE_BOARD_TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color(SCORE_BOARD_TEXT_COLOR)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", False, align=ALIGNMENT, font=FONT)

    def score_increase_right(self):
        self.r_score += SCORE_INCREMENT
        self.update_score_board()

    def score_increase_left(self):
        self.l_score += SCORE_INCREMENT
        self.update_score_board()
