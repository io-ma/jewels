import arcade
import random
import jewels as j


class TestMyGame():

    def test_setup(self):
        game = j.MyGame()
        game.setup()
        assert len(game.grid) == j.ROW_COUNT
        assert len(game.grid[0]) == j.COLUMN_COUNT
        assert len(game.gem_sprite_list) == j.ROW_COUNT * j.COLUMN_COUNT
