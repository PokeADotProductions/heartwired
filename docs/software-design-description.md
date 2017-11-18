# 6.1. Introduction

This document presents the architecture and detailed design for the software for the Heartwired application. Heartwired is a puzzle-platformer video game with 3D assets and a 2D camera that users will be able to download and play on both Mac/PC. 

## 6.1.1     System Objectives

The objective of Heartwired is to provide a game client that is both intellectually engaging and visually appealing.The users will be able to control two unique characters to maneuver a three-dimensional environment and solve a variety of logic puzzles. The Heartwired game client is comprised of a menu system, with a top-level, world-selection, and settings menu, and core playable game. The user will be able to navigate the menu system to select and play either a new or saved game file, the process of which is detailed below.

## 6.1.2     Hardware, Software, and Human Interfaces

| Interface Type  | Interface Description | 
|---|---|
| Human Interface | Mouse & Keyboard  | 
| Human Interface | Monitor | 
| Human Interface | Game Controller | 
| Software Interface | Menu Interface | 
| Software Interface | Game Client | 
| Hardware Interface | Unreal Engine | 

# 6.2 Architectural Design 

## 6.2.1     Major Software Components

Looking at our [Requirements Specifications Document.](requirements-specifications.md) , the major software subsystems are the different menu interfaces and the core game. The Top Level Menu user interface includes the File Selection Menu, the World Selection Menu, and the Settings Menu. The Core Game has an informative HUD interface and Pause/Game Over Menu Screens. The Core Game provides the majority of the application to the user; it is where the user interacts with the game, including but not limited to the Platforming, Two Character, Ability, Enemy, and Health systems. 

Below, we have an image of the main menu screen.

