# 5.0  Requirements Specification
# 5.1      Introduction

This Software Requirements Specification (SRS) documents the requirements for the Cyberwitch game project. Cyberwitch is a 3D puzzle-platformer game application that will allow users to control a character to maneuver a three-dimensional environment to solve a variety of logic puzzles. The Cyberwitch game client is comprised of a menu system, with a top-level, world-selection, and settings menu, and core playable game. The user will be able to navigate the menu system to select and play either a new or saved game file, the process of which is detailed below.  


## 5.1.1   Outline

* 5.2     CSCI Component Breakdown
* 5.3      Functional Requirements by CSC
* 5.4      Performance Requirements by CSC
* 5.5      Project Environment Requirements

## 5.1.2     Definitions

| Term  | Definition  |   
|---|---|
| Player  | The person who is playing the game.  |  
|  Character  | The avatar the player is currently controlling in game.  |  
| Platformer  |  A type of video game in which a player guides their character to jump between suspended platforms and/or over obstacles to traverse their environment.  |  
| Game Client  | Umbrella term for every aspect of the game, including the top-level menu selection screen and the core game.   |  
| Core Game  | Playable portion of the game, including the HUD, the pause menu, and manipulable characters and puzzles.  |  
| HUD  | The heads-up display, or HUD, presents visual information to players in the Core Game as a part of the game’s UI.     |  
| Worlds  | A space that holds anywhere from 3 to 20 playable levels. Each world has a unique appearance, and the levels within a world share similar qualities.    |  
| Levels  |  A space containing portions of the Core Game available to the player, where the main objective consists of a series of puzzles that end in a checkpoint.  |  
| Puzzle  | An in-game problem that tests the player’s ingenuity. Coming to a solution to the puzzle progresses the game.   |  
| Checkpoint  | A location in the game where the player can respawn if the character dies and where the game autosaves.   |  
| Screens  | A viewable portion of the game screen. Some levels are an entire screen, while some may be multi-screen with a moving camera.   | 

# 5.2       CSCI Component Breakdown

### 5.2.1 Top Level Menu

5.2.1.1 File Selection Menu    
5.2.1.2 World Selection Menu      
5.2.1.3 Settings Menu      
&nbsp;&nbsp;&nbsp;&nbsp;5.2.1.3.1 Controls     
&nbsp;&nbsp;&nbsp;&nbsp;5.2.1.3.2 Sound       

### 5.2.2 Core Game   

5.2.2.1 Platforming System    
5.2.2.2 Two Character System (TCS)    
5.2.2.3 Ability System    
5.2.2.4 Enemy System    
5.2.2.5 Terrain System    
5.2.2.6 Health System    
5.2.2.7 Camera System    
5.2.2.8 HUD    
5.2.2.9 Pause Menu    
5.2.2.10 Game Over Screen  
      

# 5.3       Functional Requirements

## 5.3.1     Game Client

### 5.3.1.1   Menu

5.3.1.1.1 The Main Menu for the application shall provide the user with a way to select what function of the application they want to proceed to.      

  There will exist a tree of menus as follows:      
  - Top Level Menu
    - File Selection Menu
      - World Selection Menu
    - Settings Menu

5.3.1.1.2 Top Level Menu         
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.1.2.1 The Top Level Menu shall allow the player to access the submenus File Selection and Settings.     
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.1.2.2 The Top Level Menu shall allow the player to quit the application.       

5.3.1.1.3 Settings Menu      

&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.1.3.1 The Settings Menu shall allow the player to change the buttons for controlling the game. These buttons will include, but not be limited to, the following buttons:            
* Left     
* Right      
* Up     
* Down     
* Switch     
* Ability 1     
* Ability 2     
      
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.1.3.2 The Settings Menu shall allow the player to edit the sound levels of the application.       
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.1.3.3 The Settings Menu shall provide the player access back to the Top Level Menu.      
  
5.3.1.1.4 File Selection Menu               
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.1.4.1 The File Selection Screen shall display a list of saved files.          
* The player will be able to select a file to continue with.  
* The player will be able to delete a saved file.  
    
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.1.4.2 The File selection shall provide the player access back to the Top Level Menu.           

5.3.1.1.5 World Selection Menu         
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.1.5.1 The World Selection Menu shall provide a set of buttons providing the player to accessible worlds. These worlds will include but not be limited to:      
* Farm  
* Swamp   
* City  

&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.1.5.2 The World Selection Menu shall provide the player access back to the File Selection Screen.    
  
  
###  5.3.1.2   Core Game        
The Core Game is the screen where the majority of the player's task is completed.             
The Core Game will display to the user the current game state and respond to the player's input.         

