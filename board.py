from turtle import Turtle

SCORE_FONT = ("Courier", 24, "bold")
RESULT_FONT = ("Courier", 40, "bold italic")


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.round = 1
        self.highest_score = self.get_highest_score()
        
        self.update_board()

    def update_board(self):
        self.clear()
        self.write_scores()
        self.write_rounds()
        self.draw_bottom_line()

    def draw_bottom_line(self):
        self.goto(-280 , -290)
        self.pendown()
        self.pencolor("red")
        self.pensize(3)
        self.forward(560)
        self.penup()

    def write_rounds(self):
        self.goto(150 , -350)
        self.pendown()
        self.pencolor("green")
        self.write(f"ROUND <{self.round}>",
                    align="center", 
                    font=SCORE_FONT)
        self.penup()

    def increase_score(self, score):
        self.score += score
        if self.score >= self.highest_score:
            self.highest_score = self.score
        self.update_board()

    def write_scores(self):
        self.goto(0 , 350)
        self.pendown()
        self.pencolor("green")
        self.write(f"SCORE <{self.score}> | HI-SCORE <{self.highest_score}>", 
                    align="center", 
                    font=SCORE_FONT)
        self.penup()

    def get_highest_score(self):
        try:
            with open("highest_score.txt", mode="r") as file:
                return int(file.readline())
        except FileNotFoundError:
            with open("highest_score.txt", mode="w") as file:
                file.write("0")
                return 0

    def save_highest_score(self):
        with open("highest_score.txt", mode="w") as file:
            file.write(f"{self.highest_score}")

    def announce_game_over(self):
        self.goto(0, 0)
        self.pendown()
        self.pencolor("red")
        self.write("GAME OVER", 
                    align="center", 
                    font=RESULT_FONT)
        self.penup()
        self.save_highest_score()

    def announce_winner(self):
        self.goto(0, 0)
        self.pendown()
        self.pencolor("blue")
        self.write("YOU WIN!", 
                    align="center", 
                    font=RESULT_FONT)
        self.penup()
        self.save_highest_score()
