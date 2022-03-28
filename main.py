from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from MyScreenController import Controller
from MyScreenModel import Model
from kivy.core.window import Window
from kivy.metrics import dp


class PassMVC(MDApp):
    def __init__(self):
        super().__init__()
        self.table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.9, 0.9),
            use_pagination=True,
            elevation=2,
            rows_num=7,
            pagination_menu_height=240,
            background_color=(0, 1, 0, .10),
            column_data=[
                ("[color=#123487]FIO[/color]", dp(40)),
                ("[color=#123487]Line-up (if available)[/color]", dp(40)),
                ("[color=#123487]Position[/color]", dp(20)),
                ("[color=#123487]Titles[/color]", dp(20)),
                ("[color=#123487]Sport type[/color]", dp(30)),
                ("[color=#123487]Rank[/color]", dp(25)),
            ],
        )
        self.model = Model(table=self.table)
        self.controller = Controller(self.model)

    def build(self):
        Window.size = (1920, 1080)
        return self.controller.get_screen()


PassMVC().run()
