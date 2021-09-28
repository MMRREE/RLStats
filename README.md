# RLStats

This is a repo to track the development of RLStats, a python program interfacing with [ballchasing](https://ballchasing.com/) to give comprehensive stats on players rocket league games.

## Specifications for V1.0

- [x] User Search
  - [x] Find the user on the [RLTracker](https://rocketleague.tracker.network/) database
  - [x] Find the replays that contain the user from [Ballchasing](https://ballchasing.com/)
- [ ] Data Capture:
  - [x] Group like Ballchasing does
  - [x] Create an object as a schema
  - [ ] Capture listed stats (initial query)
  - [x] Capture listed stats (independent query)
- [x] Graphing:
  - [x] Parse the schema so that choice of drop down options matches
  - [x] Group together categories that make sense (goals for/against) and graph in positive and negative direction
  - [x] Selection of data based on absoulte or percentage statistics (where applicable)
