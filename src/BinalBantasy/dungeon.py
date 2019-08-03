# Created by Hayden & Marlan
# Beginnings of a grand quest
# behold...
# Binal Bantasy

'''
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


'''

import os.path
import random
import math

import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame

import pyscroll
import pyscroll.data
from pyscroll.group import PyscrollGroup

# from pallete import *

# define configuration variables here
RESOURCES_DIR = 'Data'

HERO_MOVE_SPEED = 69  # pixels per second
MAP_FILENAME = 'BinalOverworld2.tmx'

# filename + portalnum: new filename
inPortalDict = {
    "Data/BinalOverworld2.tmxtown1": "Town1.tmx",
    "Data/BinalOverworld2.tmxsandtower": "sandtower.tmx",
    "Data/BinalOverworld2.tmxtown2": "town2.tmx",
    "Data/BinalOverworld2.tmxcity1": "city1.tmx",
    "Data/BinalOverworld2.tmxlibrary": "library-inn.tmx",
    "Data/BinalOverworld2.tmxdungeon1": "dungeon1.tmx",
    "Data/BinalOverworld2.tmxFSU": "FSU.tmx",
    "Data/BinalOverworld2.tmxcity1": "city1.tmx",
    "Data/BinalOverworld2.tmxstonehenge": "stonehenge.tmx",
    "Data/BinalOverworld2.tmxeverest": "everest.tmx",
    "Data/BinalOverworld2.tmxend": "end.tmx",
    "Data/BinalOverwold2.tmxtemple1": "temple1-inn.tmx"
}

#current filename: instance portalO (portal out)
outPortalDict = {
    "data/BinalDungeon1.tmx": "BinalDungeon1_Boss.tmx",
    
}

OldEntranceDict = {
    "Town1.tmx": (1535, 1727), 
    "sandtower.tmx": (1921, 1537),
    "town2.tmx": (2042, 541),
    "city1.tmx": (958, 511),
    "library-inn.tmx": (1470, 1214),
    "dungeon1.tmx": (1281, 1280),
    "FSU.tmx": (671, 1885),
    "city1.tmx": (958, 511),
    "stonehenge.tmx": (2050, 2597),
    "everest.tmx": (2314, 2109),
    "end.tmx": (2305, 1180),
    "temple1-inn.tmx": (1339, 2556)
}

# used to randomly select monsters
enemyNames = {
    0: "slime", 
    1: "red slime",  
    2: "draky",
    3: "mud man", 
    4: "dragon", 
    5: "ghost",
    6: "skeleton" 
}

# monster name: (image.png, (resizeX, resizeY), Y adjustor up/down, +-adj)
# (negative adj for left)
enemyImages = {
    "slime": ("slime.png", (90, 90), 40), 
    "mud man": ("mudMan.png", (180, 185), -10), 
    "draky": ("draky.png", (150, 100), 20),
    "red slime": ("redslime.png", (80, 80), 40),
    "dragon": ("dragon.png", (300, 250), -60, -120),
    "skeleton": ("skeleton.png", (120, 160), -10), 
    "ghost": ("ghost.png", (140, 160), -10),
}

# monster name: exp reward
enemyExp = {
    "slime": 5, 
    "red slime": 10, 
    "draky": 15, 
    "mud man": 30,
    "dragon": 5500, 
    "skeleton": 60, 
    "ghost": 20
}

# enemy hitpoints
enemyStats = {
    "slime": 5,
    "red slime": 6,
    "draky": 10,
    "mud man": 12,
    "dragon": 750, 
    "skeleton": 20,
    "ghost": 9
}

# current level: exp threshold to level up to next
levelDict = {
    1: 30, 2: 90, 3: 240, 4: 480, 5: 900, 6: 1000, 7: 2000, 8: 3500,
    9: 6000, 10: 9500, 11: 15000, 12: 22000, 13: 31000, 14: 50000,
    15: 69000, 16: 90000, 17: 120000, 18: 151000, 19: 200000
}

# key filename: image background for battle mode
backgroundDict = {
    "data/Tower.tmx": "Resources/towerInside.jpg",
    "Tower.tmx": "Resources/towerInside.jpg",
    "data/temple1.tmx": "Resources/desert.jpg",
    "data/house1Basement.tmx": "Resources/cellar.jpg",
    "data/temple2.tmx": "Resources/desertDungeon.jpg",
    "data/temple1.tmx": "Resources/desert.png",
    "data/house1Basement2.tmx": "Resources/cellar.jpg"

}