5.3.1.2.1 Main Game           
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.2.1.1 The Platforming System shall allow the player to platform with minimum frustration.      
* The character will be able to move left and right.       
* The character will be able to jump.      
* The character will collide with all platforms desired.     

&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.2.1.2 The Two Character System (TCS) shall provide the player the ability to seamlessly switch between characters.     
* The TCS will disable the ability to switch when desired. This includes situations including, but not limited to:      
  1. During the use of abilities     
  2. When only one avatar is available      
* The TCS will provide an Artificial Intelligence to allow uncontrolled avatars to follow the player to the best of their ability.      

&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.2.1.3 The Ability System shall provide the player access to the use of abilities. Each character has their own unique abilities.         
* Hookshot: pull the character to predefined “hookable terrain”      
* Slide: slip underneath low ceiling environments       
* Sneak: avoid enemy vision by hiding in predefined locations        
* Charge: break through breakable terrain     
* Attack: creates a hurtbox to damage an enemy       
* Push Button: press a button to affect the level       
* Push Block: move an object       
	
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.2.1.4 The Enemy System shall provide the player with a variety of obstacles the player will have to overcome.         
* The Enemy System will control the detection of player characters when in range of enemies.     
* The Enemy System will handle the attacking of the player by the enemy by:     
  1. Targeting only the active character for attack       
  2. Knocking back the hit character       
  3. Decreasing the health of hit player character       
  4. Blocking player characters from walking through or past the enemy.        

&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.2.1.5 The Health System shall include control the current status of the characters.        
* The Health System will set a maximum health for all characters and enemies (units).       
* The Health of a unit will decrease upon being hit by an attack.       
* The Health of a unit will decrease when under a terrain effect.        
* The character will receive temporary invulnerability when experiencing a reduction in health.      
    
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.2.1.6 The Terrain System shall provide the player with varying platforms to interact.         
* The Terrain System will provide the player with a platform the serves solely as a platform to stand on.       
* The Terrain System will include platforms that only specific characters can interact with and walk upon.      
* The Terrain System will include platforms that move in a variety of ways including:        
  1. Platforms that move linearly across the screen      
  2. Platforms that move rotationally across the screen      
  3. Platforms that loop from position to position continuously unless a character acts upon the environment to stop said platform     
  4. Platforms that move via command of switch or other character interactions with the environment      
  * The Terrain System will prevent platforms from falling forever.     

&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.2.1.7 The Camera System shall control what elements the play can see.         
* The Camera System will control transitions between screens by panning.     
* The Camera System will control transitions between levels by fadeout.     
* The Camera System will control camera panning through specific screens.      

5.3.1.2.2 Pause Menu
 &nbsp;&nbsp;&nbsp;&nbsp;5.3.1.2.2.1 The Pause Menu shall halt the game. While the game is halted the following elements shall be displayed on the screen:       
* "Resume" will return the game to a running state from a halted state       
* "Return to Last Checkpoint" will return the game to a running state starting from the most recent checkpoint      
* "Return to World Select" will return the game to the World Selection Menu      
* "Settings" will open the Settings Menu      

5.3.1.2.3 Game Over Screen       
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.2.3.1 The Game Over Screen shall be displayed when the player’s health drops to 0.      
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1.2.3.2 The Game Over Screen shall allow the player to choose between returning to the last checkpoint, returning to the World Selection Screen.     

## 5.3.2     Game Assets

5.3.2.1   The game shall have assets including 3D Models, animations, and textures provided by the Animation Department.     
5.3.2.2   The characters in game shall be represented the 3D Models.       
5.3.2.3   The characters in the game shall use animations.      

# 5.4       Performance Requirements

5.4.1     Game Responsiveness      
&nbsp;&nbsp;&nbsp;&nbsp;5.4.1.1   The game shall run at a reasonable speed without frame drops on most modern systems.      
&nbsp;&nbsp;&nbsp;&nbsp;5.4.1.2   The game client shall load in under 3 seconds.       
&nbsp;&nbsp;&nbsp;&nbsp;5.4.1.3   The controls shall be responsive and instant to the player.        
&nbsp;&nbsp;&nbsp;&nbsp;5.4.1.4   The game client shall handle errors in a way to avoid crashing.       

# 5.5       Environment Requirements
  
5.5.1     Unreal Engine 4 recommends this setup of hardware to run software developed in it at an adequate level:      

| Category  | Requirement  |  
|---|---|
| Operating System | Windows 7/8 64-bit  |   
| Processor | Quad-core Intel or AMD, 2.5 GHz or faster |
| Memory  | 8 GB RAM  |  
| Video Card/DirectX Version  |  DirectX 11 compatible graphics card | 


