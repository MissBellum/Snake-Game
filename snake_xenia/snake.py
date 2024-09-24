from turtle import Turtle
BODY = [(0, 0), (-20, 0), (-40, 0)]
DIRECTIONS = [0, 90, 180, 270]

class Snake():
    def __init__(self) -> None:
        self.piece = []
        self.create()
        self.head = self.piece[0]

    def create(self):
        for bod in BODY:
            self.add_bod(bod)
            
    def add_bod(self, bod):
        snake = Turtle(shape='square')
        snake.shapesize(stretch_len=1, stretch_wid=1)
        snake.color('light pink')
        #snake.penup()
        snake.speed('slow')
        snake.goto(bod)
        self.piece.append(snake)
    def extend(self):
        self.add_bod(self.piece[-1].position()) 
    def move(self):
        for each in range(len(self.piece) - 1, 0, -1):
            new_x = self.piece[each -1].xcor()
            new_y = self.piece[each -1].ycor()
            self.piece[each].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DIRECTIONS[3]:
            self.head.setheading(DIRECTIONS[1])
    def down(self):
        if self.head.heading() != DIRECTIONS[1]:
            self.head.setheading(DIRECTIONS[3])
    def left(self):
        if self.head.heading() != DIRECTIONS[0]:
            self.head.setheading(DIRECTIONS[2])
    def right(self):
        if self.head.heading() != DIRECTIONS[2]:
            self.head.setheading(DIRECTIONS[0])
