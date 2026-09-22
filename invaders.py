import random
from turtle import Turtle


class BulletManager:
    def __init__(self, aliens, shape):
        self.bullets = []
        self.shape = shape
        self.aliens = aliens

    def create_bullet(self):
        alien = random.choice(self.aliens)
        bullet = Turtle()
        bullet.penup()
        bullet.shape(self.shape)
        bullet.goto(alien.xcor(), alien.ycor() - 20)
        self.bullets.append(bullet)
        
    def shoot(self):
        if random.randint(1, 10) == 1:
            self.create_bullet()
        for bullet in self.bullets:
            bullet.goto(bullet.xcor(), bullet.ycor() - 20)

    def destroy(self, bullet):
        bullet.hideturtle()
        self.bullets.remove(bullet)


class Aliens:
    def __init__(self, alien_shapes, bullet_shape):
        self.aliens = []
        self.shapes = alien_shapes
        self.bullets = BulletManager(self.aliens, bullet_shape)
        self.moving_direction = 1
        self.moving_speed = 0.1

        self.create_aliens()

    def create_aliens(self):
        scores = [30, 20, 10]
        x_cor = -280
        y_cor = 300
        for row in range(3):
            for col in range(10):
                alien = Turtle()
                alien.penup()
                alien.shape(random.choice(self.shapes))
                alien.score = scores[row]
                alien.goto(x_cor, y_cor)
                self.aliens.append(alien)
                x_cor += 50
            y_cor -= 30
            x_cor = -280

    def move_sideways(self):
        if random.randint(1, 3) == 1:
            for alien in self.aliens:
                if alien.xcor() + 20 >= 290:
                    self.moving_direction = -1
                    break
                elif alien.xcor() - 20 <= -290:
                    self.moving_direction = 1
            
            for alien in self.aliens:
                alien.goto(alien.xcor() + (20 * self.moving_direction), alien.ycor())

    def move_down(self):
        if random.randint(1, 20) == 1:
            for alien in self.aliens:
                alien.goto(alien.xcor(), alien.ycor() - 10)

    def destroy_alien(self, alien):
        alien.hideturtle()
        self.aliens.remove(alien)

    def increase_speed(self):
        self.moving_speed /= 1.2


class UFOS:
    def __init__(self, shape):
        self.ufos = []
        self.shape = shape

    def create_ufo(self):
        ufo = Turtle()
        ufo.shape(self.shape)
        ufo.penup()
        ufo.goto(-400, 300)
        ufo.score = 50
        self.ufos.append(ufo)

    def move(self):
        for ufo in self.ufos[:]:
            ufo.goto(ufo.xcor() + 10, ufo.ycor())
            if ufo.xcor() > 400:
                self.destroy_ufo(ufo)

    def destroy_ufo(self, ufo):
        ufo.hideturtle()
        self.ufos.remove(ufo)
