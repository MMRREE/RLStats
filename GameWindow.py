import tkinter as tk
import tkinter.ttk as ttk
import FileSystem
from GUISchema import GameBar
from CollapsiblePane import CollapsiblePane
from Scrollable import ScrollableFrame
import datetime


class GameWindow(tk.Frame):
    def __init__(self, master=None, game=None, mainWindow=None):
        super().__init__(master=master)

        self.master = master
        self.mainWindow = mainWindow

        self.master.withdraw()

        self.game = game

        self.createWidgets()

        self.pack(fill="both", expand=True)

        self.master.deiconify()
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        parentGeometry = "+".join(self.mainWindow.geometry().split("x")
                                  ).split("+")
        size = tuple([int(self.master.winfo_reqwidth()),
                     int(self.master.winfo_reqheight())])
        widthOffset = self.mainWindow.winfo_width()

        x = int(parentGeometry[2]) + int(parentGeometry[0])+15
        y = int(parentGeometry[3])

        self.master.geometry("+%d+%d" % (x, y))
    # End of __init__

    def createWidgets(self):
        self.master.title(self.game.Date.strftime(
            "%d/%m: %H:%M: ") + self.game.mode)
        defaultIco = FileSystem.resource_path('icon.ico')
        self.master.iconbitmap(default=defaultIco)

        self.GameStatsBoxLabel = tk.Label(
            self, text="Game Stats")
        self.GameStatsBoxLabel.grid(
            row=0, column=0, sticky="nw", padx=2, pady=2)

        for collapsible in GameBar:
            if(collapsible['type'] == "collapsible"):
                self.createCollapsible(
                    collapsible, self)
            elif(collapsible['type'] == "widget"):
                self.createWidgetFromSchema(
                    collapsible, self)

        self.exploreSchemaAndUpdate(GameBar, self)

        self.master.protocol("WM_DELETE_WINDOW", self.onExit)
    # End of createWidgets

    def exploreSchemaAndUpdate(self, schema, Frame):
        if(type(schema) is dict):
            if(schema['type'] == "widget"):
                self.updateStat(schema, Frame)
            elif(schema['type'] == "collapsible"):
                self.exploreSchemaAndUpdate(schema['widgets'], Frame)
        elif(type(schema) is list):
            for widget in schema:
                self.exploreSchemaAndUpdate(widget, Frame)
    # End of exploreSchemaAndUpdate

    def createCollapsible(self, collapsibleInfo, master):
        self.__setattr__(collapsibleInfo['name'], CollapsiblePane(
            master, collapsibleInfo['title'] + " <<", collapsibleInfo['title'] + " >>"))
        self.__getattribute__(collapsibleInfo['name']).grid(
            row=collapsibleInfo['gridpos'][0], column=collapsibleInfo['gridpos'][1],
            rowspan=collapsibleInfo['gridspan'][0], columnspan=collapsibleInfo['gridspan'][1],
            sticky="nsew", padx=2, pady=2)

        for widget in collapsibleInfo['widgets']:
            if(widget['type'] == "collapsible"):
                self.createCollapsible(widget, self.__getattribute__(
                    collapsibleInfo['name']).content)
            else:
                self.createWidgetFromSchema(
                    widget, self.__getattribute__(collapsibleInfo['name']).content)
    # End of createCollapsible

    def createWidgetFromSchema(self, widgetInfo, master):
        if(widgetInfo['type'] == "widget"):
            self.__setattr__(widgetInfo['name'], tk.Label(
                master, text=widgetInfo['title'] + " N/A"))
        else:
            self.__setattr__(widgetInfo['name'],
                             ttk.__getattribute__(widgetInfo['type'])(master))
            if('args' in widgetInfo.keys()):
                for arg in widgetInfo['args']:
                    self.__getattribute__(widgetInfo['name']).configure(arg)

            if('binds' in widgetInfo.keys()):
                for bind in widgetInfo['binds']:

                    self.__getattribute__(widgetInfo['name']).bind(
                        next(iter(bind)), next(iter(bind.items())))
        if('sticky' in widgetInfo.keys()):
            sticky = widgetInfo['sticky']
        else:
            sticky = "nw"
        self.__getattribute__(widgetInfo['name']).grid(
            row=widgetInfo['gridpos'][0], column=widgetInfo['gridpos'][1],
            rowspan=widgetInfo['gridspan'][0], columnspan=widgetInfo['gridspan'][1],
            sticky=sticky, padx=2, pady=2)
    # End of createWidgetFromSchema

    def updateWidgetFromSchema(self, widgetInfo, value):
        self.__getattribute__(widgetInfo['name']).configure(
            text=widgetInfo['title'] + value)
    # End of updateWidgetFromSchema

    def updateStat(self, widget, Frame):
        if("tags" in widget.keys()):
            rawValue = self.returnValueFromKeyString(widget['tags'])
            if(type(rawValue) is int or type(rawValue) is float):
                value = f"{rawValue:{widget['precision']}}"
            elif(type(rawValue) is datetime.datetime):
                value = rawValue.strftime("%m-%d: %H:%M")
            else:
                value = str(rawValue)
            Frame.updateWidgetFromSchema(widget, f"{value}")
    # End of updateStat

    def returnValueFromKeyString(self, keyString):
        returnData = self.game.__dict__
        if("." in keyString):
            keys = keyString.split(".")
            for key in keys:
                if("[" in key):
                    tempLabel = key.split("]")[0]
                    newKey, ind = tempLabel.split("[")
                    returnData = returnData.get(newKey)
                else:
                    returnData = returnData.get(key)
        else:
            returnData = returnData.get(keyString)
        return returnData
    # End of returnValueFromKeyString

    def onExit(self):
        self.master.destroy()
    # End of onExit
# End of gameWindow
