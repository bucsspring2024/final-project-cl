import pygame
from src.jett import Jett
from src.room import gameController

class Controller:
    def __init__(self):
        pygame.init()
        self.screen_width = 1000
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Enter Valorant")
        self.clock = pygame.time.Clock()
        self.current_state = "menu"
        self.jett = None
        
        self.dash_cooldown = 500
        self.smoke_cooldown = 600
        self.updraft_cooldown = 2000
        
        self.last_dash_time = 0
        self.last_smoke_time = 0
        self.last_updraft_time = 0

        self.game_controller = gameController()
        self.current_room = self.game_controller.current_room.background_image
        
        self.start_time = 0
        self.best_times = [999,999.0]
        
    def mainloop(self):
        while True:
            if self.current_state == "menu":
                self.menuloop()
            elif self.current_state == "agent selection":
                self.agentloop()
            elif self.current_state == "game":
                self.gameloop()
            elif self.current_state == "gameover":
                self.gameoverloop()

    def menuloop(self):
        background_image = pygame.image.load("assets/background.png").convert()
        background_image = pygame.transform.scale(background_image, (self.screen_width, self.screen_height))
        background_rect = background_image.get_rect()
        
        show_text = True
        last_toggle_time = pygame.time.get_ticks()
        blink_interval = 500
        
        while self.current_state == "menu":
            current_time = pygame.time.get_ticks()
            if current_time - last_toggle_time >= blink_interval:
                show_text = not show_text
                last_toggle_time = current_time
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.current_state = "agent selection"
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()

            self.screen.blit(background_image, background_rect)
            
            if show_text:
                font = pygame.font.Font(None, 36)
                text = font.render("Press SPACE to Start", True, "white")
                text2 = font.render("Press ESCAPE to Quit", True, "white")
                text_rect = text.get_rect(center=(200, 500))
                text2_rect = text2.get_rect(center = (200, 550))
                self.screen.blit(text, text_rect)
                self.screen.blit(text2, text2_rect)

            pygame.display.flip()
            self.clock.tick(60)
    
    def agentloop(self):
        background_image = pygame.image.load("assets/agentSelection.png").convert()
        background_image = pygame.transform.scale(background_image, (self.screen_width, self.screen_height))
        
        text_box = pygame.image.load("assets/text/agentSelectionJett.png").convert()
        sign_image = pygame.image.load("assets/room/sign.png").convert()
        sign_image = pygame.transform.scale(sign_image, (sign_image.get_width() * 3, sign_image.get_height() * 3))
        sign_rect = sign_image.get_rect(center = (800, 250))
        
        room_left = 20
        room_top = 0
        room_right = self.screen_width - 70
        room_bottom = self.screen_height - 90
        
        self.enable_movement = False
        
        self.jett = Jett(speed = 3.5)
        self.jett.x = 475
        self.jett.y = 250
        
        while self.current_state == "agent selection":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.enable_movement = True
                    elif event.key == pygame.K_ESCAPE:
                        self.current_state = "menu"
            
            if self.jett.x < room_left:
                self.jett.x = room_left
            if self.jett.x > room_right and self.jett.y < 200:
                self.jett.x = room_right
            if self.jett.x > room_right and self.jett.y > 275:
                self.jett.x = room_right
            if self.jett.y < room_top:
                self.jett.y = room_top
            if self.jett.y > room_bottom:
                self.jett.y = room_bottom
            
            if self.jett.x > 950 and self.jett.y > 200 and self.jett.y < 275:
                self.current_state = "game"
            
            if self.enable_movement:
                self.jett.move()
                self.jett.update_animation()

            self.screen.blit(background_image, (0,0))
            
            sign_text = pygame.image.load("assets/text/agentSelectionText.png")
            self.screen.blit(sign_image,sign_rect)
            
            if sign_rect.colliderect(self.jett.rect):
                self.screen.blit(sign_text, (200, 475))
            
            self.jett.drawCharacter(self.screen)
            if not self.enable_movement:
                self.screen.blit(text_box, (262.5, 450))
            pygame.display.flip()
            self.clock.tick(60)

    def gameloop(self):
        self.start_time = pygame.time.get_ticks()
        
        self.jett = Jett(speed=5)

        bullets = []
        
        draw_gun = False
        
        self.game_controller.change_room(0)
        current_room = self.game_controller.get_current_room()

        while self.current_state == "game":
            for bullet in bullets:
                for dummy_image, (dummy_x, dummy_y) in current_room.dummies:
                    dummy_rect = pygame.Rect(dummy_x, dummy_y, dummy_image.get_width(), dummy_image.get_height())
                    if dummy_rect.colliderect(bullet.rect):
                        current_room.dummies.remove((dummy_image, (dummy_x, dummy_y)))
                        bullets.remove(bullet)
                        break
                
            for i in range(len(current_room.boundaries)):
                start_pos = current_room.boundaries[i]
                end_pos = current_room.boundaries[(i + 1) % len(current_room.boundaries)]
                pygame.draw.line(self.screen, "black", start_pos, end_pos)
            
            background_image = pygame.image.load(current_room.background_image + ".png").convert()
            screen_width, screen_height = self.screen.get_size()
            scaled_background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
            self.screen.blit(scaled_background_image, (0,0))
            
            room_left = 20
            room_top = 20
            room_right = self.screen_width - 70
            room_bottom = self.screen_height - 90           
            
            if self.jett.x < room_left:
                self.jett.x = room_left
            if self.jett.x > room_right and self.jett.y < 200:
                self.jett.x = room_right
            if self.jett.x > room_right and self.jett.y > 275:
                self.jett.x = room_right
            if self.jett.y < room_top:
                self.jett.y = room_top
            if self.jett.y > room_bottom:
                self.jett.y = room_bottom
                
            self.game_controller.update(self.jett)
            self.game_controller.draw(self.screen, self.jett) 
                
            if self.jett.updraft_timer:
                self.jett.speed = 2
            
            if self.jett.x + self.jett.width >= screen_width and self.jett.y > current_room.boundaries[1][1] and self.jett.y < current_room.boundaries[3][1]:
                next_room_index = (self.game_controller.current_room_index + 1) % len(self.game_controller.rooms)
                if next_room_index != self.game_controller.current_room_index:
                    self.game_controller.change_room(next_room_index)
                    current_room = self.game_controller.get_current_room()
                    self.jett.x = 0
                    self.jett.reset_smoke_particles()
                    if next_room_index == len(self.game_controller.rooms) - 1:
                        self.current_state = "gameover"
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    current_time = pygame.time.get_ticks()
                    if event.key == pygame.K_ESCAPE:
                        self.current_state = "agent selection"
                    elif event.key == pygame.K_e:
                        if current_time - self.last_dash_time >= self.dash_cooldown:
                            self.jett.dash()
                            self.last_dash_time = current_time
                    elif event.key == pygame.K_q:
                        current_time = pygame.time.get_ticks()
                        if current_time - self.last_updraft_time >= self.updraft_cooldown:
                            self.jett.updraft()
                            self.last_updraft_time = current_time
                    elif event.key == pygame.K_c:
                        current_time = pygame.time.get_ticks()
                        if current_time - self.last_smoke_time >= self.smoke_cooldown:
                            mouse_position = pygame.mouse.get_pos()
                            self.jett.smoke(mouse_position)
                            self.last_smoke_time = current_time
                    elif event.key == pygame.K_2:
                        draw_gun = True
                        self.jett.images = {key:[pygame.image.load(path) for path in paths] for key, paths in self.jett.image_paths_gun.items()}
                        self.jett.speed = 4.5
                    elif event.key == pygame.K_3:
                        draw_gun = False
                        self.jett.images = {key: [pygame.image.load(path) for path in paths] for key, paths in self.jett.image_paths.items()}
                        self.jett.speed = 5
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if draw_gun and not self.jett.is_dashing and not self.jett.updraft_timer and current_time - self.last_smoke_time >= 500:
                        mouse_position = pygame.mouse.get_pos()
                        self.jett.look(mouse_position)
                        bullet = self.jett.shoot(mouse_position)
                        if bullet is not None:
                            bullets.append(bullet)

            self.jett.move()
            self.jett.update(self.screen)
            self.jett.drawCharacter(self.screen, draw_gun)
            self.jett.draw_smoke(self.screen)

            for bullet in bullets:
                bullet.move()
                bullet.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

    def gameoverloop(self):
        end_time = pygame.time.get_ticks()
        elapsed_time = float((end_time - self.start_time) // 1000)
        
        if elapsed_time < min(self.best_times):
            self.best_times.append(elapsed_time)
            
        shortest_time = min(self.best_times)
        
        while self.current_state == "gameover":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.current_state = "game"
                    elif event.key == pygame.K_ESCAPE:
                        self.current_state = "menu"

            self.screen.fill("black")
            font = pygame.font.Font(None, 36)
            text = font.render("Course Completed! Press ENTER to Restart, Press ESCAPE to Quit", True, "white")
            time = font.render("Time: {} seconds".format(elapsed_time), True, "white")
            
            self.best_times.append(elapsed_time)
            shortest_time = min(self.best_times)
            
            best = font.render("Best Time: {} seconds".format(shortest_time), True, "white")
            text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            time_rect = time.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 25))
            best_rect = best.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 45))
            self.screen.blit(text, text_rect)
            self.screen.blit(time, time_rect)
            self.screen.blit(best, best_rect)

            pygame.display.flip()
            self.clock.tick(60)