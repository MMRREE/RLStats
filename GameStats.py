from dateutil.parser import parse
from datetime import timezone
import json


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
        self.Bar_Width = 0
        self.Win_Loss_Color = 'g'
        self.Target_Player_Team = 'Orange'
        self.Opposition_Team = 'Blue'
        self.Player_Team_Size = 0
        self.Opposition_Team_Size = 0

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

        # Team stats
        self.Team = teamStructure

        # Opposition stats
        self.Opposition = teamStructure

        # Individual Player stats
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
                "MVP": False
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

    def populateFromGame(self, replay, replayResult, userId):

        # General game stats (and meta data for graphing)
        self.Orange['Goals For'] = replayResult['orange']['stats']['core']['goals']
        self.Blue['Goals For'] = replayResult['blue']['stats']['core']['goals']

        # Clarify if it was win or loss and assigning the teams
        if('Win' in replay['replay_title']):
            self.Win = 1
            self.Win_Loss_Color = 'g'
            self.Target_Player_Team = "Orange" if self.Orange[
                'Goals For'] > self.Blue['Goals For'] else "Blue"
        else:
            self.Win = -1
            self.Win_Loss_Color = 'r'
            self.Target_Player_Team = "Blue" if self.Orange[
                'Goals For'] > self.Blue['Goals For'] else "Orange"
        self.Opposition_Team = "Orange" if not "Orange" in self.Target_Player_Team else "Blue"

        if(replayResult['overtime']):
            self.Overtime = replayResult['overtime_seconds']
        else:
            self.Overtime = -2

        self.Date = parse(replayResult['date']).astimezone(timezone.utc)
        self.Time_Played = replayResult['duration']

        self.Bar_Width = self.Time_Played*0.00001157407

        # Team sizes
        self.Player_Team_Size = len(
            replayResult[self.Target_Player_Team.lower()]['players'])
        self.Opposition_Team_Size = len(
            replayResult[self.Opposition_Team.lower()]['players'])

        # Team stats
        print(replayResult['orange']['stats'])
        self.Team['Goals For'] = replayResult[self.Target_Player_Team.lower()
                                              ]['stats']['core']['goals']

        self.Team['Goals Against'] = replayResult[self.Target_Player_Team.lower()
                                                  ]['stats']['core']['goals_against']

        self.Team['Assists'] = replayResult[self.Target_Player_Team.lower()
                                            ]['stats']['core']['assists']

        self.Team['Shots'] = replayResult[self.Target_Player_Team.lower()
                                          ]['stats']['core']['shots']

        self.Team['Saves'] = replayResult[self.Target_Player_Team.lower()
                                          ]['stats']['core']['saves']

        self.Team['Demos Inflicted'] = replayResult[self.Target_Player_Team.lower()
                                                    ]['stats']['demo']['inflicted']

        self.Team['Demos Received'] = replayResult[self.Target_Player_Team.lower()
                                                   ]['stats']['demo']['taken']

        self.Team['Total Score'] = replayResult[self.Target_Player_Team.lower()
                                                ]['stats']['core']['score']

        self.Team['Average Score'] = self.Team['Total Score'] / \
            self.Player_Team_Size

        self.Team['Average Shooting Percent'] = replayResult[self.Target_Player_Team.lower()
                                                             ]['stats']['core']['shooting_percentage']

        self.Team['Time in possesion'] = replayResult[self.Target_Player_Team.lower()
                                                      ]['stats']['ball']['possession_time']

        self.Team['Time ball in defensive half'] = replayResult[self.Target_Player_Team.lower()
                                                                ]['stats']['ball']['time_in_side']

        # Opposition stats
        self.Opposition['Goals For'] = replayResult[self.Opposition_Team.lower()
                                                    ]['stats']['core']['goals']
        self.Opposition['Goals Against'] = replayResult[self.Opposition_Team.lower()
                                                        ]['stats']['core']['goals_against']

        self.Opposition['Assists'] = replayResult[self.Opposition_Team.lower()
                                                  ]['stats']['core']['assists']

        self.Opposition['Shots'] = replayResult[self.Opposition_Team.lower()
                                                ]['stats']['core']['shots']

        self.Opposition['Demos Inflicted'] = replayResult[self.Opposition_Team.lower()
                                                          ]['stats']['demo']['inflicted']

        self.Opposition['Demos Received'] = replayResult[self.Opposition_Team.lower()
                                                         ]['stats']['demo']['taken']

        self.Opposition['Total Score'] = replayResult[self.Opposition_Team.lower()
                                                      ]['stats']['core']['score']

        self.Opposition['Average Score'] = self.Opposition['Total Score'] / \
            self.Opposition_Team_Size

        self.Opposition['Average Shooting Percent'] = replayResult[self.Opposition_Team.lower()
                                                                   ]['stats']['core']['shooting_percentage']

        self.Opposition['Time in possesion'] = replayResult[self.Opposition_Team.lower()
                                                            ]['stats']['ball']['possession_time']

        self.Opposition['Time ball in defensive half'] = replayResult[self.Opposition_Team.lower()
                                                                      ]['stats']['ball']['time_in_side']

        # Individual stats
        targetUser = None
        for player in replayResult[self.Target_Player_Team.lower()]['players']:
            if(player['id']['id'] == userId):
                targetUser = player

        for player in replayResult[self.Opposition_Team.lower()]['players']:
            if(player['id']['id'] == userId):
                targetUser = player

        # Individual stats
        if(targetUser is not None):
            #print(json.dumps(targetUser, indent=4))

            # General stats
            self.Individual['General']['Goals'] = targetUser['stats']['core']['goals']
            self.Individual['General']['Saves'] = targetUser['stats']['core']['saves']
            self.Individual['General']['Assists'] = targetUser['stats']['core']['assists']
            self.Individual['General']['Shots'] = targetUser['stats']['core']['shots']
            self.Individual['General']['Shots Against'] = targetUser['stats']['core']['shots_against']
            self.Individual['General']['Demos Inflicted'] = targetUser['stats']['demo']['inflicted']
            self.Individual['General']['Demos Received'] = targetUser['stats']['demo']['taken']
            self.Individual['General']['Score'] = targetUser['stats']['core']['score']
            self.Individual['General']['Shooting Percent'] = targetUser['stats']['core']['shooting_percentage']
            self.Individual['General']['Goals Against Whilst Last Defender'] = targetUser['stats']['core']['goals_against']
            self.Individual['General']['MVP'] = targetUser['stats']['core']['mvp']

            # Boost stats
            # Absolute
            self.Individual['Boost']['Average boost used per minute'] = targetUser['stats']['boost']['bpm']
            self.Individual['Boost']['Average boost collected per minute'] = targetUser['stats']['boost']['bcpm']
            self.Individual['Boost']['Average boost amount'] = targetUser['stats']['boost']['avg_amount']
            self.Individual['Boost']['Amount of boost collected'] = targetUser['stats']['boost']['amount_collected']
            self.Individual['Boost']['Amount of boost used at supersonic'] = targetUser['stats']['boost']['amount_used_while_supersonic']
            self.Individual['Boost']['Total stolen'] = targetUser['stats']['boost']['amount_stolen']
            self.Individual['Boost']['Total collected from big pads'] = targetUser['stats']['boost']['amount_collected_big']
            self.Individual['Boost']['Total stolen from big pads'] = targetUser['stats']['boost']['amount_stolen_big']
            self.Individual['Boost']['Total collected from small pads'] = targetUser['stats']['boost']['amount_collected_small']
            self.Individual['Boost']['Total stolen from small pads'] = targetUser['stats']['boost']['amount_stolen_small']
            self.Individual['Boost']['Boost overfill'] = targetUser['stats']['boost']['amount_overfill']
            self.Individual['Boost']['Stolen overfill'] = targetUser['stats']['boost']['amount_overfill_stolen']

            # Count
            self.Individual['Boost']['Big pads taken'] = targetUser['stats']['boost']['count_collected_big']
            self.Individual['Boost']['Big pads stolen'] = targetUser['stats']['boost']['count_stolen_big']
            self.Individual['Boost']['Small pads taken'] = targetUser['stats']['boost']['count_collected_small']
            self.Individual['Boost']['Small pads stolen'] = targetUser['stats']['boost']['count_stolen_small']

            # Time
            self.Individual['Boost']['0 boost']['time'] = targetUser['stats']['boost']['time_zero_boost']
            self.Individual['Boost']['100 boost']['time'] = targetUser['stats']['boost']['time_full_boost']
            self.Individual['Boost']['0-25% boost']['time'] = targetUser['stats']['boost']['time_boost_0_25']
            self.Individual['Boost']['25-50% boost']['time'] = targetUser['stats']['boost']['time_boost_25_50']
            self.Individual['Boost']['50-75% boost']['time'] = targetUser['stats']['boost']['time_boost_50_75']
            self.Individual['Boost']['75-100% boost']['time'] = targetUser['stats']['boost']['time_boost_75_100']

            # Percent
            self.Individual['Boost']['0 boost']['percent'] = targetUser['stats']['boost']['percent_zero_boost']
            self.Individual['Boost']['100 boost']['percent'] = targetUser['stats']['boost']['percent_full_boost']
            self.Individual['Boost']['0-25% boost']['percent'] = targetUser['stats']['boost']['percent_boost_0_25']
            self.Individual['Boost']['25-50% boost']['percent'] = targetUser['stats']['boost']['percent_boost_25_50']
            self.Individual['Boost']['50-75% boost']['percent'] = targetUser['stats']['boost']['percent_boost_50_75']
            self.Individual['Boost']['75-100% boost']['percent'] = targetUser['stats']['boost']['percent_boost_75_100']

            # Positioning stats
            # Percentages
            self.Individual['Positioning']['Most back']['percent'] = targetUser['stats']['positioning']['percent_most_back']
            self.Individual['Positioning']['Most forward']['percent'] = targetUser['stats']['positioning']['percent_most_forward']
            self.Individual['Positioning']['Defensive third']['percent'] = targetUser['stats']['positioning']['percent_defensive_third']
            self.Individual['Positioning']['Neutral third']['percent'] = targetUser['stats']['positioning']['percent_neutral_third']
            self.Individual['Positioning']['Offensive third']['percent'] = targetUser['stats']['positioning']['percent_offensive_third']
            self.Individual['Positioning']['Defensive half']['percent'] = targetUser['stats']['positioning']['percent_defensive_half']
            self.Individual['Positioning']['Offensive half']['percent'] = targetUser['stats']['positioning']['percent_offensive_half']
            self.Individual['Positioning']['Closest to ball']['percent'] = targetUser['stats']['positioning']['percent_closest_to_ball']
            self.Individual['Positioning']['Farthest from ball']['percent'] = targetUser['stats']['positioning']['percent_farthest_from_ball']
            self.Individual['Positioning']['Behind the ball']['percent'] = targetUser['stats']['positioning']['percent_behind_ball']
            self.Individual['Positioning']['In front of the ball']['percent'] = targetUser['stats']['positioning']['percent_infront_ball']

            # Absolutes
            self.Individual['Positioning']['Most back']['time'] = targetUser['stats']['positioning']['time_most_back']
            self.Individual['Positioning']['Most forward']['time'] = targetUser['stats']['positioning']['time_most_forward']
            self.Individual['Positioning']['Defensive third']['time'] = targetUser['stats']['positioning']['time_defensive_third']
            self.Individual['Positioning']['Neutral third']['time'] = targetUser['stats']['positioning']['time_neutral_third']
            self.Individual['Positioning']['Offensive third']['time'] = targetUser['stats']['positioning']['time_offensive_third']
            self.Individual['Positioning']['Defensive half']['time'] = targetUser['stats']['positioning']['time_defensive_half']
            self.Individual['Positioning']['Offensive half']['time'] = targetUser['stats']['positioning']['time_offensive_half']
            self.Individual['Positioning']['Closest to ball']['time'] = targetUser['stats']['positioning']['time_closest_to_ball']
            self.Individual['Positioning']['Farthest from ball']['time'] = targetUser['stats']['positioning']['time_farthest_from_ball']
            self.Individual['Positioning']['Behind the ball']['time'] = targetUser['stats']['positioning']['time_behind_ball']
            self.Individual['Positioning']['In front of the ball']['time'] = targetUser['stats']['positioning']['time_infront_ball']

            # Averages
            if(self.Player_Team_Size > 1):
                self.Individual['Positioning']['Average distance to teammates'] = targetUser['stats']['positioning']['avg_distance_to_mates']
            self.Individual['Positioning']['Average distance to the ball'] = targetUser['stats']['positioning']['avg_distance_to_ball']
            self.Individual['Positioning']['Average distance to the ball in possesion'] = targetUser[
                'stats']['positioning']['avg_distance_to_ball_possession']
            self.Individual['Positioning']['Average distance to the ball out of possesion'] = targetUser[
                'stats']['positioning']['avg_distance_to_ball_no_possession']

            # Movement stats
            # Averages
            self.Individual['Movement']['Average speed']['absolute'] = targetUser['stats']['movement']['avg_speed']
            self.Individual['Movement']['Average speed']['percent'] = targetUser['stats']['movement']['avg_speed_percentage']
            self.Individual['Movement']['Average powerslide duration'] = targetUser['stats']['movement']['avg_powerslide_duration']
            self.Individual['Movement']['Total distance travelled'] = targetUser['stats']['movement']['total_distance']*3.653/1000
            self.Individual['Movement']['Powerslide total duration'] = targetUser['stats']['movement']['time_powerslide']
            self.Individual['Movement']['Number of powerslides'] = targetUser['stats']['movement']['count_powerslide']

            self.Individual['Movement']['Supersonic']['percent'] = targetUser['stats']['movement']['percent_supersonic_speed']
            self.Individual['Movement']['Boost speed']['percent'] = targetUser['stats']['movement']['percent_boost_speed']
            self.Individual['Movement']['Slow speed']['percent'] = targetUser['stats']['movement']['percent_slow_speed']
            self.Individual['Movement']['On the ground']['percent'] = targetUser['stats']['movement']['percent_ground']
            self.Individual['Movement']['In low air']['percent'] = targetUser['stats']['movement']['percent_low_air']
            self.Individual['Movement']['In high air']['percent'] = targetUser['stats']['movement']['percent_high_air']

            self.Individual['Movement']['Supersonic']['time'] = targetUser['stats']['movement']['time_supersonic_speed']
            self.Individual['Movement']['Boost speed']['time'] = targetUser['stats']['movement']['time_boost_speed']
            self.Individual['Movement']['Slow speed']['time'] = targetUser['stats']['movement']['time_slow_speed']
            self.Individual['Movement']['On the ground']['time'] = targetUser['stats']['movement']['time_ground']
            self.Individual['Movement']['In low air']['time'] = targetUser['stats']['movement']['time_low_air']
            self.Individual['Movement']['In high air']['time'] = targetUser['stats']['movement']['time_high_air']

        #print(json.dumps(self.__dict__, indent=4, default=str))

    # End of populateFromGame
