from turtle import Turtle
ALIGN = 'center'
FONT = ('Calibri', '17', 'normal')

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.shape()
        self.color('light pink')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=222)
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)
    def up_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)
    def game_over(self):
        self.goto(x=0, y=0)
        self.write('GAME OVER', align=ALIGN, font=FONT)
