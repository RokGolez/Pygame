from settings import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        # image
        self.image = pygame.Surface(SIZE["paddle"])
        pygame.draw.rect(self.image, COLOURS['paddle'], pygame.FRect((0, 0), SIZE['paddle']), 0, 4)
            
        # rect & movement        
        self.rect = self.image.get_frect(center=POS["player"])
        self.old_rect = self.rect.copy()  # Save the initial state
        self.direction = 0
        
    def move(self,dt):
        self.rect.centery += self.direction * self.speed * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom    
        
    def update(self, dt):
        self.old_rect = self.rect.copy()  # Save the current position
        self.get_direction()
        self.move(dt)
        
class Player(Paddle):
    def __init__(self, groups):
        super().__init__(groups)
        self.speed = SPEED["player"] 
        
    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = (int(keys[pygame.K_DOWN]) or int(keys[pygame.K_s])) - (int(keys[pygame.K_UP]) or int(keys[pygame.K_w]))
    
class Opponent(Paddle):
    def __init__(self, groups, ball):
        super().__init__(groups)
        self.speed = SPEED["opponent"] 
        self.rect.center = POS["opponent"]
        self.ball = ball
    
    def get_direction(self):
        self.direction = 1 if self.ball.rect.centery > self.rect.centery else - 1
        
class Ball(pygame.sprite.Sprite):
    def __init__(self,groups, paddle_sprites, update_score):
        super().__init__(groups)
        self.paddle_sprites = paddle_sprites       
        self.update_score = update_score      
        # image
        self.image = pygame.Surface(SIZE["ball"], pygame.SRCALPHA)
        pygame.draw.circle(self.image, COLOURS["ball"], (SIZE["ball"][0] / 2, SIZE["ball"][1] / 2), SIZE["ball"][0] / 2)
       
        # rect and movement
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/ 2 ))
        self.old_rect = self.rect.copy()
        self.direction = pygame.Vector2(choice((1,-1)),(uniform(0.7,0.8) * choice((-1,1))))
    
    def move(self, dt):
        self.rect.x += self.direction.x * SPEED["ball"] * dt
        self.collision("horizontal")
        self.rect.y += self.direction.y * SPEED["ball"] * dt
        self.collision("vertical")

    
    def collision(self, direction):
        for sprite in self.paddle_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    # Ball approaching from the left
                    if self.rect.right > sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.direction.x *= -1
                    # Ball approaching from the right
                    elif self.rect.left < sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.direction.x *= -1

                elif direction == "vertical":
                    # Ball approaching from the top
                    if self.rect.bottom > sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.direction.y *= -1
                    # Ball approaching from the bottom
                    elif self.rect.top < sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y *= -1         
    
    def wall_collision(self):
        if self.rect.top <=0:
            self.rect.top = 0
            self.direction.y *= -1
        
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1
        
        if self.rect.right >= WINDOW_WIDTH or self.rect.left <= 0:
           self.update_score("player" if self.rect.x < WINDOW_WIDTH / 2 else "opponent")
           self.reset()
    
    def reset(self):
        self.rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.direction = pygame.Vector2(choice((1,-1)),(uniform(0.7,0.8) * choice((-1,1))))
       
    def update(self,dt):
        self.old_rect = self.rect.copy()
        self.move(dt)
        self.wall_collision()