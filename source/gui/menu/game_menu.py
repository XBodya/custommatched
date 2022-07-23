import arcade
import pathlib

path_to_graphics = ''


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

        # спрайты названия игры, кнопок: ИГРАТЬ, НАСТРОЙКИ, МОДЫ, ВЫХОД
        self.game_title = arcade.Sprite('{}menu/buttons_ui/logo.png'.format(path_to_graphics))

        self.game_title.scale = 0.4
        self.game_title.center_x = self.size[0] * 0.5
        self.game_title.center_y = self.size[1] * 0.8

        self.game_start = arcade.Sprite('{}menu/buttons_ui/play.png'.format(path_to_graphics))

        self.game_start.scale = 0.3
        self.game_start.center_x = self.size[0] * 0.5
        self.game_start.center_y = self.size[1] * 0.55

        self.game_settings = arcade.Sprite('{}menu/buttons_ui/settings.png'.format(path_to_graphics))

        self.game_settings.scale = 0.3
        self.game_settings.center_x = self.size[0] * 0.5
        self.game_settings.center_y = self.size[1] * 0.4

        self.game_mods = arcade.Sprite('{}menu/buttons_ui/mods.png'.format(path_to_graphics))

        self.game_mods.scale = 0.3
        self.game_mods.center_x = self.size[0] * 0.5
        self.game_mods.center_y = self.size[1] * 0.25

        self.game_exit = arcade.Sprite('{}menu/buttons_ui/quit.png'.format(path_to_graphics))

        self.game_exit.scale = 0.3
        self.game_exit.center_x = self.size[0] * 0.5
        self.game_exit.center_y = self.size[1] * 0.1

        self.menu_buttons.extend(
            [
                self.game_title,
                self.game_start,
                self.game_settings,
                self.game_mods,
                self.game_exit
            ]
        )

    def on_update(self, delta: float):
        self.menu_buttons.update()

    def on_draw(self):
        arcade.start_render()
        self.menu_buttons.draw()


if '__main__' == __name__:
    path_to_graphics = "{}/graphics/".format('/'.join(str(pathlib.Path.cwd()).split('\\')[:-3]))
    WIDTH, HEIGHT = 1280, 720
    test_mainMenu = MainMenu(
        WIDTH,
        HEIGHT,
        'TEST MAIN MENU'
    )
    test_mainMenu.setup()
    arcade.run()
