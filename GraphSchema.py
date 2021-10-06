graphConfiguration = {
    "Win/Losses": {
        "type": "option",
        "value": "Win/Loss",
        "label": "Win/Loss",
        "yaxis": "Win/Losses",
        "title": "Wins and Losses",
        "tags": ["Win", "Loss"],
        "invert": True,
        "formatter": lambda value, ticknumber: "Win" if value == 1 else "Loss" if value == -1 else ""
    },
    "Time Played": {
        "type": "option",
        "value": "Time Played",
        "label": "Time Played",
        "yaxis": "Time Played (s)",
        "title": "Time Played",
        "tags": ["Time_Played"]
    },
    "Overtime": {
        "type": "option",
        "value": "Overtime",
        "label": "Overtime",
        "yaxis": "Overtime Played (s)",
        "title": "Overtime Played",
        "tags": ["Overtime"]
    },
    "Individual": {
        "type": "cascade",
        "General": {
            "type": "cascade",
            "Goals": {
                "type": "option",
                "value": "Individual General Goals",
                "label": "Goals",
                "yaxis": "Goals",
                "title": "Individual Goals",
                "tags": ["Individual.General.Goals"]
            },
            "Saves": {
                "type": "option",
                "value": "Individual General Saves",
                "label": "Saves",
                "yaxis": "Saves",
                "title": "Individual Saves",
                "tags": ["Individual.General.Saves"]
            },
            "Assists": {
                "type": "option",
                "value": "Individual General Assists",
                "label": "Assists",
                "yaxis": "Assists",
                "title": "Individual Assists",
                "tags": ["Individual.General.Assists"]
            },
            "Shots": {
                "type": "option",
                "value": "Individual General Shots",
                "label": "Shots",
                "yaxis": "Shots",
                "title": "Individual Shots",
                "tags": ["Individual.General.Shots"]
            },
            "Demos Inflicted/Received": {
                "type": "option",
                "value": "Individual Demos Inflicted/Received",
                "label": "Demos Inflicted/Received",
                "yaxis": "Demos Inflicted/Received",
                "title": "Individual Demos Inflicted/Received",
                "tags": ["Individual.General.Demos Inflicted", "Individual.General.Demos Received"],
                "invert": True
            },
            "Score": {
                "type": "option",
                "value": "Individual General Score",
                "label": "Score",
                "yaxis": "Score",
                "title": "Individual Score",
                "tags": ["Individual.General.Score"]
            },
            "Shooting Percent": {
                "type": "option",
                "value": "Individual General Shooting Percent",
                "label": "Shooting Percent",
                "yaxis": "Shooting Percent",
                "title": "Individual Shooting Percent",
                "tags": ["Individual.General.Shooting Percent"]
            },
        },
        "Boost": {
            "type": "cascade",
            "Average Boost Used/Collected per Minute": {
                "type": "option",
                "value": "Individual Boost Average Boost Used/Collected per Minute",
                "label": "Average Boost Used/Collected per Minute",
                "yaxis": "Average Boost Used/Collected per Minute",
                "title": "Average Boost Used/Collected per Minute",
                "tags": ["Individual.Boost.Average Boost Used per Minute", "Individual.Boost.Average Boost Collected per Minute"],
                "invert": False
            },
            "Average Boost Amount": {
                "type": "option",
                "value": "Individual Boost Average Boost Amount",
                "label": "Average Boost Amount",
                "yaxis": "Average Boost Amount",
                "title": "Individual Average Boost Amount",
                "tags": ["Individual.Boost.Average Boost Amount"]
            },
            "Amount of Boost Used at Supersonic": {
                "type": "option",
                "value": "Individual Boost Amount of Boost Used at Supersonic",
                "label": "Amount of Boost Used at Supersonic",
                "yaxis": "Amount of Boost Used at Supersonic",
                "title": "Individual Amount of Boost Used at Supersonic",
                "tags": ["Individual.Boost.Amount of Boost Used at Supersonic"]
            },
            "Amount of Boost Collected": {
                "type": "option",
                "value": "Individual Boost Amount of Boost Collected",
                "label": "Amount of Boost Collected",
                "yaxis": "Amount of Boost Collected",
                "title": "Individual Amount of Boost Collected",
                "tags": ["Individual.Boost.Amount of Boost Collected"]
            },
            "Big Pads Taken/Stolen": {
                "type": "option",
                "value": "Individual Boost Big Pads Taken/Stolen",
                "label": "Big Pads Taken/Stolen",
                "yaxis": "Big Pads Taken/Stolen",
                "title": "Individual Big Pads Taken/Stolen",
                "tags": ["Individual.Boost.Big Pads Taken", "Individual.Boost.Big Pads Stolen"],
                "invert": False
            },
            "Small Pads Taken/Stolen": {
                "type": "option",
                "value": "Individual Boost Small Pads Taken/Stolen",
                "label": "Small Pads Taken/Stolen",
                "yaxis": "Small Pads Taken/Stolen",
                "title": "Individual Small Pads Taken/Stolen",
                "tags": ["Individual.Boost.Small Pads Taken", "Individual.Boost.Small Pads Stolen"],
                "invert": False
            },
            "Boost Overfill/Stolen Overfill": {
                "type": "option",
                "value": "Individual Boost Overfill/Stolen Overfill",
                "label": "Boost Overfill/Stolen Overfill",
                "yaxis": "Boost Overfill/Stolen Overfill",
                "title": "Individual Goals",
                "tags": ["Individual.Boost.Boost Overfill", "Individual.Boost.Stolen Overfill"]
            },
            "0 Boost/100 Boost": {
                "type": "option",
                "value": "Individual Boost 0 Boost/100 Boost",
                "label": "0 Boost/100 Boost",
                "yaxis": "0 Boost/100 Boost",
                "title": "Individual 0 Boost/100 Boost",
                "tags": ["Individual.Boost.0 Boost", "Individual.Boost.100 Boost"],
                "invert": False
            },
            "0-25% Boost": {
                "type": "option",
                "value": "Individual Boost 0-25% Boost",
                "label": "0-25% Boost",
                "yaxis": "0-25% Boost",
                "title": "Individual 0-25% Boost",
                "tags": ["Individual.Boost.0-25% Boost"]
            },
            "25-50% Boost": {
                "type": "option",
                "value": "Individual Boost 25-50% Boost",
                "label": "25-50% Boost",
                "yaxis": "25-50% Boost",
                "title": "Individual 25-50% Boost",
                "tags": ["Individual.Boost.25-50% Boost"]
            },
            "50-75% Boost": {
                "type": "option",
                "value": "Individual Boost 50-75% Boost",
                "label": "50-75% Boost",
                "yaxis": "50-75% Boost",
                "title": "Individual 50-75% Boost",
                "tags": ["Individual.Boost.50-75% Boost"]
            },
            "75-100% Boost": {
                "type": "option",
                "value": "Individual Boost 75-100% Boost",
                "label": "75-100% Boost",
                "yaxis": "75-100% Boost",
                "title": "Individual 75-100% Boost",
                "tags": ["Individual.Boost.75-100% Boost"]
            }
        },
        "Positioning": {
            "type": "cascade",
            "Average Distance to Teammates": {
                "type": "option",
                "value": "Individual Positioning Average Distance to Teammates",
                "label": "Average Distance to Teammates",
                "yaxis": "Average Distance to Teammates",
                "title": "Individual Average Distance to Teammates",
                "tags": ["Individual.Positioning.Average Distance to Teammates"]
            },
            "Average Distance to the Ball": {
                "type": "option",
                "value": "Individual Positioning Average Distance to the Ball",
                "label": "Average Distance to the Ball",
                "yaxis": "Average Distance to the Ball",
                "title": "Individual Average Distance to the Ball",
                "tags": ["Individual.Positioning.Average Distance to the Ball"]
            },
            "Average Distance to the Ball in/out of Possession": {
                "type": "option",
                "value": "Individual Positioning Average Distance to the Ball in/out of Possession",
                "label": "Average Distance to the Ball in/out of Possession",
                "yaxis": "Average Distance to the Ball in/out of Possession",
                "title": "Individual Average Distance to the Ball in/out of Possession",
                "tags": ["Individual.Positioning.Average Distance to the Ball in Possession", "Individual.Positioning.Average Distance to the Ball out of Possession"],
                "invert": False
            },
            "Most Back/Forward": {
                "type": "option",
                "value": "Individual Positioning Most Back/Forward",
                "label": "Most Back/Forward",
                "yaxis": "Most Back/Forward",
                "title": "Individual Most Back/Forward",
                "tags": ["Individual.Positioning.Most Back", "Individual.Positioning.Most Forward"],
                "invert": False
            },
            "Defensive/Neutral/Offensive Third": {
                "type": "option",
                "value": "Individual Positioning Defensive/Neutral/Offensive Third",
                "label": "Defensive/Neutral/Offensive Third",
                "yaxis": "Defensive/Neutral/Offensive Third",
                "title": "Individual Defensive/Neutral/Offensive Third",
                "tags": ["Individual.Positioning.Defensive Third", "Individual.Positioning.Neutral Third", "Individual.Positioning.Offensive Third"],
                "invert": False
            },
            "Defensive/Offensive Half": {
                "type": "option",
                "value": "Individual Positioning Defensive/Offensive Half",
                "label": "Defensive/Offensive Half",
                "yaxis": "Defensive/Offensive Half",
                "title": "Individual Defensive/Offensive Half",
                "tags": ["Individual.Positioning.Defensive Half", "Individual.Positioning.Offensive Half"],
                "invert": False
            },
            "Closest to/Farthest from Ball": {
                "type": "option",
                "value": "Individual Positioning Closest to/Farthest from Ball",
                "label": "Closest to/Farthest from Ball",
                "yaxis": "Closest to/Farthest from Ball",
                "title": "Individual Closest to/Farthest from Ball",
                "tags": ["Individual.Positioning.Closest to Ball", "Individual.Positioning.Farthest from Ball"],
                "invert": False
            },
            "Behind/In front of the Ball": {
                "type": "option",
                "value": "Individual Positioning Behind/In front of the Ball",
                "label": "Behind/In front of the Ball",
                "yaxis": "Behind/In front of the Ball",
                "title": "Individual Behind/In front of the Ball",
                "tags": ["Individual.Positioning.Behind the Ball", "Individual.Positioning.In front of the Ball"],
                "invert": False
            },
        },
        "Movement": {
            "type": "cascade",
            "Average Speed": {
                "type": "option",
                "value": "Individual Movement Average Speed",
                "label": "Average Speed",
                "yaxis": "Average Speed",
                "title": "Individual Average Speed",
                "tags": ["Individual.Movement.Average Speed"]
            },
            "Average/Total Powerslide Duration": {
                "type": "option",
                "value": "Individual Movement Average/Total Powerslide Duration",
                "label": "Average/Total Powerslide Duration",
                "yaxis": "Average/Total Powerslide Duration",
                "title": "Individual Average/Total Powerslide Duration",
                "tags": ["Individual.Movement.Average Powerslide Duration", "Individual.Movement.Powerslide Total Duration"],
                "invert": False
            },
            "Number of Powerslides": {
                "type": "option",
                "value": "Individual Movement Number of Powerslides",
                "label": "Number of Powerslides",
                "yaxis": "Number of Powerslides",
                "title": "Individual Number of Powerslides",
                "tags": ["Individual.Movement.Number of Powerslides"]
            },
            "Total Distance Travelled": {
                "type": "option",
                "value": "Individual Movement Total Distance Travelled",
                "label": "Total Distance Travelled",
                "yaxis": "Total Distance Travelled",
                "title": "Individual Total Distance Travelled",
                "tags": ["Individual.Movement.Total Distance Travelled"]
            },
            "Slow/Boost/Supersonic Speed": {
                "type": "option",
                "value": "Individual Movement Slow/Boost/Supersonic Speed",
                "label": "Slow/Boost/Supersonic Speed",
                "yaxis": "Slow/Boost/Supersonic Speed",
                "title": "Individual Slow/Boost/Supersonic Speed",
                "tags": ["Individual.Movement.Slow Speed", "Individual.Movement.Boost Speed", "Individual.Movement.Supersonic"],
                "invert": False
            },
            "Height Positioning": {
                "type": "option",
                "value": "Individual Movement Height Positioning",
                "label": "Height Positioning",
                "yaxis": "Height Positioning",
                "title": "Individual Height Positioning",
                "tags": ["Individual.Movement.On the Ground", "Individual.Movement.In Low Air", "Individual.Movement.In High Air"],
                "invert": False
            },
        }
    },
    "Team": {
        "type": "cascade",
        "Goals For/Against": {
            "type": "option",
            "value": "Team Goals For/Against",
            "label": "Goals For/Against",
            "yaxis": "Goals For/Against",
            "title": "Team Goals For and Team Goals Against",
            "tags": ["Team.Goals For", "Team.Goals Against"],
            "invert": True
        },
        "Assists": {
            "type": "option",
            "value": "Team Assists",
            "label": "Assists",
            "yaxis": "Assists",
            "title": "Team Assists",
            "tags": ["Team.Assists"]
        },
        "Shots": {
            "type": "option",
            "value": "Team Shots",
            "label": "Shots",
            "yaxis": "Shots",
            "title": "Team Shots",
            "tags": ["Team.Shots"]
        },
        "Demos Inflicted/Received": {
            "type": "option",
            "value": "Team Demos Inflicted/Received",
            "label": "Demos Inflicted/Received",
            "yaxis": "Demos Inflicted/Received",
            "title": "Team Demos Inflicted and Team Demos Received",
            "tags": ["Team.Demos Inflicted", "Team.Demos Received"],
            "invert": True
        },
        "Total Score": {
            "type": "option",
            "value": "Team Total Score",
            "label": "Total Score",
            "yaxis": "Total Score",
            "title": "Team Total Score",
            "tags": ["Team.Total Score"]
        },
        "Average Score": {
            "type": "option",
            "value": "Team Average Score",
            "label": "Average Score",
            "yaxis": "Average Score",
            "title": "Team Average Score",
            "tags": ["Team.Average Score"]
        },
        "Average Shooting Percent": {
            "type": "option",
            "value": "Team Average Shooting Percent",
            "label": "Average Shooting Percent",
            "yaxis": "Average Accuracy (%)",
            "title": "Team Average Shooting Accuracy",
            "tags": ["Team.Average Shooting Percent"]
        },
        "Time in Possession": {
            "type": "option",
            "value": "Team Time in Possession",
            "label": "Time in Possession",
            "yaxis": "Time in Possession (s)",
            "title": "Team Time in Possession",
            "tags": ["Team.Time in Possession"]
        },
        "Time Ball in Defensive Half": {
            "type": "option",
            "value": "Team Time Ball in Defensive Half",
            "label": "Time Ball in Defensive Half",
            "yaxis": "Time Ball in Defensive Half (s)",
            "title": "Team Time Ball in Defensive Half",
            "tags": ["Team.Time Ball in Defensive Half"]
        }
    },
    "Opposition": {
        "type": "cascade",
        "Goals For/Against": {
            "type": "option",
            "value": "Opposition Goals For/Against",
            "label": "Goals For/Against",
            "yaxis": "Goals For/Against",
            "title": "Opposition Goals For and Opposition Goals Against",
            "tags": ["Opposition.Goals For", "Opposition.Goals Against"],
            "invert": True
        },
        "Assists": {
            "type": "option",
            "value": "Opposition Assists",
            "label": "Assists",
            "yaxis": "Assists",
            "title": "Opposition Assists",
            "tags": ["Opposition.Assists"]
        },
        "Shots": {
            "type": "option",
            "value": "Opposition Shots",
            "label": "Shots",
            "yaxis": "Shots",
            "title": "Opposition Shots",
            "tags": ["Opposition.Shots"]
        },
        "Demos Inflicted/Received": {
            "type": "option",
            "value": "Opposition Demos Inflicted/Received",
            "label": "Demos Inflicted/Received",
            "yaxis": "Demos Inflicted/Received",
            "title": "Opposition Demos Inflicted and Opposition Demos Received",
            "tags": ["Opposition.Demos Inflicted", "Opposition.Demos Received"],
            "invert": True
        },
        "Total Score": {
            "type": "option",
            "value": "Opposition Total Score",
            "label": "Total Score",
            "yaxis": "Total Score",
            "title": "Opposition Total Score",
            "tags": ["Opposition.Total Score"]
        },
        "Average Score": {
            "type": "option",
            "value": "Opposition Average Score",
            "label": "Average Score",
            "yaxis": "Average Score",
            "title": "Opposition Average Score",
            "tags": ["Opposition.Average Score"]
        },
        "Average Shooting Percent": {
            "type": "option",
            "value": "Opposition Average Shooting Percent",
            "label": "Average Shooting Percent",
            "yaxis": "Average Accuracy (%)",
            "title": "Opposition Average Shooting Accuracy",
            "tags": ["Opposition.Average Shooting Percent"]
        },
        "Time in Possession": {
            "type": "option",
            "value": "Opposition Time in Possession",
            "label": "Time in Possession",
            "yaxis": "Time in Possession (s)",
            "title": "Opposition Time in Possession",
            "tags": ["Opposition.Time in Possession"]
        },
        "Time Ball in Defensive Half": {
            "type": "option",
            "value": "Opposition Time Ball in Defensive Half",
            "label": "Time Ball in Defensive Half",
            "yaxis": "Time Ball in Defensive Half (s)",
            "title": "Opposition Time Ball in Defensive Half",
            "tags": ["Opposition.Time Ball in Defensive Half"]
        }
    },
}
