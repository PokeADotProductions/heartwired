# 4.1   Plan Introduction

This Software Development Plan provides the details of the planned development for the Heartwired application, a 2D puzzle-platformer video game that users will be able to download and play on both Mac/PC. 

## 4.1.1 Project Deliverables

* Project Proposal Document (9/20)
* Requirements Specification (9/27
* Software Development Plan Document (10/11)
* Preliminary Design Review Presentations (11/01)
* Software Design Description Document (Architecture Section) (11/01) 
* Software Design Description Document (Detailed Section) (11/15)
* Critical Design Review (CDR) Presentations (11/15)
* Test Plan Document (11/29)
* AlphaBeta Project Presentations (11/29)
  * We will be presenting 
* User’s Manual (12/06)
* User’s Manual Final Updates (12/15) 
* Final Project Presentation (12/16)
  * We will be presenting 
* Oral Status Reports
* Written Status Reports in Project SDF

# 4.2   Project Resources
## 4.2.1 Hardware Resources

| Operating System  | CPU Name  | CPU Speed | # of CPU Cores | Amount of RAM | Name of GPU | Amount of VRAM | Purpose |   
|---|---|---|---|---|---|---|---|
| Windows | Intel Xeon | 2.60 GHz | 20 cores | 64.0 GB | NVIDIA Quadro M400 | 8912 MB | Development |
| Windows | Intel Core i5 | 2.30 GHz | 5 cores | 8.0 GB | Intel HD Graphics 520 | 8060 MB | Development |

## 4.2.2 Software Resources 

| Resource  | Development | Execution |   
|---|---|---|
| Unreal Engine Blueprints | ✓  | ✓ |
| Github | ✓ |  |


# 4.3 Project Organization

# 4.4 Project Schedule 

Since Heartwired will be built upon in increasing complexity, the development of the game will be split into weekly sprints, starting with basic functionality that will grow into complex features interacting and relying on each other. These sprints are our best projection of the time that it will take to program these features into the game; if the time required for these tasks does not align with our schedule, we will adjust as follows with our three weeks of buffer space.

A detailed description of the sprint schedule follows:

Week 1:
  * Ability to move and jump.
  * Collision.
  * Switching.
  * Camera between screens. (can just jump doesn't need to pan)
  * Menu system to load into menu.

Week 2:
  * Jump with a platformy feel
  * Follow at all points.
  * Permanently moving platforms
  * Camera transition between screens.
  * Camera transition between Zones
  * All menus.
  
Week 3:
  * Saving/Loading.
  * Follow unless told to hold.
  * Switches.
  * Enemies present and detecting at a range and moving.
  * Begin adding in rough animations.
  * Pause Menu.

Week 4:
  * Collision works well.
  * Animations should be linked.
  * Switches can be linked to certain types of environments.
  * Follow AI can sometimes detect when it cannot follow. (Easiest way might be to just have physical indicators)
  * Health system.
  * Bear attacking.
  * Hookshot to some things.

Week 5:
  * Checkpoints.
  * HUD system.
  * All types of hookshot independently.
  * Bear charge.
  * Sneak.
  * Enemy AI done except fine tuning.

Week 6:
  * All animations in (still rough though).
  * All animations smoothly transition.
  * Hookshot toggling (choosing correct destination).
  * Hookshot rope and shit.
  * Menu animations.
  * Marker when other avatar is on other screen.
  * Toggling characters when on other screen.
  
Week 7: 
  * Saving completed levels and not reloading them as they are.
  * Ability cooldowns.
  * Locking out switching on ability use.
  * World select.

Understanding the importance of testing our game early and often, we have allocated time for playtesting throughout the semester. 

## 4.4.1 PERT / GANTT Chart

![GANTT Chart]()

## 4.4.2 Task / Resource Table

| Task | Hardware | Software |   
|---|---|---|
| Platforming Movement | Windows PC | Unreal Blueprints | 
| Switching | Windows PC | Unreal Blueprints | 
| Follow AI | Windows PC | Unreal Blueprints | 
| Taliah Abilities | Windows PC | Unreal Blueprints | 
| B.E.A.R. Abilities | Windows PC | Unreal Blueprints | 
| Enemy AI | Windows PC | Unreal Blueprints | 
| Health | Windows PC | Unreal Blueprints | 
| Camera | Windows PC | Unreal Blueprints | 
| Menu / Save | Windows PC | Unreal Blueprints | 
| HUD | Windows PC | Unreal Blueprints | 










