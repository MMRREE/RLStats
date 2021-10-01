from GameStats import GameStat
import datetime


class GameSession():
    def __init__(self):
        # Games Array (for reference)
        self.Games = []

        # General Aggregated Stats
        self.Wins = 0
        self.Losses = 0
        self.Time_Played = 0
        self.Overtime = 0
        self.StartDate = 0
        self.EndDate = 0
        self.WinRate = 0

        teamStructure = {
            "Goals For": 0,
            "Saves": 0,
            "Assists": 0,
            "Shots": 0,
            "Goals Against": 0,
            "Demos Inflicted": 0,
            "Demos Received": 0,
            "Total Score": 0,
            "Average Score": 0,
            "Average Shooting Percent": 0,
            "Time in possesion": 0,
            "Time ball in defensive half": 0
        }

        # Team Stats
        self.Team = teamStructure

        # Opposition Stats
        self.Opposition = teamStructure

        # Individual Stats
        self.Individual = {
            "General": {
                "Goals": 0,
                "Saves": 0,
                "Assists": 0,
                "Shots": 0,
                "Shots Against": 0,
                "Demos Inflicted": 0,
                "Demos Received": 0,
                "Score": 0,
                "Shooting Percent": 0,
                "Goals Against Whilst Last Defender": 0,
                "MVP": 0
            },
            "Boost": {
                "Average boost used per minute": 0,
                "Average boost collected per minute": 0,
                "Average boost amount": 0,
                "Amount of boost used at supersonic": 0,
                "Amount of boost collected": 0,
                "Big pads taken": 0,
                "Big pads stolen": 0,
                "Small pads taken": 0,
                "Small pads stolen": 0,
                "Boost overfill": 0,
                "Stolen overfill": 0,
                "0 boost": {"time": 0, "percent": 0},
                "100 boost": {"time": 0, "percent": 0},
                "0-25% boost": {"time": 0, "percent": 0},
                "25-50% boost": {"time": 0, "percent": 0},
                "50-75% boost": {"time": 0, "percent": 0},
                "75-100% boost": {"time": 0, "percent": 0},
                'Total stolen': 0,
                'Total collected from big pads': 0,
                'Total stolen from big pads': 0,
                'Total collected from small pads': 0,
                'Total stolen from small pads': 0,
            },
            "Positioning": {
                "Average distance to teammates": 0,
                "Average distance to the ball": 0,
                "Average distance to the ball in possesion": 0,
                "Average distance to the ball out of possesion": 0,
                "Most back": {"time": 0, "percent": 0},
                "Most forward": {"time": 0, "percent": 0},
                "Defensive third": {"time": 0, "percent": 0},
                "Neutral third": {"time": 0, "percent": 0},
                "Offensive third": {"time": 0, "percent": 0},
                "Defensive half": {"time": 0, "percent": 0},
                "Offensive half": {"time": 0, "percent": 0},
                "Closest to ball": {"time": 0, "percent": 0},
                "Farthest from ball": {"time": 0, "percent": 0},
                "Behind the ball": {"time": 0, "percent": 0},
                "In front of the ball": {"time": 0, "percent": 0},
            },
            "Movement": {
                "Average speed": {"absolute": 0, "percent": 0},
                "Average powerslide duration": 0,
                "Powerslide total duration": 0,
                "Total distance travelled": 0,
                "Number of powerslides": 0,
                "Supersonic": {"time": 0, "percent": 0},
                "Boost speed": {"time": 0, "percent": 0},
                "Slow speed": {"time": 0, "percent": 0},
                "On the ground": {"time": 0, "percent": 0},
                "In low air": {"time": 0, "percent": 0},
                "In high air": {"time": 0, "percent": 0},
            }
        }
    # End of __init__

    def addGame(self, game):
        self.Games.append(game)

        # General Stats for session
        self.Wins += 1 if game.Win == 1 else 0
        self.Losses += 1 if game.Win == -1 else 0
        self.Overtime += game.Overtime if game.Overtime != -2 else 0
        self.EndDate = game.Date + \
            datetime.timedelta(
                seconds=game.Time_Played) if self.EndDate == 0 else self.EndDate
        self.Time_Played += game.Time_Played
        self.StartDate = game.Date

        # Team
        self.Team['Goals For'] += game.Team['Goals For']
        self.Team['Goals Against'] += game.Team['Goals Against']
        self.Team['Assists'] += game.Team['Assists']
        self.Team['Shots'] += game.Team['Shots']
        self.Team['Saves'] += game.Team['Saves']
        self.Team['Demos Inflicted'] += game.Team['Demos Inflicted']
        self.Team['Demos Received'] += game.Team['Demos Received']
        self.Team['Total Score'] += game.Team['Total Score']
        self.Team['Average Score'] = (
            self.Team['Average Score'] + game.Team['Average Score'])/2
        self.Team['Average Shooting Percent'] = (
            self.Team['Average Shooting Percent'] + game.Team['Average Shooting Percent'])/2
        self.Team['Time in possesion'] += game.Team['Time in possesion']
        self.Team['Time ball in defensive half'] += game.Team['Time ball in defensive half']

        # Opposition
        self.Opposition['Goals For'] += game.Opposition['Goals For']
        self.Opposition['Goals Against'] += game.Opposition['Goals Against']
        self.Opposition['Assists'] += game.Opposition['Assists']
        self.Opposition['Shots'] += game.Opposition['Shots']
        self.Opposition['Saves'] += game.Opposition['Saves']
        self.Opposition['Demos Inflicted'] += game.Opposition['Demos Inflicted']
        self.Opposition['Demos Received'] += game.Opposition['Demos Received']
        self.Opposition['Total Score'] += game.Opposition['Total Score']
        self.Opposition['Average Score'] = (
            self.Opposition['Average Score'] + game.Opposition['Average Score'])/2
        self.Opposition['Average Shooting Percent'] = (
            self.Opposition['Average Shooting Percent'] + game.Opposition['Average Shooting Percent'])/2
        self.Opposition['Time in possesion'] += game.Opposition['Time in possesion']
        self.Opposition['Time ball in defensive half'] += game.Opposition['Time ball in defensive half']

        # Individual Stats
        # General Stats
        self.Individual['General']['Goals'] += game.Individual['General']['Goals']
        self.Individual['General']['Saves'] += game.Individual['General']['Saves']
        self.Individual['General']['Assists'] += game.Individual['General']['Assists']
        self.Individual['General']['Shots'] += game.Individual['General']['Shots']
        self.Individual['General']['Shots Against'] += game.Individual['General']['Shots Against']
        self.Individual['General']['Demos Inflicted'] += game.Individual['General']['Demos Inflicted']
        self.Individual['General']['Demos Received'] += game.Individual['General']['Demos Received']
        self.Individual['General']['Score'] += game.Individual['General']['Score']
        self.Individual['General']['Shooting Percent'] = (
            self.Individual['General']['Shooting Percent'] + game.Individual['General']['Shooting Percent'])/2
        self.Individual['General']['Goals Against Whilst Last Defender'] += game.Individual['General']['Goals Against Whilst Last Defender']
        self.Individual['General']['MVP'] += 1 if game.Individual['General']['MVP'] else 0

        # Boost Stats
        # Averages
        self.Individual['Boost']['Average boost used per minute'] = (
            self.Individual['Boost']['Average boost used per minute'] + game.Individual['Boost']['Average boost used per minute'])/2
        self.Individual['Boost']['Average boost collected per minute'] = (
            self.Individual['Boost']['Average boost collected per minute'] + game.Individual['Boost']['Average boost collected per minute'])/2
        self.Individual['Boost']['Average boost amount'] = (
            self.Individual['Boost']['Average boost amount'] + game.Individual['Boost']['Average boost amount'])/2

        # Absolutes
        self.Individual['Boost']['Amount of boost collected'] += game.Individual['Boost']['Amount of boost collected']
        self.Individual['Boost']['Amount of boost used at supersonic'] += game.Individual['Boost']['Amount of boost used at supersonic']
        self.Individual['Boost']['Total stolen'] +=\
            game.Individual['Boost']['Total stolen']
        self.Individual['Boost']['Total collected from big pads'] += game.Individual['Boost']['Total collected from big pads']
        self.Individual['Boost']['Total stolen from big pads'] += game.Individual['Boost']['Total stolen from big pads']
        self.Individual['Boost']['Total collected from small pads'] += game.Individual['Boost']['Total collected from small pads']
        self.Individual['Boost']['Total stolen from small pads'] += game.Individual['Boost']['Total stolen from small pads']
        self.Individual['Boost']['Boost overfill'] += game.Individual['Boost']['Boost overfill']
        self.Individual['Boost']['Stolen overfill'] += game.Individual['Boost']['Stolen overfill']

        # Count
        self.Individual['Boost']['Big pads taken'] += game.Individual['Boost']['Big pads taken']
        self.Individual['Boost']['Big pads stolen'] += game.Individual['Boost']['Big pads stolen']
        self.Individual['Boost']['Small pads taken'] += game.Individual['Boost']['Small pads taken']
        self.Individual['Boost']['Small pads stolen'] += game.Individual['Boost']['Small pads stolen']

        # Time
        self.Individual['Boost']['0 boost']['time'] += game.Individual['Boost']['0 boost']['time']
        self.Individual['Boost']['100 boost']['time'] += game.Individual['Boost']['100 boost']['time']
        self.Individual['Boost']['0-25% boost']['time'] += game.Individual['Boost']['0-25% boost']['time']
        self.Individual['Boost']['25-50% boost']['time'] += game.Individual['Boost']['25-50% boost']['time']
        self.Individual['Boost']['50-75% boost']['time'] += game.Individual['Boost']['50-75% boost']['time']
        self.Individual['Boost']['75-100% boost']['time'] += game.Individual['Boost']['75-100% boost']['time']

        # Percent
        self.Individual['Boost']['0 boost']['percent'] = (
            self.Individual['Boost']['0 boost']['percent'] + game.Individual['Boost']['0 boost']['percent'])/2
        self.Individual['Boost']['100 boost']['percent'] = (
            self.Individual['Boost']['100 boost']['percent'] + game.Individual['Boost']['100 boost']['percent'])/2
        self.Individual['Boost']['0-25% boost']['percent'] = (
            self.Individual['Boost']['0-25% boost']['percent'] + game.Individual['Boost']['0-25% boost']['percent'])/2
        self.Individual['Boost']['25-50% boost']['percent'] = (
            self.Individual['Boost']['25-50% boost']['percent'] + game.Individual['Boost']['25-50% boost']['percent'])/2
        self.Individual['Boost']['50-75% boost']['percent'] = (
            self.Individual['Boost']['50-75% boost']['percent'] + game.Individual['Boost']['50-75% boost']['percent'])/2
        self.Individual['Boost']['75-100% boost']['percent'] = (
            self.Individual['Boost']['75-100% boost']['percent'] + game.Individual['Boost']['75-100% boost']['percent'])/2

        # Positioning stats
        # Percentages
        self.Individual['Positioning']['Most back']['percent'] = (
            self.Individual['Positioning']['Most back']['percent'] + game.Individual['Positioning']['Most back']['percent'])/2
        self.Individual['Positioning']['Most forward']['percent'] = (
            self.Individual['Positioning']['Most forward']['percent'] + game.Individual['Positioning']['Most forward']['percent'])/2
        self.Individual['Positioning']['Defensive third']['percent'] = (
            self.Individual['Positioning']['Defensive third']['percent'] + game.Individual['Positioning']['Defensive third']['percent'])/2
        self.Individual['Positioning']['Neutral third']['percent'] = (
            self.Individual['Positioning']['Neutral third']['percent'] + game.Individual['Positioning']['Neutral third']['percent']) / 2
        self.Individual['Positioning']['Offensive third']['percent'] = (
            self.Individual['Positioning']['Offensive third']['percent'] + game.Individual['Positioning']['Offensive third']['percent'])/2
        self.Individual['Positioning']['Defensive half']['percent'] = (
            self.Individual['Positioning']['Defensive half']['percent'] + game.Individual['Positioning']['Defensive half']['percent'])/2
        self.Individual['Positioning']['Offensive half']['percent'] = (
            self.Individual['Positioning']['Offensive half']['percent'] + game.Individual['Positioning']['Offensive half']['percent'])/2
        self.Individual['Positioning']['Closest to ball']['percent'] = (
            self.Individual['Positioning']['Closest to ball']['percent'] + game.Individual['Positioning']['Closest to ball']['percent'])/2
        self.Individual['Positioning']['Farthest from ball']['percent'] = (
            self.Individual['Positioning']['Farthest from ball']['percent'] + game.Individual['Positioning']['Farthest from ball']['percent'])/2
        self.Individual['Positioning']['Behind the ball']['percent'] = (
            self.Individual['Positioning']['Behind the ball']['percent'] + game.Individual['Positioning']['Behind the ball']['percent'])/2
        self.Individual['Positioning']['In front of the ball']['percent'] = (
            self.Individual['Positioning']['In front of the ball']['percent'] + game.Individual['Positioning']['In front of the ball']['percent'])/2

        # Absolutes
        self.Individual['Positioning']['Most back']['time'] += game.Individual['Positioning']['Most back']['time']
        self.Individual['Positioning']['Most forward']['time'] += game.Individual['Positioning']['Most forward']['time']
        self.Individual['Positioning']['Defensive third']['time'] += game.Individual['Positioning']['Defensive third']['time']
        self.Individual['Positioning']['Neutral third']['time'] += game.Individual['Positioning']['Neutral third']['time']
        self.Individual['Positioning']['Offensive third']['time'] += game.Individual['Positioning']['Offensive third']['time']
        self.Individual['Positioning']['Defensive half']['time'] += game.Individual['Positioning']['Defensive half']['time']
        self.Individual['Positioning']['Offensive half']['time'] += game.Individual['Positioning']['Offensive half']['time']
        self.Individual['Positioning']['Closest to ball']['time'] += game.Individual['Positioning']['Closest to ball']['time']
        self.Individual['Positioning']['Farthest from ball']['time'] += game.Individual['Positioning']['Farthest from ball']['time']
        self.Individual['Positioning']['Behind the ball']['time'] += game.Individual['Positioning']['Behind the ball']['time']
        self.Individual['Positioning']['In front of the ball']['time'] += game.Individual['Positioning']['In front of the ball']['time']

        # Averages
        if(game.Player_Team_Size > 1):
            self.Individual['Positioning']['Average distance to teammates'] = (
                self.Individual['Positioning']['Average distance to teammates'] + game.Individual['Positioning']['Average distance to teammates'])/2
        self.Individual['Positioning']['Average distance to the ball'] = (
            self.Individual['Positioning']['Average distance to the ball'] + game.Individual['Positioning']['Average distance to the ball'])/2
        self.Individual['Positioning']['Average distance to the ball in possesion'] = (
            self.Individual['Positioning']['Average distance to the ball in possesion'] + game.Individual['Positioning']['Average distance to the ball in possesion'])/2
        self.Individual['Positioning']['Average distance to the ball out of possesion'] = (
            self.Individual['Positioning']['Average distance to the ball out of possesion'] + game.Individual['Positioning']['Average distance to the ball out of possesion'])/2

        # Movement stats
        # Averages
        self.Individual['Movement']['Average speed']['absolute'] += game.Individual['Movement']['Average speed']['absolute']
        self.Individual['Movement']['Average speed']['percent'] = (
            self.Individual['Movement']['Average speed']['percent'] + game.Individual['Movement']['Average speed']['percent'])/2
        self.Individual['Movement']['Average powerslide duration'] = (
            self.Individual['Movement']['Average powerslide duration'] + game.Individual['Movement']['Average powerslide duration'])/2
        self.Individual['Movement']['Total distance travelled'] += game.Individual['Movement']['Total distance travelled']
        self.Individual['Movement']['Powerslide total duration'] += game.Individual['Movement']['Powerslide total duration']
        self.Individual['Movement']['Number of powerslides'] += game.Individual['Movement']['Number of powerslides']

        self.Individual['Movement']['Supersonic']['percent'] = (
            self.Individual['Movement']['Supersonic']['percent'] + game.Individual['Movement']['Supersonic']['percent'])/2
        self.Individual['Movement']['Boost speed']['percent'] = (
            self.Individual['Movement']['Boost speed']['percent'] + game.Individual['Movement']['Boost speed']['percent'])/2
        self.Individual['Movement']['Slow speed']['percent'] = (
            self.Individual['Movement']['Slow speed']['percent'] + game.Individual['Movement']['Slow speed']['percent'])/2
        self.Individual['Movement']['On the ground']['percent'] = (
            self.Individual['Movement']['On the ground']['percent'] + game.Individual['Movement']['On the ground']['percent'])/2
        self.Individual['Movement']['In low air']['percent'] = (
            self.Individual['Movement']['In low air']['percent'] + game.Individual['Movement']['In low air']['percent'])/2
        self.Individual['Movement']['In high air']['percent'] = (
            self.Individual['Movement']['In high air']['percent'] + game.Individual['Movement']['In high air']['percent'])/2

        self.Individual['Movement']['Supersonic']['time'] += game.Individual['Movement']['Supersonic']['time']
        self.Individual['Movement']['Boost speed']['time'] += game.Individual['Movement']['Boost speed']['time']
        self.Individual['Movement']['Slow speed']['time'] += game.Individual['Movement']['Slow speed']['time']
        self.Individual['Movement']['On the ground']['time'] += game.Individual['Movement']['On the ground']['time']
        self.Individual['Movement']['In low air']['time'] += game.Individual['Movement']['In low air']['time']
        self.Individual['Movement']['In high air']['time'] += game.Individual['Movement']['In high air']['time']
    # End of addGame

    def checkGameInSession(self, game):
        if(len(self.Games) < 1):
            endSearchDate = game.Date
            startSearchDate = game.Date
        else:
            endSearchDate = self.Games[len(self.Games)-1].Date
            startSearchDate = self.Games[len(
                self.Games)-1].Date + datetime.timedelta(minutes=-20)

        if(startSearchDate <= game.Date <= endSearchDate):
            return True
        return False
    # End of checkGameInSession

    def updateStat(self, widget, Frame):
        if("tags" in widget.keys()):
            if("." not in widget['tags']):
                rawValue = self.__getattribute__(widget['tags'])
                if(type(rawValue) is int or type(rawValue) is float):
                    value = f"{rawValue:{widget['precision']}}"
                else:
                    value = str(rawValue)
            else:
                print(widget)
                rawValue = self.returnValueFromKeyString(widget['tags'])
                print(rawValue)
                value = f"{rawValue:{widget['precision']}}"
        else:
            value = ""
        Frame.updateWidgetFromSchema(widget, f"{value}")

    # End of updateStat

    def returnValueFromKeyString(self, keyString):
        keys = keyString.split(".")
        returnData = self.__dict__
        for key in keys:
            if("[" in key):
                tempLabel = key.split("]")[0]
                newKey, ind = tempLabel.split("[")
                returnData = returnData.get(newKey)
            else:
                returnData = returnData.get(key)
        return returnData
    # End of returnValueFromKeyString

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

    def updateSessionStats(self, Frame, schema):
        self.WinRate = self.Wins/(self.Wins+self.Losses)*100

        self.exploreSchemaAndUpdate(schema, Frame)
    # End of updateSessionStats
# End of GameSession
