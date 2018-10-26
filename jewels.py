"""
My kind of Ultimate Jewels

"""
import arcade
import random
from collections import Counter

# GAME SCENE
# constants
SPRITE_SCALING_GEM = 0.7
#GEM_COUNT = 5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CELL_WIDTH = 55
CELL_HEIGHT = 55
MARGIN = 5
ROW_COUNT = 6 #10
COLUMN_COUNT = 4 #10
GRID_WIDTH = (CELL_WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
GRID_HEIGHT = (CELL_HEIGHT + MARGIN) * ROW_COUNT + MARGIN



class Gem(arcade.Sprite):
    """ Here the gems are created """


    def reset_pos(self):
        """ Resets the position above the screen """
        # reset the gem to a spot above the screen
        self.center_y = GRID_HEIGHT

    def update(self):
        """ Updates the state of the gem"""
        # moves the gem downward
        self.center_y -= 60
        if self.top < 0:
            self.reset_pos()

    def set_gem_color(self):
        return random.randrange(6)

    def get_gem_color(self):
        pass


# I NEED A GRID and place each gem inside a grid cell.

class Player(object):
    """ Here the player is created"""


    def __init__(self):
        # Player score should start at 0
        self.score = 0

# GAME ENGINE GOES HERE
# check pattern of same coloured gems on the grid
#
# establish the possible patterns
    #
    # 3 gems - 15 points
        # vertical or horizontal
        # we have 16 vertical possible combos
        # and 12 horizontal possible combos
        # a total of 28 possible combos
        #
    # 4 gems - 40 points
        # vertical or horizontal
        # we have 12 vertical possible combos
        # and 6 horizontal possible combos
        # a total of 18 possbile combos
        #
    # 5 gems - 100 points
        # vertical, horizontal, key shape
        # we have 8 vertical possible combos
        # and
        # a total of  possible combos


# THIS BUILDS THE GAME
class MyGame(arcade.Window):
    """ Custom Window Class"""


    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "JEWELS")
        # 2 dimensional list
        self.grid = []
        self.gem = Gem()
        #player = Player()
        self.score = 0
        # Show the mouse cursor
        self.set_mouse_visible(True)

        arcade.set_background_color((119, 107, 136))

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Score logic will go here

        #sprite list
        self.gem_sprite_list = arcade.SpriteList()

        for row in range(ROW_COUNT):
            # Add an empty list  that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):

                x = 250 + (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
                y = 250 + (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2

                cell = self.gem.set_gem_color()

                if cell == 0:
                    gem_sprite = Gem("images/gems/white.png", SPRITE_SCALING_GEM)
                elif cell == 1:
                    gem_sprite = Gem("images/gems/violet.png", SPRITE_SCALING_GEM)
                elif cell == 2:
                    gem_sprite = Gem("images/gems/green.png", SPRITE_SCALING_GEM)
                elif cell == 3:
                    gem_sprite = Gem("images/gems/blue.png", SPRITE_SCALING_GEM)
                elif cell == 4:
                    gem_sprite = Gem("images/gems/yellow.png", SPRITE_SCALING_GEM)
                elif cell == 5:
                    gem_sprite = Gem("images/gems/red.png", SPRITE_SCALING_GEM)
                print(type(gem_sprite))

                gem_sprite.cell = cell
                gem_sprite.center_x = x
                gem_sprite.center_y = y

                self.grid[row].append(gem_sprite) # Append a cell
                self.gem_sprite_list.append(gem_sprite)


    def match_gems(self):
       # Check for horizontal matches
        result = []
        match_count = 0
        for row in range(len(self.grid)):
            cell_type = -1
            for column in range(len(self.grid[0])):
                sprite = self.grid[row][column]
                if sprite.cell == cell_type:
                    match_count += 1
                else:
                    if match_count >= 3:
                        result.append(f"Match of {match_count} on row {row} from column {column - match_count}, {column - 1}")
                    cell_type = sprite.cell
                    match_count = 1
                print(sprite.cell, end=" ")

            if match_count >= 3:
                result.append(f"Match of {match_count} on row {row} from column {column - match_count + 1}, {column}")

            print()

        print(result)
        print()


    def on_draw(self):
        """ Draws the game """
        arcade.start_render()

        # draw grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = 250 + (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
                y = 250 + (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2
                color = (82, 73, 93)
                arcade.draw_rectangle_filled(x, y, CELL_WIDTH, CELL_HEIGHT, color)

        # draw gems 
        self.gem_sprite_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)



    def update(self, delta_time):
        self.match_gems()



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

