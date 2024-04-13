from turtle import Turtle

STARTING_POSITIONS=(0,-270)
MOVE_DISTANCE=10
FINISH_LINE_Y=280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITIONS)
        self.setheading(90)



    def go_up(self):
        new_y=self.ycor()+10
        new_x=self.xcor()
        self.goto(new_x,new_y)

    def is_at_finish_line(self):
        self.goto(0,280)

    def go_to_start(self):
        self.goto(STARTING_POSITIONS)




