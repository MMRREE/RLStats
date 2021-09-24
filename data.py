from dateutil.parser import parse
from datetime import timezone


class GameStat():
    def __init__(self):
        # General stats
        self.Win = -1
        self.Time_Played = 0
        self.Overtime = 0
        self.Orange = {"Goals For": 0}
        self.Blue = {"Goals For": 0}

        # MetaData stats (to do with graphing)
        self.Date = 0
        self.BarWidth = 0
        self.WinLossColor = 'g'
        self.TargetPlayerTeam = 'Orange'
        self.OppositionTeam = 'Blue'
        self.PlayerTeamSize = 0
        self.OppositionTeamSize = 0

        # Team stats
        self.Team = {
            "Goals For": 0,
            "Goals Against": 0,
            "Assists": 0,
            "Shots": 0,
            "Demos Inflicted": 0,
            "Demos Received": 0,
            "Total Score": 0,
            "Average Score": 0,
            "Average Shooting Percent": 0,
            "Time in possesion": 0,
            "Time ball in defensive half": 0
        }

        # Opposition stats
        self.Opposition = {
            "Goals For": 0,
            "Goals Against": 0,
            "Assists": 0,
            "Shots": 0,
            "Demos Inflicted": 0,
            "Demos Received": 0,
            "Total Score": 0,
            "Average Score": 0,
            "Average Shooting Percent": 0,
            "Time in possesion": 0,
            "Time ball in defensive half": 0
        }

        # Individual Player stats
        self.Individual = {
            "General": {
                "Goals": 0,
                "Saves": 0,
                "Assists": 0,
                "Shots": 0,
                "Demos Inflicted": 0,
                "Demos Received": 0,
                "Score": 0,
                "Shooting Percent": 0,
                "Goals Against Whilst Last Defender": 0
            },
            "Boost": {
                "Average boost used per minute": 0,
                "Average boost collected per minute": 0,
                "Average boost amount": 0,
                "Second with 0 boost": 0,
                "Seconds with 100 boost": 0,
                "Big pads taken": 0,
                "Big pads stolen (in opponents half)": 0,
                "Small pads taken": 0,
                "Small pads stolen (in opponents half)": 0,
                "Boost overfill": 0,
                "Stolen overfill": 0,
                "Time at 0-25% boost": 0,
                "Time at 25-50% boost": 0,
                "Time at 50-75% boost": 0,
                "Time at 75-100% boost": 0,
                "Amount of boost used at supersonic": 0,
                "Amount of boost collected": 0
            },
            "Positioning": {
                "Average distance to teammates": 0,
                "% of time spent most back": 0,
                "% of time spent most forward": 0,
                "% of time in defensive third": 0,
                "% of time in neutral third": 0,
                "% of time in offensive third": 0,
                "% of time in defensive half": 0,
                "% of time in offensive half": 0,
                "% of time closest to ball (overall)": 0,
                "% of time farthest from ball (overall)": 0,
                "% of time behind the ball": 0,
                "% of time in front of the ball": 0,
                "Average distance to the ball": 0,
                "Average distance to the ball in possesion": 0,
                "Average distance to the ball out of possesion": 0
            },
            "Movement": {
                "Average speed (as a % of max speed)": 0,
                "Total distance travelled": 0,
                "% of time supersonic": 0,
                "% of time at boost speed (between boosting and supersonic)": 0,
                "% of time at slow speed (below boosting)": 0,
                "% of time on the ground": 0,
                "% of time in low air (below crossbar)": 0,
                "% of time in high air (above crossbar)": 0,
                "Powerslide total duration": 0,
                "Powerslide average duration": 0,
                "Number of powerslides": 0
            }
        }
    # End of __init__

    def populateFromGame(self, replay, replayResult):
        # Clarify if it was win or loss and assigning the teams
        if('Win' in replay['replay_title']):
            self.Win = 1
            self.WinLossColor = 'g'
            self.TargetPlayerTeam = "Orange" if self.Orange[
                'Goals For'] > self.Blue['Goals For'] else "Blue"
        else:
            self.Win = -1
            self.WinLossColor = 'r'
            self.TargetPlayerTeam = "Blue" if self.Orange['Goals For'] > self.Blue['Goals For'] else "Orange"
        self.OppositionTeam = "Orange" if not "Orange" in self.TargetPlayerTeam else "Blue"

        # General game stats (and meta data for graphing)
        self.Orange['Goals For'] = replayResult['orange']['stats']['core']['goals']
        self.Blue['Goals For'] = replayResult['blue']['stats']['core']['goals']

        self.Date = parse(replayResult['date']).astimezone(timezone.utc)
        self.Time_Played = replayResult['duration']

        self.BarWidth = self.Time_Played*0.00001

        # Team sizes
        self.PlayerTeamSize = len(
            replayResult[self.TargetPlayerTeam.lower()]['players'])
        self.OppositionTeamSize = len(
            replayResult[self.OppositionTeam.lower()]['players'])

        # Team stats
        print(self.TargetPlayerTeam.lower())
        self.Team['Goals For'] = replayResult[self.TargetPlayerTeam.lower()
                                              ]['stats']['core']['goals']

        self.Team['Goals Against'] = replayResult[self.TargetPlayerTeam.lower()
                                                  ]['stats']['core']['goals_against']*-1

        self.Team['Assists'] = replayResult[self.TargetPlayerTeam.lower()
                                            ]['stats']['core']['assists']

        self.Team['Shots'] = replayResult[self.TargetPlayerTeam.lower()
                                          ]['stats']['core']['shots']

        self.Team['Demos Inflicted'] = replayResult[self.TargetPlayerTeam.lower()
                                                    ]['stats']['demo']['inflicted']

        self.Team['Demos Received'] = replayResult[self.TargetPlayerTeam.lower()
                                                   ]['stats']['demo']['taken']

        self.Team['Total Score'] = replayResult[self.TargetPlayerTeam.lower()
                                                ]['stats']['core']['score']

        self.Team['Average Score'] = self.Team['Total Score'] / \
            self.PlayerTeamSize

        self.Team['Average Shooting Percent'] = replayResult[self.TargetPlayerTeam.lower()
                                                             ]['stats']['core']['shooting_percentage']

        self.Team['Time in possesion'] = replayResult[self.TargetPlayerTeam.lower()
                                                      ]['stats']['ball']['possession_time']

        self.Team['Time ball in defensive half'] = replayResult[self.TargetPlayerTeam.lower()
                                                                ]['stats']['ball']['time_in_side']

        # Opposition stats
        print(self.OppositionTeam.lower())
        self.Opposition['Goals For'] = replayResult[self.OppositionTeam.lower()
                                                    ]['stats']['core']['goals']
        self.Opposition['Goals Against'] = replayResult[self.TargetPlayerTeam.lower()
                                                        ]['stats']['core']['goals_against']*-1

        self.Opposition['Assists'] = replayResult[self.OppositionTeam.lower()
                                                  ]['stats']['core']['assists']

        self.Opposition['Shots'] = replayResult[self.OppositionTeam.lower()
                                                ]['stats']['core']['shots']

        self.Opposition['Demos Inflicted'] = replayResult[self.OppositionTeam.lower()
                                                          ]['stats']['demo']['inflicted']

        self.Opposition['Demos Received'] = replayResult[self.OppositionTeam.lower()
                                                         ]['stats']['demo']['taken']

        self.Opposition['Total Score'] = replayResult[self.OppositionTeam.lower()
                                                      ]['stats']['core']['score']

        self.Opposition['Average Score'] = self.Opposition['Total Score'] / \
            self.OppositionTeamSize

        self.Opposition['Average Shooting Percent'] = replayResult[self.OppositionTeam.lower()
                                                                   ]['stats']['core']['shooting_percentage']

        self.Opposition['Time in possesion'] = replayResult[self.OppositionTeam.lower()
                                                            ]['stats']['ball']['possession_time']

        self.Opposition['Time ball in defensive half'] = replayResult[self.OppositionTeam.lower()
                                                                      ]['stats']['ball']['time_in_side']

    # End of populateFromGame
