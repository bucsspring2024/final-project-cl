import pygame
# import your controller

class Entity:
    pass
    # add Jett
    # Enemy
    # Cypher

class Jett:
    def __init__(self, speed, gun):
        self.speed = speed
        self.health = 100
        self.gun = gun
        
    def TakeDamages(self, dmg):
        self.health -= dmg
        # take dmg from gun
        
    def Move(self):
        pass
        # move based on the keys
    
    def Look(self):
        pass
        # make your character follow where your cursor is
        # vector math
        
    def Shoot(self):
        print(self.gun.damage)
        pass
        # shoot when you click
        # if you move while you shoot its inaccurate
        # a bullet moves in that direction
        # sparks when you shoot
        # draw the flash separately from the character and add a timer for it
        
    def Dash(self):
        pass
        # dash Forward Timer (shoot the player at the direction that im looking at)
        
    def Smoke(self):
        pass
        # throw smoke Only can use 3 times (vector based on where you look)
        
    def Updraft(self):
        pass
        # updraft Only can use 1 time (decrease opacity and make invincible)
        
    def Reload(self):
        pass
        # reload
        
class Enemy(Jett):
    def __init__(self, EnemyType, Speed):
        self.type = EnemyType
        self.speed = Speed
        self.health = 100
        
    def Move(self):
        pass
        # move towards player when in view
        # randomly path find
        # stops to shoot (1-3 bullets)
    
    def Look(self):
        pass
        # look at player when in view
        
    def Shoot(self):
        pass
        # sparks when shoot
        # shoot in increments (1-3 bullets)
        
class Obstacle:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        
    def BlockPlayer(self):
        pass
        # block the player
        
class Cypher:
    def __init__(self, speed, gun):
        self.speed = speed
        self.gun = gun
        self.health = 125
    
    def TakeDamage(self):
        pass
        # takes 26 damage from Classic
        
    def Move(self):
        pass
        # shoots 5-8 shots quickly and then runs
        # Places trip wires
        # Place camera
        # Put down cage
        
    def Look(self):
        pass
        # looks at player
        
    def Shoot(self):
        pass
        # when seeing player shoots a random number (1-12) before running out of sight
        
    def Trips(self):
        pass
        # places trip
        
    def Camera(self):
        pass
        # Not very plausible
        
    def Cage(self):
        pass
        # Act like a Smoke
        
class Gun(Classic):

class Classic:
    reload = 0 # change
    damage = 26
    ammo = 12
    shooting_speed = 0 # change
    
    def Bullet(self):
        pass
        
class Ghost:
    def __init__(self):
        self.reload = 0 # reload speed

def main():
    pygame.init()
    background = ("white")
    screen = pygame.display.set_mode((300,300))
    screen.fill(background)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # Create an instance on your controller object
    # Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
