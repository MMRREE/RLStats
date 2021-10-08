import tkinter as tk
import FileSystem


class GameWindow(tk.Frame):
    def __init__(self, master=None, game=None):
        super().__init__(master=master)

        self.master = master
        self.game = game

        self.createWidgets()
    # End of __init__

    def createWidgets(self):
        self.master.title(self.game.Date.strftime(
            "%d/%m: %H:%M: ") + self.game.mode)
        defaultIco = FileSystem.resource_path('icon.ico')
        self.master.iconbitmap(default=defaultIco)

        self.master.protocol("WM_DELETE_WINDOW", self.onExit)
    # End of createWidgets

    def onExit(self):
        self.master.destroy()
    # End of onExit
# End of gameWindow