# character states to determine is random encounters take place
heroStates = {
    'data/BinalOverworld2.tmx': 'Overworld'
}

# simple wrapper to keep the screen resizeable
def init_screen(width, height):
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    return screen


# make loading maps a little easier
def get_map(filename):
    return os.path.join(RESOURCES_DIR, filename)


# make loading images a little easier
def load_image(filename):
    return pygame.image.load(os.path.join(RESOURCES_DIR, filename))

# make playing music easier
def playMusic(song):
    # does not crash if file misnamed/does not quite exist
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1, 0.0) # '-1' as first parameter
                                         # therefore loops
    except pygame.error: 
        print("music error:", song)


# object for multirow/column pallete of characters
class Pallete(pygame.sprite.Sprite):
    # initializes images with pallete of character sprites
    def __init__(self, filename, rows=1,cols=1, row=0, col=0):
        self.rows = rows
        self.cols = cols
        pygame.sprite.Sprite.__init__(self)
        image = load_image(filename).convert_alpha() 
        (width, height) = image.get_size()
        (self.width, self.height) = (width, height)
        (charWidth, charHeight) = (width / cols, height / rows)
        self.image= image.subsurface(
                    (col * charWidth, row * charHeight, charWidth, charHeight))
        self.image = pygame.transform.scale(self.image, (32, 40))


class Hero(Pallete):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('hero.png').convert_alpha()
        self.velocity = [0, 0]
        self._position = [0, 0]
        self._old_position = self.position
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * .5, 8)
        self.type = "hero"

        Pallete.__init__(self, 'heroes.png', 8, 12, 2, 4)
        (rows, cols) = (self.rows, self.cols)
        image = load_image('heroes.png').convert_alpha() 
        (width, height) = (self.width, self.height)
        (charWidth, charHeight) = (width / cols, height / rows)

        self.maxHitPoints = 10
        self.hitPoints = self.maxHitPoints
        self.maxMana = 10
        self.mana = self.maxMana
        self.experiencePoints = 0
        self.level = 1

        self.ups = list()
        self.rights = list()
        self.downs = list()
        self.lefts = list()

        # the image frames are in a grid, so below deals with the cells
        for col in range(0,2):
            self.ups.append(image.subsurface(
                        ((col+3) * charWidth, 6 * charHeight, 
                            charWidth, charHeight)))
            self.ups[col]= pygame.transform.scale(self.ups[col], (32, 40))
            self.rights.append(image.subsurface(
                        ((col+3) * charWidth, 5 * charHeight, 
                            charWidth, charHeight)))
            self.rights[col] = pygame.transform.scale(self.rights[col], 
                                                            (33, 41))
            self.downs.append(image.subsurface(
                        ((col+3) * charWidth, 4 * charHeight, 
                            charWidth, charHeight)))
            self.downs[col] = pygame.transform.scale(self.downs[col], (32, 40))
            self.lefts.append( image.subsurface(
                        ((col+3) * charWidth, 7 * charHeight, 
                            charWidth, charHeight)))
            self.lefts[col] = pygame.transform.scale(self.lefts[col], (33, 41))
        # begin game looking forward idle animation
        self.currImageList = self.ups

    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)

    def update(self, dt):
        self._old_position = self._position[:]
        self._position[0] += self.velocity[0] * dt
        self._position[1] += self.velocity[1] * dt
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self, dt):
        """ If called after an update, the sprite can move back
        """
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def walkAnimation(self, ticks):
        # adds animation for hero character
        n = 0
        if self.velocity[0] == 0 and self.velocity[1] == 0:
            ticks = ticks//500*500
            if ticks%500 == 0:
                n = 0
            if ticks%1000 == 0:
                n = 1
        else:
            ticks = ticks //350*350
            if ticks%350 == 0:
                n = 0
            if ticks%700 == 0:
                n = 1
        self.image = self.currImageList[n]

    def levelup(self):
        self.level += 1
        self.maxHitPoints += self.maxHitPoints *.1
        self.hitPoints = self.maxHitPoints
        self.maxMana += self.maxMana * .1
        self.mana = self.maxMana


