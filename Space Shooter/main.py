import pygame 
from os.path import join, dirname, abspath
from random import randint, uniform

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join(ASSETS_DIR, "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()
        self.speed = 300
        
        # Cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 300
      
        # Mask
        self.mask = pygame.mask.from_surface(self.image) # Not needed as per documentation but nice to have for later projects

        
    def laser_timer(self): 
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
            
            
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf,self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            laser_sound.play()
        
        self.laser_timer()
      
class Star(pygame.sprite.Sprite):
    def __init__(self, groups,surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)))
            
class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self, pos):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0: 
                self.kill()  # Killing the Sprite after the laser is outside of the window.
                
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.original_surf = surf
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000 # 5 sec
        self.direction = pygame.Vector2(uniform(-0.5, 0.5),1)
        self.speed = randint(400,500)
        self.rotation_speed = randint(40,70)
        self.rotation = 0
        
                 
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime: # Killing off a meteor after 5 sec
            self.kill() 
        
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1)
        self.rect = self.image.get_frect(center = self.rect.center)
 
class Explosion(pygame.sprite.Sprite):
    def __init__(self, frames, pos, group):
        super().__init__(group) 
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        self.rect = self.image.get_frect(center=pos)

    def update(self, dt):
        # Increment frame index
        self.frame_index +=  35 * dt
        
        # Check if there are still frames to show
        if int(self.frame_index) < len(self.frames):
            self.image = self.frames[int(self.frame_index)]  # Update image
        else:
            self.kill()  # Destroy the sprite when the animation ends
           
def collisions():
    global running 
    
    # Player collision with meteors
    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, False, pygame.sprite.collide_mask)
    if collision_sprites:
        running = False

    # Laser collisions with meteors
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()  # Kill the laser on collision
            explosion_sound.play()
            
            # Spawn an explosion at the meteor's position
            Explosion(explosion_frames, laser.rect.midtop, all_sprites)
        
def display_score():
   current_time = pygame.time.get_ticks() // 100  
   text_surf = font.render(str(current_time), True, "white") # True to smooth out the edges  
   text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
   display_surface.blit(text_surf,text_rect)
   pygame.draw.rect(display_surface, (240,240,240), text_rect.inflate(20,10).move(0,-8), 5, 10) # Rounded padding around the timer
    
# Define directories for assets
ASSETS_DIR = join(dirname(abspath(__file__)), "images")
AUDIO_DIR = join(dirname(abspath(__file__)), "audio")
    
# General setup 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
running = True
clock = pygame.time.Clock()

# Import
star_surface = pygame.image.load(join(ASSETS_DIR, "star.png")).convert_alpha() #importing stars just once
meteor_surf = pygame.image.load(join(ASSETS_DIR, "meteor.png")).convert_alpha()
laser_surf = pygame.image.load(join(ASSETS_DIR, "laser.png")).convert_alpha()
explosion_frames = [pygame.image.load(join(ASSETS_DIR, "explosion", f"{i}.png")).convert_alpha() for i in range(21)]

# Sound Effects
laser_sound = pygame.mixer.Sound(join(AUDIO_DIR, "laser.wav"))
laser_sound.set_volume(0.1)
explosion_sound = pygame.mixer.Sound(join(AUDIO_DIR, "explosion.wav"))
explosion_sound.set_volume(0.1)
game_music =  pygame.mixer.Sound(join(AUDIO_DIR, "game_music.wav"))
game_music.set_volume(0.1)

game_music.play() 

# Text
font = pygame.font.Font(join(ASSETS_DIR,"Oxanium-Bold.ttf"), 40)

# Sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for _ in range(20):
    Star(all_sprites,star_surface)
player = Player(all_sprites)

# Custom events  > meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 100)


while running:
    dt = clock.tick() / 1000
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x, y = randint(0,WINDOW_WIDTH), randint(-200, -100) # Random coordinates to spawn a meteor
            Meteor(meteor_surf, (x,y), (all_sprites, meteor_sprites))
            
    # Update
    all_sprites.update(dt)
    
    # Collisions
    collisions()
   
    # Draw the game
    display_surface.fill("#323338" )
    display_score() 
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()
     