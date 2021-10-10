'''
RLStat.py

Version 1.0.0
Written By: Eamonn Trim (eamonntrim@gmail.com)
Last update: 03/10/2021

Generate a .exe from this by using the command
pyinstaller --noconsole -F --hidden-import "babel.numbers" --add-data "icon.ico;." --icon=icon.ico RLStats.py

Once the file has been made, needs games.json and icon.ico - These are loaded during the startup
'''

import matplotlib.pyplot as plt
import GraphFormat as gf
import requests as req
import tkinter as tk

from tkImageURL import tkLabelImageURL, tkRawImageURL
from matplotlib.backends.backend_tkagg import *
from matplotlib.ticker import MaxNLocator
from GameStats import GameStat
from GameSession import GameSession
from tkinter import ttk
from CollapsiblePane import CollapsiblePane
from GUISchema import SessionSidebar
from Scrollable import ScrollableFrame
from tkcalendar import Calendar, DateEntry
from AuthenticationWindow import AuthenticationWindow
from GraphSchema import graphConfiguration

import datetime
import time
import json
import FileSystem


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.master = master

        self.master.withdraw()

        self._typing_after_id = None
        self._resizing_after_id = None
        self.graph_init = True

        self.user_cache = {}
        self.searchCache = []
        self.gameSessionsCache = []

        self.loadedGames = FileSystem.loadJson('rlstats/data/games.json')

        self.authentication = FileSystem.loadJson('rlstats/data/auth.json')

        self.pack(fill="both", expand=True)

        if(self.authentication.get('bc') is not None):
            self.ballchasingHeaders = {
                'Authorization': self.authentication.get('bc')}
            self.create_widgets()
        else:
            self.master.withdraw()
            self.AuthenticationWindow = tk.Toplevel()
            self.AuthenticationFrame = AuthenticationWindow(
                self.AuthenticationWindow, self.master)

        self.master.deiconify()
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        size = tuple([int(self.master.winfo_reqwidth()),
                     int(self.master.winfo_reqheight())])

        x = screen_width/2 - size[0]/2
        y = screen_height/2 - size[1]/2

        self.master.geometry("+%d+%d" % (x, y))

        self.master.protocol("WM_DELETE_WINDOW", self.onExit)
        self.master.bind("<Configure>", self.resize)
    # End of __init__

    def resize(self, event):
        if(hasattr(self, 'GraphBox')):
            if(event.widget == self.GraphBox):
                if(self._resizing_after_id is not None):
                    self.after_cancel(self._resizing_after_id)

                self._resizing_after_id = self.after(150, self.refreshGraph)

    # End of resize

    def create_widgets(self):
        self.master.title("Rocket League Stats")
        defaultIco = FileSystem.resource_path('icon.ico')
        self.master.iconbitmap(default=defaultIco)

        self.menu = tk.Menu(self)
        self.m_file = tk.Menu(self, tearoff=0)
        self.m_file.add_command(label="Exit", command=self.onExit)
        self.menu.add_cascade(label="File", menu=self.m_file)
        self.master.config(menu=self.menu)

        self.SearchBox = tk.Frame(self, relief="groove", borderwidth=1)
        self.SearchBox.grid(row=0, column=0, columnspan=5, sticky="nsew")

        self.createSearchBox(self.SearchBox)

        self.UserBox = tk.Frame(self, relief="groove", borderwidth=1)
        self.UserBox.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.createUserBox(self.UserBox)

        self.GraphOptionsBox = tk.Frame(
            self, relief="groove", borderwidth=1)
        self.GraphOptionsBox.grid(row=1, column=3, columnspan=1, sticky="nsew")

        self.createGraphOptionsBox(self.GraphOptionsBox)

        self.SessionBox = tk.Frame(
            self, relief="groove", borderwidth=1)
        self.SessionBox.grid(row=1, column=4, columnspan=1, sticky="nsew")

        self.createSessionBox(self.SessionBox)

        self.GraphBox = tk.Frame(
            self, relief="groove", borderwidth=1)
        self.GraphBox.grid(row=2, column=0, columnspan=3, sticky="nsew")

        self.SessionStatsBox = tk.Frame(
            self, relief="groove", borderwidth=1)
        self.SessionStatsBox.grid(row=2, column=3, columnspan=2, sticky="nsew")

        self.createSessionStatsBox(self.SessionStatsBox)

        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=2, weight=1)

        self.createGraph()

        self.master.update()
        self.master.update_idletasks()
        self.master.minsize(self.master.winfo_width(),
                            self.master.winfo_height())

        self.SessionStatsScrollBox.recalculateScrollBox()

        '''self.searchReplays(
            {"platformSlug": "steam", "platformUserIdentifier": '76561198072178785', 'platformUserHandle': 'Gavin8a2can'})'''
        '''self.searchReplays({
            'platformSlug': "epic", "platformUserHandle": "MMRREE", "platformUserIdentifier": "MMRREE"
        })'''
    # End of create_widgets(self)

    def getMaps(self):
        url = 'https://ballchasing.com/api/maps'
        searchGames = req.get(url, headers=self.ballchasingHeaders)
        result = searchGames.json()
        self.mapsTranslation = result
        maps = list(result.values())
        return maps
    # End of getMaps

    def comboSelectUser(self, event):
        user = list(self.user_cache.values())[self.UserSearch.current()]
        if("avatarUrl" in user.keys() and user['avatarUrl'] is not None):
            imageURL = user['avatarUrl']
        else:
            imageURL = 'https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png'

        rawImage = tkRawImageURL(imageURL, (50, 50))
        self.UserSearchImage.image = rawImage
        self.UserSearchImage.configure(image=rawImage)

    # End of comboSelectUser

    def createSearchBox(self, master):
        self.UserSearchLabel = tk.Label(
            master, text="User to Search For:")
        self.UserSearchLabel.grid(
            row=0, column=0, sticky="nw", padx=2, pady=2)

        self.UserSearch = ttk.Combobox(master)
        self.UserSearch.bind('<KeyRelease>', self.checkInput)
        self.UserSearch.bind('<<ComboboxSelected>>', self.comboSelectUser)
        self.UserSearch.grid(row=1, column=0, sticky="new", padx=2, pady=2)

        self.UserSearchImage = tkLabelImageURL(
            'https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png', master, (50, 50))
        self.UserSearchImage.grid(
            row=2, column=0, rowspan=2, sticky="new", padx=2, pady=2)

        self.OneVOneFilter = tk.BooleanVar(master, False, "1v1")
        self.OneVOneCheckbox = tk.Checkbutton(
            master, text="1v1", variable=self.OneVOneFilter)
        self.OneVOneCheckbox.grid(
            row=0, column=1, sticky="nw", padx=2, pady=2)

        self.TwoVTwoFilter = tk.BooleanVar(master, True, "2v2")
        self.TwoVTwoCheckbox = tk.Checkbutton(
            master, text="2v2", variable=self.TwoVTwoFilter)
        self.TwoVTwoCheckbox.grid(
            row=1, column=1, sticky="nw", padx=2, pady=2)

        self.ThreeVThreeFilter = tk.BooleanVar(master, True, "3v3")
        self.ThreeVThreeCheckbox = tk.Checkbutton(
            master, text="3v3", variable=self.ThreeVThreeFilter)
        self.ThreeVThreeCheckbox.grid(
            row=2, column=1, sticky="nw", padx=2, pady=2)

        self.RankedFilter = tk.BooleanVar(master, True, "Ranked")
        self.RankedCheckbox = tk.Checkbutton(
            master, text="Ranked", variable=self.RankedFilter)
        self.RankedCheckbox.grid(
            row=3, column=1, sticky="nw", padx=2, pady=2)

        self.HoopsFilter = tk.BooleanVar(master, False, "Hoops")
        self.HoopsCheckbox = tk.Checkbutton(
            master, text="Hoops", variable=self.HoopsFilter)
        self.HoopsCheckbox.grid(row=0, column=2, sticky="nw", padx=2, pady=2)

        self.RumbleFilter = tk.BooleanVar(master, False, "Rumble")
        self.RumbleCheckbox = tk.Checkbutton(
            master, text="Rumble", variable=self.RumbleFilter)
        self.RumbleCheckbox.grid(
            row=1, column=2, sticky="nw", padx=2, pady=2)

        self.DropshotFilter = tk.BooleanVar(master, False, "Dropshot")
        self.DropshotCheckbox = tk.Checkbutton(
            master, text="Dropshot", variable=self.DropshotFilter)
        self.DropshotCheckbox.grid(
            row=2, column=2, sticky="nw", padx=2, pady=2)

        self.SnowdayFilter = tk.BooleanVar(master, False, "Snowday")
        self.SnowdayCheckbox = tk.Checkbutton(
            master, text="Snowday", variable=self.SnowdayFilter)
        self.SnowdayCheckbox.grid(
            row=3, column=2, sticky="nw", padx=2, pady=2)

        self.SeasonSelectionLabel = tk.Label(
            master, text="Season:")
        self.SeasonSelectionLabel.grid(
            row=0, column=3, sticky="nw", padx=2, pady=2)

        self.SeasonFilter = tk.StringVar(
            master, name="Season")
        self.SeasonSelection = ttk.Combobox(
            master, textvariable=self.SeasonFilter)
        self.SeasonSelection['values'] = ("S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9",
                                          "S10", "S11", "S12", "S13", "S14", "Season 1", "Season 2", "Season 3", "Season 4", "Any")
        self.SeasonSelection['values'] = self.SeasonSelection['values'][::-1]
        self.SeasonFilter.set(self.SeasonSelection['values'][0])
        self.SeasonSelection.grid(
            row=1, column=3, sticky="nsew", padx=2, pady=2)

        self.MapSelectionLabel = tk.Label(master, text="Map:")
        self.MapSelectionLabel.grid(
            row=2, column=3, sticky="nw", padx=2, pady=2)

        self.MapFilter = tk.StringVar(master, name="Map")
        self.MapSelection = ttk.Combobox(master, textvariable=self.MapFilter)
        maps = self.getMaps()
        maps = ["Any"] + maps
        self.MapSelection['values'] = maps
        self.MapFilter.set(self.MapSelection['values'][0])
        self.MapSelection.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)

        self.DateBeforeLabel = tk.Label(
            master, text="Replay Before:")
        self.DateBeforeLabel.grid(
            row=0, column=4, sticky="nw", padx=2, pady=2)

        self.ReplayBeforeFilter = DateEntry(master)
        self.ReplayBeforeFilter.grid(
            row=1, column=4, sticky="nsew", padx=2, pady=2)

        self.DateAfterLabel = tk.Label(
            master, text="Replay After:")
        self.DateAfterLabel.grid(
            row=2, column=4, sticky="nw", padx=2, pady=2)

        self.ReplayAfterFilter = DateEntry(master)
        beginingOfTime = datetime.date.today() - datetime.timedelta(days=31)
        self.ReplayAfterFilter.set_date(beginingOfTime)
        self.ReplayAfterFilter.grid(
            row=3, column=4, sticky="nsew", padx=2, pady=2)

        self.SearchImage = tkRawImageURL(
            'https://icons-for-free.com/iconfiles/png/512/search+icon-1320183705543171170.png', (25, 25))
        self.SearchButton = tk.Button(
            master, image=self.SearchImage, text=" Search", compound="left", command=self.searchClicked)
        self.SearchButton.grid(row=1, column=5, rowspan=2,
                               sticky="nsew", padx=2, pady=2)

        self.equalWeightsGrid(master)
    # End of createSearchBox

    def equalWeightsGrid(self, master):
        columns, rows = master.grid_size()
        for row in range(rows):
            master.grid_rowconfigure(row, weight=1)
        for column in range(columns):
            master.grid_columnconfigure(column, weight=1)
    # End of equalWeightsGrid

    def searchClicked(self):
        user = list(self.user_cache.values())[self.UserSearch.current()]
        self.searchReplays(user)
    # End of searchClicked

    def createUserBox(self, master):
        self.userImage = tkLabelImageURL(
            'https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png', master)
        self.userImage.grid(row=0, column=0, rowspan=5,
                            sticky="nsew", padx=2, pady=2)

        self.UsernameLabel = tk.Label(
            master, text="Username")
        self.UsernameLabel.grid(
            row=0, column=1, columnspan=2, sticky="nw", padx=2)

        self.OneVOneMMRLabel = tk.Label(
            master, text="1v1: N/A")
        self.OneVOneMMRLabel.grid(row=1, column=1, sticky="nw", padx=2)

        self.TwoVTwoMMRLabel = tk.Label(
            master, text="2v2: N/A")
        self.TwoVTwoMMRLabel.grid(row=2, column=1, sticky="nw", padx=2)

        self.ThreeVThreeMMRLabel = tk.Label(
            master, text="3v3: N/A")
        self.ThreeVThreeMMRLabel.grid(
            row=1, column=2, sticky="nw", padx=2)

        self.SeasonRewradLabel = tk.Label(
            master, text="Season Rewards: N/A")
        self.SeasonRewradLabel.grid(
            row=2, column=2, sticky="nw", padx=2)

        self.WinsLabel = tk.Label(master, text="Wins: N/A")
        self.WinsLabel.grid(row=0, column=3, sticky="nw", padx=2)

        self.GoalsLabel = tk.Label(
            master, text="Goals: N/A")
        self.GoalsLabel.grid(row=1, column=3, sticky="nw", padx=2)

        self.SavesLabel = tk.Label(
            master, text="Saves: N/A")
        self.SavesLabel.grid(row=2, column=3, sticky="nw", padx=2)

        self.MVPSLabel = tk.Label(master, text="MVPS: N/A")
        self.MVPSLabel.grid(row=3, column=3, sticky="nw", padx=2)

        self.AssistsLabel = tk.Label(
            master, text="Assists: N/A")
        self.AssistsLabel.grid(row=0, column=4, sticky="nw", padx=2)

        self.ShotsLabel = tk.Label(
            master, text="Shots: N/A")
        self.ShotsLabel.grid(row=1, column=4, sticky="nw", padx=2)

        self.ShootingPercentLabel = tk.Label(
            master, text="Shooting Accuracy: N/A")
        self.ShootingPercentLabel.grid(
            row=2, column=4, sticky="nw", padx=2)

        self.TotalScoreLabel = tk.Label(
            master, text="Total Points: N/A")
        self.TotalScoreLabel.grid(row=3, column=4, sticky="nw", padx=2)

        self.equalWeightsGrid(master)
    # End of createUserBox

    def createGraphOptionsBox(self, master):
        self.graphOptionsBoxLabel = tk.Label(master, text="Graph Options")
        self.graphOptionsBoxLabel.grid(
            row=0, column=0, sticky="nw", padx=2, pady=2)

        self.graphSelectionVar = tk.StringVar(self, "", name="GraphSelection")
        self.graphMenu = tk.Menubutton(
            master, textvariable=self.graphSelectionVar, indicatoron=True, borderwidth=1, relief="raised")
        self.gM = tk.Menu(self.graphMenu, tearoff=False)

        self.populateMenuFromKeysOfDict(graphConfiguration, menu=self.gM,
                                        variable=self.graphSelectionVar)
        self.graphSelectionVar.trace('w', self.graphSelectionHandler)

        self.graphMenu.configure(menu=self.gM)
        self.graphMenu.grid(row=1, column=0, sticky="n", padx=2, pady=2)

        self.absoluteValues = tk.BooleanVar(self, False, "absoluteValues")
        self.absoluteValues.trace('w', self.graphAbsoluteValueHandler)
        self.absoluteValuesCheckbox = tk.Checkbutton(
            master, text="Absolute Values", variable=self.absoluteValues)
        self.absoluteValuesCheckbox.grid(
            row=2, column=0, sticky="s", padx=2, pady=2)

        self.equalWeightsGrid(master)
    # End of createGraphOptionsBox

    def createSessionBox(self, master):
        self.SessionBoxLabel = tk.Label(
            master, text="Sessions")
        self.SessionBoxLabel.grid(row=0, column=0, sticky="nw", padx=2, pady=2)

        self.sessionListBox = tk.Listbox(
            master, height=6, exportselection=False)
        self.sessionListBox.bind('<<ListboxSelect>>', self.sessionSelect)
        self.sessionListBox.grid(
            row=1, column=0, sticky="nsew", padx=2, pady=2)

        self.equalWeightsGrid(master)
    # End of createSessionBox

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

    def createSessionStatsBox(self, master):

        self.SessionStatsBoxLabel = tk.Label(
            self.SessionStatsBox, text="Session Stats")
        self.SessionStatsBoxLabel.grid(
            row=0, column=0, sticky="nw", padx=2, pady=2)

        self.SessionStatsScrollBox = ScrollableFrame(master)
        self.SessionStatsScrollBox.grid(row=1, column=0, sticky="nsew")

        for collapsible in SessionSidebar:
            if(collapsible['type'] == "collapsible"):
                self.createCollapsible(
                    collapsible, self.SessionStatsScrollBox.contentFrame)
            elif(collapsible['type'] == "widget"):
                self.createWidgetFromSchema(
                    collapsible, self.SessionStatsScrollBox.contentFrame)

        self.SessionStatsGamesList = tk.Listbox(
            self.SessionStatsScrollBox.contentFrame, exportselection=False)
        self.SessionStatsGamesList.bind("<Double-Button-1>", self.gameSelected)
        self.SessionStatsGamesList.grid(
            row=5, column=0, columnspan=4, sticky="nsew")

        self.SessionStatsScrollBox.recalculateScrollBox()
    # End of createSessionsStatsBox

    def gameSelected(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)

        sessionIndex = self.sessionListBox.curselection()[0]
        session = self.gameSessionsCache[sessionIndex]
        session.openGame(index, self.master)
    # End of gameSelected

    def sessionSelect(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        index = (len(self.gameSessionsCache)-1)-index
        session = self.gameSessionsCache[index]
        session.updateSessionStats(
            self, SessionSidebar, self.SessionStatsGamesList)

        lowerDate = session.StartDate + datetime.timedelta(minutes=-3)
        higherDate = session.EndDate + datetime.timedelta(minutes=3)
        self.goalsAx.set_xlim(lowerDate, higherDate)
        self.refreshGraph()

        self.goalsCanvas.draw()
    # End of sessionSelect

    def populateMenuFromDict(self, dictionary, parentTags="", menu=None, variable=None):
        if(menu == None):
            menu = tk.Menu(self.graphMenu)
        if(type(dictionary) is dict):
            for tag, val in dictionary.items():
                if(parentTags != ""):
                    currentTags = parentTags + "." + tag
                else:
                    currentTags = tag

                if(type(val) is dict or type(val) is list):
                    newMenu = tk.Menu(self.graphMenu, tearoff=False)
                    menu.add_cascade(label=tag, menu=newMenu)
                    self.populateMenuFromDict(
                        val, currentTags, newMenu, variable)
                else:
                    label = tag
                    menu.add_radiobutton(
                        value=currentTags, label=tag, indicatoron=True, variable=variable)
                    if(variable.get() == ""):
                        variable.set(tag)
        elif(type(dictionary) is list):
            for obj in dictionary:
                self.populateMenuFromDict(obj, parentTags=parentTags,
                                          variable=variable, menu=menu)
        else:
            if(parentTags == ""):
                currentTags = dictionary
            else:
                currentTags = parentTags + "." + dictionary
            menu.add_radiobutton(
                value=currentTags, label=dictionary, indicatoron=True, variable=variable)
            if(variable.get() == ""):
                variable.set(dictionary)
    # End of populateMenuFromDict

    def populateMenuFromKeysOfDict(self, dictionary, parentTags="", menu=None, variable=None):
        if(menu == None):
            menu = tk.Menu(self.graphMenu)
        if(type(dictionary) is dict):
            for tag, val in dictionary.items():
                if(tag == "type"):
                    continue
                if(parentTags != ""):
                    currentTags = parentTags + "." + tag
                else:
                    currentTags = tag

                if(val.get('type') == "cascade"):
                    newMenu = tk.Menu(self.graphMenu, tearoff=False)
                    menu.add_cascade(label=tag, menu=newMenu)
                    self.populateMenuFromKeysOfDict(
                        val, currentTags, newMenu, variable)
                else:
                    menu.add_radiobutton(
                        value=val.get('value'), label=val.get('label'), indicatoron=True, variable=variable)
                    if(variable.get() == ""):
                        variable.set(val.get('value'))
        elif(type(dictionary) is list):
            for obj in dictionary:
                self.populateMenuFromKeysOfDict(obj, parentTags=parentTags,
                                                variable=variable, menu=menu)
        else:
            if(parentTags == ""):
                currentTags = dictionary
            else:
                currentTags = parentTags + "." + dictionary
            menu.add_radiobutton(
                value=currentTags, label=dictionary, indicatoron=True, variable=variable)
            if(variable.get() == ""):
                variable.set(dictionary)
    # End of populateMenuFromKeysOfDict

    def graphDataArrayFromKeyString(self, keyString, originalDictionary):
        keys = keyString.split(".")
        returnData = originalDictionary
        for key in keys:
            if("[" in key):
                tempLabel = key.split("]")[0]
                newKey, ind = tempLabel.split("[")
                returnData = [d.get(newKey) for d in returnData]
            else:
                returnData = [d.get(key) for d in returnData]
        return returnData
    # End of graphDataArrayFromKeyString

    def findGraphConfiguration(self, menuSelectedValue="Win/Loss", currentLevel=None):
        for tag, val in currentLevel.items():
            if(tag == "type"):
                continue
            if(val.get('type') == "cascade"):
                cascadedSearchResult = self.findGraphConfiguration(
                    menuSelectedValue=menuSelectedValue, currentLevel=val)
                if(cascadedSearchResult is not None):
                    return cascadedSearchResult
            elif(val.get('value') == menuSelectedValue):
                return val
    # End of findGraphConfiguration

    def refreshGraph(self):
        dataChoiceValue = self.graphSelectionVar.get()

        graphConfig = self.findGraphConfiguration(
            dataChoiceValue, graphConfiguration)

        currentLow, currentHigh = self.goalsAx.get_xlim()

        self.clearGraph()

        self.goalsAx.get_yaxis().set_major_locator(
            MaxNLocator(integer=True))

        for tag in graphConfig.get('tags'):
            graphData = self.graphDataArrayFromKeyString(tag, self.searchCache)

            if(type(graphData[0]) is dict):
                if(self.absoluteValues.get() is True):
                    choice = [x for x in graphData[0].keys() if x !=
                              "percent"][0]
                else:
                    choice = [x for x in graphData[0].keys() if x ==
                              "percent"][0]
                graphData = [x[choice] for x in graphData]

            if(graphConfig.get('tags').index(tag) == 1 and graphConfig.get('invert')):
                graphData = [d*-1 for d in graphData]

            self.goalsAx.bar([d['Date'] for d in self.searchCache],
                             graphData,
                             color=[d['Win_Loss_Color']
                                    for d in self.searchCache],
                             width=[d['Bar_Width'] for d in self.searchCache],
                             align='edge',
                             alpha=0.5)

        if(graphConfig.get('formatter') is not None):
            self.goalsAx.yaxis.set_major_formatter(
                plt.FuncFormatter(graphConfig['formatter']))

        self.goalsAx.set_ylabel(graphConfig.get('yaxis'))
        self.goalsAx.set_title(graphConfig.get('title'))

        self.goalsAx.set_xticklabels(
            self.goalsAx.get_xticks(), rotation=30)
        self.goalsAx.set_xlabel("Date")

        if(self.graph_init is not True):
            self.goalsAx.set_xlim(currentLow, currentHigh)

        else:
            self.graph_init = False

        gf.dateGraphMajorTicksCalculation(self.goalsAx)
        gf.repaintMajorTicks(self.goalsAx)
        self.goalsFigure.tight_layout()
        self.goalsAx.patch.set_alpha(0)

        self.redrawIconBehindGraph()

        self.goalsCanvas.draw()
    # End of refreshGraph

    def clearGraph(self):
        self.goalsAx.clear()
        self.goalsAx.remove()
        self.goalsFigure.clear()
        self.goalsAx = self.goalsFigure.add_subplot(111)
    # End of clearGraphy

    def graphAbsoluteValueHandler(self, name, index, mode):
        self.refreshGraph()
    # End of graphAbsoluteValueHandler

    def graphSelectionHandler(self, name, index, mode):
        self.refreshGraph()
    # End of graphSelectionHandler

    def checkInput(self, event):
        if(event.keysym == "Escape"):
            self.UserSearch.set("")

        if(self._typing_after_id is not None):
            self.after_cancel(self._typing_after_id)

        self._typing_after_id = self.after(750, self.autocompleteSearch)
    # End of checkInput

    def autocompleteSearch(self):
        if(self.UserSearch.get() != ""):
            if(self.user_cache is not None):
                self.user_cache.clear()
            userSearchSteamResp = req.get('https://api.tracker.gg/api/v2/rocket-league/standard/search?platform=steam&autocomplete=true&query=' +
                                          self.UserSearch.get(),
                                          headers={
                                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
                                              'Accept': 'application/json, text/plain, */*',
                                              'Accept-Language': 'en',
                                              'Sec-Fetch-Dest': 'empty',
                                              'Sec-Fetch-Mode': 'cors',
                                              'Sec-Fetch-Site': 'cross-site',
                                          })
            userSearchSteamRespJson = userSearchSteamResp.json()
            dataSteam = userSearchSteamRespJson['data']
            users = []
            for user in dataSteam:
                if(user['platformUserHandle'] == self.UserSearch.get()):
                    self.user_cache[user['platformSlug'] +
                                    user['platformUserHandle'] + user['platformUserIdentifier']] = user

            userSearchEpicResp = req.get('https://api.tracker.gg/api/v2/rocket-league/standard/search?platform=epic&autocomplete=true&query=' +
                                         self.UserSearch.get(),
                                         headers={
                                             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
                                             'Accept': 'application/json, text/plain, */*',
                                             'Accept-Language': 'en',
                                             'Sec-Fetch-Dest': 'empty',
                                             'Sec-Fetch-Mode': 'cors',
                                             'Sec-Fetch-Site': 'cross-site',
                                         })
            userSearchEpicRespJson = userSearchEpicResp.json()
            dataEpic = userSearchEpicRespJson['data']

            for user in dataEpic:
                if(user['platformUserHandle'] == self.UserSearch.get()):
                    self.user_cache[user['platformSlug'] +
                                    user['platformUserHandle'] + user['platformUserIdentifier']] = user

            self.UserSearch['values'] = [self.user_cache.get(
                user)['platformUserHandle'] for user in self.user_cache]
            self.UserSearch.event_generate('<Down>')
        else:
            if(self.user_cache is not None):
                self.user_cache.clear()
            self.UserSearch['values'] = []
    # End of autocompleteSearch

    def updateUserBox(self, user):
        userId = user['platformUserIdentifier'] if user['platformSlug'] == "steam" else user['platformUserHandle']

        searchUrl = "https://api.tracker.gg/api/v2/rocket-league/standard/profile/" + \
            user['platformSlug']+"/"+userId+"?"

        userStatsResp = req.get(searchUrl,
                                headers={
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
                                    "Accept": "application/json, text/plain, */*",
                                    "Accept-Language": "en",
                                    "Sec-Fetch-Dest": "empty",
                                    "Sec-Fetch-Mode": "cors",
                                    "Sec-Fetch-Site": "cross-site",
                                    "Cache-Control": "max-age=0",
                                    "If-Modified-Since": "Wed, 29 Sep 2021 09:14:31 GMT"
                                }
                                )

        userStats = userStatsResp.json()['data']

        if("avatarUrl" in userStats['platformInfo'].keys() and userStats['platformInfo']['avatarUrl'] is not None):
            imageURL = userStats['platformInfo']['avatarUrl']
        else:
            imageURL = 'https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png'

        newImage = tkRawImageURL(imageURL)
        self.userImage.configure(image=newImage)
        self.userImage.image = newImage

        self.UsernameLabel.configure(
            text=userStats['platformInfo']['platformUserHandle'])

        userOverallStats = None
        for segment in userStats['segments']:
            if(segment['type'] == "overview"):
                userOverallStats = segment['stats']
            elif(segment['type'] == "playlist" and segment['metadata']['name'] == "Ranked Duel 1v1"):
                self.OneVOneMMRLabel.configure(
                    text="1v1: " + segment['stats']['rating']['displayValue'] + " mmr")
            elif(segment['type'] == "playlist" and segment['metadata']['name'] == "Ranked Doubles 2v2"):
                self.TwoVTwoMMRLabel.configure(
                    text="2v2: " + segment['stats']['rating']['displayValue'] + " mmr")
            elif(segment['type'] == "playlist" and segment['metadata']['name'] == "Ranked Standard 3v3"):
                self.ThreeVThreeMMRLabel.configure(
                    text="3v3: " + segment['stats']['rating']['displayValue'] + " mmr")

        self.WinsLabel.configure(
            text="Wins: " + userOverallStats['wins']['displayValue'])

        self.GoalsLabel.configure(
            text="Goals: " + userOverallStats['goals']['displayValue'])

        self.AssistsLabel.configure(
            text="Assists: " + userOverallStats['assists']['displayValue'])

        self.MVPSLabel.configure(
            text="MVPS: " + userOverallStats['mVPs']['displayValue'])

        self.SavesLabel.configure(
            text="Saves: " + userOverallStats['saves']['displayValue'])

        self.ShotsLabel.configure(
            text="Shots: " + userOverallStats['shots']['displayValue'])

        self.ShootingPercentLabel.configure(
            text="Shooting Accuracy: " + userOverallStats['goalShotRatio']['displayValue'] + "%")

        self.SeasonRewradLabel.configure(
            text="Season Rewards: " + userOverallStats['seasonRewardLevel']['metadata']['rankName'] + " [" + userOverallStats['seasonRewardWins']['displayValue'] + "/10]")

        self.TotalScoreLabel.configure(
            text="Total Points: " + userOverallStats['score']['displayValue'])

        self.master.update()
    # End of updateUserBox

    def getReplaysFromBallchasing(self, user):
        userId = user['platformUserIdentifier'] if user['platformSlug'] == "steam" else user['platformUserHandle']

        url = 'https://ballchasing.com/api/replays?'
        url += ('player-id=steam:' +
                userId) if user['platformSlug'] == "steam" else ('player-name=' + userId)

        if(self.OneVOneFilter.get()):
            url += "&playlist=" + "ranked-duels" if self.RankedFilter.get() else "unranked-duels"
        if(self.TwoVTwoFilter.get()):
            url += "&playlist=" + "ranked-doubles" if self.RankedFilter.get() else "unranked-doubles"
        if(self.ThreeVThreeFilter.get()):
            url += "&playlist=" + "ranked-standard" if self.RankedFilter.get() else "unranked-standard"
        if(self.HoopsFilter.get()):
            url += "&playlist=" + "ranked-hoops" if self.RankedFilter.get() else "hoops"
        if(self.RumbleFilter.get()):
            url += "&playlist=" + "ranked-rumble" if self.RankedFilter.get() else "rumble"
        if(self.DropshotFilter.get()):
            url += "&playlist=" + "ranked-dropshot" if self.RankedFilter.get() else "dropshot"
        if(self.SnowdayFilter.get()):
            url += "&playlist=" + "ranked-snowday" if self.RankedFilter.get() else "snowday"

        if(self.SeasonFilter.get() != "Any"):
            rawSeason = self.SeasonFilter.get()
            if("Season" not in rawSeason):
                url += "&season=" + rawSeason[1:]
            else:
                url += "&season=f" + rawSeason.split(" ")[1]

        if(self.MapFilter.get() != "Any"):
            mapCode = [d[0] for d in self.mapsTranslation.items()
                       if d[1] == self.MapFilter.get()]
            url += "&map=" + mapCode[0]

        beforeDate = self.ReplayBeforeFilter.get_date()
        midnightHour = datetime.time(
            hour=23, minute=59, second=59)
        beforeDate = datetime.datetime.combine(beforeDate, midnightHour)

        url += "&replay-date-before=" + \
            beforeDate.strftime("%Y-%m-%dT%H:%M:%S%%2B00:00")
        url += "&replay-date-after=" + \
            self.ReplayAfterFilter.get_date().strftime("%Y-%m-%dT%H:%M:%S%%2B00:00")

        searchGames = req.get(url, headers=self.ballchasingHeaders)
        result = searchGames.json()
        return result
    # End of getReplaysFromBallchasing

    def processReplays(self, replays, user):
        self.progressBar = ttk.Progressbar(
            self.GraphBox, orient="horizontal", length=200)
        self.progressBar.pack(side="left", fill="both", expand=True)

        self.progressBar.configure(maximum=len(replays))

        self.searchCache = []
        self.gameSessionsCache = []
        seenGUIDs = {}

        for replay in replays:
            self.progressBar.step()
            self.master.update()
            fetched = True

            if (self.loadedGames.get(replay['id']) is not None):
                replayResult = self.loadedGames.get(replay['id'])
                fetched = False
            else:
                gameReplay = req.get(
                    replay['link'], headers=self.ballchasingHeaders)
                replayResult = gameReplay.json()
                self.loadedGames[replay['id']] = replayResult

            if(replayResult.get('match_guid', None) is not None and seenGUIDs.get(replayResult.get('match_guid', None), None) is None):
                seenGUIDs[replayResult['match_guid']] = True
            else:
                continue

            localGame = GameStat()
            localGame.populateFromGame(
                replay, replayResult, user['platformUserHandle'])
            if(len(self.gameSessionsCache) == 0 or
               not self.gameSessionsCache[len(self.gameSessionsCache)-1].checkGameInSession(localGame)):
                self.gameSessionsCache.append(GameSession())

            if(self.gameSessionsCache[len(self.gameSessionsCache)-1].checkGameInSession(localGame)):
                self.gameSessionsCache[len(
                    self.gameSessionsCache)-1].addGame(localGame)
                self.searchCache.append(localGame.__dict__)

            if fetched:
                time.sleep(0.5)

        FileSystem.writeJson('rlstats/data/games.json', self.loadedGames)

        for session in self.gameSessionsCache:
            sessionDict = session.__dict__
            self.sessionListBox.insert(
                0, session.StartDate.strftime("%d/%m: %H:%M: ") + sessionDict['GameMode'])

        self.progressBar.pack_forget()
    # End of processReplays

    def redrawIconBehindGraph(self):
        xBottomLeft, yBottomLeft, xTopRight, yTopRight = self.goalsAx.bbox.extents

        width = xTopRight - xBottomLeft
        height = yTopRight - yBottomLeft

        xOffset = xBottomLeft + width/2
        yOffset = yBottomLeft + height/2

        image = plt.imread(FileSystem.resource_path('icon.ico'))

        yOffset -= len(image)/2
        xOffset -= len(image)/2

        self.goalsFigure.figimage(
            image, alpha=0.25, zorder=-1, xo=xOffset, yo=yOffset)
    # End of redrawIconBehindGraph

    def createGraph(self):
        graphWidth = self.UserBox.winfo_width()
        scaleFactor = graphWidth/100
        self.goalsFigure = plt.Figure(
            figsize=(scaleFactor, scaleFactor*0.75), dpi=graphWidth/scaleFactor)
        if (hasattr(self, 'goalsCanvas')):
            self.goalsCanvas.get_tk_widget().pack_forget()
        self.goalsAx = self.goalsFigure.add_subplot(111)

        self.goalsAx.patch.set_alpha(0)

        self.redrawIconBehindGraph()

        self.goalsCanvas = FigureCanvasTkAgg(self.goalsFigure, self.GraphBox)
        self.goalsCanvas.get_tk_widget().pack(
            side="bottom", anchor="w", fill="both", expand=True)

        self.mouse_down = False
        self.lastevent = None

        cid = self.goalsFigure.canvas.mpl_connect(
            'button_press_event', self.onClick)
        rid = self.goalsFigure.canvas.mpl_connect(
            'button_release_event', self.onRelease)
        mid = self.goalsFigure.canvas.mpl_connect(
            'motion_notify_event', self.onMouseMove)
        sid = self.goalsFigure.canvas.mpl_connect(
            'scroll_event', self.onScroll)
    # End of createGraph

    def searchReplays(self, user):
        self.sessionListBox.delete(0, tk.END)

        self.updateUserBox(user)

        ballchasingResult = self.getReplaysFromBallchasing(user)

        self.processReplays(ballchasingResult['list'], user)

        self.refreshGraph()

        self.master.minsize(self.master.winfo_width(),
                            self.master.winfo_height())
    # End searchReplays

    def onClick(self, event):
        if(event.button == 1):
            self.mouse_down = True
    # End of onClick

    def onRelease(self, event):
        if(event.button == 1):
            self.mouse_down = False
    # End of onRelease

    def onScroll(self, event):
        if(event.inaxes):
            xlimLow, xlimHigh = self.goalsAx.get_xlim()
            xlimWidth = xlimHigh - xlimLow

            lowestPixelAxes = self.goalsAx.get_position(
            ).x0 * self.goalsFigure.get_size_inches()[0] * self.goalsFigure.dpi
            highestPixelAxes = self.goalsAx.get_position(
            ).x1 * self.goalsFigure.get_size_inches()[0] * self.goalsFigure.dpi
            axesWidthPixels = highestPixelAxes - lowestPixelAxes
            mousePosition = event.x - lowestPixelAxes

            # Caclulate where the mouse is
            mousePercentageAcross = mousePosition/axesWidthPixels
            newxlimHigh = xlimHigh
            newxlimLow = xlimLow

            if(event.button == "up"):
                if(mousePercentageAcross > 0.66):
                    newxlimLow = xlimHigh - xlimWidth * 0.9
                elif(mousePercentageAcross < 0.33):
                    newxlimHigh = xlimLow + xlimWidth * 0.9
                else:
                    newxlimLow = xlimHigh - xlimWidth * 0.95
                    newxlimHigh = xlimLow + xlimWidth * 0.95
            elif(event.button == "down"):
                if(mousePercentageAcross > 0.66):
                    newxlimLow = xlimHigh - xlimWidth * 1.1
                elif(mousePercentageAcross < 0.33):
                    newxlimHigh = xlimLow + xlimWidth * 1.1
                else:
                    newxlimLow = xlimHigh - xlimWidth * 1.05
                    newxlimHigh = xlimLow + xlimWidth * 1.05

            self.goalsAx.set_xlim(
                newxlimLow, newxlimHigh)

            gf.dateGraphMajorTicksCalculation(self.goalsAx)

            gf.repaintMajorTicks(self.goalsAx)
            self.goalsFigure.tight_layout()
            self.goalsCanvas.draw()
    # End of onScroll

    def onMouseMove(self, event):
        if(self.mouse_down and event.inaxes and self.lastevent != None):
            xlimLow, xlimHigh = self.goalsAx.get_xlim()
            xlimWidth = xlimHigh - xlimLow
            mouseMovement = event.x - self.lastevent.x

            lowestPixelAxes = self.goalsAx.get_position(
            ).x0 * self.goalsFigure.get_size_inches()[0] * self.goalsFigure.dpi
            highestPixelAxes = self.goalsAx.get_position(
            ).x1 * self.goalsFigure.get_size_inches()[0] * self.goalsFigure.dpi
            axesWidthPixels = highestPixelAxes - lowestPixelAxes

            axMovement = mouseMovement * \
                xlimWidth / axesWidthPixels
            self.goalsAx.set_xlim(
                xlimLow-axMovement, xlimHigh-axMovement)

            gf.repaintMajorTicks(self.goalsAx)
            self.goalsFigure.tight_layout()
            self.goalsCanvas.draw()
        self.lastevent = event
    # End of onMouseMove

    def onExit(self):
        if(self.master is not None):
            self.master.destroy()
        if(hasattr(self, 'AuthenticationWindow') and self.AuthenticationWindow is not None):
            self.AuthenticationWindow.destroy()
    # End of onExit
# End Application


root = tk.Tk()
app = Application(master=root)
app.mainloop()
