import pygame
import math

class Classic:
    def __init__(self):
        self.damage = 26
        self.ammo = 12
        self.shooting_speed = 0.5
        self.bullet_speed = 0
        self.spray = 0
        
        self.image = {
            'right' : pygame.image.load("assets/gun/classic/classicRight.png"),
            'left' : pygame.image.load("assets/gun/classic/classicLeft.png")
        }

    def shoot_bullet(self, start_pos, target_pos):
        bullet = Bullet(start_pos, target_pos, self.damage)
        return bullet
    
class Bullet:
    def __init__(self, start_pos, target_pos, damage):
        self.x, self.y = start_pos
        self.target_x, self.target_y = target_pos
        self.damage = damage
        self.speed = 10

    def move(self):
        direction = math.atan2(self.target_y - self.y, self.target_x - self.x)
        self.x += self.speed * math.cos(direction)
        self.y += self.speed * math.sin(direction)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (int(self.x), int(self.y)), 5)