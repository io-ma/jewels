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
        # a total of 28 possbile combos
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
        gem = Gem()
        self.match = []
        self.matcher = {}
        for row in range(ROW_COUNT):
            # Add an empty list  that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.cell = gem.set_gem_color()
                self.grid[row].append(self.cell) # Append a cell
                self.match.append(self.cell)
        print(f"self.match is: {self.match}")
        #self.matcher = Counter(self.match)
        #print(self.matcher)
        #print(f"self.grid[row] is: {self.grid[row]}")
        """for x in self.matcher:
            print(f"cell is: {x}")
            if x in self.grid[row]:
                print(f"x index: {self.grid[row].index(x)}")
            else:
                print("Not in this row")"""

        self.white_list = None
        self.violet_list = None
        self.blue_list = None
        self.green_list = None
        self.yellow_list = None
        self.red_list = None
        self.gems = None
        print(self.grid)
        # Set up the player info
        # self.score = 0

        # Show the mouse cursor
        self.set_mouse_visible(True)

        arcade.set_background_color((119, 107, 136))

    def match(self):
        matches = []
        matches.append(cell) for cell in self.grid[row] if cell == cell.next()
        return matches

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Sprite lists
        # self.gem_list = arcade.SpriteList()

        # Score logic will go here
        self.score = 0

        self.white_list = arcade.SpriteList()
        self.violet_list = arcade.SpriteList()
        self.blue_list = arcade.SpriteList()
        self.green_list = arcade.SpriteList()
        self.yellow_list = arcade.SpriteList()
        self.red_list = arcade.SpriteList()

        # Create the gems
        #for i in range(self.GEM_COUNT):

        # Create the gem instance
        white = Gem("images/gems/white.png", SPRITE_SCALING_GEM)
        red = Gem("images/gems/red.png", SPRITE_SCALING_GEM)
        blue = Gem("images/gems/blue.png", SPRITE_SCALING_GEM)
        green = Gem("images/gems/green.png", SPRITE_SCALING_GEM)
        yellow = Gem("images/gems/yellow.png", SPRITE_SCALING_GEM)
        violet = Gem("images/gems/violet.png", SPRITE_SCALING_GEM)

        # I have to implement this better!
        self.violet_list.append(violet)
        self.red_list.append(red)
        self.blue_list.append(blue)
        self.green_list.append(green)
        self.yellow_list.append(yellow)
        self.white_list.append(white)
        self.gems = [self.white_list, self.violet_list, self.red_list, self.blue_list, self.yellow_list, self.green_list]


    def position_gems(self,gem_list,row, column):
        # Position the gem
        """self.set_gem_color()"""
        for gem in gem_list:
            gem.center_x = 250 + (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
            gem.center_y = 250 + (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2

    """def match_gems(self):
        match = [self.grid[row][column]]
        print(Counter(match))"""


    def on_draw(self):
        """ Draws the game """
        arcade.start_render()

        # Draw the grid
        # Draw the box
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                color = (82, 73, 93)

                # Figure out where the cell is
                x = 250 + (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
                y = 250 + (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2

                arcade.draw_rectangle_filled(x, y, CELL_WIDTH, CELL_HEIGHT, color)

                #THIS NEEDS more thinking
                # Position the gem
                for gem_list in self.gems:
                    self.position_gems(gem_list, row, column)
                if self.grid[row][column] == 0:
                    self.white_list.draw()
                elif self.grid[row][column] == 1:
                    self.violet_list.draw()
                elif self.grid[row][column] == 2:
                    self.green_list.draw()
                elif self.grid[row][column] == 3:
                    self.blue_list.draw()
                elif self.grid[row][column] == 4:
                    self.yellow_list.draw()
                else:
                    self.red_list.draw()


        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        #self.match_gems()
        print(f"matches in self.match are: {self.match()}")
        arcade.finish_render()


    def update(self, delta_time):
        # updates the gem list as time passes
        self.white_list.update()
        self.violet_list.update()
        self.blue_list.update()
        self.yellow_list.update()
        self.green_list.update()
        self.red_list.update()



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

