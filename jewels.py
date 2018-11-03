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

# Constants for color/texture
WHITE = 0
VIOLET = 1
GREEN = 2
BLUE = 3
YELLOW = 4
RED = 5

# Create a list of textures to be used
gem_texture_list = []
gem_texture = arcade.load_texture("images/gems/white.png", scale=SPRITE_SCALING_GEM)
gem_texture_list.append(gem_texture)
gem_texture = arcade.load_texture("images/gems/violet.png", scale=SPRITE_SCALING_GEM)
gem_texture_list.append(gem_texture)
gem_texture = arcade.load_texture("images/gems/green.png", scale=SPRITE_SCALING_GEM)
gem_texture_list.append(gem_texture)
gem_texture = arcade.load_texture("images/gems/blue.png", scale=SPRITE_SCALING_GEM)
gem_texture_list.append(gem_texture)
gem_texture = arcade.load_texture("images/gems/yellow.png", scale=SPRITE_SCALING_GEM)
gem_texture_list.append(gem_texture)
gem_texture = arcade.load_texture("images/gems/red.png", scale=SPRITE_SCALING_GEM)
gem_texture_list.append(gem_texture)


class Gem(arcade.Sprite):
    """ Here the gems are created """

    def __init__(self):
        super().__init__()
        self.cell = random.randrange(6)
        self.texture = gem_texture_list[self.cell]


    def get_texture(self):
        """This returns gem texture """
        return self.texture


    def reset_pos(self):
        """ Resets the position above the screen """
        # reset the gem to a spot above the screen
        self.center_y = GRID_HEIGHT


    def update(self):
        """ Updates the state of the gem"""
        # moves the gem downward
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class Player(object):
    """ Here the player is created"""


    def __init__(self):
        # Player score should start at 0
        self.score = 0


# THIS BUILDS THE GAME
class MyGame(arcade.Window):
    """ Custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "JEWELS")
        # 2 dimensional list
        self.grid = list(list(range(0, COLUMN_COUNT)) for i in range(0, ROW_COUNT))
        self.x = None
        self.y = None

        #player = Player()        
        self.score = 0
        # Show the mouse cursor
        self.set_mouse_visible(True)
        arcade.set_background_color((119, 107, 136))


    def position(self, row, col):
        self.x = 250 + (MARGIN + CELL_WIDTH) * col + MARGIN + CELL_WIDTH // 2
        self.y = 250 + (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2


    def setup(self):
        """ Set up the game and initialize the variables. """

        #create sprite list
        self.gem_sprite_list = arcade.SpriteList()
        self.score = 0

        # initialize gems, establish their position
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                self.position(row, col)
                gem_sprite = Gem()
                gem_sprite.center_x = self.x
                gem_sprite.center_y = self.y
                self.grid[row][col] = gem_sprite.cell
                self.gem_sprite_list.append(gem_sprite)


    def match_gems(self):
       # Check for horizontal matches
        result = []
        match_count = 0
        match = 0
        for row in range(len(self.grid)):
            cell_type = -1
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == cell_type:
                    match_count += 1
                else:
                    if match_count >= 3:
                        result.append(f"Match of {match_count} on row {row} from column {col - match_count}, {col - 1}")
                        if match_count == 3:
                            match = 3
                        elif match_count == 4:
                            match = 4
                    cell_type = self.grid[row][col]
                    match_count = 1
                #print(self.grid[row][col], end=" ")

            if match_count >= 3:
                result.append(f"Match of {match_count} on row {row} from column {col - match_count + 1}, {col}")

            #print()

        #print(result)
        #print()
        return match

    def set_score(self):
        if self.match_gems() == 3:
            self.score += 15
        elif self.match_gems() == 4:
            self.score += 40


    def on_draw(self):
        """ Draws the game """
        arcade.start_render()

        # draw grid
        for row in range(ROW_COUNT):
            for col in range(COLUMN_COUNT):
                self.position(row, col)
                x = self.x
                y = self.y
                color = (82, 73, 93)
                arcade.draw_rectangle_filled(x, y, CELL_WIDTH, CELL_HEIGHT, color)

        # draw gems 
        self.gem_sprite_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)



    def update(self, delta_time):
        self.match_gems()
        self.set_score()


    def on_mouse_press(self, x, y, button, modifiers):
        # Calculate grid location based on mouse click
        row = (y - 250) // (MARGIN + CELL_HEIGHT)
        column = (x - 250) // (MARGIN + CELL_WIDTH)
        print("Clicked on",column, row)

        # Set the grid location to a value
        self.grid[row][column] == WHITE

        # Set the texture to the right spot
        sprite_index = row * COLUMN_COUNT + column
        self.gem_sprite_list[sprite_index].texture = gem_texture_list[WHITE]



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