# End of GameStat


graphChoices = [
    "Win/Losses",
    "Time Played",
    "Overtime",
    {
        "Team": [
            "Goals For/Against",
            "Assists",
            "Shots",
            "Demos Inflicted/Received",
            "Total Score",
            "Average Score",
            "Average Shooting Percent",
            "Time in possesion",
            "Time ball in defensive half"
        ],
        "Opposition": [
            "Goals For/Against",
            "Assists",
            "Shots",
            "Demos Inflicted/Received",
            "Total Score",
            "Average Score",
            "Average Shooting Percent",
            "Time in possesion",
            "Time ball in defensive half"
        ],
        "Individual": [
            {
                "General": [
                    "Goals",
                    "Saves",
                    "Assists",
                    "Shots",
                    "Demos Inflicted/Received",
                    "Score",
                    "Shooting Percent",
                    "Goals Against Whilst Last Defender",
                ],
            },
            {
                "Boost": [
                    "Average boost used/collected per minute",
                    "Average boost amount",
                    "Amount of boost used at supersonic",
                    "Amount of boost collected",
                    "Big pads taken",
                    "Big pads stolen",
                    "Small pads taken",
                    "Small pads stolen",
                    "Boost overfill",
                    "Stolen overfill",
                    "0 boost",
                    "100 boost",
                    "0-25% boost",
                    "25-50% boost",
                    "50-75% boost",
                    "75-100% boost"
                ],
            },
            {
                "Positioning": [
                    "Average distance to teammates",
                    "Average distance to the ball",
                    "Average distance to the ball in possesion",
                    "Average distance to the ball out of possesion",
                    "Most back",
                    "Most forward",
                    "Defensive third",
                    "Neutral third",
                    "Offensive third",
                    "Defensive half",
                    "Offensive half",
                    "Closest to ball",
                    "Farthest from ball",
                    "Behind the ball",
                    "In front of the ball"
                ],
            },
            {
                "Movement": [
                    "Average speed",
                    "Average powerslide duration",
                    "Powerslide total duration",
                    "Total distance travelled",
                    "Number of powerslides",
                    "Supersonic",
                    "Boost speed",
                    "Slow speed",
                    "On the ground",
                    "In low air",
                    "In high air"
                ]
            }
        ]
    },
]
