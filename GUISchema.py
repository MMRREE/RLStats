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
                "precision": ".2f"
            },
            {
                'name': 'SessionIndividualSore',
                'title': 'Score: ',
                'gridpos': (2, 2),
                'gridspan': (1, 1),
                "type": "widget",
                'tags': "Individual.General.Score",
                "precision": ".2f"
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
                        'tags': "Individual.Boost.Average boost used per minute",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostCPM',
                        'title': 'BCPM: ',
                        'gridpos': (0, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Average boost collected per minute",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostAverage',
                        'title': 'Average Boost: ',
                        'gridpos': (0, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Average boost amount",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostZeroTwentyFive',
                        'title': '0-25%: ',
                        'gridpos': (1, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.0-25% boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostTwentyFiveFifty',
                        'title': '25-50%: ',
                        'gridpos': (1, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.25-50% boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostFiftySeventyFive',
                        'title': '50-75%: ',
                        'gridpos': (1, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.50-75% boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostSeventyFiveHundred',
                        'title': '75-100%: ',
                        'gridpos': (1, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.75-100% boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostZero',
                        'title': '0 Boost: ',
                        'gridpos': (2, 0),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Boost.0 boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostHundred',
                        'title': '100 Boost: ',
                        'gridpos': (2, 2),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Boost.100 boost.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualBoostTotalCollected',
                        'title': 'Total Collected: ',
                        'gridpos': (3, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Amount of boost collected",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostTotalCollectedFromBP',
                        'title': 'From Big Pads: ',
                        'gridpos': (3, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total collected from big pads",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostTotalCollectedFromSP',
                        'title': 'From Small Pads: ',
                        'gridpos': (3, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total collected from small pads",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostOverfill',
                        'title': 'Overfill: ',
                        'gridpos': (3, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Boost overfill",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostNumBP',
                        'title': '# of Big Pads: ',
                        'gridpos': (4, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Big pads taken",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostNumSP',
                        'title': '# of Small Pads: ',
                        'gridpos': (4, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Small pads taken",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostUsedAtSS',
                        'title': 'Used at Supersonic: ',
                        'gridpos': (4, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Big pads taken",
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
                        'tags': "Individual.Boost.Total stolen",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostStolenFromBP',
                        'title': 'From Big Pads: ',
                        'gridpos': (6, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total stolen from big pads",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostStolenFromSP',
                        'title': 'From Small Pads: ',
                        'gridpos': (6, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Total stolen from small pads",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostStolenOverfill',
                        'title': 'Overfill: ',
                        'gridpos': (6, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Stolen overfill",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostStolenNumBP',
                        'title': '# of Big Pads: ',
                        'gridpos': (7, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Big pads stolen",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualBoostStolenNumSP',
                        'title': '# of Small Pads: ',
                        'gridpos': (7, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Boost.Small pads stolen",
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
                        "type": "widget",
                    },
                    {
                        'name': 'SessionIndividualPositioningTeammates',
                        'title': 'Teammates: ',
                        'gridpos': (1, 0),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Average distance to teammates",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallPos',
                        'title': 'Ball (Possesion): ',
                        'gridpos': (1, 2),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Average distance to the ball in possesion",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallOutOfPos',
                        'title': 'Ball (Out of Possesion): ',
                        'gridpos': (1, 4),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Average distance to the ball out of possesion",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningMostBack',
                        'title': 'Most Back: ',
                        'gridpos': (2, 1),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Most back.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningMostForward',
                        'title': 'Most Forward: ',
                        'gridpos': (2, 3),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Most forward.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningDefensiveHalf',
                        'title': 'Defensive Half: ',
                        'gridpos': (3, 1),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Defensive half.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningOffensiveHalf',
                        'title': 'Offensive Half: ',
                        'gridpos': (3, 3),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Offensive half.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningDefensiveThird',
                        'title': 'Defensive Third: ',
                        'gridpos': (4, 0),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Defensive third.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningNeutralThird',
                        'title': 'Neutral Third: ',
                        'gridpos': (4, 2),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Neutral third.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningOffensiveThird',
                        'title': 'Offensive Third: ',
                        'gridpos': (4, 4),
                        'gridspan': (1, 2),
                        "type": "widget",
                        'tags': "Individual.Positioning.Offensive third.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallTitle',
                        'title': 'Ball: ',
                        'gridpos': (5, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                    },
                    {
                        'name': 'SessionIndividualPositioningBallClosest',
                        'title': 'Closest: ',
                        'gridpos': (5, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.Closest to ball.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallFarthest',
                        'title': 'Farthest: ',
                        'gridpos': (5, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.Farthest from ball.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallBehind',
                        'title': 'Behind: ',
                        'gridpos': (5, 3),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.Behind the ball.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualPositioningBallInfront',
                        'title': 'Infront: ',
                        'gridpos': (5, 4),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Positioning.In front of the ball.percent",
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
                        'tags': "Individual.Movement.Average speed.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementTotalDistance',
                        'title': 'Total Distance: ',
                        'gridpos': (0, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Total distance travelled",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementPowerslideDuration',
                        'title': 'Powerslide Duration: ',
                        'gridpos': (1, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Powerslide total duration",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementNumPowerslides',
                        'title': '# of Powerslides: ',
                        'gridpos': (1, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Number of powerslides",
                        "precision": "g"
                    },
                    {
                        'name': 'SessionIndividualMovementAveragePowerslidesLength',
                        'title': 'Average Powerslide Length: ',
                        'gridpos': (1, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Average powerslide duration",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementSlowSpeed',
                        'title': 'Slow: ',
                        'gridpos': (2, 0),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Slow speed.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementBoostSpeed',
                        'title': 'Boost: ',
                        'gridpos': (2, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.Boost speed.percent",
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
                        'tags': "Individual.Movement.On the ground.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementLowAir',
                        'title': 'Low Air: ',
                        'gridpos': (3, 1),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.In low air.percent",
                        "precision": ".2f"
                    },
                    {
                        'name': 'SessionIndividualMovementHighAir',
                        'title': 'High Air: ',
                        'gridpos': (3, 2),
                        'gridspan': (1, 1),
                        "type": "widget",
                        'tags': "Individual.Movement.In high air.percent",
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
                "tags": "Team.Time in possesion",
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
                "tags": "Team.Time ball in defensive half",
                "precision": "g"
            }
        ]
    }
]
