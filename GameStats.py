from dateutil.parser import parse
from datetime import timezone, datetime, timedelta
import json


class GameStat():
    def __init__(self):
        self.Win = -1
        self.Loss = 1
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

        self.Team = {
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
            "Time in Possession": 0,
            "Time Ball in Defensive Half": 0
        }

        self.Opposition = {
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
            "Time in Possession": 0,
            "Time Ball in Defensive Half": 0
        }

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
                "Average Boost Used per Minute": 0,
                "Average Boost Collected per Minute": 0,
                "Average Boost Amount": 0,
                "Amount of Boost Used at Supersonic": 0,
                "Amount of Boost Collected": 0,
                "Big Pads Taken": 0,
                "Big Pads Stolen": 0,
                "Small Pads Taken": 0,
                "Small Pads Stolen": 0,
                "Boost Overfill": 0,
                "Stolen Overfill": 0,
                "0 Boost": {"time": 0, "percent": 0},
                "100 Boost": {"time": 0, "percent": 0},
                "0-25% Boost": {"time": 0, "percent": 0},
                "25-50% Boost": {"time": 0, "percent": 0},
                "50-75% Boost": {"time": 0, "percent": 0},
                "75-100% Boost": {"time": 0, "percent": 0},
            },
            "Positioning": {
                "Average Distance to Teammates": 0,
                "Average Distance to the Ball": 0,
                "Average Distance to the Ball in Possession": 0,
                "Average Distance to the Ball out of Possession": 0,
                "Most Back": {"time": 0, "percent": 0},
                "Most Forward": {"time": 0, "percent": 0},
                "Defensive Third": {"time": 0, "percent": 0},
                "Neutral Third": {"time": 0, "percent": 0},
                "Offensive Third": {"time": 0, "percent": 0},
                "Defensive Half": {"time": 0, "percent": 0},
                "Offensive Half": {"time": 0, "percent": 0},
                "Closest to Ball": {"time": 0, "percent": 0},
                "Farthest from Ball": {"time": 0, "percent": 0},
                "Behind the Ball": {"time": 0, "percent": 0},
                "In front of the Ball": {"time": 0, "percent": 0},
            },
            "Movement": {
                "Average Speed": {"absolute": 0, "percent": 0},
                "Average Powerslide Duration": 0,
                "Powerslide Total Duration": 0,
                "Total Distance Travelled": 0,
                "Number of Powerslides": 0,
                "Supersonic": {"time": 0, "percent": 0},
                "Boost Speed": {"time": 0, "percent": 0},
                "Slow Speed": {"time": 0, "percent": 0},
                "On the Ground": {"time": 0, "percent": 0},
                "In Low Air": {"time": 0, "percent": 0},
                "In High Air": {"time": 0, "percent": 0},
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

        self.targetUser = None
        for player in blue.get('players', []):
            if(player['name'] == userName):
                self.Win = 1 if self.Blue['Goals For'] > self.Orange['Goals For'] else 0
                self.Win_Loss_Color = 'g' if self.Win == 1 else 'r'
                self.Target_Player_Team = blue
                self.Opposition_Team = orange
                self.targetUser = player

        for player in orange.get('players', []):
            if(player['name'] == userName):
                self.Win = 1 if self.Orange['Goals For'] > self.Blue['Goals For'] else 0
                self.Win_Loss_Color = 'g' if self.Win == 1 else 'r'
                self.Target_Player_Team = orange
                self.Opposition_Team = blue
                self.targetUser = player

        self.Loss = 0 if self.Win == 1 else 1

        self.Overtime = replayResult.get('overtime_seconds', int(0))

        self.Date = parse(replayResult.get('date',
                          str(datetime.now()))).astimezone(timezone.utc)
        self.Time_Played = replayResult.get('duration', int(0))
        self.EndDate = self.Date + timedelta(seconds=self.Time_Played)

        self.Bar_Width = self.Time_Played*0.00001157407

        self.Player_Team_Size = len(self.Target_Player_Team.get('players', []))
        self.Opposition_Team_Size = len(
            self.Opposition_Team.get('players', []))

        targetPlayerTeamStats = self.Target_Player_Team.get('stats', None)
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

        self.Team['Time in Possession'] = targetPlayerTeamStatsBall.get(
            'possession_time', int(0))

        self.Team['Time Ball in Defensive Half'] = targetPlayerTeamStatsBall.get(
            'time_in_side', int(0))

        oppositionTeamStats = self.Opposition_Team.get('stats', None)
        oppositionTeamStatsCore = oppositionTeamStats.get('core', None)

        self.Opposition['Goals For'] = oppositionTeamStatsCore.get(
            'goals', int(0))
        self.Opposition['Goals Against'] = oppositionTeamStatsCore.get(
            'goals_against', int(0))

        self.Opposition['Assists'] = oppositionTeamStatsCore.get(
            'assists', int(0))

        self.Opposition['Shots'] = oppositionTeamStatsCore.get('shots', int(0))

        self.Opposition['Saves'] = oppositionTeamStatsCore.get('saves', int(0))

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

        self.Opposition['Time in Possession'] = oppositionTeamStatsBall.get(
            'possession_time', int(0))

        self.Opposition['Time Ball in Defensive Half'] = oppositionTeamStatsBall.get(
            'time_in_side', int(0))

        if(self.targetUser is not None):
            targetUserStats = self.targetUser.get('stats', None)
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
            self.Individual['Boost']['Average Boost Used per Minute'] = targetUserStatsBoost.get(
                'bpm', int(0))
            self.Individual['Boost']['Average Boost Collected per Minute'] = targetUserStatsBoost.get(
                'bcpm', int(0))
            self.Individual['Boost']['Average Boost Amount'] = targetUserStatsBoost.get(
                'avg_amount', int(0))
            self.Individual['Boost']['Amount of Boost Collected'] = targetUserStatsBoost.get(
                'amount_collected', int(0))
            self.Individual['Boost']['Amount of Boost Used at Supersonic'] = targetUserStatsBoost.get(
                'amount_used_while_supersonic', int(0))
            self.Individual['Boost']['Total Stolen'] = targetUserStatsBoost.get(
                'amount_stolen', int(0))
            self.Individual['Boost']['Total Collected from Big Pads'] = targetUserStatsBoost.get(
                'amount_collected_big', int(0))
            self.Individual['Boost']['Total Stolen from Big Pads'] = targetUserStatsBoost.get(
                'amount_stolen_big', int(0))
            self.Individual['Boost']['Total Collected from Small Pads'] = targetUserStatsBoost.get(
                'amount_collected_small', int(0))
            self.Individual['Boost']['Total Stolen from Small Pads'] = targetUserStatsBoost.get(
                'amount_stolen_small', int(0))
            self.Individual['Boost']['Boost Overfill'] = targetUserStatsBoost.get(
                'amount_overfill', int(0))
            self.Individual['Boost']['Stolen Overfill'] = targetUserStatsBoost.get(
                'amount_overfill_stolen', int(0))

            self.Individual['Boost']['Big Pads Taken'] = targetUserStatsBoost.get(
                'count_collected_big', int(0))
            self.Individual['Boost']['Big Pads Stolen'] = targetUserStatsBoost.get(
                'count_stolen_big', int(0))
            self.Individual['Boost']['Small Pads Taken'] = targetUserStatsBoost.get(
                'count_collected_small', int(0))
            self.Individual['Boost']['Small Pads Stolen'] = targetUserStatsBoost.get(
                'count_stolen_small', int(0))

            self.Individual['Boost']['0 Boost']['time'] = targetUserStatsBoost.get(
                'time_zero_boost', int(0))
            self.Individual['Boost']['100 Boost']['time'] = targetUserStatsBoost.get(
                'time_full_boost', int(0))
            self.Individual['Boost']['0-25% Boost']['time'] = targetUserStatsBoost.get(
                'time_boost_0_25', int(0))
            self.Individual['Boost']['25-50% Boost']['time'] = targetUserStatsBoost.get(
                'time_boost_25_50', int(0))
            self.Individual['Boost']['50-75% Boost']['time'] = targetUserStatsBoost.get(
                'time_boost_50_75', int(0))
            self.Individual['Boost']['75-100% Boost']['time'] = targetUserStatsBoost.get(
                'time_boost_75_100', int(0))

            self.Individual['Boost']['0 Boost']['percent'] = targetUserStatsBoost.get(
                'percent_zero_boost', int(0))
            self.Individual['Boost']['100 Boost']['percent'] = targetUserStatsBoost.get(
                'percent_full_boost', int(0))
            self.Individual['Boost']['0-25% Boost']['percent'] = targetUserStatsBoost.get(
                'percent_boost_0_25', int(0))
            self.Individual['Boost']['25-50% Boost']['percent'] = targetUserStatsBoost.get(
                'percent_boost_25_50', int(0))
            self.Individual['Boost']['50-75% Boost']['percent'] = targetUserStatsBoost.get(
                'percent_boost_50_75', int(0))
            self.Individual['Boost']['75-100% Boost']['percent'] = targetUserStatsBoost.get(
                'percent_boost_75_100', int(0))

            targetUserStatsPositioning = targetUserStats.get(
                'positioning', None)

            self.Individual['Positioning']['Most Back']['percent'] = targetUserStatsPositioning.get(
                'percent_most_back', int(0))
            self.Individual['Positioning']['Most Forward']['percent'] = targetUserStatsPositioning.get(
                'percent_most_forward', int(0))
            self.Individual['Positioning']['Defensive Third']['percent'] = targetUserStatsPositioning.get(
                'percent_defensive_Third', int(0))
            self.Individual['Positioning']['Neutral Third']['percent'] = targetUserStatsPositioning.get(
                'percent_neutral_Third', int(0))
            self.Individual['Positioning']['Offensive Third']['percent'] = targetUserStatsPositioning.get(
                'percent_offensive_Third', int(0))
            self.Individual['Positioning']['Defensive Half']['percent'] = targetUserStatsPositioning.get(
                'percent_defensive_Half', int(0))
            self.Individual['Positioning']['Offensive Half']['percent'] = targetUserStatsPositioning.get(
                'percent_offensive_Half', int(0))
            self.Individual['Positioning']['Closest to Ball']['percent'] = targetUserStatsPositioning.get(
                'percent_closest_to_ball', int(0))
            self.Individual['Positioning']['Farthest from Ball']['percent'] = targetUserStatsPositioning.get(
                'percent_farthest_from_ball', int(0))
            self.Individual['Positioning']['Behind the Ball']['percent'] = targetUserStatsPositioning.get(
                'percent_behind_ball', int(0))
            self.Individual['Positioning']['In front of the Ball']['percent'] = targetUserStatsPositioning.get(
                'percent_infront_ball', int(0))

            self.Individual['Positioning']['Most Back']['time'] = targetUserStatsPositioning.get(
                'time_most_back', int(0))
            self.Individual['Positioning']['Most Forward']['time'] = targetUserStatsPositioning.get(
                'time_most_forward', int(0))
            self.Individual['Positioning']['Defensive Third']['time'] = targetUserStatsPositioning.get(
                'time_defensive_Third', int(0))
            self.Individual['Positioning']['Neutral Third']['time'] = targetUserStatsPositioning.get(
                'time_neutral_Third', int(0))
            self.Individual['Positioning']['Offensive Third']['time'] = targetUserStatsPositioning.get(
                'time_offensive_Third', int(0))
            self.Individual['Positioning']['Defensive Half']['time'] = targetUserStatsPositioning.get(
                'time_defensive_Half', int(0))
            self.Individual['Positioning']['Offensive Half']['time'] = targetUserStatsPositioning.get(
                'time_offensive_Half', int(0))
            self.Individual['Positioning']['Closest to Ball']['time'] = targetUserStatsPositioning.get(
                'time_closest_to_ball', int(0))
            self.Individual['Positioning']['Farthest from Ball']['time'] = targetUserStatsPositioning.get(
                'time_farthest_from_ball', int(0))
            self.Individual['Positioning']['Behind the Ball']['time'] = targetUserStatsPositioning.get(
                'time_behind_ball', int(0))
            self.Individual['Positioning']['In front of the Ball']['time'] = targetUserStatsPositioning.get(
                'time_infront_ball', int(0))

            if(self.Player_Team_Size > 1):
                self.Individual['Positioning']['Average Distance to Teammates'] = targetUserStatsPositioning.get(
                    'avg_distance_to_mates', int(0))
            self.Individual['Positioning']['Average Distance to the Ball'] = targetUserStatsPositioning.get(
                'avg_distance_to_ball', int(0))
            self.Individual['Positioning']['Average Distance to the Ball in Possession'] = targetUserStatsPositioning.get(
                'avg_distance_to_ball_possession', int(0))
            self.Individual['Positioning']['Average Distance to the Ball out of Possession'] = targetUserStatsPositioning.get(
                'avg_distance_to_ball_no_possession', int(0))

            targetUserStatsMovement = targetUserStats.get('movement', None)

            self.Individual['Movement']['Average Speed']['absolute'] = targetUserStatsMovement.get(
                'avg_speed', int(0))
            self.Individual['Movement']['Average Speed']['percent'] = targetUserStatsMovement.get(
                'avg_speed_percentage', int(0))
            self.Individual['Movement']['Average Powerslide Duration'] = targetUserStatsMovement.get(
                'avg_powerslide_duration', int(0))
            self.Individual['Movement']['Total Distance Travelled'] = targetUserStatsMovement.get(
                'total_distance', int(0))*3.653/1000
            self.Individual['Movement']['Powerslide Total Duration'] = targetUserStatsMovement.get(
                'time_powerslide', int(0))
            self.Individual['Movement']['Number of Powerslides'] = targetUserStatsMovement.get(
                'count_powerslide', int(0))

            self.Individual['Movement']['Supersonic']['percent'] = targetUserStatsMovement.get(
                'percent_supersonic_speed', int(0))
            self.Individual['Movement']['Boost Speed']['percent'] = targetUserStatsMovement.get(
                'percent_boost_speed', int(0))
            self.Individual['Movement']['Slow Speed']['percent'] = targetUserStatsMovement.get(
                'percent_slow_speed', int(0))
            self.Individual['Movement']['On the Ground']['percent'] = targetUserStatsMovement.get(
                'percent_ground', int(0))
            self.Individual['Movement']['In Low Air']['percent'] = targetUserStatsMovement.get(
                'percent_low_air', int(0))
            self.Individual['Movement']['In High Air']['percent'] = targetUserStatsMovement.get(
                'percent_high_air', int(0))

            self.Individual['Movement']['Supersonic']['time'] = targetUserStatsMovement.get(
                'time_supersonic_speed', int(0))
            self.Individual['Movement']['Boost Speed']['time'] = targetUserStatsMovement.get(
                'time_boost_speed', int(0))
            self.Individual['Movement']['Slow Speed']['time'] = targetUserStatsMovement.get(
                'time_slow_speed', int(0))
            self.Individual['Movement']['On the Ground']['time'] = targetUserStatsMovement.get(
                'time_ground', int(0))
            self.Individual['Movement']['In Low Air']['time'] = targetUserStatsMovement.get(
                'time_low_air', int(0))
            self.Individual['Movement']['In High Air']['time'] = targetUserStatsMovement.get(
                'time_high_air', int(0))

    # End of populateFromGame
# End of GameStat