# End of GameStat


statMenuChoices = [
    "Wins/Losses",
    {
        "Individual": [{
            "General": [
                "Goals",
                "Saves",
                "Assists",
                "Shots",
                "Demos Inflicted/Received",
                "Score",
                "Shooting Percent",
                "Goals against while last defender"
            ]
        }, {
            "Boost": [
                "Average boost used per minute",
                "Average boost collected per minute",
                "Average boost amount",
                "Second with 0 boost",
                "Seconds with 100 boost",
                "Big pads taken",
                "Big pads stolen (in opponents half)",
                "Small pads taken",
                "Small pads stolen (in opponents half)",
                "Boost overfill",
                "Stolen overfill",
                "Time at 0-25% boost",
                "Time at 25-50% boost",
                "Time at 50-75% boost",
                "Time at 75-100% boost",
                "Amount of boost used at supersonic",
                "Amount of boost collected"
            ]
        }, {
            "Positioning": [
                "Average distance to teammates",
                "% of time spent most back",
                "% of time spent most forward",
                "% of time in defensive third",
                "% of time in neutral third",
                "% of time in offensive third",
                "% of time in defensive half",
                "% of time in offensive half",
                "% of time closest to ball (overall)",
                "% of time farthest from ball (overall)",
                "% of time behind the ball",
                "% of time in front of the ball",
                "Average distance to the ball",
                "Average distance to the ball in possesion",
                "Average distance to the ball out of possesion"
            ]
        }, {
            "Movement": [
                "Average speed (as a % of max speed)",
                "Total distance travelled",
                "% of time supersonic",
                "% of time at boost speed (between boosting and supersonic)",
                "% of time at slow speed (below boosting)",
                "% of time on the ground",
                "% of time in low air (below crossbar)",
                "% of time in high air (above crossbar)",
                "Powerslide total duration",
                "Powerslide average duration",
                "Number of powerslides"
            ]
        }],
        "Teams": [
            "Goals For/Against",
            "Saves",
            "Assists",
            "Shots",
            "Demos Inflicted/Received",
            "Total Score",
            "Average Score",
            "Average Shooting Percent",
            "Time in possesion",
            "Time ball in defensive half"
        ]

    }
]
