import pygame
import math
from src.gun import Classic

class Jett:
    def __init__(self, speed):
        self.speed = speed
        self.gun = Classic()
        self.gun_offset = (20, 0)
        self.gun_angle = 270
        self.width = 16
        self.height = 24
        self.x = 25
        self.y = 250
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image_paths = {
            'front': ["assets/jettStanding/JettFront.png", "assets/jettWalking/front/JettFrontWalking1.png", "assets/jettWalking/front/JettFrontWalking2.png", "assets/jettWalking/front/JettFrontWalking3.png"],
            'back': ["assets/jettStanding/JettBack.png", "assets/jettWalking/back/JettBackWalking1.png", "assets/jettWalking/back/JettBackWalking2.png", "assets/jettWalking/back/JettBackWalking3.png"],
            'left': ["assets/jettStanding/JettLeft.png", "assets/jettWalking/left/JettLeftWalking1.png", "assets/jettWalking/left/JettLeftWalking2.png", "assets/jettWalking/left/JettLeftWalking3.png"],
            'right': ["assets/jettStanding/JettRight.png", "assets/jettWalking/right/JettRightWalking1.png", "assets/jettWalking/right/JettRightWalking2.png", "assets/jettWalking/right/JettRightWalking3.png"],
            'back right': ["assets/jettStanding/JettBackRight.png", "assets/jettWalking/back right/JettBackRightWalking1.png", "assets/jettWalking/back right/JettBackRightWalking2.png", "assets/jettWalking/back right/JettBackRightWalking3.png"],
            'back left': ["assets/jettStanding/JettBackLeft.png", "assets/jettWalking//back left/JettBackLeftWalking1.png", "assets/jettWalking//back left/JettBackLeftWalking2.png", "assets/jettWalking//back left/JettBackLeftWalking3.png"],
            'front right': ["assets/jettStanding/JettFront.png", "assets/jettWalking/front/JettFrontWalking1.png", "assets/jettWalking/front/JettFrontWalking2.png", "assets/jettWalking/front/JettFrontWalking3.png"],
            'front left': ["assets/jettStanding/JettFront.png", "assets/jettWalking/front/JettFrontWalking1.png", "assets/jettWalking/front/JettFrontWalking2.png", "assets/jettWalking/front/JettFrontWalking3.png"]
        }
        
        self.images = {key: [pygame.image.load(path) for path in paths] for key, paths in self.image_paths.items()}
        
        self.direction = 'front'
        self.is_walking = False
        self.is_dashing = False
        self.dash_distance = 30
        self.dash_speed = 100
        self.dash_timer = 0
        
        self.dash_images = {
            'front': pygame.image.load("assets/jettDashing/JettDashFront.png"),
            'back': pygame.image.load("assets/jettDashing/JettDashBack.png"),
            'left': pygame.image.load("assets/jettDashing/JettDashLeft.png"),
            'right': pygame.image.load("assets/jettDashing/JettDashRight.png"),
            'back right': pygame.image.load("assets/jettDashing/JettDashBackRight.png"),
            'back left': pygame.image.load("assets/jettDashing/JettDashBackLeft.png"),
            'front right': pygame.image.load("assets/jettDashing/JettDashRight.png"),
            'front left': pygame.image.load("assets/jettDashing/JettDashLeft.png")
            }
        
        self.updraft_images = {
            'front': pygame.image.load("assets/jettUpdraft/JettUpdraftRight.png"),
            'back' : pygame.image.load("assets/jettUpdraft/JettUpdraftRight.png"),
            'left': pygame.image.load("assets/jettUpdraft/JettUpdraftLeft.png"),
            'right': pygame.image.load("assets/jettUpdraft/JettUpdraftRight.png"),
            'back right': pygame.image.load("assets/jettUpdraft/JettUpdraftRight.png"),
            'back left': pygame.image.load("assets/jettUpdraft/JettUpdraftLeft.png"),
            'front right': pygame.image.load("assets/jettUpdraft/JettUpdraftRight.png"),
            'front left': pygame.image.load("assets/jettUpdraft/JettUpdraftLeft.png")
        }
        
        self.throw_smoke_images = {
            'front': pygame.image.load("assets/jettSmoke/JettSmokeFront.png"),
            'back' : pygame.image.load("assets/jettSmoke/JettSmokeBack.png"),
            'left': pygame.image.load("assets/jettSmoke/JettSmokeLeft.png"),
            'right': pygame.image.load("assets/jettSmoke/JettSmokeRight.png"),
            'back right': pygame.image.load("assets/jettSmoke/JettSmokeBackRight.png"),
            'back left': pygame.image.load("assets/jettSmoke/JettSmokeBackLeft.png"),
            'front right': pygame.image.load("assets/jettSmoke/JettSmokeRight.png"),
            'front left': pygame.image.load("assets/jettSmoke/JettSmokeLeft.png")
        }
        
        self.image_paths_gun = {
            'front': ["assets/jettStandingGun/JettFrontGun.png", "assets/jettWalkingGun/front/JettFrontWalkingGun1.png", "assets/jettWalkingGun/front/JettFrontWalkingGun2.png", "assets/jettWalkingGun/front/JettFrontWalkingGun3.png"],
            'back': ["assets/jettStandingGun/JettBackGun.png", "assets/jettWalkingGun/back/JettBackWalkingGun1.png", "assets/jettWalkingGun/back/JettBackWalkingGun2.png", "assets/jettWalkingGun/back/JettBackWalkingGun3.png"],
            'left': ["assets/jettStandingGun/JettLeftGun.png", "assets/jettWalkingGun/left/JettLeftWalkingGun1.png", "assets/jettWalkingGun/left/JettLeftWalkingGun2.png", "assets/jettWalkingGun/left/JettLeftWalkingGun3.png"],
            'right': ["assets/jettStandingGun/JettRightGun.png", "assets/jettWalkingGun/right/JettRightWalkingGun1.png", "assets/jettWalkingGun/right/JettRightWalkingGun2.png", "assets/jettWalkingGun/right/JettRightWalkingGun3.png"],
            'back right': ["assets/jettStandingGun/JettBackRightGun.png", "assets/jettWalkingGun/back right/JettBackRightWalkingGun1.png", "assets/jettWalkingGun/back right/JettBackRightWalkingGun2.png", "assets/jettWalkingGun/back right/JettBackRightWalkingGun3.png"],
            'back left': ["assets/jettStandingGun/JettBackLeftGun.png", "assets/jettWalkingGun//back left/JettBackLeftWalkingGun1.png", "assets/jettWalkingGun/back left/JettBackLeftWalkingGun2.png", "assets/jettWalkingGun/back left/JettBackLeftWalkingGun3.png"],
            'front right': ["assets/jettStandingGun/JettFrontGun.png", "assets/jettWalkingGun/front/JettFrontWalkingGun1.png", "assets/jettWalkingGun/front/JettFrontWalkingGun2.png", "assets/jettWalkingGun/front/JettFrontWalkingGun3.png"],
            'front left': ["assets/jettStandingGun/JettFrontGun.png", "assets/jettWalkingGun/front/JettFrontWalkingGun1.png", "assets/jettWalkingGun/front/JettFrontWalkingGun2.png", "assets/jettWalkingGun/front/JettFrontWalkingGun3.png"]
        }
        
        self.gun_offset = {
            'front': (45, 60),
            'back': (40, 40),
            'left': (0, 55),
            'right': (45,55),
            'back right': (15, 50),
            'back left': (40, 50),
            'front right': (20, 0),
            'front left': (20,0)
        }
        
        self.smoke_image = pygame.image.load("assets/jettSmoke/SmokeBall.png")
        self.smoke_speed = 10
        self.smoke_particles = []
        self.last_smoke_trigger_time = 0
        
        self.current_frame = 0
        self.animation_speed = 0.25
        self.last_update_time = pygame.time.get_ticks()
        
        self.updraft_timer = None
        
    def drawCharacter(self, screen, draw_gun = False):
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        
        is_any_movement_key_pressed = any(keys[key] for key in [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s])
        
        if self.is_dashing:
            if self.direction in self.dash_images:
                dash_image = self.dash_images[self.direction]
                scaled_dash_image = pygame.transform.scale(dash_image, (self.width * 3, self.height * 2.5))
                screen.blit(scaled_dash_image, (self.x, self.y))
        elif self.updraft_timer:
            updraft_sprite = self.updraft_images[self.direction]
            scaled_sprite = pygame.transform.scale(updraft_sprite, (self.width * 3, self.height * 2.5))
            screen.blit(scaled_sprite, (self.x, self.y))
        elif is_any_movement_key_pressed:
            current_image_list = self.images.get(self.direction)
            if current_image_list:
                current_image = current_image_list[self.current_frame]
                scaled_image = pygame.transform.scale(current_image, (self.width * 3, self.height * 3))
                screen.blit(scaled_image, (self.x, self.y))
        elif current_time - self.last_smoke_trigger_time < 500:
            if self.smoke_particles:
                smoke_image = self.throw_smoke_images[self.direction]
                scaled_smoke_image = pygame.transform.scale(smoke_image, (self.width * 3, self.height * 3))
                screen.blit(scaled_smoke_image, (self.x, self.y))
    
        else:
            current_image_list = self.images.get(self.direction)
            if current_image_list:
                current_image = current_image_list[0]
                scaled_image = pygame.transform.scale(current_image, (self.width * 3, self.height * 3))
                screen.blit(scaled_image, (self.x, self.y))
        
        if draw_gun and not self.is_dashing and not self.updraft_timer and not (current_time - self.last_smoke_trigger_time < 500):
            gun_image = pygame.transform.rotate(self.gun.image[self.direction], -self.gun_angle)
            if self.direction in ['left', 'back left', 'front left']:
                gun_image = pygame.transform.rotate(pygame.transform.flip(pygame.image.load("assets/gun/classic/classicLeft.png"), True, True), -self.gun_angle)
            gun_rect = gun_image.get_rect(center = (self.x + self.gun_offset.get(self.direction, (0,0))[0], self.y + self.gun_offset.get(self.direction, (0,0))[1]))
            screen.blit(gun_image, gun_rect)
        
    def move(self):
        keys = pygame.key.get_pressed()
        
        is_any_movement_key_pressed = any(keys[key] for key in [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s])
        
        self.is_walking = is_any_movement_key_pressed
                    
        if not self.is_dashing:
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
            if keys[pygame.K_w] and keys[pygame.K_a]:
                self.direction = 'back left'
            if keys[pygame.K_s] and keys[pygame.K_a]:
                self.direction = 'front left'
            if keys[pygame.K_s] and keys[pygame.K_d]:
                self.direction = 'front right'
                
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def look(self, mouse_position):
        dx = mouse_position[0] - (self.x + self.gun_offset.get(self.direction, (0, 0))[0])
        dy = mouse_position[1] - (self.y + self.gun_offset.get(self.direction, (0, 0))[1])
        self.gun_angle = math.degrees(math.atan2(dy,dx))
        angle = math.atan2(dy, dx)
        angle_degrees = math.degrees(angle)
        
        if -22.5 < angle_degrees <= 45:
            self.direction = 'right'
        elif 45 < angle_degrees <= 135:
            self.direction = 'front'
        elif 135 < angle_degrees <= 202.5:
            self.direction = 'left'
        elif -157.5 < angle_degrees <= -112.5:
            self.direction = 'back left'
        elif -112.5 < angle_degrees <= -67.5:
            self.direction = 'back'
        elif -67.5 < angle_degrees <= -22.5:
            self.direction = 'back right'
    
    def shoot(self, mouse_position):
        start_pos = (self.x + self.gun_offset.get(self.direction, (0, 0))[0], self.y + self.gun_offset.get(self.direction, (0, 0))[1])
        target_pos = mouse_position
        bullet = self.gun.shoot_bullet(start_pos, target_pos)
        return bullet
    
    def dash(self):
        if not self.is_dashing:
            self.is_dashing = True
            self.dash_timer = pygame.time.get_ticks()
    
    def updraft(self):
        if not self.updraft_timer:
            self.is_dashing = False
            self.updraft_timer = pygame.time.get_ticks()
    
    def smoke(self, mouse_position):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_smoke_trigger_time >= 500:
            self.last_smoke_trigger_time = current_time
            
        click_x, click_y = mouse_position
        start_pos = (self.x, self.y)

        dx = click_x - start_pos[0]
        dy = click_y - start_pos[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)

        unit_x = dx / distance
        unit_y = dy / distance

        target_pos = (start_pos[0] + unit_x * 250, start_pos[1] + unit_y * 250)

        self.smoke_particles.append({
                "position": start_pos,
                "target": target_pos,
                "velocity": (unit_x * self.smoke_speed, unit_y * self.smoke_speed),
                "scale_factor": 1.0,
                "max_scale_factor": 2.0,
                "lifespan": 300
            })
        
        self.look(target_pos)

    def update(self, screen):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_speed * 1000:
            self.last_update_time = current_time
            self.current_frame = (self.current_frame + 1) % len(self.images[self.direction])
            
        if self.is_dashing:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.dash_timer
            
            if elapsed_time < self.dash_distance / self.dash_speed * 1000:
                move_distance = self.dash_speed * (elapsed_time / 1000)
                
                if self.direction == 'front':
                    self.y += move_distance
                elif self.direction == 'back':
                    self.y -= move_distance
                elif self.direction == 'left':
                    self.x -= move_distance
                elif self.direction == 'right':
                    self.x += move_distance
                elif self.direction == 'back left':
                    self.x -= move_distance / math.sqrt(2)
                    self.y -= move_distance / math.sqrt(2)
                elif self.direction == 'back right':
                    self.x += move_distance / math.sqrt(2)
                    self.y -= move_distance / math.sqrt(2)
                elif self.direction == 'front left':
                    self.x -= move_distance / math.sqrt(2)
                    self.y += move_distance / math.sqrt(2)
                elif self.direction == 'front right':
                    self.x += move_distance / math.sqrt(2)
                    self.y += move_distance / math.sqrt(2)
            else:
                self.is_dashing = False
        elif self.updraft_timer:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.updraft_timer
            if elapsed_time < 400:
                self.y -= 4
            elif elapsed_time < 2000:
                self.y += 1
            else:
                self.speed = 5
                self.is_dashing = False
                self.updraft_timer = None
        for smoke_particle in self.smoke_particles:
            if smoke_particle["lifespan"] > 0:
                if not smoke_particle.get("stopped", False):
                    smoke_particle["position"] = (smoke_particle["position"][0] + smoke_particle["velocity"][0],
                                                  smoke_particle["position"][1] + smoke_particle["velocity"][1])
                    smoke_particle["lifespan"] -= 1

                    if math.hypot(smoke_particle["position"][0] - smoke_particle["target"][0],
                                   smoke_particle["position"][1] - smoke_particle["target"][1]) < 5:
                        smoke_particle["stopped"] = True
                        smoke_particle["velocity"] = (0, 0)
                else:
                    if smoke_particle["scale_factor"] < smoke_particle["max_scale_factor"]:
                        smoke_particle["scale_factor"] = min(smoke_particle["scale_factor"] + 0.02,
                                                          smoke_particle["max_scale_factor"])
                    
                scaled_smoke_image = pygame.transform.scale(self.smoke_image,
                                                            (int(self.smoke_image.get_width() * smoke_particle["scale_factor"]),
                                                             int(self.smoke_image.get_height() * smoke_particle["scale_factor"])))
                screen.blit(scaled_smoke_image, smoke_particle["position"])

            smoke_particle["lifespan"] -= 1
            if smoke_particle["lifespan"] <= 0:
                self.smoke_particles.remove(smoke_particle)
                
    def draw_smoke(self, screen):
        for smoke_particle in self.smoke_particles:
            scaled_smoke_image = pygame.transform.scale(self.smoke_image,
                                                    (int(self.smoke_image.get_width() * smoke_particle["scale_factor"]),
                                                     int(self.smoke_image.get_height() * smoke_particle["scale_factor"])))
            screen.blit(scaled_smoke_image, smoke_particle["position"])
            
    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_speed * 1000:
            self.last_update_time = current_time
            self.current_frame = (self.current_frame + 1) % len(self.images[self.direction])
    
    def reset_smoke_particles(self):
        self.smoke_particles = []