
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class MyGridLayout(GridLayout):
    pass

class GridApp(App):
    def build(self):
        return MyGridLayout()



if __name__ == "__main__":
    app = GridApp()
    app.run()
