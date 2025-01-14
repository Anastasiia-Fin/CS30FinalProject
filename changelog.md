# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1] - 2024-12-11

### Added

- Main logic for printing the different passing days (Anastasiia)
- Database for npc information (Kiera)
- Character class and common attributes between all characters (Anastasiia)
- Character class return message (Anastasiia)
- Named all functions necessary (Kiera)

### Fixed


### Changed


### Removed


## [1.2] - 2024-12-13

### Added

- Make map function and external file (Kiera)
- Check map function to print map to user (Kiera)
- Explore function (Kiera)
- Explore function user input error catching (Kiera and Anastasiia)
- Database of room descriptions (Kiera)
- Database of days (Anastasiia)
- Function for each day (Anastasiia)
- Menu database; game options, rooms (Anastasiia and Kiera)
- Empty storage class (Anastasiia)
- Empty item class (Anastasiia)
- Empty room (storage, washroom, utility, medical) functions

### Changed

- Made day function print daily options using menu database and let user pick (Anastasiia)
- Made day function loop through daily options until user picked next day (Anastasiia)
- Made quit function work (Anastasiia)
- Made empty functions print something related to their use for testing (Anastasiia)

## [1.3] - 2024-12-17

### Added

- Storage class inventory attribute
- Storage class object that is passed to player/user object

### Changed

### Removed

## [2.1] - 2024-12-18

### Added

- Player dies if food or water values go to zero using if statements in game function (Anastasiia)
- Take away daily portion of food and water (1) each day (Anastasiia)
- Cause of death under end function; ran out of resources like food or water, infected, or murdered (Kiera)
- Comments in game function/main logic, day, check_map, make_map, and chat functions (Anastasiia)
- Win function message (Kiera)
- Option to chat with NPCs and user input works (Anastasiia)
- Dialogue placeholders for each character in NPC database (Kiera)

### Changed

- NPC database names (Anastasiia and Kiera)
- Storyline under end function (Kiera)
- Storyline under win function (Kiera)

## [2.2] - 2024-12-18

### Added

- Dialogue and descriptions for each NPC under NPC database (Kiera)
- Wrote item and room descriptions (Kiera)
- Docstrings for every other function other than the day functions (Kiera and Anastasiia)

### Changed

- Made sure line character length does not exceed 80 characters as per PEP 8 rules (Kiera and Anastasiia)

## [3.1] - 2024-12-20

### Added

- Introduction story line under intro function (Anastasiia and Kiera)
- Days 1-5 functions (Anastasiia and Kiera)
- Day description for each day (Anastasiia and Kiera)
- Choice to keep or kick Ella on day 5 (Anastasiia)
- Change Ella's status attribute if kicked out (Anastasiia)

## [3.2] - 2024-12-20

### Added

- Fight menu in menus (Anastasiia)
- Weapons menu in menus (Anastasiia)
- Fight menu logic and let user pick (Anastasiia)
- Fight function logic and let user pick (Anastasiia)
- Hands function (Kiera)
- Gun function (Kiera)
- Axe function (Kiera)
- Run function (Kiera)
- Deleting weapon from dictionary once used (Kiera)

### Changed

- Check if player is dead after the day function is run in the game function main logic so that in case the player is dead, the day does not continue on (Anastasiia)

## [3.3] - 2024-12-22

### Added

- Wrote days 6-10 (Kiera)
- Created the challenge player faces on day 6. (Kiera and Anastasiia)

### Fixed

- Spelling and grammar mistakes

## [3.4] - 2024-12-12

### Added

- check_chars function to check for alive characters using object attributes and return a list (Anastasiia)
- Days 11-15 (Anastasiia)
- Gave option to kill off character and save rations, which affect the user's survival results (Anastasiia)
- Added a ruined ruined map list that will print instead of actual map on day 15 (Anastasiia)

## [3.5] - 2025-01-09

### Added

- Finish writting the storyline for days 16-20 (Kiera and Anastasiia)
- Mick fighting function (Kiera)
- Day 16 fight function with rats (Anastasiia)
- Day 17 storyline choice (eat the rats) (Kiera and Anastasiia)
- Day 18 character development (Anastasiia and Kiera)
- Day 19 storyline choice (Kiera)
- Wrote endings to story (Kiera)
- Ending logic in main game function (Anastasiia)

## [3.6] - 2025-01-07

### Added

- Made Tic, Tac, Toe game (Kiera)
- Made hangman game (Anastasiia)
- Made rock, paper, scissors game (Anastasiia)
- Dialogue for characters in chat function (Kiera)
- Randomizer for dialogue (Anastasiia)

### Changed

- Split game into modules (Kiera and Anastasiia)
- Made map function more modular, map is passed to map function (Anastasiia)

### Fixed

- Formating; docstrings, comments, and line length (Anastasiia and Kiera)

## [4.0] - 2025-01-13

### Added

- Day 7 choice to ration water (Anastasiia and Kiera)

### Fixed

- Formating; docstrings, comments, and line length (Anastasiia and Kiera)
