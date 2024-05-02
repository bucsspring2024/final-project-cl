import pygame
import random

class Room:
    def __init__(self, background_image, boundaries, obstacles = None, signs = None, text_image = None, dummy = None):
        self.background_image = background_image
        self.boundaries = boundaries
        self.obstacles = obstacles if obstacles else []
        self.signs = signs if signs else []
        self.text_image = text_image
        self.dummy = dummy
        self.collision_rects = []
        self.dummies = []
        
        for obstacle in self.obstacles:
            if obstacle == "pit":
                self.collision_rects.append(pygame.Rect(760, 20, 130, 560))
            if obstacle == "wall":
                self.collision_rects.append(pygame.Rect(820, 20, 40, 560))
            if obstacle == "big pit":
                self.collision_rects.append(pygame.Rect(520, 20, 300, 560))
        
        for start_pos, end_pos in zip(boundaries, boundaries[1:] + [boundaries[0]]):
            self.collision_rects.append(pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
            
class gameController:
    def __init__(self):
        self.current_room = None
        self.rooms = [
            Room(background_image="assets/room/backgroundRoom1", boundaries=[(0, 0), (1000, 0), (1000, 600), (0, 600)], obstacles = ["pit"], signs = [pygame.Rect(650, 200, 50, 100)], text_image="assets/text/room1Text.png"),
            Room(background_image="assets/room/backgroundRoom2", boundaries=[(0, 0), (1000, 0), (1000, 600), (0, 600)], obstacles = ["wall"], signs = [pygame.Rect(750, 200, 50, 100)], text_image="assets/text/room2Text.png"),
            Room(background_image="assets/room/backgroundRoom3", boundaries=[(0, 0), (1000, 0), (1000, 600), (0, 600)], obstacles = ["big pit"], signs = [pygame.Rect(450, 200, 50, 100)], text_image="assets/text/room3Text.png"),
            Room(background_image="assets/room/backgroundRoom4", boundaries=[(0, 0), (1000, 0), (1000, 600), (0, 600)], signs = [pygame.Rect(150, 200, 50, 100)], text_image="assets/text/room4Text.png"),
            Room(background_image="assets/room/backgroundRoom5", boundaries=[(0, 0), (1000, 0), (1000, 600), (0, 600)], signs = [pygame.Rect(150, 200, 50, 100)], text_image="assets/text/room5Text.png", dummy = "assets/dummy.png"),
            Room(background_image="assets/room/backgroundRoom1", boundaries=[(0, 0), (1000, 0), (1000, 600), (0, 600)])
        ]
        
        self.current_room_index = 0  # Start with the first room
        self.change_room(0)

    def change_room(self, room_index):
        self.current_room_index = room_index
        self.current_room = self.rooms[room_index]
        
        if room_index == 4:
            self.spawn_dummies(3)
        
    def get_current_room(self):
        return self.current_room

    def spawn_dummies(self, num_dummies):
        current_room = self.get_current_room()
        dummy_images = []
        dummy_positions = []
        
        dummy_image = pygame.image.load(current_room.dummy)
        dummy_width = dummy_image.get_width()
        dummy_height = dummy_image.get_height()
        scaled_width = dummy_width * 2
        scaled_height = dummy_height * 2
        
        available_area = (current_room.boundaries[1][0] - dummy_width, current_room.boundaries[2][1] - dummy_height)
        
        for i in range(num_dummies):
            x = random.randint(current_room.boundaries[0][0], available_area[0])
            y = random.randint(current_room.boundaries[0][1], available_area[1])
            dummy_positions.append((x,y))
            scaled_dummy_image = pygame.transform.scale(dummy_image, (scaled_width, scaled_height))
            dummy_images.append(scaled_dummy_image)
            
        current_room.dummies = list(zip(dummy_images, dummy_positions))

    def handle_input(self):
        # Handle player input to move Jett or interact with objects in the room
        pass

    def update(self, jett):
        current_room = self.get_current_room()
        
        if current_room.dummies:
            if jett.x > 950:
                jett.x = 950
                
        for obstacle_rect in current_room.collision_rects:
            if obstacle_rect.colliderect(jett.rect):
                if "pit" in current_room.obstacles and not jett.is_dashing and not jett.updraft_timer:
                    jett.x = 25
                    jett.y = 250
                elif "wall" in current_room.obstacles and not jett.updraft_timer:
                    if jett.direction == 'right':
                        jett.x = 800
                    elif jett.direction == 'left':
                        jett.x = 865
                elif "big pit" in current_room.obstacles and not jett.is_dashing and not jett.updraft_timer:
                    jett.x = 25
                    jett.y = 250
                break
                
    def draw(self, screen, jett):
        current_room = self.get_current_room()
        
        for sign_rect in current_room.signs:
            sign_image = pygame.image.load("assets/room/sign.png")
            sign_image = pygame.transform.scale(sign_image, (sign_image.get_width() * 3, sign_image.get_height() * 3))
            screen.blit(sign_image, sign_rect)
        
        for dummy_image, (x, y) in current_room.dummies:
            screen.blit(dummy_image, (x, y))
            
        for sign_rect in current_room.signs:
            if sign_rect.colliderect(jett.rect):
                if current_room.text_image:
                    text_image = pygame.image.load(current_room.text_image)
                    screen.blit(text_image, (175, 425))
                break
            
    def main_loop(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()