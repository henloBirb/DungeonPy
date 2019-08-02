    
    ~ presenting ~
    
      __                                                                          
     /\ \                                                                         
     \_\ \  __  __    ___      __      __    ___     ___        _____   __  __    
     /'_` \/\ \/\ \ /' _ `\  /'_ `\  /'__`\ / __`\ /' _ `\     /\ '__`\/\ \/\ \   
    /\ \L\ \ \ \_\ \/\ \/\ \/\ \L\ \/\  __//\ \L\ \/\ \/\ \  __\ \ \L\ \ \ \_\ \  
    \ \___,_\ \____/\ \_\ \_\ \____ \ \____\ \____/\ \_\ \_\/\_\\ \ ,__/\/`____ \ 
     \/__,_ /\/___/  \/_/\/_/\/___L\ \/____/\/___/  \/_/\/_/\/_/ \ \ \/  `/___/> \
                               /\____/                            \ \_\     /\___/
                               \_/__/                              \/_/     \/__/ 


    ~ a game developed in python by ~

         _____                                               
      __|  _  |__  ____  __    _ _____   ______  ____   _    
     |  |_| |    ||    \ \ \  //|     \ |   ___||    \ | |   
     |   _  |    ||     \ \ \// |      \|   ___||     \| |   
     |__| |_|  __||__|\__\/__/  |______/|______||__/\____|   
        |_____|                                              
      ____    ____   _  _____                                
     |    \  |    \ | ||     \                               
     |     \ |     \| ||      \                              
     |__|\__\|__/\____||______/                              
         _____                                               
     ___|    _|__  ____    _____   ____    ____    ____   _  
    |    \  /  | ||    \  |     | |    |  |    \  |    \ | | 
    |     \/   | ||     \ |     \ |    |_ |     \ |     \| | 
    |__/\__/|__|_||__|\__\|__|\__\|______||__|\__\|__/\____| 
        |_____|                                              


    ~ also known as ~

     __  __     ______     __    __        ______     ______     __    __     ______     ______    
    /\ \_\ \   /\  __ \   /\ "-./  \      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   /\  ___\   
    \ \  __ \  \ \  __ \  \ \ \-./\ \     \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\   \ \___  \  
     \ \_\ \_\  \ \_\ \_\  \ \_\ \ \_\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\  \/\_____\ 
      \/_/\/_/   \/_/\/_/   \/_/  \/_/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/   \/_____/ 



    ~ under the working title of ~



              ▀█████████▄   ▄█  ███▄▄▄▄      ▄████████  ▄█                              
                ███    ███ ███  ███▀▀▀██▄   ███    ███ ███                              
                ███    ███ ███▌ ███   ███   ███    ███ ███                              
               ▄███▄▄▄██▀  ███▌ ███   ███   ███    ███ ███                              
              ▀▀███▀▀▀██▄  ███▌ ███   ███ ▀███████████ ███                              
                ███    ██▄ ███  ███   ███   ███    ███ ███                              
                ███    ███ ███  ███   ███   ███    ███ ███▌    ▄                        
              ▄█████████▀  █▀    ▀█   █▀    ███    █▀  █████▄▄██                        
                                                       ▀                                
    ▀█████████▄     ▄████████ ███▄▄▄▄       ███        ▄████████    ▄████████ ▄██   ▄   
      ███    ███   ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ ███   ██▄ 
      ███    ███   ███    ███ ███   ███    ▀███▀▀██   ███    ███   ███    █▀  ███▄▄▄███ 
     ▄███▄▄▄██▀    ███    ███ ███   ███     ███   ▀   ███    ███   ███        ▀▀▀▀▀▀███ 
    ▀▀███▀▀▀██▄  ▀███████████ ███   ███     ███     ▀███████████ ▀███████████ ▄██   ███ 
      ███    ██▄   ███    ███ ███   ███     ███       ███    ███          ███ ███   ███ 
      ███    ███   ███    ███ ███   ███     ███       ███    ███    ▄█    ███ ███   ███ 
    ▄█████████▀    ███    █▀   ▀█   █▀     ▄████▀     ███    █▀   ▄████████▀   ▀█████▀  


    ~ behold the README.md ~


Requirements: 
- PyGame
- PyTmx
- PyScroll

TMX Files Edited with:
- Tiled


# Setup

Please se the above properties and make sure you have them installed

In order to run Binal Bantasy you NEED PyGame, PyTmx, and PyScroll.

We would also recommend downloading Tiled which will allow you to
see all the areas we designed for the game without actually having to
visit them. It will also display how we handled collision.

You will find the file 'dungeon.py' in src/BinalBantasy/
Run the file there. If you are using an editor, make sure that
is the directory you have open, otherwise it may have trouble
finding the correct path to the data and resources folder which
house the images, sprite sheets, and levels that are written in
an xml-like format called tmx which is home to sprite and 
collision data and is the code that tells pygame what to draw
on the screen.

If you have any issues with setup, please feel free to reach
out to hpr11@my.fsu.edu to help get things working so you can play
the game!


