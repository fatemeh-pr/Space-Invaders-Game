from turtle import Turtle

BUNKERS_POSITIONS = [
    # first bunker
    (-240, -20), (-220, -20), (-200, -20), (-180, -20), (-240, -40),
    (-240, -60), (-240, -80), (-180, -40), (-180, -60), (-180, -80),
    # second bunker
    (-100, -20), (-80, -20), (-60, -20), (-40, -20), (-100, -40), 
    (-100, -60), (-100, -80), (-40, -40), (-40, -60), (-40, -80),
    # third bunker
    (40, -20), (60, -20), (80, -20), (100, -20), (40, -40),
    (40, -60), (40, -80), (100, -40), (100, -60), (100, -80),
    # fourth bunker
    (180, -20), (200, -20), (220, -20), (240, -20), (180, -40), 
    (180, -60), (180, -80), (240, -40), (240, -60), (240, -80)
    ]


class Bunkers:
    def __init__(self):
        self.blocks = []
        self.create_bunkers()

    def create_bunkers(self):
        for position in BUNKERS_POSITIONS:
            bunker = Turtle()
            bunker.penup()
            bunker.shape("square")
            bunker.fillcolor("yellow")
            bunker.goto(position)
            self.blocks.append(bunker)

    def destroy_block(self, bunker):
        bunker.hideturtle()
        self.blocks.remove(bunker)

    def reset_bunkers(self):
        for bunker in self.blocks:
            bunker.hideturtle()
        self.blocks.clear()
        self.create_bunkers()
