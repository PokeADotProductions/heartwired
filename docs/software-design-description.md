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

# 6.4 Database Design and Description

## 6.4.1     Database Design ER Diagram
## 6.4.2     Database Access
## 6.4.3     Database Security

