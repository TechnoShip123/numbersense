# TODO.md

### This file contains a list of TODO items, organized into planned release versions.

You can find completed versions at [the bottom of the list](#Completed).

- Create users file if it does not exist

## Bugs
- [x] Choosing not to exit program on first attempt

## 0.0.3: Practice mode and notifications

### 0.0.3a: Practice Mode and Percentages
- [x] Practice mode: Practice specific concepts & problems
- [x] Answers should only be counted correct without the leading zero.
- [x] Answers should be simplified to be counted correct



### 0.0.3b: Inbox
- [ ] DB!!!!

## 0.0.3: Timed Mode
- [ ] Timed Mode
- [ ] Percentages!
- [ ] Mixed numbers
- [ ] Inbox with notifications (ex.: failed login attempts)
- [ ] Guest information should not be saved

## 0.0.4: Questions!
- [ ] Introduce loads of new questions
- [ ] Word Problems
- [ ] Geometry
- [ ] Subscripts
- [ ] Estimation Questions
- [ ] Reset leaderboard 
- [ ] Calculus
- [ ] Add more categories to the leaderboard  

## 0.0.5: Tests
- [ ] Full length practice tests
- [ ] Options menu
	- [ ] Option to turn off changing answers

# 0.1
- [ ] 2 Player Mode
- [ ] Decrease Lag
- [ ] Improved Interface
- [ ] Learning Plans
	- [ ] Keep track of what needs improvement for each person.
- [ ] Migration: Everything goes into a DB
- [ ] Discord bot

# 0.2
- [ ] Create website?
- [ ] Mobile mode???



# Completed


### 0.0.1a: Fixes
- [x] **Project cleanup and VCS** (Saturday)
	- [x] Pass in `player1` instead of `quizMode` to `main()` function
	- [x] Shrink duplicated code when setting timer
- [x] General error clean up
- [x] Make the program able to take nothing and words as answer and not die
	- [x] Also in the `number of questions` prompt.
    - [x] Allow negative numbers.
- [x] Learn Mode, Group One 

### 0.0.1b: IDK
- [x] Info page uses `rich` package's markdown feature
- [x] Make a proper [`README.md`](https://github.com/TechnoShip123/numbersense/blob/master/README.md)
- [x] Ensure that error messages are not displayed at finishing of the program.
- [x] Proper loop when in the `additional info` section so that we can navigate back to the main menu without exiting the program
- [x] Finish more groups of Learn Mode
	- [x] Group 2
    - [x] Group 3  
- [x] Fix giveInfo() leaderboard option

## 0.0.1: Project & Git Cleanup

### 0.0.1: Final Changes
- [x] Salt/Hash password if we are going for another approach? or cryptography
    - [x] Either change/remove all instances of `createDefault(username)` because `None` type doesn't work with encryption (different hash each time).
    Currently, a temporary fix gives default users a password of `'password'` instead of `None`.

### 0.0.2a: Decimals and Hard Mode
- [x] Finish Learn Mode
- [x] Hard mode
  - [x] Leaderboard
- [x] Ability to exit program at any point.
- [x] Fix the character-hack bug
- [x] Encrypt Admin Password

### 0.0.2b: Fractions & Decimals
- [x] Decimals!! 
	- [x] Converting decimals to fraction
    - [x] Converting fractions to decimals
- [x] Adding and subtracting reverse fractions @Pikamaster23
- [x] Fix getting 0 as a number of questions @Pikamaster23
- [x] Random Mode @Pikamaster23

## 0.0.2: The Everything Update

- [x] Add CI/CD deployments for code quality & error checking. @TechnoShip123
- [x] Proper `master/` and `feature/xyz` branch structuring (`dev/` likely unnecessary, maybe if the project gains more traction). @TechnoShip123
- [x] Add [badges for build status](https://shields.io/category/build) when done.
- [x] Testing
- [x] Feedback @Pikamaster23
- [x] Quick Mode @Pikamaster23
- [x] Learn mode: Parts of the Whole Group @Pikamaster23
    - [x] Restructure
    - [x] Add new lesson 
- [x] Fix betterFracInput so that inputs like "2/" or "/4" don't cause an error. @Pikamaster23
- [x] Leaderboard in ms @Pikamaster23
- [x] View high scores options on main menu
- [x] Play Again Option @TechnoShip123
- [x] Reformat milliseconds in leaderboard
- [x] Encrypt change password
- [x] Fix createDefault
- [x] No duplicates in whitelist.json
- [x] Start tracking analytics/statistics
    - [x] ex.: Most/Least played modes 

# Public Release: 0.0.2