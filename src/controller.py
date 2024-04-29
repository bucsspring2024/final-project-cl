import pygame
from src.jett import Jett

class Controller:
    def __init__(self):
        pygame.init()
        self.screen_width = 1000
        self.screen_height = 750
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Enter Valorant")
        self.clock = pygame.time.Clock()
        self.current_state = "menu"
        self.jett = None
        
        self.dash_cooldown = 500
        self.smoke_cooldown = 600
        self.updraft_cooldown = 2000
        self.present = pygame.time.get_ticks()

    def mainloop(self):
        while True:
            if self.current_state == "menu":
                self.menuloop()
            elif self.current_state == "game":
                self.gameloop()
            elif self.current_state == "gameover":
                self.gameoverloop()

    def menuloop(self):
        while self.current_state == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.current_state = "game"
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()

            self.screen.fill("black")
            font = pygame.font.Font(None, 36)
            text = font.render("Press SPACE to Start", True, "white")
            text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(text, text_rect)

            pygame.display.flip()
            self.clock.tick(60)

    def gameloop(self):
        if self.jett is None:
            self.jett = Jett(speed=5)

        bullets = []

        while self.current_state == "game":
            self.screen.fill("gray")
            
            gap = 40
            
            for i in range(gap, self.screen_width, gap):
                pygame.draw.line(self.screen, "black", [i, 0], [i, 750])
            for i in range(gap, self.screen_height, gap):
                pygame.draw.line(self.screen, "black", [0, i], [1000, i])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.current_state = "gameover"
                    elif event.key == pygame.K_e:
                        current_time = pygame.time.get_ticks()
                        if current_time - self.present >= self.dash_cooldown:
                            self.jett.dash()
                            self.present = current_time
                    elif event.key == pygame.K_q:
                        current_time = pygame.time.get_ticks()
                        if current_time - self.present >= self.updraft_cooldown:
                            self.jett.updraft()
                            self.present = current_time
                    elif event.key == pygame.K_c:
                        current_time = pygame.time.get_ticks()
                        if current_time - self.present >= self.smoke_cooldown:
                            mouse_position = pygame.mouse.get_pos()
                            self.jett.smoke(mouse_position)
                            self.present = current_time
                    elif event.key == pygame.K_2:
                        self.jett.images = {key:[pygame.image.load(path) for path in paths] for key, paths in self.jett.image_paths_gun.items()}
                        self.jett.speed = 4.5
                    elif event.key == pygame.K_3:
                        self.jett.images = {key: [pygame.image.load(path) for path in paths] for key, paths in self.jett.image_paths.items()}
                        self.jett.speed = 5
                    elif event.key == pygame.K_1:
                        self.jett.speed = 4
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    self.jett.look(mouse_position)
                    bullet = self.jett.shoot(mouse_position)
                    bullets.append(bullet)

            self.jett.move()
            self.jett.update(self.screen)
            self.jett.drawCharacter(self.screen)
            self.jett.draw_smoke(self.screen)

            for bullet in bullets:
                bullet.move()
                bullet.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

    def gameoverloop(self):
        while self.current_state == "gameover":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.current_state = "menu"

            self.screen.fill("red")
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over! Press ENTER to Restart", True, "white")
            text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(text, text_rect)

            pygame.display.flip()
            self.clock.tick(60)