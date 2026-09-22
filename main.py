import time
from turtle import Screen
from shapes import add_shapes
from spaceship import Spaceship
from invaders import Aliens, UFOS
from board import Board
from bunkers import Bunkers

SPACESHIP_POSITION = (0, -250)
BACKUP_POSITIONS = [(-220, -330), (-170, -330)]

screen = Screen()
screen.title("Space Invaders")
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.tracer(0)

shapes = add_shapes(screen_object=screen)
board = Board()
bunkers = Bunkers()
ufos = UFOS(shapes["ufo"])
aliens = Aliens(shapes["aliens"], shapes["alien_bullet"])
spaceship = Spaceship(SPACESHIP_POSITION, shapes["spaceship"], shapes["spaceship_bullet"])
backup_spaceships = [Spaceship(BACKUP_POSITIONS[life], shapes["spaceship"], shapes["spaceship_bullet"])
                    for life in range(spaceship.lives - 1)]


def close_game():
    board.save_highest_score()
    screen.bye()


screen.getcanvas().winfo_toplevel().protocol(
    "WM_DELETE_WINDOW",
    close_game
)

screen.listen()
screen.onkey(spaceship.move_right, "Right")
screen.onkey(spaceship.move_left, "Left")
screen.onkey(spaceship.create_bullet, "space")

game_over = False
while not game_over:
    screen.update()
    time.sleep(aliens.moving_speed)

    # Level Up
    if not aliens.aliens:
        board.round += 1
        if board.round > 10:
            for remaining_bullet in spaceship.bullets[:]:
                spaceship.destroy_bullet(remaining_bullet)
            for remaining_bullet in aliens.bullets.bullets[:]:
                aliens.bullets.destroy(remaining_bullet)
            board.announce_winner()
            screen.update()
            break
        else:
            for remaining_bullet in aliens.bullets.bullets[:]:
                aliens.bullets.destroy(remaining_bullet)
            aliens.create_aliens()
            aliens.increase_speed()
            bunkers.reset_bunkers()
        board.update_board()

    spaceship.shoot() 
    aliens.bullets.shoot()
    aliens.move_sideways()
    aliens.move_down()
    ufos.move()

    # Detect spaceship bullets collisions
    for spaceship_bullet in spaceship.bullets[:]:
        destroyed = False
        # Detect spaceship bullets collision with top border line
        if spaceship_bullet.ycor() > 320:
            spaceship.destroy_bullet(spaceship_bullet)
            continue

        # Detect spaceship bullets collision with aliens
        for alien in aliens.aliens:
            if (abs(alien.xcor() - spaceship_bullet.xcor()) < 18 
                and abs(alien.ycor() - spaceship_bullet.ycor()) < 15):
                board.increase_score(alien.score)
                spaceship.destroy_bullet(spaceship_bullet)
                aliens.destroy_alien(alien)
                # Create a UFO everytime 10 aliens die
                if aliens.aliens and len(aliens.aliens) % 10 == 0 and board.round != 10:
                    ufos.create_ufo()
                destroyed = True
                break
        if destroyed:
            continue
                
        # Detect spaceship bullets collision with ufo ships
        for ufo in ufos.ufos:
            if spaceship_bullet.distance(ufo) < 30:
                board.increase_score(ufo.score)
                ufos.destroy_ufo(ufo)
                spaceship.destroy_bullet(spaceship_bullet)
                destroyed = True
                break
        if destroyed:
            continue

        # Detect spaceship bullets and aliens bullets collision
        for alien_bullet in aliens.bullets.bullets:
            if (abs(alien_bullet.xcor() - spaceship_bullet.xcor()) < 10 
                and abs(alien_bullet.ycor() - spaceship_bullet.ycor()) < 13):
                spaceship.destroy_bullet(spaceship_bullet)
                aliens.bullets.destroy(alien_bullet)
                destroyed = True
                break
        if destroyed:
            continue

        # Detect spaceship bullets collision with bunkers
        for bunker in bunkers.blocks:
            if spaceship_bullet.distance(bunker) < 15:
                spaceship.destroy_bullet(spaceship_bullet)
                bunkers.destroy_block(bunker)
                destroyed = True
                break
        if destroyed:
            continue


    # Detect aliens bullets collisions
    for alien_bullet in aliens.bullets.bullets[:]:
        destroyed = False
        # Detect aliens bullet collision with bottom border line
        if alien_bullet.ycor() < -280:
            aliens.bullets.destroy(alien_bullet)
            continue

        # Detect aliens bullet collision with spaceship
        if (abs(alien_bullet.xcor() - spaceship.xcor()) < 25 
            and abs(alien_bullet.ycor() - spaceship.ycor()) < 20):
            if spaceship.lives > 1:
                spaceship.lives -= 1
                backup_spaceships[0].goto(1000, 1000)
                backup_spaceships.pop(0)
                aliens.bullets.destroy(alien_bullet)
            else:
                board.announce_game_over()
                game_over = True
            break

        # Detect aliens bullets collision with bunkers
        for bunker in bunkers.blocks:
            if alien_bullet.distance(bunker) < 15:
                aliens.bullets.destroy(alien_bullet)
                bunkers.destroy_block(bunker)
                destroyed = True
                break
        if destroyed:
            continue

    # Detect  if aliens reach the bottom border line or the spaceship
    for alien in aliens.aliens:
        if alien.distance(spaceship) <= 35 or alien.ycor() <= -280:
            board.announce_game_over()
            game_over = True
            break

screen.mainloop()
