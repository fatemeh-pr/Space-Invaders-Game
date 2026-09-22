from turtle import Turtle


class Spaceship(Turtle):
    def __init__(self, position, spaceship_shape, bullet_shape):
        super().__init__()
        self.shape(spaceship_shape)
        self.penup()
        self.setheading(90)
        self.goto(position)
        self.lives = 3
        self.bullets_shape = bullet_shape
        self.bullets = []

    def move_right(self):
        x_cor, y_cor = self.xcor(), self.ycor()
        if x_cor < 270:
            self.goto(x_cor + 10, y_cor)

    def move_left(self):
        x_cor, y_cor = self.xcor(), self.ycor()
        if x_cor > -270:
            self.goto(x_cor - 10, y_cor)

    def create_bullet(self):
        bullet = Turtle()
        bullet.penup()
        bullet.shape(self.bullets_shape)
        bullet.goto(self.xcor(), self.ycor() + 20)
        self.bullets.append(bullet)

    def shoot(self):
        for bullet in self.bullets:
            bullet.goto(bullet.xcor(), bullet.ycor() + 10)

    def destroy_bullet(self, bullet):
        bullet.hideturtle()
        self.bullets.remove(bullet)
