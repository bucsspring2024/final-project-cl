import pygame
    
class Jett:
    def __init__(self, speed, gun):
        self.speed = speed
        self.health = 100
        self.gun = gun
        self.width = 16
        self.height = 24
        self.x = 400
        self.y = 500
        self.images = {
            'front' : pygame.image.load("assets/JettFront.png"),
            'back' : pygame.image.load("assets/JettBack.png"),
            'left' : pygame.image.load("assets/JettLeft.png"),
            'right' : pygame.image.load("assets/JettRight.png"),
            'back right' : pygame.image.load("assets/JettBackRight.png"),
            'back left' : pygame.image.load("assets/JettBackLeft.png")
        }
        self.direction = 'front'
        
    def drawCharacter(self, screen):
        scaled_image = pygame.transform.scale(self.images[self.direction], (self.width * 3, self.height * 3))
        screen.blit(scaled_image, (self.x, self.y))
        
    def takeDamages(self, dmg):
        self.health -= dmg
        # take dmg from gun
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = 'left'
        if keys[pygame.K_d]:
            self.x += self.speed
            self.direction = 'right'
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = 'back'
        if keys[pygame.K_s]:
            self.y += self.speed
            self.direction = 'front'
        if keys[pygame.K_w] and keys[pygame.K_d]:
            self.direction = 'back right'
        elif keys[pygame.K_w] and keys[pygame.K_a]:
            self.direction = 'back left'
        # move based on the keys
    
    def look(self):
        pass
        # make your character follow where your cursor is
        # vector math
        
    def shoot(self):
        print(self.gun.damage)
        pass
        # shoot when you click
        # if you move while you shoot its inaccurate
        # a bullet moves in that direction
        # sparks when you shoot
        # draw the flash separately from the character and add a timer for it
        
    def dash(self):
        pass
        # dash Forward Timer (shoot the player at the direction that im looking at)
        
    def smoke(self):
        pass
        # throw smoke Only can use 3 times (vector based on where you look)
        
    def updraft(self):
        pass
        # updraft Only can use 1 time (decrease opacity and make invincible)
        
    def reload(self):
        pass
        # reload
        
class Enemy(Jett):
    def __init__(self, EnemyType, Speed):
        self.type = EnemyType
        self.speed = Speed
        self.health = 100
        
    def move(self):
        pass
        # move towards player when in view
        # randomly path find
        # stops to shoot (1-3 bullets)
    
    def look(self):
        pass
        # look at player when in view
        
    def shoot(self):
        pass
        # sparks when shoot
        # shoot in increments (1-3 bullets)
        
class Obstacle:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        
    def blockPlayer(self):
        pass
        # block the player
        
class Cypher:
    def __init__(self, speed, gun):
        self.speed = speed
        self.gun = gun
        self.health = 125
    
    def takeDamage(self):
        pass
        # takes 26 damage from Classic
        
    def move(self):
        pass
        # shoots 5-8 shots quickly and then runs
        # Places trip wires
        # Place camera
        # Put down cage
        
    def look(self):
        pass
        # looks at player
        
    def shoot(self):
        pass
        # when seeing player shoots a random number (1-12) before running out of sight
        
    def trips(self):
        pass
        # places trip
        
    def camera(self):
        pass
        # Not very plausible
        
    def cage(self):
        pass
        # Act like a Smoke

class Classic:
    reload = 0 # change
    damage = 26
    ammo = 12
    shooting_speed = 0 # change
    
    def bullet(self):
        pass
        
class Ghost:
    def __init__(self):
        self.reload = 0 # reload speed

def main():
    pygame.init()
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
