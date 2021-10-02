# RLStats

This is a repo to track the development of RLStats, a python program interfacing with [ballchasing](https://ballchasing.com/) to give comprehensive stats on players rocket league games.

## Specifications for V1.0

- [x] User Search
  - [x] Find the user on the [RLTracker](https://rocketleague.tracker.network/) database
  - [x] Find the replays that contain the user from [Ballchasing](https://ballchasing.com/)
  - [x] Filter by the standard filters using the interactive buttons at the top of the screen
- [x] Data Capture:
  - [x] Game:
    - [x] Group like Ballchasing does
    - [x] Create an object as a schema
    - [x] Capture listed stats (initial query)
    - [x] Capture listed stats (independent query)
  - [ ] Sessions:
    - [x] Accumulation of statistics for the session
    - [x] Zoom graph into session when selected
    - [x] Scrollable section to display session statistics
    - [ ] Populate session GUI from a data structure (Still need to finish team aspects)
- [x] Graphing:
  - [x] Parse the schema so that choice of drop down options matches
  - [x] Group together categories that make sense (goals for/against) and graph in positive and negative direction
  - [x] Selection of data based on absoulte or percentage statistics (where applicable)
  - [ ] Set the axis properly
  - [ ] Set the title properly
  - [ ] Bug fix displaying two keys on the same graph (e.g. Goals For/Against)
  - [ ] Graph selections from schema
