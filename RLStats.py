from io import BytesIO
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import *
from tkinter.ttk import Progressbar
import requests as req
import numpy as np
import time
import json
from dateutil.parser import parse
from requests.api import head
import GraphFormat as gf
from datetime import timezone
from PIL import Image, ImageTk

# Initialise data from stored files
gamesFile = open('games.json', 'r+')
gamesData = gamesFile.read()
games = json.loads(gamesData)
gamesFile.close()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self._after_id = None
        self.user_cache = {}

        self.pack()
        self.create_widgets()

        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)
    # End __init__

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

        self.topFrame = tk.Frame(self)
        self.topFrame.pack(side='top')

        # Create a user image
        imageURL = 'https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png'
        imageReq = req.get(imageURL)
        photo = Image.open(BytesIO(imageReq.content))
        photo = photo.resize((120, 120), Image.ANTIALIAS)
        imageRaw = ImageTk.PhotoImage(photo)
        self.userImage = tk.Label(
            self.topFrame, image=imageRaw, width=120, height=120)
        self.userImage.image = imageRaw
        self.userImage.pack(side='left', padx=10, pady=10)

        # Get a list of available stats from
        exampleGame = next(iter(games.values()))
        #print(json.dumps(exampleGame, indent=4, sort_keys=True))

        self.graphSelectionVar = tk.StringVar(name="GraphSelection")
        self.graphSelectionVar.trace('w', self.graphSelectionHandler)
        self.graphMenu = tk.Menubutton(
            self.topFrame, textvariable=self.graphSelectionVar, indicatoron=True, borderwidth=1, relief="raised")
        self.gM = tk.Menu(self.graphMenu, tearoff=False)

        def exploreDict(dictionary, parentTags="", menu=tk.Menu()):
            for tag, val in dictionary.items():
                if(parentTags != ""):
                    currentTags = parentTags + "." + tag
                else:
                    currentTags = tag

                if(type(val) is dict):
                    newMenu = tk.Menu(self.graphMenu, tearoff=False)
                    menu.add_cascade(label=tag, menu=newMenu)
                    exploreDict(val, currentTags, newMenu)
                elif(type(val) is list):
                    for obj in val:
                        if(type(obj) is dict):
                            currentTags += "[" + str(val.index(obj)) + "]"
                            newMenu = tk.Menu(self.graphMenu, tearoff=False)
                            menu.add_cascade(label=tag, menu=newMenu)
                            exploreDict(obj, currentTags, newMenu)
                        else:
                            # Add to list
                            menu.add_radiobutton(
                                value=currentTags, label=tag, indicatoron=True, variable=self.graphSelectionVar)
                else:
                    # Add to list
                    menu.add_radiobutton(
                        value=currentTags, label=tag, indicatoron=True, variable=self.graphSelectionVar)

        exploreDict(exampleGame, menu=self.gM)

        self.graphMenu.configure(menu=self.gM)
        self.graphMenu.pack(side='left', padx=10, pady=10)

        self.labelValue = tk.Label(self.topFrame)
        self.labelValue.configure(text="test")
        self.labelValue.pack(side='left', padx=10, pady=10)

        # Create a basic search entry
        self.search = ttk.Combobox(self.topFrame)
        self.search.bind('<KeyRelease>', self.check_input)
        self.search.pack(side="left", padx=10, pady=10)
        self.search.bind('<<ComboboxSelected>>', self.comboSelectUser)

        # Automatically run search
        self.search_replays('76561198072178785')
    # End create_widgets(self)

    def graphSelectionHandler(self, name, index, mode):
        exampleGame = next(iter(games.values()))
        keys = self.graphSelectionVar.get().split(".")
        gotLabel = exampleGame
        for key in keys:
            if("[" in key):
                tempLabel = key.split("]")[0]
                newKey, ind = tempLabel.split("[")
                gotLabel = gotLabel.get(newKey)
                gotLabel = gotLabel[int(ind)]
            else:
                gotLabel = gotLabel.get(key)
        self.labelValue.configure(
            text=gotLabel)

    def comboSelectUser(self, event):
        user = self.user_cache[self.search.get()]
        print(user)
        imageURL = user['avatarUrl']
        print(imageURL)
        imageReq = req.get(imageURL)
        photo = Image.open(BytesIO(imageReq.content))
        photo = photo.resize((120, 120), Image.ANTIALIAS)
        newImage = ImageTk.PhotoImage(photo)
        self.userImage.configure(image=newImage)
        self.userImage.image = newImage
        self.master.update()
        # 76561198072178785
        self.search_replays(user['platformUserIdentifier'])

    def check_input(self, event):
        if(event.keysym == "Escape"):
            self.search.set("")

        if(self._after_id is not None):
            self.after_cancel(self._after_id)

        # Create a new job to run after the use has typed
        self._after_id = self.after(600, self.autocompleteSearch)

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

    def search_replays(self, steamId):
        # UI Element to update user of progress
        self.progressBar = Progressbar(
            self.master, orient="horizontal", length=200)
        self.progressBar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Search elements
        url = 'https://ballchasing.com/api/replays?player-id=Steam%3A' + steamId
        headers = {'Authorization': 'ZZrm3Av50XYFihxOW8t24pMeDRgHopHfwJJovVRF'}
        searchGames = req.get(url, headers=headers)
        result = searchGames.json()

        # Configuring UI with the relelvant progress
        self.progressBar.configure(maximum=len(result['list']))

        # Stats to be updated for the current search list
        orangeGoals = []
        blueGoals = []
        gameTimes = []
        gameLengths = []

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
                #print("Seen this replay before!", replayResult['match_guid'])
                continue

            #print("reached past the continue")
            # Data processing on the replay
            orangeGoals.append(
                replayResult['orange']['stats']['core']['goals'])
            blueGoals.append(replayResult['blue']['stats']['core']['goals'])
            gameTimes.append(
                parse(replayResult['date']).astimezone(timezone.utc))
            # print(gameTimes[len(gameTimes)-1])
            gameLengths.append(replayResult['duration'])
            # print(gameTimes)

            # Wait 500 ms before looking at the next (rate limiter on api calls)
            if fetched:
                time.sleep(0.5)
        # Print an example of a game json
        #exampleGame = next(iter(games.values()))

        # Save the updated games list to file
        gamesFile = open('games.json', 'w+')
        json.dump(games, gamesFile)
        gamesFile.close()
        barLengths = []
        for gameLength in gameLengths:
            barLengths.append(0.00001*gameLength)

        # UI plotting of data for the search period and removing loading bar
        self.progressBar.pack_forget()

        # Creating the graph object
        self.goalsFigure = plt.Figure()
        if hasattr(self, 'goalsCanvas'):
            self.goalsCanvas.get_tk_widget().pack_forget()
        self.goalsAx = self.goalsFigure.add_subplot(111)

        # Plot the data
        self.goalsAx.bar(gameTimes, orangeGoals,
                         color='r', width=barLengths, alpha=0.5, align='edge')
        self.goalsAx.bar(gameTimes, blueGoals, color='b',
                         width=barLengths, alpha=0.5, align='edge')

        # Format the axis and add a title
        self.goalsAx.set_xticklabels(self.goalsAx.get_xticks(), rotation=30)
        self.goalsAx.set_ylabel("Team Goals")
        self.goalsAx.set_xlabel("Time")
        self.goalsAx.set_title("Testing")
        gf.reformatMajorTicks(
            self.goalsAx, "%d/%m", "Day", range(32))
        self.goalsFigure.tight_layout()

        # Calculate major ticks
        gf.repaintMajorTicks(self.goalsAx)
        self.goalsAx.set_xlim(
            self.goalsAx.get_xlim()[1]-4, self.goalsAx.get_xlim()[1])

        # Mouse handle event variable initialisaiton
        self.mouse_down = False
        self.lastevent = None

        def onclick(event):
            if(event.button == 1):
                self.mouse_down = True

        def onrelease(event):
            if(event.button == 1):
                self.mouse_down = False

        def onscroll(event):
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
                newxlimWidth = newxlimHigh - newxlimLow

                # Calculate the major ticks requirement
                if(newxlimWidth < 0.000694*2):
                    gf.reformatMajorTicks(
                        self.goalsAx, "%M:%S", "Second", [0, 15, 30, 45])
                elif(newxlimWidth < 0.041*2):
                    gf.reformatMajorTicks(
                        self.goalsAx, "%H:%M", "Minute", [0, 15, 30, 45])
                elif(newxlimWidth < 0.041*6):
                    gf.reformatMajorTicks(
                        self.goalsAx, "%H:%M", "Hour", range(24))
                elif(newxlimWidth < 0.041*12):
                    gf.reformatMajorTicks(
                        self.goalsAx, "%H:%M", "Hour", [0, 3, 6, 9, 12, 15, 18, 21])
                elif(newxlimWidth < 1.5):
                    gf.reformatMajorTicks(
                        self.goalsAx, "%d/%m, %H:%M", "Hour", [0, 6, 12, 18])
                else:
                    gf.reformatMajorTicks(
                        self.goalsAx, "%d/%m", "Day", range(31))

                # Recalculate the major ticks
                gf.repaintMajorTicks(self.goalsAx)
                self.goalsFigure.tight_layout()
                self.goalsCanvas.draw()

        def onmousemove(event):
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

        cid = self.goalsFigure.canvas.mpl_connect(
            'button_press_event', onclick)
        rid = self.goalsFigure.canvas.mpl_connect(
            'button_release_event', onrelease)
        mid = self.goalsFigure.canvas.mpl_connect(
            'motion_notify_event', onmousemove)
        sid = self.goalsFigure.canvas.mpl_connect('scroll_event', onscroll)

        # Add the grpah to the window
        self.goalsCanvas = FigureCanvasTkAgg(self.goalsFigure, self.master)
        self.goalsCanvas.get_tk_widget().pack()
        # self.goalsFigure.tight_layout()
    # End search_replays(self)

    def on_exit(self):
        self.master.destroy()
    # End of on_exit
# End Application(Frame)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
