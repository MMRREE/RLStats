# RLStats

This is a repo to track the development of RLStats, a python program interfacing with [ballchasing](https://ballchasing.com/) to give comprehensive stats on players rocket league games.

## Specifications for V1.0

- [x] User Search
  - [x] Find the user on the [RLTracker](https://rocketleague.tracker.network/) database
  - [x] Find the replays that contain the user from [Ballchasing](https://ballchasing.com/)
- [ ] Game Analysis:
  - [ ] Find the number of:
    - [x] Wins/Losses
    - [ ] **Individual (vs others)**:
      - [ ] **General**:
        - [ ] Goals
        - [ ] Saves
        - [ ] Assists
        - [ ] Shots
        - [ ] Demos Inflicted/Received
        - [ ] Score
        - [ ] Shooting percent
        - [ ] Goals against while last defender
      - [ ] **Boost**:
        - [ ] Average boost used per minute
        - [ ] Average boost collected per minute
        - [ ] Average Boost amount
        - [ ] Seconds with 0 boost
        - [ ] Seconds with 100 boost
        - [ ] Big pads taken
        - [ ] Stolen big pads (in other half - mid does not count)
        - [ ] Small pads taken
        - [ ] Stolen small pads (in other half)
        - [ ] Boost 'overfill' (amount of boost collected that would go past 100)
        - [ ] Stolen overfill
        - [ ] Time at 0-25% boost
        - [ ] Time at 25-50% boost
        - [ ] Time at 50-75% boost
        - [ ] Time at 75-100% boost
        - [ ] Amount of boost used at supersonic
        - [ ] Amount of boost collected
      - [ ] **Positioning**:
        - [ ] Average distance to teammates
        - [ ] % of time spent most back
        - [ ] % of time spent most forward
        - [ ] % of time in defensive third
        - [ ] % of time in neutral thrid
        - [ ] % of time in offensive third
        - [ ] % of time in defensive half
        - [ ] % of time in offensive half
        - [ ] % of time closest to ball
        - [ ] % of time farthest from ball
        - [ ] % of time behind ball
        - [ ] % of time in front of ball
        - [ ] Average distance to ball
        - [ ] Average distance to ball in possesion
        - [ ] Average distance to ball out of possesion
      - [ ] **Movement**:
        - [ ] Average speed as percent of max speed
        - [ ] Total distance travelled
        - [ ] % of time super sonic
        - [ ] % of time at boost speed (above just accelerating)
        - [ ] % of time at slow speed (not boosting)
        - [ ] % of time on the ground
        - [ ] % of time low in the air (lower than xBar)
        - [ ] % of time high in the air (higher than xBar)
        - [ ] Powerslide total duration
        - [ ] Powerslide average duration
        - [ ] Number of powerslides
    - [ ] **Teams**:
      - [ ] Goals For/Against
      - [ ] Saves
      - [ ] Assists
      - [ ] Shots
      - [ ] Demos Inflicted/Received
      - [ ] Total Score
      - [ ] Average Score
      - [ ] Average Shooting Percent
      - [ ] Time in possesion
      - [ ] Time in half