class Monster(object):
    def __init__(self, name, battle, surface):
        # load monster image
        filename = enemyImages[name][0]
        self.image = load_image(filename).convert_alpha()
        self.battle = battle
        self.screen = surface
        self.name = name
        # resize image
        (x, y) = enemyImages[name][1]
        self.image = pygame.transform.scale(self.image, (x, y))
        self.hitpoints = enemyStats[name]
        self.reposition = enemyImages[name][2]
        self.text = "What will you do?"
        self.text2 = None

        # enemy attack on hero
        def attack(self, hero):
            screen = self.screen
            timeDelay(300)

            # perform attack 
            damage = math.ceil(random.randrange(1, self.hitpoints) *.5)
            hero.hitpoints -= damage
            if hero.hitpoints < 0:
                hero.hitpoints = 0
            
            # play hit sound
            playSound("enemyhit.wav", 1)

            self.text = other.name + " took " + str(damage) + " damage!"

            # refresh battle text
            self.battle.drawBattle(screen)
            timeDelay(600)

        # hero faints if hp is 0
        if other.hitpoints == 0:
            self.text = str(other.name) + " has fainted!"
            # battle text
            pygame.mixer.music.pause()
            self.battle.drawBattle(screen)
            timeDelay(1500)

class Battle(object):
    def __init__(self, game, hero, position, screen):
        self.hero = hero
        self.heroLevel = hero.level
        self.leveled = False
        self.game = game
        self.screen = screen
        self.position = position

        # background for battle screen
        image = "Resources/field.jpg"
        self.enemyName = enemyNames[random.randrange(0, len(enemyNames))]

        if game.mode2 != "Overworld":
            image = backgroundDict[game.filename]

        self.enemy = Monster(self.enemyName, self, screen)
        self.enemyDefeatText = "The " + self.enemyName + " was defeated!"

        self.background = pygame.image.load(image)

    # draw battle windows
    def drawRectMenu(self, surface, x, y):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(surface, BLACK, [x/5, y/2 + 70, x/2+100, y/5])
        pygame.draw.rect(surface, WHITE, [x/5, y/2 + 70, x/2+100, y/5], 5)

    def drawBattle(self, surface):
        # draws monster image and menus
        x = surface.get_width()
        y = surface.get_height()
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(surface, BLACK, [100, 100, x - 200, y-200])
        pygame.draw.rect(surface, WHITE, [100, 100, x - 200, y-200], 5)
        myFont = pygame.font.SysFont("monospace", 30)
        text = myFont.render(" Battle", 1, WHITE)

        # draw background
        self.background = pygame.transform.scale(self.background, (x - 200, y-200))
        surface.blit(self.background, (100, 100))
        surface.blit(text, (100, 100))

        # 


