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

### Fixed

- Fix typos in recent README changes.
- Update outdated unreleased diff link.

## [3.3] - 2024-12-22

### Added

- Wrote days 6-10 (Kiera)
- Created the challenge player faces on day 6. (Kiera and Anastasiia)

### Fixed

- Spelling and grammar mistakes

## [0.0.6] - 2014-12-12

### Added

- README section on "yanked" releases.

## [0.0.5] - 2014-08-09

### Added

- Markdown links to version tags on release headings.
- Unreleased section to gather unreleased changes and encourage note
  keeping prior to releases.

## [0.0.4] - 2014-08-09

### Added

- Better explanation of the difference between the file ("CHANGELOG")
  and its function "the change log".

### Changed

- Refer to a "change log" instead of a "CHANGELOG" throughout the site
  to differentiate between the file and the purpose of the file — the
  logging of changes.

### Removed

- Remove empty sections from CHANGELOG, they occupy too much space and
  create too much noise in the file. People will have to assume that the
  missing sections were intentionally left out because they contained no
  notable changes.

## [0.0.3] - 2014-08-09

### Added

- "Why should I care?" section mentioning The Changelog podcast.

## [0.0.2] - 2014-07-10

### Added

- Explanation of the recommended reverse chronological release ordering.

## [0.0.1] - 2014-05-31

### Added

- This CHANGELOG file to hopefully serve as an evolving example of a
  standardized open source project CHANGELOG.
- CNAME file to enable GitHub Pages custom domain.
- README now contains answers to common questions about CHANGELOGs.
- Good examples and basic guidelines, including proper date formatting.
- Counter-examples: "What makes unicorns cry?".

[unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.1.1...HEAD
[1.1.1]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.3.0...v1.0.0
[0.3.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.8...v0.1.0
[0.0.8]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.7...v0.0.8
[0.0.7]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/olivierlacan/keep-a-changelog/releases/tag/v0.0.1