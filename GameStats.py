from dateutil.parser import parse
from datetime import timezone, datetime, timedelta
import json


class GameStat():
    def __init__(self):
        self.Win = -1
        self.Time_Played = 0
        self.Overtime = 0
        self.Orange = {"Goals For": 0}
        self.Blue = {"Goals For": 0}

        self.Date = 0
        self.Bar_Width = 0
        self.Win_Loss_Color = 'g'
        self.Target_Player_Team = 'Orange'
        self.Opposition_Team = 'Blue'
        self.Player_Team_Size = 0
        self.Opposition_Team_Size = 0
        self.Match_GUID = ""
        self.mode = "2v2"

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

        self.Team = teamStructure

        self.Opposition = teamStructure

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

    def populateFromGame(self, replay, replayResult, userName):
        self.mode = replayResult['playlist_id']

        self.Match_GUID = replayResult['match_guid']

        orange = replayResult.get('orange', None)
        blue = replayResult.get('blue', None)

        orangeStats = orange.get('stats', None)
        orangeStatsCore = orangeStats.get('core', None)

        blueStats = blue.get('stats', None)
        blueStatsCore = blueStats.get('core', None)

        self.Orange['Goals For'] = orangeStatsCore.get('goals', int(0))
        self.Blue['Goals For'] = blueStatsCore.get('goals', int(0))

        targetUser = None
        for player in blue.get('players', []):
            if(player['name'] == userName):
                self.Win = 1 if self.Blue['Goals For'] < self.Orange['Goals For'] else -1
                self.Win_Loss_Color = 'g' if self.Blue['Goals For'] < self.Orange['Goals For'] else 'r'
                self.Target_Player_Team = "Blue"
                targetUser = player

        for player in orange.get('players', []):
            if(player['name'] == userName):
                self.Win = 1 if self.Orange['Goals For'] < self.Blue['Goals For'] else -1
                self.Win_Loss_Color = 'g' if self.Orange['Goals For'] < self.Blue['Goals For'] else 'r'
                self.Target_Player_Team = "Orange"
                targetUser = player

        self.Opposition_Team = "Orange" if not "Orange" in self.Target_Player_Team else "Blue"

        self.Overtime = replayResult.get('overtime_seconds', int(0))

        self.Date = parse(replayResult.get('date',
                          str(datetime.now()))).astimezone(timezone.utc)
        self.Time_Played = replayResult.get('duration', int(0))
        self.EndDate = self.Date + timedelta(seconds=self.Time_Played)

        self.Bar_Width = self.Time_Played*0.00001157407

        targetPlayerTeam = replayResult.get(
            self.Target_Player_Team.lower(), None)
        oppositionTeam = replayResult.get(self.Opposition_Team.lower(), None)

        self.Player_Team_Size = len(targetPlayerTeam.get('players', []))
        self.Opposition_Team_Size = len(oppositionTeam.get('players', []))

        targetPlayerTeamStats = targetPlayerTeam.get('stats', None)
        targetPlayerTeamStatsCore = targetPlayerTeamStats.get('core', None)
        self.Team['Goals For'] = targetPlayerTeamStatsCore.get('goals', int(0))

        self.Team['Goals Against'] = targetPlayerTeamStatsCore.get(
            'goals_against', int(0))

        self.Team['Assists'] = targetPlayerTeamStatsCore.get('assists', int(0))

        self.Team['Shots'] = targetPlayerTeamStatsCore.get('shots', int(0))

        self.Team['Saves'] = targetPlayerTeamStatsCore.get('saves', int(0))

        targetPlayerTeamStatsDemo = targetPlayerTeamStats.get('demo', None)

        self.Team['Demos Inflicted'] = targetPlayerTeamStatsDemo.get(
            'inflicted', int(0))

        self.Team['Demos Received'] = targetPlayerTeamStatsDemo.get(
            'taken', int(0))

        self.Team['Total Score'] = targetPlayerTeamStatsCore.get(
            'score', int(0))

        self.Team['Average Score'] = self.Team['Total Score'] / \
            self.Player_Team_Size if self.Player_Team_Size > 0 else 0

        self.Team['Average Shooting Percent'] = targetPlayerTeamStatsCore.get(
            'shooting_percentage', int(0))

        targetPlayerTeamStatsBall = targetPlayerTeamStats.get('ball', None)

        self.Team['Time in possesion'] = targetPlayerTeamStatsBall.get(
            'possession_time', int(0))

        self.Team['Time ball in defensive half'] = targetPlayerTeamStatsBall.get(
            'time_in_side', int(0))

        oppositionTeamStats = oppositionTeam.get('stats', None)
        oppositionTeamStatsCore = oppositionTeamStats.get('core', None)

        self.Opposition['Goals For'] = oppositionTeamStatsCore.get(
            'goals', int(0))
        self.Opposition['Goals Against'] = oppositionTeamStatsCore.get(
            'goals_against', int(0))

        self.Opposition['Assists'] = oppositionTeamStatsCore.get(
            'assists', int(0))

        self.Opposition['Shots'] = oppositionTeamStatsCore.get('shots', int(0))

        oppositionTeamStatsDemo = oppositionTeamStats.get('demo', None)

        self.Opposition['Demos Inflicted'] = oppositionTeamStatsDemo.get(
            'inflicted', int(0))

        self.Opposition['Demos Received'] = oppositionTeamStatsDemo.get(
            'taken', int(0))

        self.Opposition['Total Score'] = oppositionTeamStatsCore.get(
            'score', int(0))

        self.Opposition['Average Score'] = self.Opposition['Total Score'] / \
            self.Opposition_Team_Size if self.Opposition_Team_Size > 0 else 0

        self.Opposition['Average Shooting Percent'] = oppositionTeamStatsCore.get(
            'shooting_percentage', int(0))

        oppositionTeamStatsBall = oppositionTeamStats.get('ball', None)

        self.Opposition['Time in possesion'] = oppositionTeamStatsBall.get(
            'possession_time', int(0))

        self.Opposition['Time ball in defensive half'] = oppositionTeamStatsBall.get(
            'time_in_side', int(0))

        if(targetUser is not None):
            targetUserStats = targetUser.get('stats', None)
            targetUserStatsCore = targetUserStats.get('core', None)
            targetUserStatsDemo = targetUserStats.get('demo', None)

            self.Individual['General']['Goals'] = targetUserStatsCore.get(
                'goals', int(0))
            self.Individual['General']['Saves'] = targetUserStatsCore.get(
                'saves', int(0))
            self.Individual['General']['Assists'] = targetUserStatsCore.get(
                'assists', int(0))
            self.Individual['General']['Shots'] = targetUserStatsCore.get(
                'shots', int(0))
            self.Individual['General']['Demos Inflicted'] = targetUserStatsDemo.get(
                'inflicted', int(0))
            self.Individual['General']['Demos Received'] = targetUserStatsDemo.get(
                'taken', int(0))
            self.Individual['General']['Score'] = targetUserStatsCore.get(
                'score', int(0))
            self.Individual['General']['Shooting Percent'] = targetUserStatsCore.get(
                'shooting_percentage', int(0))
            self.Individual['General']['MVP'] = targetUserStatsCore.get(
                'mvp', False)

            targetUserStatsBoost = targetUserStats.get('boost', None)
            self.Individual['Boost']['Average boost used per minute'] = targetUserStatsBoost.get(
                'bpm', int(0))
            self.Individual['Boost']['Average boost collected per minute'] = targetUserStatsBoost.get(
                'bcpm', int(0))
            self.Individual['Boost']['Average boost amount'] = targetUserStatsBoost.get(
                'avg_amount', int(0))
            self.Individual['Boost']['Amount of boost collected'] = targetUserStatsBoost.get(
                'amount_collected', int(0))
            self.Individual['Boost']['Amount of boost used at supersonic'] = targetUserStatsBoost.get(
                'amount_used_while_supersonic', int(0))
            self.Individual['Boost']['Total stolen'] = targetUserStatsBoost.get(
                'amount_stolen', int(0))
            self.Individual['Boost']['Total collected from big pads'] = targetUserStatsBoost.get(
                'amount_collected_big', int(0))
            self.Individual['Boost']['Total stolen from big pads'] = targetUserStatsBoost.get(
                'amount_stolen_big', int(0))
            self.Individual['Boost']['Total collected from small pads'] = targetUserStatsBoost.get(
                'amount_collected_small', int(0))
            self.Individual['Boost']['Total stolen from small pads'] = targetUserStatsBoost.get(
                'amount_stolen_small', int(0))
            self.Individual['Boost']['Boost overfill'] = targetUserStatsBoost.get(
                'amount_overfill', int(0))
            self.Individual['Boost']['Stolen overfill'] = targetUserStatsBoost.get(
                'amount_overfill_stolen', int(0))

            self.Individual['Boost']['Big pads taken'] = targetUserStatsBoost.get(
                'count_collected_big', int(0))
            self.Individual['Boost']['Big pads stolen'] = targetUserStatsBoost.get(
                'count_stolen_big', int(0))
            self.Individual['Boost']['Small pads taken'] = targetUserStatsBoost.get(
                'count_collected_small', int(0))
            self.Individual['Boost']['Small pads stolen'] = targetUserStatsBoost.get(
                'count_stolen_small', int(0))

            self.Individual['Boost']['0 boost']['time'] = targetUserStatsBoost.get(
                'time_zero_boost', int(0))
            self.Individual['Boost']['100 boost']['time'] = targetUserStatsBoost.get(
                'time_full_boost', int(0))
            self.Individual['Boost']['0-25% boost']['time'] = targetUserStatsBoost.get(
                'time_boost_0_25', int(0))
            self.Individual['Boost']['25-50% boost']['time'] = targetUserStatsBoost.get(
                'time_boost_25_50', int(0))
            self.Individual['Boost']['50-75% boost']['time'] = targetUserStatsBoost.get(
                'time_boost_50_75', int(0))
            self.Individual['Boost']['75-100% boost']['time'] = targetUserStatsBoost.get(
                'time_boost_75_100', int(0))

            self.Individual['Boost']['0 boost']['percent'] = targetUserStatsBoost.get(
                'percent_zero_boost', int(0))
            self.Individual['Boost']['100 boost']['percent'] = targetUserStatsBoost.get(
                'percent_full_boost', int(0))
            self.Individual['Boost']['0-25% boost']['percent'] = targetUserStatsBoost.get(
                'percent_boost_0_25', int(0))
            self.Individual['Boost']['25-50% boost']['percent'] = targetUserStatsBoost.get(
                'percent_boost_25_50', int(0))
            self.Individual['Boost']['50-75% boost']['percent'] = targetUserStatsBoost.get(
                'percent_boost_50_75', int(0))
            self.Individual['Boost']['75-100% boost']['percent'] = targetUserStatsBoost.get(
                'percent_boost_75_100', int(0))

            targetUserStatsPositioning = targetUserStats.get(
                'positioning', None)

            self.Individual['Positioning']['Most back']['percent'] = targetUserStatsPositioning.get(
                'percent_most_back', int(0))
            self.Individual['Positioning']['Most forward']['percent'] = targetUserStatsPositioning.get(
                'percent_most_forward', int(0))
            self.Individual['Positioning']['Defensive third']['percent'] = targetUserStatsPositioning.get(
                'percent_defensive_third', int(0))
            self.Individual['Positioning']['Neutral third']['percent'] = targetUserStatsPositioning.get(
                'percent_neutral_third', int(0))
            self.Individual['Positioning']['Offensive third']['percent'] = targetUserStatsPositioning.get(
                'percent_offensive_third', int(0))
            self.Individual['Positioning']['Defensive half']['percent'] = targetUserStatsPositioning.get(
                'percent_defensive_half', int(0))
            self.Individual['Positioning']['Offensive half']['percent'] = targetUserStatsPositioning.get(
                'percent_offensive_half', int(0))
            self.Individual['Positioning']['Closest to ball']['percent'] = targetUserStatsPositioning.get(
                'percent_closest_to_ball', int(0))
            self.Individual['Positioning']['Farthest from ball']['percent'] = targetUserStatsPositioning.get(
                'percent_farthest_from_ball', int(0))
            self.Individual['Positioning']['Behind the ball']['percent'] = targetUserStatsPositioning.get(
                'percent_behind_ball', int(0))
            self.Individual['Positioning']['In front of the ball']['percent'] = targetUserStatsPositioning.get(
                'percent_infront_ball', int(0))

            self.Individual['Positioning']['Most back']['time'] = targetUserStatsPositioning.get(
                'time_most_back', int(0))
            self.Individual['Positioning']['Most forward']['time'] = targetUserStatsPositioning.get(
                'time_most_forward', int(0))
            self.Individual['Positioning']['Defensive third']['time'] = targetUserStatsPositioning.get(
                'time_defensive_third', int(0))
            self.Individual['Positioning']['Neutral third']['time'] = targetUserStatsPositioning.get(
                'time_neutral_third', int(0))
            self.Individual['Positioning']['Offensive third']['time'] = targetUserStatsPositioning.get(
                'time_offensive_third', int(0))
            self.Individual['Positioning']['Defensive half']['time'] = targetUserStatsPositioning.get(
                'time_defensive_half', int(0))
            self.Individual['Positioning']['Offensive half']['time'] = targetUserStatsPositioning.get(
                'time_offensive_half', int(0))
            self.Individual['Positioning']['Closest to ball']['time'] = targetUserStatsPositioning.get(
                'time_closest_to_ball', int(0))
            self.Individual['Positioning']['Farthest from ball']['time'] = targetUserStatsPositioning.get(
                'time_farthest_from_ball', int(0))
            self.Individual['Positioning']['Behind the ball']['time'] = targetUserStatsPositioning.get(
                'time_behind_ball', int(0))
            self.Individual['Positioning']['In front of the ball']['time'] = targetUserStatsPositioning.get(
                'time_infront_ball', int(0))

            if(self.Player_Team_Size > 1):
                self.Individual['Positioning']['Average distance to teammates'] = targetUserStatsPositioning.get(
                    'avg_distance_to_mates', int(0))
            self.Individual['Positioning']['Average distance to the ball'] = targetUserStatsPositioning.get(
                'avg_distance_to_ball', int(0))
            self.Individual['Positioning']['Average distance to the ball in possesion'] = targetUserStatsPositioning.get(
                'avg_distance_to_ball_possession', int(0))
            self.Individual['Positioning']['Average distance to the ball out of possesion'] = targetUserStatsPositioning.get(
                'avg_distance_to_ball_no_possession', int(0))

            targetUserStatsMovement = targetUserStats.get('movement', None)

            self.Individual['Movement']['Average speed']['absolute'] = targetUserStatsMovement.get(
                'avg_speed', int(0))
            self.Individual['Movement']['Average speed']['percent'] = targetUserStatsMovement.get(
                'avg_speed_percentage', int(0))
            self.Individual['Movement']['Average powerslide duration'] = targetUserStatsMovement.get(
                'avg_powerslide_duration', int(0))
            self.Individual['Movement']['Total distance travelled'] = targetUserStatsMovement.get(
                'total_distance', int(0))*3.653/1000
            self.Individual['Movement']['Powerslide total duration'] = targetUserStatsMovement.get(
                'time_powerslide', int(0))
            self.Individual['Movement']['Number of powerslides'] = targetUserStatsMovement.get(
                'count_powerslide', int(0))

            self.Individual['Movement']['Supersonic']['percent'] = targetUserStatsMovement.get(
                'percent_supersonic_speed', int(0))
            self.Individual['Movement']['Boost speed']['percent'] = targetUserStatsMovement.get(
                'percent_boost_speed', int(0))
            self.Individual['Movement']['Slow speed']['percent'] = targetUserStatsMovement.get(
                'percent_slow_speed', int(0))
            self.Individual['Movement']['On the ground']['percent'] = targetUserStatsMovement.get(
                'percent_ground', int(0))
            self.Individual['Movement']['In low air']['percent'] = targetUserStatsMovement.get(
                'percent_low_air', int(0))
            self.Individual['Movement']['In high air']['percent'] = targetUserStatsMovement.get(
                'percent_high_air', int(0))

            self.Individual['Movement']['Supersonic']['time'] = targetUserStatsMovement.get(
                'time_supersonic_speed', int(0))
            self.Individual['Movement']['Boost speed']['time'] = targetUserStatsMovement.get(
                'time_boost_speed', int(0))
            self.Individual['Movement']['Slow speed']['time'] = targetUserStatsMovement.get(
                'time_slow_speed', int(0))
            self.Individual['Movement']['On the ground']['time'] = targetUserStatsMovement.get(
                'time_ground', int(0))
            self.Individual['Movement']['In low air']['time'] = targetUserStatsMovement.get(
                'time_low_air', int(0))
            self.Individual['Movement']['In high air']['time'] = targetUserStatsMovement.get(
                'time_high_air', int(0))

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
