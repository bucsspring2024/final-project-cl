import pygame
import sys
sys.path.insert(0, '/Users/chenlin/github-classroom/bucsspring2024/final-project-cl')
import main
from main import Jett

class Controller:
  
  def __init__(self):
    pygame.init()
    self.screen_width = 1000
    self.screen_height = 750
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("Enter Valorant")
    self.clock = pygame.time.Clock()
    
    self.current_state = "menu"
    #setup pygame data
    
  def mainloop(self):
    while True:
      if self.current_state == "menu":
        self.menuloop()
      elif self.current_state == "game":
        self.gameloop()
      elif self.current_state == "gameover":
        self.gameoverloop()
  
  ### below are some sample loop states ###

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
            
      self.screen.fill(("black"))
      font = pygame.font.Font(None, 36)
      text = font.render("Press SPACE to Start", True, ("white"))
      text_rect = text.get_rect(center = (self.screen_width // 2, self.screen_height // 2))
      self.screen.blit(text, text_rect)

      pygame.display.flip()
      self.clock.tick(60)
      
  def gameloop(self):
    jett = Jett(5, main.Classic)
    
    while self.current_state == "game":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.current_state = "gameover"
            
      self.screen.fill("gray")
      
      gap = 40
      for i in range(gap, self.screen_width, gap):
        pygame.draw.line(self.screen, "black", [i, 0], [i, 750])
      for i in range(gap, self.screen_height, gap):
        pygame.draw.line(self.screen, "black", [0, i], [1000, i])

      jett.move()

      jett.drawCharacter(self.screen)
      
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
      text_rect = text.get_rect(center = (self.screen_width // 2, self.screen_height // 2))
      self.screen.blit(text, text_rect)
      
      pygame.display.flip()
      self.clock.tick(60)
          
if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