class BinalGame(object):
    """ This class is a basic game.

    This class will load data, create a pyscroll group, a hero object.
    It also reads input and moves the Hero around the map.
    Finally, it uses a pyscroll group to render the map and Hero.
    """
    filename = get_map(MAP_FILENAME)

    def __init__(self, filename, oldEntrance=None, oldmap=None, hero=None):
        self.portalName = ''
        self.portalsIn = list()
        self.portalsOut = list()
        
        self.olfFilename = None
        self.filename = get_map(filename)
        
        if self.filename in heroStates:
            self.mode = heroStates[self.filename]
        else:
            self.mode = "Peaceful"
        
        if oldmap == None:
            self.oldMap = filename
        else:
            self.oldMap = oldmap

        overworld = 'BinalOverworld2.tmx'
        self.oldEntrance = oldEntrance
        self.battleInstance = False

        
        # true while running
        self.running = False

        # load data from pytmx
        tmx_data = load_pygame(self.filename)

        # setup level geometry with simple pygame rects, loaded from pytmx
        self.walls = list()
        for object in tmx_data.objects:
            self.walls.append(pygame.Rect(
                object.x, object.y,
                object.width, object.height))

        # create new data source for pyscroll
        map_data = pyscroll.data.TiledMapData(tmx_data)

        # create new renderer (camera)
        self.map_layer = pyscroll.BufferedRenderer(map_data, screen.get_size(), clamp_camera=False, tall_sprites=1)
        self.map_layer.zoom = 2

        # pyscroll supports layered rendering.  our map has 3 'under' layers
        # layers begin with 0, so the layers are 0, 1, and 2.
        # since we want the sprite to be on top of layer 1, we set the default
        # layer for sprites as 2
        self.group = PyscrollGroup(map_layer=self.map_layer, default_layer=2)

        self.hero = Hero()

        # put the hero in the center of the map
        # self.hero.position = self.map_layer.map_rect.center
        # self.hero._position[0] += 200
        # self.hero._position[1] += 400

        # add our hero to the group
        self.group.add(self.hero)

        # startpoints
        self.startpoints = []
        for object in tmx_data.objects:
            if object.name == "startpoint":
                self.startpoints.append((object.x, object.y))

        self.hero.position = (self.startpoints[0][0], self.startpoints[0][1])
        self.oldPosition = self.hero.position
        self.group.add(self.hero)
        self.steps = 0
        self.battle = 1

        # set default zoom when not in overworld
        if self.oldMap == overworld and self.filename != "data/" + overworld:
            self.map_layer.zoom = self.map_layer.zoom - .25
        
        self.portalNames = list()
        # add portals to collider lists
        for object in tmx_data.objects:
            if object.type == "portalIn":
                self.portalNames.append(object)
                self.portalsIn.append(pygame.Rect(
                    object.x, object.y,
                    object.width, object.height))
            elif object.type == "portalO":
                self.portalsOut.append(pygame.Rect(
                    object.x, object.y,
                    object.width, object.height))
            
    def draw(self, surface):

        # center the map/screen on our Hero
        self.group.center(self.hero.rect.center)

        # draw the map and all sprites
        self.group.draw(surface)

    def nearestPortal(self, trigger=False):
        (x, y) = self.hero.position
        for portal in self.portalsIn:
            if trigger == False:
                trigger = True
                self.oldEntrance = (portal.x, portal.y)
                (p, q) = self.oldEntrance
            distanceNew = (math.sqrt((x - portal.x)**2+(y-portal.y)**2))
            distanceOld = (math.sqrt((x - p)**2+(y-q)**2))
        
            if distanceNew < distanceOld:
                distanceOld = distanceNew
                self.oldEntrance = (portal.x, portal.y)
                (p, q) = (portal.x, portal.y)
        for portal in self.portalNames:
            if self.almostEqual((p,q), (portal.x, portal.y)):
                self.portalName = portal.name

    def handle_input(self):
        """ Handle pygame input events
        """
        poll = pygame.event.poll
        clock = pygame.time.Clock()

        event = poll()
        while event:
            ticks = pygame.time.get_ticks()

            if event.type == QUIT:
                self.running = False
                break

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                    break

                elif event.key == K_EQUALS:
                    self.map_layer.zoom += .25

                elif event.key == K_MINUS:
                    value = self.map_layer.zoom - .25
                    if value > 0:
                        self.map_layer.zoom = value

            # this will be handled if the window is resized
            elif event.type == VIDEORESIZE:
                init_screen(event.w, event.h)
                self.map_layer.set_size((event.w, event.h))

            event = poll()

        # using get_pressed is slightly less accurate than testing for events
        # but is much easier to use.
        pressed = pygame.key.get_pressed()
        # if pressed[K_UP]:
        #     self.hero.velocity[1] = -HERO_MOVE_SPEED
        # elif pressed[K_DOWN]:
        #     self.hero.velocity[1] = HERO_MOVE_SPEED
        # else:
        #     self.hero.velocity[1] = 0

        # if pressed[K_LEFT]:
        #     self.hero.velocity[0] = -HERO_MOVE_SPEED
        # elif pressed[K_RIGHT]:
        #     self.hero.velocity[0] = HERO_MOVE_SPEED
        # else:
        #     self.hero.velocity[0] = 0

        # if self.moving != False:
        ticks = pygame.time.get_ticks()
        if pressed[K_UP]: 
            self.hero.currImageList = self.hero.downs
            self.hero.walkAnimation(ticks)
            self.hero.velocity[1] = -HERO_MOVE_SPEED
            #self.steps += 1
        elif pressed[K_DOWN]:
            self.hero.currImageList = self.hero.ups
            self.hero.walkAnimation(ticks)
            self.hero.velocity[1] = HERO_MOVE_SPEED
            #self.steps += 1
        else:
            self.hero.velocity[1] = 0
        if pressed[K_LEFT]:
            self.hero.currImageList = self.hero.lefts
            self.hero.walkAnimation(ticks)
            self.hero.velocity[0] = -HERO_MOVE_SPEED
            #self.steps += 1
        elif pressed[K_RIGHT]:
            self.hero.currImageList = self.hero.rights
            self.hero.walkAnimation(ticks)
            self.hero.velocity[0] = HERO_MOVE_SPEED
            #self.steps += 1
        
        else:
            self.hero.velocity[0] = 0
        # sprint
        if pressed[K_SPACE]:
            self.hero.velocity[0] *= 1.7
            self.hero.velocity[1] *= 1.7
            # more likely to battle encounter if sprinting
            # if self.hero.velocity[0] > 0 or self.hero.velocity[1] > 0:
            #     #self.steps += 2
            # if self.hero.velocity[0] >= 1.5 * HERO_MOVE_SPEED:
            #     pass
            # if self.hero.velocity[1] >= 1.5 * HERO_MOVE_SPEED:
            #     pass

        # stops character from moving when battlescreen is initiated
        #if self.mode == "Battle":
        #    (self.hero.velocity[0], self.hero.velocity[1]) = (0, 0)

    def update(self, dt):
        """ Tasks that occur over time should be handled here
        """
        self.group.update(dt)

        # check if the sprite's feet are colliding with wall
        # sprite must have a rect called feet, and move_back method,
        # otherwise this will fail
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.portalsIn) > -1:
                if sprite.type == "hero":

                    self.nearestPortal()
                    self.filename = inPortalDict[self.filename+self.portalName]
                    self.hero.position = (self.startpoints[0][0], self.startpoints[0][1])
            elif sprite.feet.collidelist(self.portalsOut) > -1:
                if sprite.type == "hero":
                    filename = outPortalDict[self.filename]
                    self.filename = filename
                    self.hero.position = (self.startpoints[0][0], self.startpoints[0][1])
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back(dt)

    # plays music based on map file keyed to dictionary
    # also covers changing map sound effect
    # def changeMusicAndInstance(self, surface, oldMusic=None):
    #     tmap = self.filename
    #     song = MusicDict[tmap]
    #     # instance change sound, from Zelda stairs sound
    #     playSound("Enter.wav", .15)

    #     if oldMusic == None:
    #         oldMusic = MusicDict[self.oldMap]
       
    #     if self.mode != "Overworld":
    #         if song == oldMusic: return None
       
    #     # loops music indefinitely for that map
    #     playMusic(song)
    #     def showStartScreen(self):
    #     self.draw('title_demo')
    #     if checkForKeyPress():
    #         self.run()

    @staticmethod
    def almostEqual(position1, position2):
        (x1, y1) = position1
        (x2, y2) = position2
        epsilon = 60
        if abs(x1-x2) < epsilon:
            if abs(y1-y2) < epsilon:
                 return True
        return False

    def randomBattle(self):
       # prevents battle from happening right on town portal
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.portalsIn) > -1:
                return None
        if self.almostEqual(position, self.oldPosition): 
            return None
        if self.mode == "Peaceful" or self.mode == "Battle": 
            return None
        diceRoll = random.randint(0, 100)
        #increased encounter rate when walking without encountering
        # a single battle for a certain number of steps
        threshold = 600
        if self.steps > threshold:
            if diceRoll < 50:
                self.mode = "Battle"
                self.steps = 0

        if self.steps > 200:
        # lower encounter rate when just beginning to walk
            if diceRoll < 200:
                self.mode = "Battle"
                self.steps = 0


        self.oldPosition = position 

    def run(self):
        """ Run the game loop
        """
        filename = self.filename
        clock = pygame.time.Clock()
        self.running = True

        from collections import deque
        times = deque(maxlen=30)

        #idle hero animation
        ticks = pygame.time.get_ticks()
        self.hero.walkAnimation(ticks)
        playMusic('overworld.wav')

        try:
            while self.running:
                dt = clock.tick() / 1000.
                times.append(clock.get_fps())
                # print(sum(times)/len(times))#idle hero animation
                ticks = pygame.time.get_ticks()
                self.hero.walkAnimation(ticks)
                # self.randomBattle()
                
                # changing map
                if self.filename != filename:
                    # leaving map toward overworld
                    if self.oldMap == os.path.join(RESOURCES_DIR, self.filename):
                        oldMap = inPortalDict[str(os.path.join(RESOURCES_DIR, self.filename)) + self.portalName]
                    else:
                        oldMap = outPortalDict[str(os.path.join(RESOURCES_DIR, self.filename))]
                    self.__init__(self.filename, self.oldEntrance, oldMap, self.hero)
                    self.oldEntrance = OldEntranceDict[filename]

                    if os.path.join(RESOURCES_DIR, inPortalDict[filename]) == self.filename:
                        if self.oldEntrance != None:
                            position = (self.oldEntrance[0], self.oldEntrance[1])
                            self.hero.position = position
                            self.oldPosition = position
                    self.run()
        

                self.handle_input()
                self.update(dt)
                self.draw(screen)
                pygame.display.flip()

        except KeyboardInterrupt:
            self.running = False


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    screen = init_screen(800, 600)
    pygame.display.set_caption('Binal Bantasy')

    try:
        game = BinalGame('BinalOverworld2.tmx')
        game.run()
    except:
        pygame.quit()
        raise