![Main Menu Screen](https://raw.githubusercontent.com/sashadmitrieva96/cyberwitch/master/docs/heartwired-menu.jpg)


## 6.2.2 Major Software Interactions

Heartwired does not link multiple softwares, and therefore does not have interactions between them to list.

### 6.2.3. Architectural Design Diagrams 

#### Use-Case
The user's interactions with the software are contained within the menu, where they can acccess new or saved game files and change options, and in the game client, where they can manipulate character pawns to solve puzzles. In the Use-Case Diagram below, we show how the user can navigate the two main interfaces of our application.

![Use-Case Diagram](https://raw.githubusercontent.com/sashadmitrieva96/cyberwitch/master/docs/heartwired-usecase.png)

#### Top-Level 

The diagram below describes our system at a top-level. We show how the action interface of character abilities and movements interacts with the AI controller and fits into the overarching game mode, which is present in each stand-alone level.

![Top-Level Diagram](https://raw.githubusercontent.com/sashadmitrieva96/cyberwitch/master/docs/heartwired-toplevel.png)

#### Game State 

Since Heartwired does not interact with external software and is contained within a package exported from the Unreal Engine, we present a Game State Diagram that describes the different states the user will be in when accessing both the menu and game client.

![Game State Diagram](https://raw.githubusercontent.com/sashadmitrieva96/cyberwitch/master/docs/heartwired-gamestate.png)


# 6.3 CSC and CSU Descriptions

This section of the document provides a detailed description of the software for the Heartwired game application as described in the [Requirements Specifications Document.](requirements-specifications.md)

## 6.3.1 Detailed Class Descriptions Section

The following section provides the details of all the classes used in the Heartwired application. 

### 6.3.1.1 Main Game Mode CSC Description

The Main Game Mode, or known as the “Core Game” in our Requirements Specification Document, is a Class that implements other classes and interfaces to provide the user with a playable game. The Main Game Mode Class comprises the majority of the application, with the exception of the Main Menu.

#### 6.3.1.1.1 Platforming System CSU Description 

The platforming system contains classes that encompass different types of platforms, such as default platforms and moving platforms.

* Moving Platform Class: Allows platforms the ability to move in the game
* Damaging Platform Class: Damages the player character upon contact

#### 6.3.1.1.2 Two Character System (TCS) CSU Description
The Two Character System contains the blueprints of our player character and defines what the characters are capable of. 

* Base Controller Class: The default class for our player characters. Defines what both players can do.
* Taliah Class: Defines what abilities and unique characteristics Taliah has.
    * Taliah Animation Blueprint: Plays and blends Taliah animation states together when corresponding actions are taken.
* BEAR Class: Defines what abilities and unique characteristics Bear has. 
    * BEAR Animation Blueprint: Plays and blends BEAR animation states together when corresponding actions are taken.

#### 6.3.1.1.3 Enemy System CSU Description

The Enemy System defines the enemies in our game as well as the AI that control them.

* AI Controller Class: Defines the basic movement and action characteristics that all AI units share.
    * Pig Class: Contains the Pig’s AI which each instance of the Pig inherits.
    * Grunt Class: Contains the Grunt AI which each instance of the Grunt inherits. 

#### 6.3.1.1.4 Terrain System CSU Description

The Terrain System defines the various different terrains we have in our game.
* Interactive Environment Class: Defines unique environment interactables that the player can affect to solve puzzles
    * Breakable Environment Class: Defines environment objects whose mesh can be destroyed with character abilities. 

#### 6.3.1.1.5 Camera System CSU Description

The Camera System defines how we control the various different cameras in our game and how we switch between them.

* Moving Camera Class: The Moving Camera Class defines a camera that can follow the player character.
* Levels/Screens: The Levels/Screens camera is placed within certain sections of the game and left there.

## 6.3.2. Detailed Interface Descriptions Section

The following section provides the details of all the interfaces used in the Heartwired application. (NOTE: There may not be interfaces in each of these sections, I’m just copying from requirements doc and filling it in after.)

### 6.3.2.1 Top Level Menu Interface CSC Description
The Top Level Menu contains the base for various interfaces within the game.

#### 6.3.2.1.1 File Selection Menu CSU Description
The File Selection Menu allows user to load a file previously saved by the user

#### 6.3.2.1.2 World Selection Menu CSU Description
The World Selection Menu allows the user to change which world the user is currently in

#### 6.3.2.1.3 Settings Menu CSU Description
The Settings Menu allows the user to change the settings of the game. Methods include:
* Change game controls
* Change sound volume

#### 6.3.2.1.4 Pause Menu CSU Description
The Pause Menu displays after the user pauses the game, giving the user these options:
* Go back to Game
* Go back to Main Menu
* Open Options Menu
* Load another save file
* Change world

### 6.3.2.2 Core Game Interfaces CSC Descriptions 
The Core Game Interface describes the interfaces that appear in game to the user while in play.

#### 6.3.2.2.1 Platforming System CSU Description

The Platforming System of the Core Game is mainly informed by the Action Interface, which is a controller that details basic actions that all characters can take, including:
* Idle
* Movement
* Jumping
* Switching

#### 6.3.2.2.2 Two Character System (TCS) CSU Description
The Two Character System encompasses the abilities of our characters in the Character Ability Interface, a controller that each character has.
* Taliah abilities: Hookshot, Slide, Sneak
* BEAR abilities: Attack, Break, Roll 


#### 6.3.2.2.3 Health System CSU Description
The Health System contains our Health/Damage Interface.
* Describes the user interface displaying the health bar. 
* Informs the character's lives system with dying and respawning in a level.
	
## 6.3.3 Detailed Data Structures Description Section
The following section provides the details of all the data structures used in the Heartwired application. (NOTE: This section is still subject to change.)

The only data structure of note will be the combinations of data structures we may have to use when designing the Follow AI for our two characters. Since the Follow AI is still in testing changes, currently nothing is solidified under this section.


# 6.4 Database Design and Description

Since our project operates off of Unreal Engine 4, all of the assets and data are stored in engine. The project is packaged and run using the engine provided. Therefore, Heartwired is not using any external database or software. 

