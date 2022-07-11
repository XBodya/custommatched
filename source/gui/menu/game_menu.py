import arcade
import pathlib

path_to_graphics = "{}/graphics".format('/'.join(str(pathlib.Path.cwd()).split('\\')[:-3]))


class MainMenu(arcade.Window):
    """
    Главное меню нахрена я это пишу
    """

    def __init__(self, wight, height, title):
        """

        :param wight: очев
        :param height: очев
        :param title: очев
        """
        super(MainMenu, self).__init__(wight, height, title)

        arcade.set_background_color((0, 0, 0))

        self.menu_buttons = None

        self.game_title = None
        self.game_start = None
        self.game_settings = None
        self.game_mods = None
        self.game_exit = None

    def setup(self):
        self.menu_buttons = arcade.SpriteList()

        self.game_title = arcade.Sprite('{}/menu/buttons_ui/alpha_gmtt.png'.format(path_to_graphics))

        self.game_title.scale = 0.2
        self.game_title.center_x = self.size[0] * 0.5
        self.game_title.center_y = self.size[1] * 0.86

        self.menu_buttons.append(self.game_title)

    def on_update(self, delta: float):
        self.menu_buttons.update()

    def on_draw(self):
        arcade.start_render()
        self.menu_buttons.draw()


if '__main__' == __name__:
    WIDTH, HEIGHT = 1280, 720
    test_mainMenu = MainMenu(
        WIDTH,
        HEIGHT,
        'TEST MAIN MENU'
    )
    test_mainMenu.setup()
    arcade.run()
