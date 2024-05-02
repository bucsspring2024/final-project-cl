import pygame
import math

class Classic:
    def __init__(self):
        self.damage = 26
        self.ammo = 12
        self.shooting_speed = 0.25
        self.last_shot_time = 0
        self.bullet_speed = 0
        
        self.image = {
            'front' : pygame.image.load("assets/gun/classic/classicRight.png"),
            'back' : pygame.image.load("assets/gun/classic/classicRight.png"),
            'right' : pygame.image.load("assets/gun/classic/classicRight.png"),
            'left' : pygame.image.load("assets/gun/classic/classicRight.png"),
            'back right' : pygame.image.load("assets/gun/classic/classicRight.png"),
            'back left' : pygame.image.load("assets/gun/classic/classicRight.png"),
            'front right' : pygame.image.load("assets/gun/classic/classicRight.png"),
            'front left' : pygame.image.load("assets/gun/classic/classicRight.png")
        }

    def shoot_bullet(self, start_pos, target_pos):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shooting_speed * 1000:
            bullet = Bullet(start_pos, target_pos, self.damage)
            self.last_shot_time = current_time
            return bullet
        return None
    
class Bullet:
    def __init__(self, start_pos, target_pos, damage):
        self.x, self.y = start_pos
        self.target_x, self.target_y = target_pos
        self.damage = damage
        self.speed = 20
        self.direction = math.atan2(self.target_y - self.y, self.target_x - self.x)
        self.radius = 7.5
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius *2)

    def move(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.x), int(self.y)), self.radius)