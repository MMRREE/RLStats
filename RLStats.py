# As imports
from tkImageURL import tkLabelImageURL, tkRawImageURL
import matplotlib.pyplot as plt
import GraphFormat as gf
import requests as req
import tkinter as tk

# From imports
from matplotlib.backends.backend_tkagg import *
from tkinter import ttk

# Direct imports
import time
import json

from data import GameStat

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

        self.pack()

        self.create_widgets()

        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)
    # End of __init__

    def create_widgets(self):
        # Setting up window name and icon
        self.master.title("Rocket League Stats")
        self.master.iconbitmap(default='./icon.ico')

        # Create an interface menu
        self.menu = tk.Menu(self)
        self.m_file = tk.Menu(self, tearoff=0)
        self.m_file.add_command(label="Exit", command=self.on_exit)
        self.menu.add_cascade(label="File", menu=self.m_file)
        self.master.config(menu=self.menu)

        # Create a frame
        self.topFrame = tk.Frame(self)
        self.topFrame.pack(side='top')

        # Create a user image
        self.userImage = tkLabelImageURL(
            'https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png', self.topFrame)
        self.userImage.pack(side="left", padx=10, pady=10)

        # Get a list of available stats from
        exampleGame = next(iter(games.values()))
        #print(json.dumps(exampleGame, indent=4, sort_keys=True))

        self.graphSelectionVar = tk.StringVar(name="GraphSelection")
        self.graphMenu = tk.Menubutton(
            self.topFrame, textvariable=self.graphSelectionVar, indicatoron=True, borderwidth=1, relief="raised")
        self.gM = tk.Menu(self.graphMenu, tearoff=False)

        statMenuChoices = GameStat().__dict__

        self.exploreDict(statMenuChoices, menu=self.gM,
                         variable=self.graphSelectionVar)
        self.graphSelectionVar.trace('w', self.graphSelectionHandler)

        self.graphMenu.configure(menu=self.gM)
        self.graphMenu.pack(side='left', padx=10, pady=10)

        # Create a basic search entry
        self.search = ttk.Combobox(self.topFrame)
        self.search.bind('<KeyRelease>', self.check_input)
        self.search.pack(side="left", padx=10, pady=10)
        self.search.bind('<<ComboboxSelected>>', self.comboSelectUser)

        self.absoluteValues = tk.BooleanVar(self, False)
        self.absoluteValuesCheckbox = tk.Checkbutton(
            self.topFrame, text="Absolute Values", variable=self.absoluteValues)
        self.absoluteValuesCheckbox.pack(side="left", padx=10, pady=10)

        # Automatically run search
        self.search_replays('76561198072178785')
    # End of create_widgets(self)

    def populateMenuFromDict(self, dictionary, menu=None, variable=None):
        if(menu == None):
            menu = tk.Menu(self.graphMenu)
        if(type(dictionary) is dict):
            for tag, val in dictionary.items():
                if(type(val) is dict or type(val) is list):
                    newMenu = tk.Menu(self.graphMenu, tearoff=False)
                    menu.add_cascade(label=tag, menu=newMenu)
                    self.populateMenuFromDict(
                        dictionary=val, variable=variable, menu=newMenu)
                else:
                    menu.add_radiobutton(
                        value=val, label=tag, indicatoron=True, variable=variable)
                    if(variable.get() is None):
                        variable.set(val)
        elif(type(dictionary) is list):
            for obj in dictionary:
                self.populateMenuFromDict(obj, variable=variable, menu=menu)
        else:
            menu.add_radiobutton(
                value=dictionary, label=dictionary, indicatoron=True, variable=variable)
            if(variable.get() == ""):
                variable.set(dictionary)
    # End of populateMenuFromDict

    def exploreDict(self, dictionary, parentTags="", menu=None, variable=None):
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
                    self.exploreDict(val, currentTags, newMenu, variable)
                else:
                    # Add to list
                    menu.add_radiobutton(
                        value=currentTags, label=tag, indicatoron=True, variable=variable)
                    if(variable.get() == ""):
                        variable.set(tag)
        elif(type(dictionary) is list):
            for obj in dictionary:
                if(parentTags != ""):
                    currentTags = parentTags + \
                        "[" + str(dictionary.index(obj)) + "]"
                else:
                    currentTags = "[" + str(dictionary.index(obj)) + "]"
                self.exploreDict(obj, parentTags=currentTags,
                                 variable=variable, menu=menu)
        else:
            menu.add_radiobutton(
                value=dictionary, label=dictionary, indicatoron=True, variable=variable)
            if(variable.get() == ""):
                print(dictionary)
                variable.set(dictionary)
    # End of exploreDict

    def graphSelectionHandler(self, name, index, mode):
        #print(name, index, mode)
        newValue = self.graphSelectionVar.get()
        if("Wins/Losses" in newValue):
            print("win/loss")
        elif("Demos Inflicted/Received" in newValue):
            print("Demos")
        else:
            print("Default case")
            print(newValue)

    # End of graphSelectionHandler

    def comboSelectUser(self, event):
        user = self.user_cache[self.search.get()]
        imageURL = user['avatarUrl']
        newImage = tkRawImageURL(imageURL)
        self.userImage.configure(image=newImage)
        self.userImage.image = newImage
        self.master.update()
        # 76561198072178785
        self.search_replays(user['platformUserIdentifier'])
    # End of comboSelectUser

    def check_input(self, event):
        if(event.keysym == "Escape"):
            self.search.set("")

        if(self._after_id is not None):
            self.after_cancel(self._after_id)

        # Create a new job to run after the use has typed
        self._after_id = self.after(600, self.autocompleteSearch)
    # End of check_input

    def autocompleteSearch(self):
        if(self.search.get() != ""):
            userSearchResp = req.get('https://api.tracker.gg/api/v2/rocket-league/standard/search?platform=steam&autocomplete=true&query=' +
                                     self.search.get(),
                                     headers={
                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
                                         'Accept': 'application/json, text/plain, */*',
                                         'Accept-Language': 'en',
                                         'Sec-Fetch-Dest': 'empty',
                                         'Sec-Fetch-Mode': 'cors',
                                         'Sec-Fetch-Site': 'cross-site',
                                     })
            userSearchRespJson = userSearchResp.json()
            data = userSearchRespJson['data']
            users = []
            for user in data:
                users.append(user['platformUserHandle'])
                self.user_cache[user['platformUserHandle']] = user
            self.search['values'] = users
            self.search.event_generate('<Down>')
        else:
            self.search['values'] = []
    # End of autocompleteSearch

    def search_replays(self, steamId):
        # UI Element to update user of progress
        self.progressBar = ttk.Progressbar(
            self.master, orient="horizontal", length=200)
        self.progressBar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Search elements
        url = 'https://ballchasing.com/api/replays?player-id=Steam%3A' + steamId
        headers = {'Authorization': 'ZZrm3Av50XYFihxOW8t24pMeDRgHopHfwJJovVRF'}
        searchGames = req.get(url, headers=headers)
        result = searchGames.json()
        #print(json.dumps(result['list'], indent=4, sort_keys=True))

        # Configuring UI with the relelvant progress
        self.progressBar.configure(maximum=len(result['list']))

        # Stats to be updated for the current search list
        localSearchedGames = []

        seenGUIDs = {}

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
            localGame.populateFromGame(replay, replayResult, steamId)
            localSearchedGames.append(localGame.__dict__)
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

        # UI plotting of data for the search period and removing loading bar
        self.progressBar.pack_forget()

        # Creating the graph object
        self.goalsFigure = plt.Figure()
        if hasattr(self, 'goalsCanvas'):
            self.goalsCanvas.get_tk_widget().pack_forget()
        self.goalsAx = self.goalsFigure.add_subplot(111)

        # Plot the data
        print(json.dumps(result['list'][0], indent=4, default=str))
        print(json.dumps(
            games.get(result['list'][0]['id']), indent=4, default=str))
        print(json.dumps(localSearchedGames[0], indent=4, default=str))
        self.goalsAx.bar([d['Date'] for d in localSearchedGames], [d['Win'] for d in localSearchedGames], color=[d['WinLossColor'] for d in localSearchedGames], width=[d['BarWidth'] for d in localSearchedGames],
                         align='edge', alpha=0.5)

        # Format the axis and add a title
        self.goalsAx.set_xticklabels(self.goalsAx.get_xticks(), rotation=30)
        self.goalsAx.set_ylabel("Wins/Loss")
        self.goalsAx.set_xlabel("Time")
        self.goalsAx.set_title("Wins Vs Losses")

        # Calculate major ticks
        self.goalsAx.set_xlim(
            self.goalsAx.get_xlim()[1]-1, self.goalsAx.get_xlim()[1])
        gf.dateGraphMajorTicksCalculation(self.goalsAx)
        gf.repaintMajorTicks(self.goalsAx)
        self.goalsFigure.tight_layout()

        # Mouse handle event variable initialisaiton
        self.mouse_down = False
        self.lastevent = None

        cid = self.goalsFigure.canvas.mpl_connect(
            'button_press_event', self.onclick)
        rid = self.goalsFigure.canvas.mpl_connect(
            'button_release_event', self.onrelease)
        mid = self.goalsFigure.canvas.mpl_connect(
            'motion_notify_event', self.onmousemove)
        sid = self.goalsFigure.canvas.mpl_connect(
            'scroll_event', self.onscroll)

        # Add the grpah to the window
        self.goalsCanvas = FigureCanvasTkAgg(self.goalsFigure, self.master)
        self.goalsCanvas.get_tk_widget().pack()
        # self.goalsFigure.tight_layout()

        # print(results)
    # End search_replays

    def onclick(self, event):
        if(event.button == 1):
            self.mouse_down = True
    # End of onclick

    def onrelease(self, event):
        if(event.button == 1):
            self.mouse_down = False
    # End of onrelease

    def onscroll(self, event):
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
    # End of onscroll

    def onmousemove(self, event):
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
    # End of onmousemove

    def on_exit(self):
        self.master.destroy()
    # End of on_exit
# End Application


root = tk.Tk()
app = Application(master=root)
app.mainloop()
