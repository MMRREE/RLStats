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

        self.Team = {
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
            "Time in Possession": int(0),
            "Time Ball in Defensive Half": int(0)
        }

        self.Opposition = {
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
            "Time in Possession": int(0),
            "Time Ball in Defensive Half": int(0)
        }

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
                "Average Boost Used per Minute": int(0),
                "Average Boost Collected per Minute": int(0),
                "Average Boost Amount": int(0),
                "Amount of Boost Used at Supersonic": int(0),
                "Amount of Boost Collected": int(0),
                "Big Pads Taken": int(0),
                "Big Pads Stolen": int(0),
                "Small Pads Taken": int(0),
                "Small Pads Stolen": int(0),
                "Boost Overfill": int(0),
                "Stolen Overfill": int(0),
                "0 Boost": {"time": int(0), "percent": int(0)},
                "100 Boost": {"time": int(0), "percent": int(0)},
                "0-25% Boost": {"time": int(0), "percent": int(0)},
                "25-50% Boost": {"time": int(0), "percent": int(0)},
                "50-75% Boost": {"time": int(0), "percent": int(0)},
                "75-100% Boost": {"time": int(0), "percent": int(0)},
                'Total Stolen': int(0),
                'Total Collected from Big Pads': int(0),
                'Total Stolen from Big Pads': int(0),
                'Total Collected from Small Pads': int(0),
                'Total Stolen from Small Pads': int(0),
            },
            "Positioning": {
                "Average Distance to Teammates": int(0),
                "Average Distance to the Ball": int(0),
                "Average Distance to the Ball in Possession": int(0),
                "Average Distance to the Ball out of Possession": int(0),
                "Most Back": {"time": int(0), "percent": int(0)},
                "Most Forward": {"time": int(0), "percent": int(0)},
                "Defensive Third": {"time": int(0), "percent": int(0)},
                "Neutral Third": {"time": int(0), "percent": int(0)},
                "Offensive Third": {"time": int(0), "percent": int(0)},
                "Defensive Half": {"time": int(0), "percent": int(0)},
                "Offensive Half": {"time": int(0), "percent": int(0)},
                "Closest to Ball": {"time": int(0), "percent": int(0)},
                "Farthest from Ball": {"time": int(0), "percent": int(0)},
                "Behind the Ball": {"time": int(0), "percent": int(0)},
                "In front of the Ball": {"time": int(0), "percent": int(0)},
            },
            "Movement": {
                "Average Speed": {"absolute": int(0), "percent": int(0)},
                "Average Powerslide Duration": int(0),
                "Powerslide Total Duration": int(0),
                "Total Distance Travelled": int(0),
                "Number of Powerslides": int(0),
                "Supersonic": {"time": int(0), "percent": int(0)},
                "Boost Speed": {"time": int(0), "percent": int(0)},
                "Slow Speed": {"time": int(0), "percent": int(0)},
                "On the Ground": {"time": int(0), "percent": int(0)},
                "In Low Air": {"time": int(0), "percent": int(0)},
                "In High Air": {"time": int(0), "percent": int(0)},
            }
        }
    # End of __init__

    def average(self, list):
        return sum(list) / len(list)
    # End of average

    def calculateSessionStats(self):
        self.Wins = sum([1 for d in self.Games if d.Win == 1])
        self.Losses = sum([1 for d in self.Games if d.Loss == 1])
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
        self.Team['Time in Possession'] = sum(
            [d.get('Time in Possession', 0) for d in gameTeams])
        self.Team['Time Ball in Defensive Half'] = sum(
            [d.get('Time Ball in Defensive Half', 0) for d in gameTeams])

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
        self.Opposition['Time in Possession'] = sum(
            [d.get('Time in Possession', 0) for d in gameOppositionTeams])
        self.Opposition['Time Ball in Defensive Half'] = sum(
            [d.get('Time Ball in Defensive Half', 0) for d in gameOppositionTeams])

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
        self.Individual['Boost']['Average Boost Used per Minute'] = self.average(
            [d.get('Average Boost Used per Minute', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Average Boost Collected per Minute'] = self.average(
            [d.get('Average Boost Collected per Minute', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Average Boost Amount'] = self.average(
            [d.get('Average Boost Amount', 0) for d in gameIndividualBoosts])

        self.Individual['Boost']['Amount of Boost Collected'] = sum(
            [d.get('Amount of Boost Collected', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Amount of Boost Used at Supersonic'] = sum(
            [d.get('Amount of Boost Used at Supersonic', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Total Stolen'] = sum(
            [d.get('Total Stolen', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Total Collected from Big Pads'] = sum(
            [d.get('Total Collected from Big Pads', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Total Stolen from Big Pads'] = sum(
            [d.get('Total Stolen from Big Pads', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Total Collected from Small Pads'] = sum(
            [d.get('Total Collected from Small Pads', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Total Stolen from Small Pads'] = sum(
            [d.get('Total Stolen from Small Pads', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Boost Overfill'] = sum(
            [d.get('Boost Overfill', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Stolen Overfill'] = sum(
            [d.get('Stolen Overfill', 0) for d in gameIndividualBoosts])

        self.Individual['Boost']['Big Pads Taken'] = sum(
            [d.get('Big Pads Taken', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Big Pads Stolen'] = sum(
            [d.get('Big Pads Stolen', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Small Pads Taken'] = sum(
            [d.get('Small Pads Taken', 0) for d in gameIndividualBoosts])
        self.Individual['Boost']['Small Pads Stolen'] = sum(
            [d.get('Small Pads Stolen', 0) for d in gameIndividualBoosts])

        self.Individual['Boost']['0 Boost']['time'] = sum(
            [d['0 Boost']['time'] for d in gameIndividualBoosts])
        self.Individual['Boost']['100 Boost']['time'] = sum(
            [d['100 Boost']['time'] for d in gameIndividualBoosts])
        self.Individual['Boost']['0-25% Boost']['time'] = sum(
            [d['0-25% Boost']['time'] for d in gameIndividualBoosts])
        self.Individual['Boost']['25-50% Boost']['time'] = sum(
            [d['25-50% Boost']['time'] for d in gameIndividualBoosts])
        self.Individual['Boost']['50-75% Boost']['time'] = sum(
            [d['50-75% Boost']['time'] for d in gameIndividualBoosts])
        self.Individual['Boost']['75-100% Boost']['time'] = sum(
            [d['75-100% Boost']['time'] for d in gameIndividualBoosts])

        self.Individual['Boost']['0 Boost']['percent'] = self.average(
            [d['0 Boost']['percent'] for d in gameIndividualBoosts])
        self.Individual['Boost']['100 Boost']['percent'] = self.average(
            [d['100 Boost']['percent'] for d in gameIndividualBoosts])
        self.Individual['Boost']['0-25% Boost']['percent'] = self.average(
            [d['0-25% Boost']['percent'] for d in gameIndividualBoosts])
        self.Individual['Boost']['25-50% Boost']['percent'] = self.average(
            [d['25-50% Boost']['percent'] for d in gameIndividualBoosts])
        self.Individual['Boost']['50-75% Boost']['percent'] = self.average(
            [d['50-75% Boost']['percent'] for d in gameIndividualBoosts])
        self.Individual['Boost']['75-100% Boost']['percent'] = self.average(
            [d['75-100% Boost']['percent'] for d in gameIndividualBoosts])

        gameIndividualPositionings = [
            d.get('Positioning', None) for d in gameIndividuals]
        self.Individual['Positioning']['Most Back']['percent'] = self.average(
            [d['Most Back']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Most Forward']['percent'] = self.average(
            [d['Most Forward']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Defensive Third']['percent'] = self.average(
            [d['Defensive Third']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Neutral Third']['percent'] = self.average(
            [d['Neutral Third']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Offensive Third']['percent'] = self.average(
            [d['Offensive Third']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Defensive Half']['percent'] = self.average(
            [d['Defensive Half']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Offensive Half']['percent'] = self.average(
            [d['Offensive Half']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Closest to Ball']['percent'] = self.average(
            [d['Closest to Ball']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Farthest from Ball']['percent'] = self.average(
            [d['Farthest from Ball']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Behind the Ball']['percent'] = self.average(
            [d['Behind the Ball']['percent'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['In front of the Ball']['percent'] = self.average(
            [d['In front of the Ball']['percent'] for d in gameIndividualPositionings])

        self.Individual['Positioning']['Most Back']['time'] = sum(
            [d['Most Back']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Most Forward']['time'] = sum(
            [d['Most Forward']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Defensive Third']['time'] = sum(
            [d['Defensive Third']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Neutral Third']['time'] = sum(
            [d['Neutral Third']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Offensive Third']['time'] = sum(
            [d['Offensive Third']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Defensive Half']['time'] = sum(
            [d['Defensive Half']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Offensive Half']['time'] = sum(
            [d['Offensive Half']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Closest to Ball']['time'] = sum(
            [d['Closest to Ball']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Farthest from Ball']['time'] = sum(
            [d['Farthest from Ball']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['Behind the Ball']['time'] = sum(
            [d['Behind the Ball']['time'] for d in gameIndividualPositionings])
        self.Individual['Positioning']['In front of the Ball']['time'] = sum(
            [d['In front of the Ball']['time'] for d in gameIndividualPositionings])

        self.Individual['Positioning']['Average Distance to Teammates'] = self.average(
            [d.get('Average Distance to Teammates', 0) for d in gameIndividualPositionings])
        self.Individual['Positioning']['Average Distance to the Ball'] = self.average(
            [d.get('Average Distance to the Ball', 0) for d in gameIndividualPositionings])
        self.Individual['Positioning']['Average Distance to the Ball in Possession'] = self.average(
            [d.get('Average Distance to the Ball in Possession', 0) for d in gameIndividualPositionings])
        self.Individual['Positioning']['Average Distance to the Ball out of Possession'] = self.average(
            [d.get('Average Distance to the Ball out of Possession', 0) for d in gameIndividualPositionings])

        gameIndividualMovements = [
            d.get('Movement', None) for d in gameIndividuals]
        self.Individual['Movement']['Average Speed']['absolute'] = self.average(
            [d['Average Speed']['absolute'] for d in gameIndividualMovements])
        self.Individual['Movement']['Average Speed']['percent'] = self.average(
            [d['Average Speed']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['Average Powerslide Duration'] = self.average(
            [d['Average Powerslide Duration'] for d in gameIndividualMovements])
        self.Individual['Movement']['Total Distance Travelled'] = sum(
            [d.get('Total Distance Travelled', 0) for d in gameIndividualMovements])
        self.Individual['Movement']['Powerslide Total Duration'] = sum(
            [d.get('Powerslide Total Duration', 0) for d in gameIndividualMovements])
        self.Individual['Movement']['Number of Powerslides'] = sum(
            [d.get('Number of Powerslides', 0) for d in gameIndividualMovements])

        self.Individual['Movement']['Supersonic']['percent'] = self.average(
            [d['Supersonic']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['Boost Speed']['percent'] = self.average(
            [d['Boost Speed']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['Slow Speed']['percent'] = self.average(
            [d['Slow Speed']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['On the Ground']['percent'] = self.average(
            [d['On the Ground']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['In Low Air']['percent'] = self.average(
            [d['In Low Air']['percent'] for d in gameIndividualMovements])
        self.Individual['Movement']['In High Air']['percent'] = self.average(
            [d['In High Air']['percent'] for d in gameIndividualMovements])

        self.Individual['Movement']['Supersonic']['time'] = self.average(
            [d['Supersonic']['time'] for d in gameIndividualMovements])
        self.Individual['Movement']['Boost Speed']['time'] = self.average(
            [d['Boost Speed']['time'] for d in gameIndividualMovements])
        self.Individual['Movement']['Slow Speed']['time'] = self.average(
            [d['Slow Speed']['time'] for d in gameIndividualMovements])
        self.Individual['Movement']['On the Ground']['time'] = self.average(
            [d['On the Ground']['time'] for d in gameIndividualMovements])
        self.Individual['Movement']['In Low Air']['time'] = self.average(
            [d['In Low Air']['time'] for d in gameIndividualMovements])
        self.Individual['Movement']['In High Air']['time'] = self.average(
            [d['In High Air']['time'] for d in gameIndividualMovements])
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
