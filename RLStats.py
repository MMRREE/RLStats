# As imports
import matplotlib.pyplot as plt
import GraphFormat as gf
import requests as req
import tkinter as tk

# From imports
from tkImageURL import tkLabelImageURL, tkRawImageURL
from matplotlib.backends.backend_tkagg import *
from matplotlib.ticker import MaxNLocator
from GameStats import graphChoices, GameStat
from GameSession import GameSession
from tkinter import ttk
from CollapsiblePane import CollapsiblePane
from GUISchema import SessionSidebar
from Scrollable import ScrollableFrame

# Direct imports
import datetime
import time
import json


# Initialise data from stored files
gamesFile = open('games.json', 'r+')
gamesData = gamesFile.read()
games = json.loads(gamesData)
gamesFile.close()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.master = master

        self._after_id = None
        self.user_cache = {}
        self.graph_init = True

        self.pack(fill="both", expand=True)

        self.create_widgets()

        self.master.protocol("WM_DELETE_WINDOW", self.onExit)
        #self.master.bind("<Configure>", self.resize)
        self.SessionStatsScrollBox.recalculateScrollBox()
    # End of __init__

    def resize(self, event):
        # print(event.widget)
        if(self.SessionStatsScrollBox.contentFrame is event.widget):
            self.SessionStatsScrollBox.recalculateScrollBox()
    # End of resize

    def create_widgets(self):
        # Setting up window name and icon
        self.master.title("Rocket League Stats")
        self.master.iconbitmap(default='./icon.ico')

        # Create an interface menu
        self.menu = tk.Menu(self)
        self.m_file = tk.Menu(self, tearoff=0)
        self.m_file.add_command(label="Exit", command=self.onExit)
        self.menu.add_cascade(label="File", menu=self.m_file)
        self.master.config(menu=self.menu)

        # Create the scaffold for the application
        self.SearchBox = tk.Frame(self, relief="groove", borderwidth=1)
        self.SearchBox.grid(row=0, column=0, columnspan=5, sticky="nsew")

        self.createSearchBox(self.SearchBox)

        # Second Row
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

        # Bottom Frame
        self.GraphBox = tk.Frame(
            self, relief="groove", borderwidth=1)
        self.GraphBox.grid(row=2, column=0, columnspan=3, sticky="nsew")

        self.SessionStatsBox = tk.Frame(
            self, relief="groove", borderwidth=1)
        self.SessionStatsBox.grid(row=2, column=3, columnspan=2, sticky="nsew")

        self.createSessionStatsBox(self.SessionStatsBox)

        # Configure the columns to expand properly when window is resized
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=2, weight=1)

        self.master.update()
        self.master.minsize(self.master.winfo_width(),
                            self.master.winfo_height())

        # Automatically run search
        self.searchReplays(
            {"platformSlug": "steam", "platformUserIdentifier": '76561198072178785'})
    # End of create_widgets(self)

    def createSearchBox(self, master):
        self.UserSearchLabel = tk.Label(
            master, text="User to Search For:")
        self.UserSearchLabel.grid(
            row=0, column=0, sticky="nw", padx=2, pady=2)

        self.UserSearch = ttk.Combobox(master)
        self.UserSearch.bind('<KeyRelease>', self.checkInput)
        self.UserSearch.bind('<<ComboboxSelected>>', self.comboSelectUser)
        self.UserSearch.grid(row=1, column=0, sticky="nw", padx=2, pady=2)

        self.OneVOneCheckbox = tk.Checkbutton(master, text="1v1")
        self.OneVOneCheckbox.grid(
            row=0, column=1, sticky="nw", padx=2, pady=2)

        self.TwoVTwoCheckbox = tk.Checkbutton(master, text="2v2")
        self.TwoVTwoCheckbox.grid(
            row=1, column=1, sticky="nw", padx=2, pady=2)

        self.ThreeVThreeCheckbox = tk.Checkbutton(master, text="3v3")
        self.ThreeVThreeCheckbox.grid(
            row=2, column=1, sticky="nw", padx=2, pady=2)

        self.RankedCheckbox = tk.Checkbutton(master, text="Ranked")
        self.RankedCheckbox.grid(
            row=3, column=1, sticky="nw", padx=2, pady=2)

        self.HoopsCheckbox = tk.Checkbutton(
            master, text="Hoops")
        self.HoopsCheckbox.grid(row=0, column=2, sticky="nw", padx=2, pady=2)

        self.RumbleCheckbox = tk.Checkbutton(
            master, text="Rumble")
        self.RumbleCheckbox.grid(
            row=1, column=2, sticky="nw", padx=2, pady=2)

        self.DropshotCheckbox = tk.Checkbutton(
            master, text="Dropshot")
        self.DropshotCheckbox.grid(
            row=2, column=2, sticky="nw", padx=2, pady=2)

        self.SnowdayCheckbox = tk.Checkbutton(
            master, text="Snowday")
        self.SnowdayCheckbox.grid(
            row=3, column=2, sticky="nw", padx=2, pady=2)

        self.SeasonSelectionLabel = tk.Label(
            master, text="Season:")
        self.SeasonSelectionLabel.grid(
            row=0, column=3, sticky="nw", padx=2, pady=2)

        self.SeasonSelection = ttk.Combobox(master)
        self.SeasonSelection.grid(
            row=1, column=3, sticky="nw", padx=2, pady=2)

        self.MapSelectionLabel = tk.Label(master, text="Map:")
        self.MapSelectionLabel.grid(
            row=2, column=3, sticky="nw", padx=2, pady=2)

        self.MapSelection = ttk.Combobox(master)
        self.MapSelection.grid(row=3, column=3, sticky="nw", padx=2, pady=2)

        self.DateBeforeLabel = tk.Label(
            master, text="Replay Before:")
        self.DateBeforeLabel.grid(
            row=0, column=4, sticky="nw", padx=2, pady=2)

        self.ReplayBeforeFilter = ttk.Combobox(master)
        self.ReplayBeforeFilter.grid(
            row=1, column=4, sticky="nw", padx=2, pady=2)

        self.DateAfterLabel = tk.Label(
            master, text="Replay After:")
        self.DateAfterLabel.grid(
            row=2, column=4, sticky="nw", padx=2, pady=2)

        self.ReplayAfterFilter = ttk.Combobox(master)
        self.ReplayAfterFilter.grid(
            row=3, column=4, sticky="nw", padx=2, pady=2)
    # End of createSearchBox

    def createUserBox(self, master):
        self.userImage = tkLabelImageURL(
            'https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png', master)
        self.userImage.grid(row=0, column=0, rowspan=5,
                            sticky="nw", padx=2, pady=2)

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
    # End of createUserBox

    def createGraphOptionsBox(self, master):
        # Get a list of available stats from
        exampleGame = next(iter(games.values()))
        # print(json.dumps(exampleGame, indent=4, sort_keys=True))

        self.graphOptionsBoxLabel = tk.Label(master, text="Graph Options")
        self.graphOptionsBoxLabel.grid(
            row=0, column=0, sticky="nw", padx=2, pady=2)

        self.graphSelectionVar = tk.StringVar(self, "", name="GraphSelection")
        self.graphMenu = tk.Menubutton(
            master, textvariable=self.graphSelectionVar, indicatoron=True, borderwidth=1, relief="raised")
        self.gM = tk.Menu(self.graphMenu, tearoff=False)

        # statMenuChoices = GameStat().__dict__
        statMenuChoices = graphChoices

        self.populateMenuFromDict(statMenuChoices, menu=self.gM,
                                  variable=self.graphSelectionVar)
        self.graphSelectionVar.trace('w', self.graphSelectionHandler)

        self.graphMenu.configure(menu=self.gM)
        self.graphMenu.grid(row=1, column=0, sticky="n", padx=2, pady=2)

        # Create a absolute values checkbox
        self.absoluteValues = tk.BooleanVar(self, False, "absoluteValues")
        self.absoluteValues.trace('w', self.graphAbsoluteValueHandler)
        self.absoluteValuesCheckbox = tk.Checkbutton(
            master, text="Absolute Values", variable=self.absoluteValues)
        self.absoluteValuesCheckbox.grid(
            row=2, column=0, sticky="s", padx=2, pady=2)
    # End of createGraphOptionsBox

    def createSessionBox(self, master):
        # Create a listbox to show all the sessions
        self.SessionBoxLabel = tk.Label(
            master, text="Sessions")
        self.SessionBoxLabel.grid(row=0, column=0, sticky="nw", padx=2, pady=2)

        self.sessionListBox = tk.Listbox(master, height=6)
        self.sessionListBox.bind('<<ListboxSelect>>', self.sessionSelect)
        self.sessionListBox.grid(row=1, column=0, sticky="sw", padx=2, pady=2)
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

            for arg in widgetInfo['args']:
                self.__getattribute__(widgetInfo['name']).configure(arg)
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

        # Generate the sidebar from the schema
        for collapsible in SessionSidebar:
            if(collapsible['type'] == "collapsible"):
                self.createCollapsible(
                    collapsible, self.SessionStatsScrollBox.contentFrame)
            elif(collapsible['type'] == "widget"):
                self.createWidgetFromSchema(
                    collapsible, self.SessionStatsScrollBox.contentFrame)

        self.SessionStatsScrollBox.recalculateScrollBox()
    # End of createSessionsStatsBox

    def sessionSelect(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        for session in self.GameSessions:
            if(str(session.StartDate) == value):
                session.updateSessionStats(self, SessionSidebar)

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
                    # Add to list
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
                # print(dictionary)
                variable.set(dictionary)
    # End of populateMenuFromDict

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

    def refreshGraph(self):
        dataChoiceValue = self.graphSelectionVar.get()

        currentLow, currentHigh = self.goalsAx.get_xlim()

        self.clearGraph()

        self.goalsAx.get_yaxis().set_major_locator(
            MaxNLocator(integer=True))

        if("/" in dataChoiceValue):
            if(dataChoiceValue == "Win/Losses"):
                # print([d['Win'] for d in self.searchCache])
                self.goalsAx.bar(
                    [d['Date'] for d in self.searchCache],
                    [d['Win'] for d in self.searchCache],
                    color=[d['Win_Loss_Color'] for d in self.searchCache],
                    width=[d['Bar_Width'] for d in self.searchCache],
                    align='edge',
                    alpha=0.5)

                # Format the axis and add a title
                self.goalsAx.yaxis.set_major_formatter(plt.FuncFormatter(
                    lambda value, ticknumber: "Win" if value == 1 else "Loss" if value == -1 else ""))
                self.goalsAx.set_ylabel("Wins/Loss")
                self.goalsAx.set_title("Wins Vs Losses")
            else:
                choiceA, choiceB = dataChoiceValue.split("/")
                if(" " in choiceA):
                    tag, choiceA = choiceA.split(" ")
                    choiceA = tag + " " + choiceA
                    choiceB = tag + " " + choiceB

                graphDataA = self.graphDataArrayFromKeyString(
                    choiceA, self.searchCache)
                graphDataB = self.graphDataArrayFromKeyString(
                    choiceB, self.searchCache)

                graphDataB = [-1*x for x in graphDataB]

                # print(graphDataA)
                # print(graphDataB)

                self.goalsAx.bar(
                    [d['Date'] for d in self.searchCache],
                    graphDataA,
                    color=[d['Win_Loss_Color']
                           for d in self.searchCache],
                    width=[d['Bar_Width'] for d in self.searchCache],
                    align='edge',
                    alpha=0.5)

                self.goalsAx.bar(
                    [d['Date'] for d in self.searchCache],
                    graphDataB,
                    color=[d['Win_Loss_Color']
                           for d in self.searchCache],
                    width=[d['Bar_Width'] for d in self.searchCache],
                    align='edge',
                    alpha=0.5)

                # Format the axis and add a title
                self.goalsAx.set_ylabel(dataChoiceValue)
                self.goalsAx.set_title(dataChoiceValue)
        else:
            if(dataChoiceValue == "Time Played"):
                dataChoiceValue = "Time_Played"
            graphData = self.graphDataArrayFromKeyString(
                dataChoiceValue, self.searchCache)

            # If a dict then can either be absolute or percent (this graph updating also needs to be checked when updating absolute value)
            if(type(graphData[0]) is dict):
                if(self.absoluteValues.get() is True):
                    choice = [x for x in graphData[0].keys() if x !=
                              "percent"][0]
                else:
                    choice = [x for x in graphData[0].keys() if x ==
                              "percent"][0]
                graphData = [x[choice] for x in graphData]

            # print(graphData)

            self.goalsAx.bar(
                [d['Date'] for d in self.searchCache],
                graphData,
                color=[d['Win_Loss_Color']
                       for d in self.searchCache],
                width=[d['Bar_Width'] for d in self.searchCache],
                align='edge',
                alpha=0.5)
            # Format the axis and add a title
            self.goalsAx.set_xticklabels(
                self.goalsAx.get_xticks(), rotation=30)
            self.goalsAx.set_ylabel(dataChoiceValue.replace("_", " "))
            self.goalsAx.set_title(dataChoiceValue.replace("_", " "))

        # Calculate major ticks
        self.goalsAx.set_xticklabels(
            self.goalsAx.get_xticks(), rotation=30)
        self.goalsAx.set_xlabel("Date")

        if(self.graph_init is not True):
            self.goalsAx.set_xlim(currentLow, currentHigh)
        else:
            self.graph_init = False

        gf.dateGraphMajorTicksCalculation(self.goalsAx)
        self.goalsAx.axhline(y=0, ls="--", color="black", lw=0.25)
        gf.repaintMajorTicks(self.goalsAx)
        self.goalsFigure.tight_layout()

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
        # Clear Graph
        self.refreshGraph()
    # End of graphSelectionHandler

    def comboSelectUser(self, event):
        user = list(self.user_cache.values())[event.widget.current()]
        self.searchReplays(user)
    # End of comboSelectUser

    def checkInput(self, event):
        if(event.keysym == "Escape"):
            self.UserSearch.set("")

        if(self._after_id is not None):
            self.after_cancel(self._after_id)

        # Create a new job to run after the use has typed
        self._after_id = self.after(600, self.autocompleteSearch)
    # End of checkInput

    def autocompleteSearch(self):
        if(self.UserSearch.get() != ""):
            if(self.user_cache is not None):
                self.user_cache.clear()
            # Steam Search
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

            # Epic Search
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
            # print(self.user_cache)

            # Fill in data
            # print([self.user_cache.get(user)['platformUserHandle']
                  # for user in self.user_cache])
            self.UserSearch['values'] = [self.user_cache.get(
                user)['platformUserHandle'] for user in self.user_cache]
            self.UserSearch.event_generate('<Down>')
        else:
            if(self.user_cache is not None):
                self.user_cache.clear()
            self.UserSearch['values'] = []
    # End of autocompleteSearch

    def searchReplays(self, user):
        # UI Element to update user of progress
        # print(user)
        playerId = user['platformSlug'] + \
            ":" + user['platformUserIdentifier']
        self.progressBar = ttk.Progressbar(
            self.GraphBox, orient="horizontal", length=200)
        self.progressBar.pack(side="left", fill="both", expand=True)

        self.sessionListBox.delete(0, tk.END)

        id = user['platformUserIdentifier'] if user['platformSlug'] == "steam" else user['platformUserHandle']

        searchUrl = "https://api.tracker.gg/api/v2/rocket-league/standard/profile/" + \
            user['platformSlug']+"/"+id+"?"

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

        # print(userStats)

        if("avatarUrl" in userStats['platformInfo'].keys() and userStats['platformInfo']['avatarUrl'] is not None):
            imageURL = userStats['platformInfo']['avatarUrl']
        else:
            imageURL = 'https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png'

        newImage = tkRawImageURL(imageURL)
        self.userImage.configure(image=newImage)
        self.userImage.image = newImage

        self.UsernameLabel.configure(
            text=userStats['platformInfo']['platformUserHandle'])

        # print(json.dumps(userStats, indent=4, default=str))

        userOverallStats = None
        for segment in userStats['segments']:
            # print(json.dumps(segment, indent=4, default=str))
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

        # Search elements
        # print(playerId)
        url = 'https://ballchasing.com/api/replays?player-id=' + playerId
        headers = {'Authorization': 'ZZrm3Av50XYFihxOW8t24pMeDRgHopHfwJJovVRF'}
        searchGames = req.get(url, headers=headers)
        result = searchGames.json()
        # print(json.dumps(result['list'], indent=4, sort_keys=True))

        # Configuring UI with the relelvant progress
        self.progressBar.configure(maximum=len(result['list']))

        # Stats to be updated for the current search list
        self.searchCache = []

        self.GameSessions = []

        seenGUIDs = {}

        self.GameSessions.append(GameSession())

        for replay in result['list']:
            # Update loading bar
            self.progressBar.step()
            self.master.update()
            fetched = True

            # Check if the replay needs to be fetched (or if it is duplicate)
            # If these are the same, then assume it is the same game
            if games.get(replay['id']) is not None:
                # Get the replay from the hash list
                # print("Retrieving game from hash " + replay['id'])
                replayResult = games.get(replay['id'])
                fetched = False
            else:
                # Fetch replay
                # print("Fetching..." + replay['link'])
                gameReplay = req.get(replay['link'], headers=headers)
                replayResult = gameReplay.json()
                games[replay['id']] = replayResult

            if(not hasattr(replayResult, 'match_guid') and seenGUIDs.get(replayResult['match_guid']) is None):
                # print("Not seen this replay before",
                # replayResult['match_guid'])
                seenGUIDs[replayResult['match_guid']] = True
            else:
                # print("Seen this replay before!", replayResult['match_guid'])
                continue

            # print("reached past the continue")
            # Data processing on the replay
            localGame = GameStat()
            localGame.populateFromGame(
                replay, replayResult, user['platformUserIdentifier'])
            if(not self.GameSessions[len(self.GameSessions)-1].checkGameInSession(localGame)):
                self.GameSessions.append(GameSession())
            self.GameSessions[len(self.GameSessions)-1].addGame(localGame)
            self.searchCache.append(localGame.__dict__)
            # print(localGame)

            # Wait 500 ms before looking at the next (rate limiter on api calls)
            if fetched:
                time.sleep(0.5)
        # Print an example of a game json
        # exampleGame = next(iter(games.values()))

        # Save the updated games list to file
        gamesFile = open('games.json', 'w+')
        json.dump(games, gamesFile, indent=4, default=str)
        gamesFile.close()

        for session in self.GameSessions:
            sessionDict = session.__dict__
            print(json.dumps(sessionDict, indent=4, default=str))
            self.sessionListBox.insert(0, str(sessionDict['StartDate']))

        # UI plotting of data for the search period and removing loading bar
        self.progressBar.pack_forget()

        # Creating the graph object
        # Set to 1 dpi so that you can set the pixels size
        graphWidth = self.UserBox.winfo_width()  # + self.GraphOptionsBox.winfo_width()
        # Scale factor for both is 10
        # Scale factor for just UserBox is 7.5
        scaleFactor = 7.5
        # 4:3 = 0.75
        # 16:9 = 0.5625
        self.goalsFigure = plt.Figure(
            figsize=(scaleFactor, scaleFactor*0.75), dpi=graphWidth/scaleFactor)
        if hasattr(self, 'goalsCanvas'):
            self.goalsCanvas.get_tk_widget().pack_forget()
        self.goalsAx = self.goalsFigure.add_subplot(111)

        # Add the grpah to the window
        self.goalsCanvas = FigureCanvasTkAgg(self.goalsFigure, self.GraphBox)
        self.goalsCanvas.get_tk_widget().pack(
            side="bottom", anchor="w", fill="both", expand=True)

        self.refreshGraph()

        # Mouse handle event variable initialisaiton
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

        self.master.update()
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
            # Find the mid point of the graph as it is
            xlimLow, xlimHigh = self.goalsAx.get_xlim()
            xlimWidth = xlimHigh - xlimLow

            # Find the position of the mouse
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
                # Zoom in
                if(mousePercentageAcross > 0.66):
                    newxlimLow = xlimHigh - xlimWidth * 0.9
                elif(mousePercentageAcross < 0.33):
                    newxlimHigh = xlimLow + xlimWidth * 0.9
                else:
                    newxlimLow = xlimHigh - xlimWidth * 0.95
                    newxlimHigh = xlimLow + xlimWidth * 0.95
            elif(event.button == "down"):
                # Zoom out
                if(mousePercentageAcross > 0.66):
                    newxlimLow = xlimHigh - xlimWidth * 1.1
                elif(mousePercentageAcross < 0.33):
                    newxlimHigh = xlimLow + xlimWidth * 1.1
                else:
                    newxlimLow = xlimHigh - xlimWidth * 1.05
                    newxlimHigh = xlimLow + xlimWidth * 1.05

            # Reformat with new limits
            self.goalsAx.set_xlim(
                newxlimLow, newxlimHigh)

            gf.dateGraphMajorTicksCalculation(self.goalsAx)

            # Recalculate the major ticks
            gf.repaintMajorTicks(self.goalsAx)
            self.goalsFigure.tight_layout()
            self.goalsCanvas.draw()
    # End of onScroll

    def onMouseMove(self, event):
        if(self.mouse_down and event.inaxes and self.lastevent != None):
            # Find the data points of the current limit
            xlimLow, xlimHigh = self.goalsAx.get_xlim()
            xlimWidth = xlimHigh - xlimLow
            mouseMovement = event.x - self.lastevent.x

            # Find the current pixels limits of the subplot
            lowestPixelAxes = self.goalsAx.get_position(
            ).x0 * self.goalsFigure.get_size_inches()[0] * self.goalsFigure.dpi
            highestPixelAxes = self.goalsAx.get_position(
            ).x1 * self.goalsFigure.get_size_inches()[0] * self.goalsFigure.dpi
            axesWidthPixels = highestPixelAxes - lowestPixelAxes

            # Calculate and update the limits
            axMovement = mouseMovement * \
                xlimWidth / axesWidthPixels
            self.goalsAx.set_xlim(
                xlimLow-axMovement, xlimHigh-axMovement)

            # Recalculate the major ticks
            gf.repaintMajorTicks(self.goalsAx)
            self.goalsFigure.tight_layout()
            self.goalsCanvas.draw()
        self.lastevent = event
    # End of onMouseMove

    def onExit(self):
        self.master.destroy()
    # End of onExit
# End Application


root = tk.Tk()
app = Application(master=root)
app.mainloop()
