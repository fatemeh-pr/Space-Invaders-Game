import glob
from tkinter import PhotoImage
from turtle import Shape

UFO = "images/ufo.gif"
SPACESHIP = "images/spaceship.gif"
SPACESHIP_BULLET = "images/spaceship_bullet.gif"
ALIEN_BULLET = "images/alien_bullet.gif"
ALIENS = glob.glob("images/alien-*.gif")


def add_shapes(screen_object):
    spaceship_shape = PhotoImage(file=SPACESHIP).subsample(3, 3)
    spaceship_bullet = PhotoImage(file=SPACESHIP_BULLET).subsample(4, 4)
    alien_bullet = PhotoImage(file=ALIEN_BULLET).subsample(4, 4)
    alien_shapes = [PhotoImage(file=alien_image).subsample(3, 3) for alien_image in ALIENS]
    ufo_shape = PhotoImage(file=UFO).subsample(4, 4)

    screen_object.addshape("spaceship_shape", Shape("image", spaceship_shape))
    screen_object.addshape("spaceship_bullet", Shape("image", spaceship_bullet))
    screen_object.addshape("alien_bullet", Shape("image", alien_bullet))
    screen_object.addshape("ufo_shape", Shape("image", ufo_shape))
    
    alien_shapes_list = []
    for i, alien_shape in enumerate(alien_shapes):
        screen_object.addshape(f"alien_shape_{i}", Shape("image", alien_shape))
        alien_shapes_list.append(f"alien_shape_{i}")

    shapes = {
        "spaceship": "spaceship_shape",
            "spaceship_bullet": "spaceship_bullet",
            "alien_bullet": "alien_bullet",
            "ufo": "ufo_shape",
            "aliens": alien_shapes_list
            }
    return shapes
