from GameStats import GameStat
import datetime


class GameSession():
    def __init__(self):
        self.Games = []

        self.Wins = int(0)
        self.Losses = int(0)
        self.Time_Played = int(0)
        self.Overtime = int(0)
        self.StartDate = int(0)
        self.EndDate = int(0)
        self.WinRate = int(0)

        teamStructure = {
            "Goals For": int(0),
            "Saves": int(0),
            "Assists": int(0),
            "Shots": int(0),
            "Goals Against": int(0),
            "Demos Inflicted": int(0),
            "Demos Received": int(0),
            "Total Score": int(0),
            "Average Score": int(0),
            "Average Shooting Percent": int(0),
            "Time in possesion": int(0),
            "Time ball in defensive half": int(0)
        }

        self.Team = teamStructure

        self.Opposition = teamStructure

        self.Individual = {
            "General": {
                "Goals": int(0),
                "Saves": int(0),
                "Assists": int(0),
                "Shots": int(0),
                "Demos Inflicted": int(0),
                "Demos Received": int(0),
                "Score": int(0),
                "Shooting Percent": int(0),
                "MVP": int(0)
            },
            "Boost": {
                "Average boost used per minute": int(0),
                "Average boost collected per minute": int(0),
                "Average boost amount": int(0),
                "Amount of boost used at supersonic": int(0),
                "Amount of boost collected": int(0),
                "Big pads taken": int(0),
                "Big pads stolen": int(0),
                "Small pads taken": int(0),
                "Small pads stolen": int(0),
                "Boost overfill": int(0),
                "Stolen overfill": int(0),
                "0 boost": {"time": int(0), "percent": int(0)},
                "100 boost": {"time": int(0), "percent": int(0)},
                "0-25% boost": {"time": int(0), "percent": int(0)},
                "25-50% boost": {"time": int(0), "percent": int(0)},
                "50-75% boost": {"time": int(0), "percent": int(0)},
                "75-100% boost": {"time": int(0), "percent": int(0)},
                'Total stolen': int(0),
                'Total collected from big pads': int(0),
                'Total stolen from big pads': int(0),
                'Total collected from small pads': int(0),
                'Total stolen from small pads': int(0),
            },
            "Positioning": {
                "Average distance to teammates": int(0),
                "Average distance to the ball": int(0),
                "Average distance to the ball in possesion": int(0),
                "Average distance to the ball out of possesion": int(0),
                "Most back": {"time": int(0), "percent": int(0)},
                "Most forward": {"time": int(0), "percent": int(0)},
                "Defensive third": {"time": int(0), "percent": int(0)},
                "Neutral third": {"time": int(0), "percent": int(0)},
                "Offensive third": {"time": int(0), "percent": int(0)},
                "Defensive half": {"time": int(0), "percent": int(0)},
                "Offensive half": {"time": int(0), "percent": int(0)},
                "Closest to ball": {"time": int(0), "percent": int(0)},
                "Farthest from ball": {"time": int(0), "percent": int(0)},
                "Behind the ball": {"time": int(0), "percent": int(0)},
                "In front of the ball": {"time": int(0), "percent": int(0)},
            },
            "Movement": {
                "Average speed": {"absolute": int(0), "percent": int(0)},
                "Average powerslide duration": int(0),
                "Powerslide total duration": int(0),
                "Total distance travelled": int(0),
                "Number of powerslides": int(0),
                "Supersonic": {"time": int(0), "percent": int(0)},
                "Boost speed": {"time": int(0), "percent": int(0)},
                "Slow speed": {"time": int(0), "percent": int(0)},
                "On the ground": {"time": int(0), "percent": int(0)},
                "In low air": {"time": int(0), "percent": int(0)},
                "In high air": {"time": int(0), "percent": int(0)},
            }
        }
    # End of __init__

    def average(self, list):
        return sum(list) / len(list)
    # End of average

    def calculateSessionStats(self):
        self.Wins = sum([1 for d in self.Games if d.Win == 1])
        self.Losses = sum([1 for d in self.Games if d.Win == -1])
        self.Overtime = sum([d.Overtime for d in self.Games])
        self.Time_Played = sum([d.Time_Played for d in self.Games])

        gameTeams = [getattr(d, 'Team') for d in self.Games]

        self.Team['Goals For'] = sum(
            [d.get('Goals For', int(0)) for d in gameTeams])
        self.Team['Goals Against'] = sum([d.get('Goals Against', 0)
                                          for d in gameTeams])
        self.Team['Assists'] = sum([d.get('Assists', 0) for d in gameTeams])
        self.Team['Shots'] = sum([d.get('Shots', 0) for d in gameTeams])
        self.Team['Saves'] = sum([d.get('Saves', 0) for d in gameTeams])
        self.Team['Demos Inflicted'] = sum([d.get('Demos Inflicted', 0)
                                            for d in gameTeams])
        self.Team['Demos Received'] = sum([d.get('Demos Received', 0)
                                           for d in gameTeams])
        self.Team['Total Score'] = sum([d.get('Total Score', 0)
                                        for d in gameTeams])
        self.Team['Average Score'] = self.average(
            [d.get('Average Score', 0) for d in gameTeams])
        self.Team['Average Shooting Percent'] = self.average(
            [d.get('Average Shooting Percent', 0) for d in gameTeams])
        self.Team['Time in possesion'] = sum(
            [d.get('Time in possesion', 0) for d in gameTeams])
        self.Team['Time ball in defensive half'] = sum(
            [d.get('Time ball in defensive half', 0) for d in gameTeams])

        gameOppositionTeams = [getattr(d, 'Opposition') for d in self.Games]

        self.Opposition['Goals For'] = sum([d.get('Goals For', 0)
                                            for d in gameOppositionTeams])
        self.Opposition['Goals Against'] = sum(
            [d.get('Goals Against', 0) for d in gameOppositionTeams])
        self.Opposition['Assists'] = sum([d.get('Assists', 0)
                                          for d in gameOppositionTeams])
        self.Opposition['Shots'] = sum([d.get('Shots', 0)
                                        for d in gameOppositionTeams])
        self.Opposition['Saves'] = sum([d.get('Saves', 0)
                                        for d in gameOppositionTeams])
        self.Opposition['Demos Inflicted'] = sum(
            [d.get('Demos Inflicted', 0) for d in gameOppositionTeams])
        self.Opposition['Demos Received'] = sum(
            [d.get('Demos Received', 0) for d in gameOppositionTeams])
        self.Opposition['Total Score'] = sum([d.get('Total Score', 0)
                                              for d in gameOppositionTeams])
        self.Opposition['Average Score'] = self.average(
            [d.get('Average Score', 0) for d in gameOppositionTeams])
        self.Opposition['Average Shooting Percent'] = self.average(
            [d.get('Average Shooting Percent', 0) for d in gameOppositionTeams])
        self.Opposition['Time in possesion'] = sum(
            [d.get('Time in possesion', 0) for d in gameOppositionTeams])
        self.Opposition['Time ball in defensive half'] = sum(
            [d.get('Time ball in defensive half', 0) for d in gameOppositionTeams])

        gameIndividuals = [getattr(d, 'Individual') for d in self.Games]
        gameIndividualGenerals = [d.get('General', None)
                                  for d in gameIndividuals]
        self.Individual['General']['Goals'] = sum(
            [d.get('Goals', 0) for d in gameIndividualGenerals])
        self.Individual['General']['Saves'] = sum(
            [d.get('Saves', 0) for d in gameIndividualGenerals])
        self.Individual['General']['Assists'] = sum(
            [d.get('Assists', 0) for d in gameIndividualGenerals])
        self.Individual['General']['Shots'] = sum(
            [d.get('Shots', 0) for d in gameIndividualGenerals])
        self.Individual['General']['Demos Inflicted'] = sum(
            [d.get('Demos Inflicted', 0) for d in gameIndividualGenerals])
        self.Individual['General']['Demos Received'] = sum(
            [d.get('Demos Received', 0) for d in gameIndividualGenerals])
        self.Individual['General']['Score'] = sum(
            [d.get('Score', 0) for d in gameIndividualGenerals])
        self.Individual['General']['Shooting Percent'] = self.average(
            [d.get('Shooting Percent', 0) for d in gameIndividualGenerals])
        self.Individual['General']['MVP'] = sum(
            [d.get('MVP', 0) for d in gameIndividualGenerals])

        gameIndividualBoosts = [d.get('Boost', None) for d in gameIndividuals]
        self.Individual['Boost']['Average boost used per minute'] = self.average(
            [d.get('Average boost used per minute', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Average boost collected per minute'] = self.average(
            [d.get('Average boost collected per minute', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Average boost amount'] = self.average(
            [d.get('Average boost amount', 0) for d in gameIndividualBoosts])

        self.Individual['Boost']['Amount of boost collected'] = sum(
            [d.get('Amount of boost collected', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Amount of boost used at supersonic'] = sum(
            [d.get('Amount of boost used at supersonic', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Total stolen'] = sum(
            [d.get('Total stolen', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Total collected from big pads'] = sum(
            [d.get('Total collected from big pads', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Total stolen from big pads'] = sum(
            [d.get('Total stolen from big pads', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Total collected from small pads'] = sum(
            [d.get('Total collected from small pads', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Total stolen from small pads'] = sum(
            [d.get('Total stolen from small pads', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Boost overfill'] = sum(
            [d.get('Boost overfill', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Stolen overfill'] = sum(
            [d.get('Stolen overfill', 0) for d in gameIndividualBoosts])

        self.Individual['Boost']['Big pads taken'] = sum(
            [d.get('Big pads taken', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Big pads stolen'] = sum(
            [d.get('Big pads stolen', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Small pads taken'] = sum(
            [d.get('Small pads taken', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Small pads stolen'] = sum(
            [d.get('Small pads stolen', 0) for d in gameIndividualBoosts])

        self.Individual['Boost']['0 boost']['time'] = sum(
            [d['0 boost']['time'] for d in gameIndividualBoosts])
        self.Individual['Boost']['100 boost']['time'] = sum(
            [d['100 boost']['time'] for d in gameIndividualBoosts])
        self.Individual['Boost']['0-25% boost']['time'] = sum(
            [d['0-25% boost']['time'] for d in gameIndividualBoosts])
        self.Individual['Boost']['25-50% boost']['time'] = sum(
            [d['25-50% boost']['time'] for d in gameIndividualBoosts])
        self.Individual['Boost']['50-75% boost']['time'] = sum(
            [d['50-75% boost']['time'] for d in gameIndividualBoosts])
        self.Individual['Boost']['75-100% boost']['time'] = sum(
            [d['75-100% boost']['time'] for d in gameIndividualBoosts])

        self.Individual['Boost']['0 boost']['percent'] = self.average(
            [d['0 boost']['percent'] for d in gameIndividualBoosts])
        self.Individual['Boost']['100 boost']['percent'] = self.average(
            [d['100 boost']['percent'] for d in gameIndividualBoosts])
        self.Individual['Boost']['0-25% boost']['percent'] = self.average(
            [d['0-25% boost']['percent'] for d in gameIndividualBoosts])
        self.Individual['Boost']['25-50% boost']['percent'] = self.average(
            [d['25-50% boost']['percent'] for d in gameIndividualBoosts])
        self.Individual['Boost']['50-75% boost']['percent'] = self.average(
            [d['50-75% boost']['percent'] for d in gameIndividualBoosts])
        self.Individual['Boost']['75-100% boost']['percent'] = self.average(
            [d['75-100% boost']['percent'] for d in gameIndividualBoosts])

        gameIndividualPositionings = [
            d.get('Positioning', None) for d in gameIndividuals]
        self.Individual['Positioning']['Most back']['percent'] = self.average(
            [d['Most back']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Most forward']['percent'] = self.average(
            [d['Most forward']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Defensive third']['percent'] = self.average(
            [d['Defensive third']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Neutral third']['percent'] = self.average(
            [d['Neutral third']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Offensive third']['percent'] = self.average(
            [d['Offensive third']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Defensive half']['percent'] = self.average(
            [d['Defensive half']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Offensive half']['percent'] = self.average(
            [d['Offensive half']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Closest to ball']['percent'] = self.average(
            [d['Closest to ball']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Farthest from ball']['percent'] = self.average(
            [d['Farthest from ball']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Behind the ball']['percent'] = self.average(
            [d['Behind the ball']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['In front of the ball']['percent'] = self.average(
            [d['In front of the ball']['percent'] for d in gameIndividualPositionings])

        self.Individual['Positioning']['Most back']['time'] = sum(
            [d['Most back']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Most forward']['time'] = sum(
            [d['Most forward']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Defensive third']['time'] = sum(
            [d['Defensive third']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Neutral third']['time'] = sum(
            [d['Neutral third']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Offensive third']['time'] = sum(
            [d['Offensive third']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Defensive half']['time'] = sum(
            [d['Defensive half']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Offensive half']['time'] = sum(
            [d['Offensive half']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Closest to ball']['time'] = sum(
            [d['Closest to ball']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Farthest from ball']['time'] = sum(
            [d['Farthest from ball']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Behind the ball']['time'] = sum(
            [d['Behind the ball']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['In front of the ball']['time'] = sum(
            [d['In front of the ball']['time'] for d in gameIndividualPositionings])

        self.Individual['Positioning']['Average distance to teammates'] = self.average(
            [d.get('Average distance to teammates', 0) for d in gameIndividualPositionings])
        self.Individual['Positioning']['Average distance to the ball'] = self.average(
            [d.get('Average distance to the ball', 0) for d in gameIndividualPositionings])
        self.Individual['Positioning']['Average distance to the ball in possesion'] = self.average(
            [d.get('Average distance to the ball in possesion', 0) for d in gameIndividualPositionings])
        self.Individual['Positioning']['Average distance to the ball out of possesion'] = self.average(
            [d.get('Average distance to the ball out of possesion', 0) for d in gameIndividualPositionings])

        gameIndividualMovements = [
            d.get('Movement', None) for d in gameIndividuals]
        self.Individual['Movement']['Average speed']['absolute'] = self.average(
            [d['Average speed']['absolute'] for d in gameIndividualMovements])
        self.Individual['Movement']['Average speed']['percent'] = self.average(
            [d['Average speed']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['Average powerslide duration'] = self.average(
            [d['Average powerslide duration'] for d in gameIndividualMovements])
        self.Individual['Movement']['Total distance travelled'] = sum(
            [d.get('Total distance travelled', 0) for d in gameIndividualMovements])
        self.Individual['Movement']['Powerslide total duration'] = sum(
            [d.get('Powerslide total duration', 0) for d in gameIndividualMovements])
        self.Individual['Movement']['Number of powerslides'] = sum(
            [d.get('Number of powerslides', 0) for d in gameIndividualMovements])

        self.Individual['Movement']['Supersonic']['percent'] = self.average(
            [d['Supersonic']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['Boost speed']['percent'] = self.average(
            [d['Boost speed']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['Slow speed']['percent'] = self.average(
            [d['Slow speed']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['On the ground']['percent'] = self.average(
            [d['On the ground']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['In low air']['percent'] = self.average(
            [d['In low air']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['In high air']['percent'] = self.average(
            [d['In high air']['percent'] for d in gameIndividualMovements])

        self.Individual['Movement']['Supersonic']['time'] = self.average(
            [d['Supersonic']['time'] for d in gameIndividualMovements])
        self.Individual['Movement']['Boost speed']['time'] = self.average(
            [d['Boost speed']['time'] for d in gameIndividualMovements])
        self.Individual['Movement']['Slow speed']['time'] = self.average(
            [d['Slow speed']['time'] for d in gameIndividualMovements])
        self.Individual['Movement']['On the ground']['time'] = self.average(
            [d['On the ground']['time'] for d in gameIndividualMovements])
        self.Individual['Movement']['In low air']['time'] = self.average(
            [d['In low air']['time'] for d in gameIndividualMovements])
        self.Individual['Movement']['In high air']['time'] = self.average(
            [d['In high air']['time'] for d in gameIndividualMovements])
    # End of calculateSessionStats

    def addGame(self, game):
        self.Games.append(game)
        self.EndDate = getattr(game, 'Date', int(0)) + \
            datetime.timedelta(
                seconds=getattr(game, 'Time_Played', int(0))) if self.EndDate == int(0) else self.EndDate
        self.StartDate = getattr(game, 'Date', int(0))

        self.calculateSessionStats()
    # End of addGame

    def checkGameInSession(self, game):
        if(len(self.Games) < 1):
            endSearchDate = game.Date
            startSearchDate = game.Date
            self.GameMode = game.mode
        else:
            endSearchDate = self.Games[len(self.Games)-1].Date
            startSearchDate = self.Games[len(
                self.Games)-1].Date + datetime.timedelta(minutes=-20)

        if(startSearchDate <= game.Date <= endSearchDate and
           game.Match_GUID not in [d.Match_GUID for d in self.Games]
           and game.mode == self.GameMode):
            return True
        return False
    # End of checkGameInSession

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
        returnData = self.__dict__
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
