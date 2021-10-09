SessionSidebar = [
    {
        "name": "SessionGeneralStatsPane",
        "type": "collapsible",
        "title": "General",
        "gridpos": (1, 0),
        "gridspan": (1, 4),
        "sticky": "nsew",
        "widgets": [
            {
                'name': 'SessionWins',
                "type": "widget",
                'title': 'Wins: ',
                'gridpos': (0, 0),
                'gridspan': (1, 1),
                'tags': "Wins",
                "precision": "g"
            },
            {
                'name': 'SessionLoss',
                'title': 'Losses: ',
                'gridpos': (0, 1),
                'gridspan': (1, 1),
                'tags': "Losses",
                "type": "widget",
                "precision": "g"
            },
            {
                'name': 'SessionWinPercent',
                'title': 'Win Rate: ',
                'gridpos': (0, 2),
                'gridspan': (1, 1),
                'tags': "WinRate",
                "type": "widget",
                "precision": "g"
            },
            {
                'name': 'SessionTimePlayed',
                'title': 'Total Time: ',
                'gridpos': (1, 0),
                'gridspan': (1, 2),
                'tags': "Time_Played",
                "type": "widget",
                "precision": "g"
            },
            {
                'name': 'SessionOvertimePlayed',
                'title': 'Overtime: ',
                'gridpos': (1, 2),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Overtime",
                "precision": "g"
            },
            {
                'name': 'SessionStart',
                'title': 'Started: ',
                'gridpos': (2, 0),
                'gridspan': (1, 2),
                "type": "widget",
                'tags': "StartDate",
                "precision": "g"
            },
            {
                'name': 'SessionEnd',
                'title': 'Ended: ',
                'gridpos': (2, 2),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "EndDate",
                "precision": "g"
            }]
    },
    {
        "name": "SessionIndividualStats",
        "type": "collapsible",
        "title": "Individual",
        "gridpos": (2, 0),
        "gridspan": (1, 4),
        "sticky": "nsew",
        "widgets": [
            {
                'name': 'SessionIndividualGoals',
                'title': 'Goals: ',
                'gridpos': (0, 0),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Goals",
                "precision": "g"
            },
            {
                'name': 'SessionIndividualSaves',
                'title': 'Saves: ',
                'gridpos': (0, 1),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Saves",
                "precision": "g"
            },
            {
                'name': 'SessionIndividualAssists',
                'title': 'Assists: ',
                'gridpos': (0, 2),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Assists",
                "precision": "g"
            },
            {
                'name': 'SessionIndividualShots',
                'title': 'Shots: ',
                'gridpos': (1, 0),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Shots",
                "precision": "g"
            },
            {
                'name': 'SessionIndividualShootingAccuracy',
                'title': 'Shooting Accuracy: ',
                'gridpos': (1, 1),
                'gridspan': (1, 2),
                "type": "widget",
                'tags': "Individual.General.Shooting Percent",
                "precision": ".2f"
            },
            {
                'name': 'SessionIndividualMVPs',
                'title': 'MVPs: ',
                'gridpos': (2, 0),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.MVP",
                "precision": "g"
            },
            {
                'name': 'SessionIndividualSore',
                'title': 'Score: ',
                'gridpos': (2, 2),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Score",
                "precision": "g"
            },
            {
                'name': 'SessionIndividualDemosReceived',
                'title': 'Demos Received: ',
                'gridpos': (3, 0),
                'gridspan': (1, 2),
                "type": "widget",
                'tags': "Individual.General.Demos Received",
                "precision": "g"
            },
            {
                'name': 'SessionIndividualDemosInflicted',
                'title': 'Demos Inflicted: ',
                'gridpos': (3, 2),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Demos Inflicted",
                "precision": "g"
            },
            {
                "name": "SessionIndividualBoost",
                "type": "collapsible",
                "title": "Boost",
                "gridpos": (4, 0),
                "gridspan": (1, 4),
                "sticky": "nsew",
                "widgets": [
                    {
                        'name': 'SessionIndividualBoostPM',
                        'title': 'BPM: ',
                        'gridpos': (0, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Average Boost Used per Minute",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostCPM',
                        'title': 'BCPM: ',
                        'gridpos': (0, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Average Boost Collected per Minute",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostAverage',
                        'title': 'Average Boost: ',
                        'gridpos': (0, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Average Boost Amount",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostZeroTwentyFive',
                        'title': '0-25%: ',
                        'gridpos': (1, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.0-25% Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostTwentyFiveFifty',
                        'title': '25-50%: ',
                        'gridpos': (1, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.25-50% Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostFiftySeventyFive',
                        'title': '50-75%: ',
                        'gridpos': (1, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.50-75% Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostSeventyFiveHundred',
                        'title': '75-100%: ',
                        'gridpos': (1, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.75-100% Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostZero',
                        'title': '0 Boost: ',
                        'gridpos': (2, 0),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Boost.0 Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostHundred',
                        'title': '100 Boost: ',
                        'gridpos': (2, 2),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Boost.100 Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostTotalCollected',
                        'title': 'Total Collected: ',
                        'gridpos': (3, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Amount of Boost Collected",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostTotalCollectedFromBP',
                        'title': 'From Big Pads: ',
                        'gridpos': (3, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total Collected from Big Pads",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostTotalCollectedFromSP',
                        'title': 'From Small Pads: ',
                        'gridpos': (3, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total Collected from Small Pads",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostOverfill',
                        'title': 'Overfill: ',
                        'gridpos': (3, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Boost Overfill",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostNumBP',
                        'title': '# of Big Pads: ',
                        'gridpos': (4, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Big Pads Taken",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostNumSP',
                        'title': '# of Small Pads: ',
                        'gridpos': (4, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Small Pads Taken",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostUsedAtSS',
                        'title': 'Used at Supersonic: ',
                        'gridpos': (4, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Big Pads Taken",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostTotalStolenSeperator',
                        'title': '',
                        'gridpos': (5, 1),
                        'gridspan': (1, 2),
                        "type": "Separator",
                        "sticky": "nsew",
                        "args":
                            [{"orient": "horizontal"}]
                    },
                    {
                        'name': 'SessionIndividualBoostTotalStolen',
                        'title': 'Total Stolen: ',
                        'gridpos': (6, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total Stolen",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostStolenFromBP',
                        'title': 'From Big Pads: ',
                        'gridpos': (6, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total Stolen from Big Pads",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostStolenFromSP',
                        'title': 'From Small Pads: ',
                        'gridpos': (6, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total Stolen from Small Pads",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostStolenOverfill',
                        'title': 'Overfill: ',
                        'gridpos': (6, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Stolen Overfill",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostStolenNumBP',
                        'title': '# of Big Pads: ',
                        'gridpos': (7, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Big Pads Stolen",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostStolenNumSP',
                        'title': '# of Small Pads: ',
                        'gridpos': (7, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Small Pads Stolen",
                        "precision": "g"
                    },
                ]
            },
            {
                "name": "SessionIndividualPositioning",
                "type": "collapsible",
                "title": "Positioning",
                "gridpos": (5, 0),
                "gridspan": (1, 4),
                "sticky": "nsew",
                "widgets": [
                    {
                        'name': 'SessionIndividualPositioningTitle',
                        'title': 'Average Distance to: ',
                        'gridpos': (0, 0),
                        'gridspan': (1, 1),
                        "type": "Label",
                        "sticky": "nw",
                        "args":
                            [{"text": "Average Distance to:"}]
                    },
                    {
                        'name': 'SessionIndividualPositioningTeammates',
                        'title': 'Teammates: ',
                        'gridpos': (1, 0),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Average Distance to Teammates",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallPos',
                        'title': 'Ball (Possesion): ',
                        'gridpos': (1, 2),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Average Distance to the Ball in Possession",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallOutOfPos',
                        'title': 'Ball (out of Possession): ',
                        'gridpos': (1, 4),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Average Distance to the Ball out of Possession",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningMostBack',
                        'title': 'Most Back: ',
                        'gridpos': (2, 1),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Most Back.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningMostForward',
                        'title': 'Most Forward: ',
                        'gridpos': (2, 3),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Most Forward.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningDefensiveHalf',
                        'title': 'Defensive Half: ',
                        'gridpos': (3, 1),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Defensive Half.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningOffensiveHalf',
                        'title': 'Offensive Half: ',
                        'gridpos': (3, 3),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Offensive Half.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningDefensiveThird',
                        'title': 'Defensive Third: ',
                        'gridpos': (4, 0),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Defensive Third.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningNeutralThird',
                        'title': 'Neutral Third: ',
                        'gridpos': (4, 2),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Neutral Third.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningOffensiveThird',
                        'title': 'Offensive Third: ',
                        'gridpos': (4, 4),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Offensive Third.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallTitle',
                        'title': 'Ball: ',
                        'gridpos': (5, 0),
                        'gridspan': (1, 1),
                        "type": "Label",
                        "sticky": "nw",
                        "args":
                            [{"text": "Ball:"}]
                    },
                    {
                        'name': 'SessionIndividualPositioningBallClosest',
                        'title': 'Closest: ',
                        'gridpos': (5, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.Closest to Ball.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallFarthest',
                        'title': 'Farthest: ',
                        'gridpos': (5, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.Farthest from Ball.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallBehind',
                        'title': 'Behind: ',
                        'gridpos': (5, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.Behind the Ball.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallInfront',
                        'title': 'Infront: ',
                        'gridpos': (5, 4),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.In front of the Ball.percent",
                        "precision": ".2f"
                    },
                ]
            },
            {
                "name": "SessionIndividualMovement",
                "type": "collapsible",
                "title": "Movement",
                "gridpos": (6, 0),
                "gridspan": (1, 4),
                "sticky": "nsew",
                "widgets": [
                    {
                        'name': 'SessionIndividualMovementAverageSpeed',
                        'title': 'Average Speed: ',
                        'gridpos': (0, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Average Speed.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementTotalDistance',
                        'title': 'Total Distance: ',
                        'gridpos': (0, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Total Distance Travelled",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementPowerslideDuration',
                        'title': 'Powerslide Duration: ',
                        'gridpos': (1, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Powerslide Total Duration",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementNumPowerslides',
                        'title': '# of Powerslides: ',
                        'gridpos': (1, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Number of Powerslides",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualMovementAveragePowerslidesLength',
                        'title': 'Average Powerslide Length: ',
                        'gridpos': (1, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Average Powerslide Duration",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementSlowSpeed',
                        'title': 'Slow: ',
                        'gridpos': (2, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Slow Speed.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementBoostSpeed',
                        'title': 'Boost: ',
                        'gridpos': (2, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Boost Speed.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementSupersonicSpeed',
                        'title': 'Supersonic: ',
                        'gridpos': (2, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Supersonic.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementGround',
                        'title': 'Ground: ',
                        'gridpos': (3, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.On the Ground.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementLowAir',
                        'title': 'Low Air: ',
                        'gridpos': (3, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.In Low Air.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementHighAir',
                        'title': 'High Air: ',
                        'gridpos': (3, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.In High Air.percent",
                        "precision": ".2f"
                    },
                ]
            }
        ]
    },
    {
        "name": "SessionTeamStats",
        "type": "collapsible",
        "title": "Team",
        "gridpos": (3, 0),
        "gridspan": (1, 4),
        "sticky": "nsew",
        "widgets": [
            {
                "name": "SessionTeamGoalsFor",
                "type": "widget",
                "title": "Goals For: ",
                "gridpos": (0, 0),
                "gridspan": (1, 1),
                "tags": "Team.Goals For",
                "precision": "g"
            },
            {
                "name": "SessionTeamGoalsAgainst",
                "type": "widget",
                "title": "Goals Against: ",
                "gridpos": (0, 1),
                "gridspan": (1, 1),
                "tags": "Team.Goals Against",
                "precision": "g"
            },
            {
                "name": "SessionTeamSaves",
                "type": "widget",
                "title": "Saves: ",
                "gridpos": (0, 2),
                "gridspan": (1, 1),
                "tags": "Team.Saves",
                "precision": "g"
            },
            {
                "name": "SessionTeamScore",
                "type": "widget",
                "title": "Score: ",
                "gridpos": (0, 3),
                "gridspan": (1, 1),
                "tags": "Team.Total Score",
                "precision": "g"
            },
            {
                "name": "SessionTeamShots",
                "type": "widget",
                "title": "Shots: ",
                "gridpos": (1, 0),
                "gridspan": (1, 1),
                "tags": "Team.Shots",
                "precision": "g"
            },
            {
                "name": "SessionTeamAssists",
                "type": "widget",
                "title": "Assists: ",
                "gridpos": (1, 2),
                "gridspan": (1, 1),
                "tags": "Team.Assists",
                "precision": "g"
            },
            {
                "name": "SessionTeamTimeInPossesion",
                "type": "widget",
                "title": "Time in Possession: ",
                "gridpos": (1, 3),
                "gridspan": (1, 1),
                "tags": "Team.Time in Possession",
                "precision": "g"
            },
            {
                "name": "SessionTeamAccuracy",
                "type": "widget",
                "title": "Shooting Accuracy: ",
                "gridpos": (2, 0),
                "gridspan": (1, 1),
                "tags": "Team.Average Shooting Percent",
                "precision": ".2f"
            },
            {
                "name": "SessionTeamDemosReceived",
                "type": "widget",
                "title": "Demos Received: ",
                "gridpos": (2, 1),
                "gridspan": (1, 1),
                "tags": "Team.Demos Received",
                "precision": "g"
            },
            {
                "name": "SessionTeamDemosInflicted",
                "type": "widget",
                "title": "Demos Inflicted: ",
                "gridpos": (2, 2),
                "gridspan": (1, 1),
                "tags": "Team.Demos Inflicted",
                "precision": "g"
            },
            {
                "name": "SessionTeamTimeDefensiveHalf",
                "type": "widget",
                "title": "Time Ball in Defensive Half: ",
                "gridpos": (2, 3),
                "gridspan": (1, 1),
                "tags": "Team.Time Ball in Defensive Half",
                "precision": "g"
            }
        ]
    },
    {
        "name": "SessionOppositionStats",
        "type": "collapsible",
        "title": "Opposition",
        "gridpos": (4, 0),
        "gridspan": (1, 4),
        "sticky": "nsew",
        "widgets": [
            {
                "name": "SessionOppositionGoalsFor",
                "type": "widget",
                "title": "Goals For: ",
                "gridpos": (0, 0),
                "gridspan": (1, 1),
                "tags": "Opposition.Goals For",
                "precision": "g"
            },
            {
                "name": "SessionOppositionGoalsAgainst",
                "type": "widget",
                "title": "Goals Against: ",
                "gridpos": (0, 1),
                "gridspan": (1, 1),
                "tags": "Opposition.Goals Against",
                "precision": "g"
            },
            {
                "name": "SessionOppositionSaves",
                "type": "widget",
                "title": "Saves: ",
                "gridpos": (0, 2),
                "gridspan": (1, 1),
                "tags": "Opposition.Saves",
                "precision": "g"
            },
            {
                "name": "SessionOppositionScore",
                "type": "widget",
                "title": "Score: ",
                "gridpos": (0, 3),
                "gridspan": (1, 1),
                "tags": "Opposition.Total Score",
                "precision": "g"
            },
            {
                "name": "SessionOppositionShots",
                "type": "widget",
                "title": "Shots: ",
                "gridpos": (1, 0),
                "gridspan": (1, 1),
                "tags": "Opposition.Shots",
                "precision": "g"
            },
            {
                "name": "SessionOppositionAssists",
                "type": "widget",
                "title": "Assists: ",
                "gridpos": (1, 2),
                "gridspan": (1, 1),
                "tags": "Opposition.Assists",
                "precision": "g"
            },
            {
                "name": "SessionOppositionTimeInPossesion",
                "type": "widget",
                "title": "Time in Possession: ",
                "gridpos": (1, 3),
                "gridspan": (1, 1),
                "tags": "Opposition.Time in Possession",
                "precision": "g"
            },
            {
                "name": "SessionOppositionAccuracy",
                "type": "widget",
                "title": "Shooting Accuracy: ",
                "gridpos": (2, 0),
                "gridspan": (1, 1),
                "tags": "Opposition.Average Shooting Percent",
                "precision": ".2f"
            },
            {
                "name": "SessionOppositionDemosReceived",
                "type": "widget",
                "title": "Demos Received: ",
                "gridpos": (2, 1),
                "gridspan": (1, 1),
                "tags": "Opposition.Demos Received",
                "precision": "g"
            },
            {
                "name": "SessionOppositionDemosInflicted",
                "type": "widget",
                "title": "Demos Inflicted: ",
                "gridpos": (2, 2),
                "gridspan": (1, 1),
                "tags": "Opposition.Demos Inflicted",
                "precision": "g"
            },
            {
                "name": "SessionOppositionTimeDefensiveHalf",
                "type": "widget",
                "title": "Time Ball in Defensive Half: ",
                "gridpos": (2, 3),
                "gridspan": (1, 1),
                "tags": "Opposition.Time Ball in Defensive Half",
                "precision": "g"
            }
        ]
    }
]

GameBar = [
    {
        "name": "GameGeneralStats",
        "type": "collapsible",
        "title": "General",
        "gridpos": (1, 0),
        "gridspan": (1, 4),
        "sticky": "nsew",
        "widgets": [
            {
                'name': 'GameWins',
                "type": "widget",
                'title': 'Win: ',
                'gridpos': (1, 0),
                'gridspan': (1, 1),
                'tags': "Win",
                "precision": "g"
            },
            {
                'name': 'GameLoss',
                'title': 'Loss: ',
                'gridpos': (1, 1),
                'gridspan': (1, 1),
                'tags': "Loss",
                "type": "widget",
                "precision": "g"
            },
            {
                'name': 'GameTimePlayed',
                'title': 'Total Time: ',
                'gridpos': (2, 0),
                'gridspan': (1, 2),
                'tags': "Time_Played",
                "type": "widget",
                "precision": "g"
            },
            {
                'name': 'GameOvertimePlayed',
                'title': 'Overtime: ',
                'gridpos': (2, 2),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Overtime",
                "precision": "g"
            },
            {
                'name': 'GameStart',
                'title': 'Date: ',
                'gridpos': (3, 0),
                'gridspan': (1, 2),
                "type": "widget",
                'tags': "Date",
                "precision": "g"
            },
        ],
    },
    {
        "name": "GameIndividualStats",
        "type": "collapsible",
        "title": "Individual",
        "gridpos": (2, 0),
        "gridspan": (1, 4),
        "sticky": "nsew",
        "widgets": [
            {
                'name': 'GameIndividualGoals',
                'title': 'Goals: ',
                'gridpos': (0, 0),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Goals",
                "precision": "g"
            },
            {
                'name': 'GameIndividualSaves',
                'title': 'Saves: ',
                'gridpos': (0, 1),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Saves",
                "precision": "g"
            },
            {
                'name': 'GameIndividualAssists',
                'title': 'Assists: ',
                'gridpos': (0, 2),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Assists",
                "precision": "g"
            },
            {
                'name': 'GameIndividualShots',
                'title': 'Shots: ',
                'gridpos': (1, 0),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Shots",
                "precision": "g"
            },
            {
                'name': 'GameIndividualShootingAccuracy',
                'title': 'Shooting Accuracy: ',
                'gridpos': (1, 1),
                'gridspan': (1, 2),
                "type": "widget",
                'tags': "Individual.General.Shooting Percent",
                "precision": ".2f"
            },
            {
                'name': 'GameIndividualMVPs',
                'title': 'MVPs: ',
                'gridpos': (2, 0),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.MVP",
                "precision": "g"
            },
            {
                'name': 'GameIndividualSore',
                'title': 'Score: ',
                'gridpos': (2, 2),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Score",
                "precision": "g"
            },
            {
                'name': 'GameIndividualDemosReceived',
                'title': 'Demos Received: ',
                'gridpos': (3, 0),
                'gridspan': (1, 2),
                "type": "widget",
                'tags': "Individual.General.Demos Received",
                "precision": "g"
            },
            {
                'name': 'GameIndividualDemosInflicted',
                'title': 'Demos Inflicted: ',
                'gridpos': (3, 2),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Demos Inflicted",
                "precision": "g"
            },
            {
                "name": "GameIndividualBoost",
                "type": "collapsible",
                "title": "Boost",
                "gridpos": (4, 0),
                "gridspan": (1, 4),
                "sticky": "nsew",
                "widgets": [
                    {
                        'name': 'GameIndividualBoostPM',
                        'title': 'BPM: ',
                        'gridpos': (0, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Average Boost Used per Minute",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualBoostCPM',
                        'title': 'BCPM: ',
                        'gridpos': (0, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Average Boost Collected per Minute",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualBoostAverage',
                        'title': 'Average Boost: ',
                        'gridpos': (0, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Average Boost Amount",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualBoostZeroTwentyFive',
                        'title': '0-25%: ',
                        'gridpos': (1, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.0-25% Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualBoostTwentyFiveFifty',
                        'title': '25-50%: ',
                        'gridpos': (1, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.25-50% Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualBoostFiftySeventyFive',
                        'title': '50-75%: ',
                        'gridpos': (1, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.50-75% Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualBoostSeventyFiveHundred',
                        'title': '75-100%: ',
                        'gridpos': (1, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.75-100% Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualBoostZero',
                        'title': '0 Boost: ',
                        'gridpos': (2, 0),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Boost.0 Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualBoostHundred',
                        'title': '100 Boost: ',
                        'gridpos': (2, 2),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Boost.100 Boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualBoostTotalCollected',
                        'title': 'Total Collected: ',
                        'gridpos': (3, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Amount of Boost Collected",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostTotalCollectedFromBP',
                        'title': 'From Big Pads: ',
                        'gridpos': (3, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total Collected from Big Pads",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostTotalCollectedFromSP',
                        'title': 'From Small Pads: ',
                        'gridpos': (3, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total Collected from Small Pads",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostOverfill',
                        'title': 'Overfill: ',
                        'gridpos': (3, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Boost Overfill",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostNumBP',
                        'title': '# of Big Pads: ',
                        'gridpos': (4, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Big Pads Taken",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostNumSP',
                        'title': '# of Small Pads: ',
                        'gridpos': (4, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Small Pads Taken",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostUsedAtSS',
                        'title': 'Used at Supersonic: ',
                        'gridpos': (4, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Big Pads Taken",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostTotalStolenSeperator',
                        'title': '',
                        'gridpos': (5, 1),
                        'gridspan': (1, 2),
                        "type": "Separator",
                        "sticky": "nsew",
                        "args":
                            [{"orient": "horizontal"}]
                    },
                    {
                        'name': 'GameIndividualBoostTotalStolen',
                        'title': 'Total Stolen: ',
                        'gridpos': (6, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total Stolen",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostStolenFromBP',
                        'title': 'From Big Pads: ',
                        'gridpos': (6, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total Stolen from Big Pads",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostStolenFromSP',
                        'title': 'From Small Pads: ',
                        'gridpos': (6, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total Stolen from Small Pads",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostStolenOverfill',
                        'title': 'Overfill: ',
                        'gridpos': (6, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Stolen Overfill",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostStolenNumBP',
                        'title': '# of Big Pads: ',
                        'gridpos': (7, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Big Pads Stolen",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualBoostStolenNumSP',
                        'title': '# of Small Pads: ',
                        'gridpos': (7, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Small Pads Stolen",
                        "precision": "g"
                    },
                ]
            },
            {
                "name": "GameIndividualPositioning",
                "type": "collapsible",
                "title": "Positioning",
                "gridpos": (5, 0),
                "gridspan": (1, 4),
                "sticky": "nsew",
                "widgets": [
                    {
                        'name': 'GameIndividualPositioningTitle',
                        'title': 'Average Distance to: ',
                        'gridpos': (0, 0),
                        'gridspan': (1, 1),
                        "type": "Label",
                        "sticky": "nw",
                        "args":
                            [{"text": "Average Distance to:"}]
                    },
                    {
                        'name': 'GameIndividualPositioningTeammates',
                        'title': 'Teammates: ',
                        'gridpos': (1, 0),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Average Distance to Teammates",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningBallPos',
                        'title': 'Ball (Possesion): ',
                        'gridpos': (1, 2),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Average Distance to the Ball in PosGame",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningBallOutOfPos',
                        'title': 'Ball (out of PosGame): ',
                        'gridpos': (1, 4),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Average Distance to the Ball out of PosGame",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningMostBack',
                        'title': 'Most Back: ',
                        'gridpos': (2, 1),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Most Back.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningMostForward',
                        'title': 'Most Forward: ',
                        'gridpos': (2, 3),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Most Forward.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningDefensiveHalf',
                        'title': 'Defensive Half: ',
                        'gridpos': (3, 1),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Defensive Half.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningOffensiveHalf',
                        'title': 'Offensive Half: ',
                        'gridpos': (3, 3),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Offensive Half.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningDefensiveThird',
                        'title': 'Defensive Third: ',
                        'gridpos': (4, 0),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Defensive Third.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningNeutralThird',
                        'title': 'Neutral Third: ',
                        'gridpos': (4, 2),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Neutral Third.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningOffensiveThird',
                        'title': 'Offensive Third: ',
                        'gridpos': (4, 4),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Offensive Third.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningBallTitle',
                        'title': 'Ball: ',
                        'gridpos': (5, 0),
                        'gridspan': (1, 1),
                        "type": "Label",
                        "sticky": "nw",
                        "args":
                            [{"text": "Ball:"}]
                    },
                    {
                        'name': 'GameIndividualPositioningBallClosest',
                        'title': 'Closest: ',
                        'gridpos': (5, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.Closest to Ball.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningBallFarthest',
                        'title': 'Farthest: ',
                        'gridpos': (5, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.Farthest from Ball.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningBallBehind',
                        'title': 'Behind: ',
                        'gridpos': (5, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.Behind the Ball.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualPositioningBallInfront',
                        'title': 'Infront: ',
                        'gridpos': (5, 4),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.In front of the Ball.percent",
                        "precision": ".2f"
                    },
                ]
            },
            {
                "name": "GameIndividualMovement",
                "type": "collapsible",
                "title": "Movement",
                "gridpos": (6, 0),
                "gridspan": (1, 4),
                "sticky": "nsew",
                "widgets": [
                    {
                        'name': 'GameIndividualMovementAverageSpeed',
                        'title': 'Average Speed: ',
                        'gridpos': (0, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Average Speed.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualMovementTotalDistance',
                        'title': 'Total Distance: ',
                        'gridpos': (0, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Total Distance Travelled",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualMovementPowerslideDuration',
                        'title': 'Powerslide Duration: ',
                        'gridpos': (1, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Powerslide Total Duration",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualMovementNumPowerslides',
                        'title': '# of Powerslides: ',
                        'gridpos': (1, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Number of Powerslides",
                        "precision": "g"
                    },
                    {
                        'name': 'GameIndividualMovementAveragePowerslidesLength',
                        'title': 'Average Powerslide Length: ',
                        'gridpos': (1, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Average Powerslide Duration",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualMovementSlowSpeed',
                        'title': 'Slow: ',
                        'gridpos': (2, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Slow Speed.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualMovementBoostSpeed',
                        'title': 'Boost: ',
                        'gridpos': (2, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Boost Speed.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualMovementSupersonicSpeed',
                        'title': 'Supersonic: ',
                        'gridpos': (2, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Supersonic.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualMovementGround',
                        'title': 'Ground: ',
                        'gridpos': (3, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.On the Ground.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualMovementLowAir',
                        'title': 'Low Air: ',
                        'gridpos': (3, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.In Low Air.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'GameIndividualMovementHighAir',
                        'title': 'High Air: ',
                        'gridpos': (3, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.In High Air.percent",
                        "precision": ".2f"
                    },
                ]
            }
        ]
    },
    {
        "name": "GameTeamStats",
        "type": "collapsible",
        "title": "Team",
        "gridpos": (3, 0),
        "gridspan": (1, 4),
        "sticky": "nsew",
        "widgets": [
            {
                "name": "GameTeamGoalsFor",
                "type": "widget",
                "title": "Goals For: ",
                "gridpos": (0, 0),
                "gridspan": (1, 1),
                "tags": "Team.Goals For",
                "precision": "g"
            },
            {
                "name": "GameTeamGoalsAgainst",
                "type": "widget",
                "title": "Goals Against: ",
                "gridpos": (0, 1),
                "gridspan": (1, 1),
                "tags": "Team.Goals Against",
                "precision": "g"
            },
            {
                "name": "GameTeamSaves",
                "type": "widget",
                "title": "Saves: ",
                "gridpos": (0, 2),
                "gridspan": (1, 1),
                "tags": "Team.Saves",
                "precision": "g"
            },
            {
                "name": "GameTeamScore",
                "type": "widget",
                "title": "Score: ",
                "gridpos": (0, 3),
                "gridspan": (1, 1),
                "tags": "Team.Total Score",
                "precision": "g"
            },
            {
                "name": "GameTeamShots",
                "type": "widget",
                "title": "Shots: ",
                "gridpos": (1, 0),
                "gridspan": (1, 1),
                "tags": "Team.Shots",
                "precision": "g"
            },
            {
                "name": "GameTeamAssists",
                "type": "widget",
                "title": "Assists: ",
                "gridpos": (1, 2),
                "gridspan": (1, 1),
                "tags": "Team.Assists",
                "precision": "g"
            },
            {
                "name": "GameTeamTimeInPossesion",
                "type": "widget",
                "title": "Time in PosGame: ",
                "gridpos": (1, 3),
                "gridspan": (1, 1),
                "tags": "Team.Time in PosGame",
                "precision": "g"
            },
            {
                "name": "GameTeamAccuracy",
                "type": "widget",
                "title": "Shooting Accuracy: ",
                "gridpos": (2, 0),
                "gridspan": (1, 1),
                "tags": "Team.Average Shooting Percent",
                "precision": ".2f"
            },
            {
                "name": "GameTeamDemosReceived",
                "type": "widget",
                "title": "Demos Received: ",
                "gridpos": (2, 1),
                "gridspan": (1, 1),
                "tags": "Team.Demos Received",
                "precision": "g"
            },
            {
                "name": "GameTeamDemosInflicted",
                "type": "widget",
                "title": "Demos Inflicted: ",
                "gridpos": (2, 2),
                "gridspan": (1, 1),
                "tags": "Team.Demos Inflicted",
                "precision": "g"
            },
            {
                "name": "GameTeamTimeDefensiveHalf",
                "type": "widget",
                "title": "Time Ball in Defensive Half: ",
                "gridpos": (2, 3),
                "gridspan": (1, 1),
                "tags": "Team.Time Ball in Defensive Half",
                "precision": "g"
            }
        ]
    },
    {
        "name": "GameOppositionStats",
        "type": "collapsible",
        "title": "Opposition",
        "gridpos": (4, 0),
        "gridspan": (1, 4),
        "sticky": "nsew",
        "widgets": [
            {
                "name": "GameOppositionGoalsFor",
                "type": "widget",
                "title": "Goals For: ",
                "gridpos": (0, 0),
                "gridspan": (1, 1),
                "tags": "Opposition.Goals For",
                "precision": "g"
            },
            {
                "name": "GameOppositionGoalsAgainst",
                "type": "widget",
                "title": "Goals Against: ",
                "gridpos": (0, 1),
                "gridspan": (1, 1),
                "tags": "Opposition.Goals Against",
                "precision": "g"
            },
            {
                "name": "GameOppositionSaves",
                "type": "widget",
                "title": "Saves: ",
                "gridpos": (0, 2),
                "gridspan": (1, 1),
                "tags": "Opposition.Saves",
                "precision": "g"
            },
            {
                "name": "GameOppositionScore",
                "type": "widget",
                "title": "Score: ",
                "gridpos": (0, 3),
                "gridspan": (1, 1),
                "tags": "Opposition.Total Score",
                "precision": "g"
            },
            {
                "name": "GameOppositionShots",
                "type": "widget",
                "title": "Shots: ",
                "gridpos": (1, 0),
                "gridspan": (1, 1),
                "tags": "Opposition.Shots",
                "precision": "g"
            },
            {
                "name": "GameOppositionAssists",
                "type": "widget",
                "title": "Assists: ",
                "gridpos": (1, 2),
                "gridspan": (1, 1),
                "tags": "Opposition.Assists",
                "precision": "g"
            },
            {
                "name": "GameOppositionTimeInPossesion",
                "type": "widget",
                "title": "Time in PosGame: ",
                "gridpos": (1, 3),
                "gridspan": (1, 1),
                "tags": "Opposition.Time in PosGame",
                "precision": "g"
            },
            {
                "name": "GameOppositionAccuracy",
                "type": "widget",
                "title": "Shooting Accuracy: ",
                "gridpos": (2, 0),
                "gridspan": (1, 1),
                "tags": "Opposition.Average Shooting Percent",
                "precision": ".2f"
            },
            {
                "name": "GameOppositionDemosReceived",
                "type": "widget",
                "title": "Demos Received: ",
                "gridpos": (2, 1),
                "gridspan": (1, 1),
                "tags": "Opposition.Demos Received",
                "precision": "g"
            },
            {
                "name": "GameOppositionDemosInflicted",
                "type": "widget",
                "title": "Demos Inflicted: ",
                "gridpos": (2, 2),
                "gridspan": (1, 1),
                "tags": "Opposition.Demos Inflicted",
                "precision": "g"
            },
            {
                "name": "GameOppositionTimeDefensiveHalf",
                "type": "widget",
                "title": "Time Ball in Defensive Half: ",
                "gridpos": (2, 3),
                "gridspan": (1, 1),
                "tags": "Opposition.Time Ball in Defensive Half",
                "precision": "g"
            }
        ]
    }
]