# Final Project Delivery Information:

## Description of Project

With Binal Bantasy, what we aimed to do was learn something new.
Neither of us had attemted to make any game before let alon a
sprawling RPG. We tried to take measures to adress scope creep
and keep things manageable but even with that it proved to be a 
huge task for the both of us!

## User Interface

The arrow keys control your movement.

The '+' and '-' keys (really '=' for '+') allow the user to zoom 
in or out. This functionality was added to allow any user on any
platform to get a view they were comfortable with in the window.

the 'esc' key closes the game.

The player begins in an overworld housing the different locations.

The intention if for the player to enter and exit the locations
on the overworld map by walking into them, or once inside, walking
to the edge of the map to exit.

The intintion is for battles to take place randomly but not inside
of towns or inns -- only in the overworld or in dungeouns. 

## Areas we Designed:

A huge amount of effort went in to making the maps and various
areas for the game. We are proud to state that Binal Bantasy 
features TWENTY-ONE different areas!

The best way to view them is opening the tiled.

List of areas:
- Overworld
- Town 1
- Town 2
- City 1
- FSU
- Library
- Temple 1
- Dungeon 1
- Final Dungeon
- Multi-floored tower
- Everest
- Stonehenge
- Houses
- Inns
- Basements
- Sand Tower

The time and effort that went into planning and designing
was very large considering neither of us are artists. We did
use open assets to design and use the sprites and to draw
the different areas. The best way to really see that in action
is to open all of the .tmx files in the Tiled editor (it's free)

## Resources used:
- PyGame documentation and tutorials
- Kids Can Code Pygame Tutorial
- PyScroll tutorial on GitHub
- Pyscroll Documentation
- Open Game Art assets
- Dragon Quest Assests
- Final Fantasy Assets
- RPG Maker Assets
- Dragon Quest VI Spritesheets
- PyTmx documentation
- Python OS library (to help with file path differences)
- The Stolen Crown (one of the only RPGs we could find)

## Challenges & Lessons Learned & Division of Tasks

Being a group of two taking on a role-playing game the biggest
challenged we faced was manpower. For Hayden it was finding time
to work on the game between two classes and a full-time job,
and for Marlan it was finding time to work on the game while also
balancing assingments and planning/writing questions for the summer
prigramming competition.

Despite that we met frequently and planned and discussed development
and where we wanted to take the game and tacked issues together and 
head on. The amount of work that went into making the game look 
VISUALLY appealing (which you want if you're making a VIDEO game)
was a really big strain. Planning and figuring out how to make sprite
animations occur in an elegant way was also a challenge.

Good examples were hard to find. While it was easy to find tutorials
for creating endless runners, mario clones, tetris clones, and the like
on YouTube in Pygame, finding RPG examples was pretty tough, and none of
them had walkthroughs. Additionally -- just about every attempt we could
find was written in Python 2. We wanted to panic -- and maybe did for
a moment -- but we resisted the urge to change to something easier
and instead devoted our time to trying to put something interesting
on the screen that really evoked the feeling of playing a late 80s
or early 90s JRPG.

We divided the work up pretty evenly with both of us reaching our 
hands into every facet of the game and the design. There really wasn't
anothe option with there only being two of us. We did a lot of work 
together by renting 4 hour chunks of the study rooms in Strozier.


# The Game

Binal Bantasy is a role-playing game inspired by the
best JRPGs of the 80s and 90s. It draws most inspiration
from franchises such as Dragon Quest and Final Fantasy.

The game features the following:
- Overworld
- Towns
- Dungeons
- Boss Monsters
- Turn-Based Combat
- Leveling
- Magic

## Overworld

The overworld is essentially a zoomed-out view of the map.
All icons in the overworld are representational. 

For example, towns, dungeons, and geography are all 
represented on the overworld. Interacting with town
and/or dungeon icons will take you to a to-scale 
map of that town and the player will be able to navigate
those locations.

## Towns

Towns are areas that are safe-zones where the player can
rest to replinish helath, talk to characters, and purchase
items to be used in the overworld. Players may also save
their game in the towns only.

## Dungeons

Dungeons are where the player must overcome challenges in
order to beat the game. There will be three dungeons which
the player can access. Each will reward the player with 1/3
required items needed to unlock the final boss and beat the
game.

## Boss Monsters

Boss mosters will be displayed visibly rather than through 
random encounters. They are larger and more difficult than 
regular enemy encounters. 

## Turn-Based Combat

The way that the player will interact with and defeat enemies
will be through a turn-based battle system. That is, that
the player will select from a variety of menu options to 
designate attacks rather than real-time action.

## Leveling

The player will gain experience as they defeat monsters. 
This will allow the player to grow stronger. The player 
will need to level up to get strong enough to defeat 
the boss mosnters.

## Magic

The player will use Magic to accomplish a variety of tasks
as well as gain access to new areas. Magic will function
essentially as a key to new areas. Players can also use
magic in combat. Magic is learned automatically by
leveling up the hero.



~~ Game Developed by Hayden Rogers and Marlan McInnes-Taylor ~~