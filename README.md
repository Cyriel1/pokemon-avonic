# Coding Challenge Avonic (~ 5 Hours)

This project is part of Avonic's selection process. It is used to give a good impression of my current programming skills in Python using OOP.

## Description

The assignment is to make a small console-based Pokemon Game. The goal of the game is to allow a player to select a Pokemon from a range of choices and to initiate a fighting sequence with another Pokemon. The fighting happens turn-based. Each Pokemon gets a turn to attack, until one Pokemon’s health is depleted. The complexity of the game mechanics is secondary, the main interest is what is built under the hood.

### Software Requirements
1. Main menu so the user can initiate actions.
2. List all available Pokemon and be able to choose one as your main Pokemon. Create as
many Pokemon as you like, with a minimum of 5.
3. Being able to change your main Pokemon at any time.
4. Ability to initiate a fighting sequence. Before actually fighting, we pick an opposing
Pokemon.
5. An overview of what happens during the fight. Who is attacking who, what are the current
health stats, etc.

## Clean Code

There are a number of aspects of the code that are important. An important aspect is the level of readability. Code is mostly read by a fellow programmer and the ability to write concise yet understandable code is crucial in a team. That is why it is strongly encouraged to code using the SOLID principles. The following principles will be looked at when reviewing the source code:

- Readability
- Separation of Concerns (SoC)
- Naming conventions
- Don’t Repeat Yourself (DRY)
- Functions should only perform a single task

## Build

- Read **HOW_TO_BUILD.md** for a thorough explanation of how to run the application.

## Side Notes:

- Running the application in the Pycharm shell does not clear the console screen and outputs a "-symbol instead.
- It is recommended to create an executable file and launch the application in a terminal, such as powershell or command prompt. Double-clicking the **.EXE** file in Windows is fine, but it can't display the logo (it's a console with fewer features).
- Still want to run from source code? The best experience is by running in another shell, such as (again) powershell or command prompt.
    - Command needed to run application: 
      > python -m app
- With the command **'make create_data'** you can generate random data, which means replay-ability!
- Just in case any unforeseen errors occur, the application has been developed in Windows 10 with Python 3.11.
- Unit tests are unfortantely not included, did not had time to fully do it :(
