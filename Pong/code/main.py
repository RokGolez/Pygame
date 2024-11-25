from settings import * 
from sprites import *
import json

class Game: 
    def __init__ (self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.running = True

        # sprites
        self.all_sprites = pygame.sprite.Group()
        self.paddle_sprites = pygame.sprite.Group()
        self.player = Player((self.all_sprites,self.paddle_sprites))
        self.ball = Ball(self.all_sprites,self.paddle_sprites, self.update_score)
        Opponent((self.all_sprites, self.paddle_sprites), self.ball)
        
        # score
        self.score = {"player": 0, "opponent": 0}
        self.font = pygame.font.Font(None, 150)
    
    def display_score(self):
        # player
        player_surf = self.font.render(str(self.score["player"]), True, COLOURS["bg detail"])
        player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2))
        self.display_surf.blit(player_surf, player_rect)
        
        # opponent
        opponent_surf = self.font.render(str(self.score["opponent"]), True, COLOURS["bg detail"])
        opponent_rect = opponent_surf.get_frect(center = (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.display_surf.blit(opponent_surf, opponent_rect)
        
        # line
        pygame.draw.line(self.display_surf, COLOURS["bg detail"], (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT), 10)
    
    def update_score(self,side):
        self.score ["player" if side == "player" else "opponent"] += 1
    
    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
                    
            # update
            self.all_sprites.update(dt)
            
            # draw
            self.display_surf.fill(COLOURS["bg"])
            self.display_score()
            self.all_sprites.draw(self.display_surf)
            pygame.display.update()
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
    