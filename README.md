[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588448&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Spring, 2024 >>

## Team Members

none

***

## Project Description

I want to make a Enter the Gungeon style game where the character you pick are from Valorant. Depending on which character you pick you get different ability from the original game.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Agent Selection - where you pick the agent (Jett)
2. Moveable Character - The agent(Jett) can be controlled to move left right and at an angle
3. Shoot - You would be able to shoot a gun at the direction you click
4. Scolling Background - you are able to move between screens
5. Game Over Screen - when you die, the game ends with a screen

### Classes

- << You should have a list of each of your classes with a description >>

## ATP

Test Case 1: Player Movement
-----------------------------
- Test Description: Verify that the player can move in all directions including diagonals
- Test Steps:
    1. Start game by pressing SPACE
    2. Move left and right with A and D respectively
    3. Move up and down with W and S respectively
    4. Move diagonals with A+W, D+W, A+S, and D+S
- Expected Outcome: The players moves in the appropriate direction and changes sprite thats corresponds with the directions

Test Case 2: Dash Ability
---------------------------
- Test Description: Verify that the player can use her dash ability
- Test Steps:
    1. Start game by pressing SPACE
    2. To use her dash ability press E
    3. The direction of the dash corresponds with the WASD keys
    4. Verify that the player moves in a specific direction quickly
    5. Verify that the sprite changes with dash
    6. Ensure that there is a slight cooldown between dashes
    7. Verify that the player can go in all 8 directions
- Expected Outcome: When utilizing her ability, the player should move very quickly towards the direction they are moving towards

Test Case 3: Updraft Ability
-----------------------------
- Test Description: Verify that the player can use her updraft ability
- Test Steps:
    1. Start game by pressing SPACE
    2. To use her updraft ability press Q
    3. Verify that she moves up and comes back down
    4. Verify that she becomes slightly transparent
    5. Verify the updraft sprite plays
    6. Ensure that there is a slight cooldown between updrafts
- Expected Outcome: When utilizing her updraft ability, she moves up and then down while being transparent and changes sprite.

Test Case 4: Smoke Ball Ability
--------------------------------
- Test Description: Verify that the player can throw smoke ball towards a certain direction
- Test Steps:
    1. Start game by pressing SPACE
    2. To use her smoke ball ability press C
    3. Verify that the player throws smoke balls towards the direction of the mouse
    4. Verify that smoke travels a fixed distance before stopping
    5. The smoke ball expands after stopping
- Expected Outcome: When utilizing the smoke ball ability, she throws a smoke ball towards the direction of the mouse before stopping and expanding before disappearing after 3-4 seconds

Test Case 5: Gun Play
---------------------
- Test Description: Verify that the player can switch between gun and hand and shoot with the gun
- Test Steps:
    1. Start the game by pressing SPACE
    2. To switch to gun press 2 and switch to hand press 3
    3. Aim with your mouse and click to shoot
    4. Verify that the bullet travels to the mouse and keeps going until hitting an obstacle
- Expected Outcome: The player switches to their gun and shoot a bullet at the direction the mouse is. The bullet will travel until either it exits the screen or hit an obstacle

