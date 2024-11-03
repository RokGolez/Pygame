from settings import *
from player import Player
from sprites import *
from random import randint, choice
from pytmx.util_pygame import load_pygame
from groups import AllSprites
from os.path import abspath, dirname, join
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampires")
        self.clock = pygame.time.Clock()
        self.running = True
               
        # Groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        # Load the map
        map_path = join(dirname(abspath(__file__)), "..", "data", "maps", "world.tmx")
        self.map = load_pygame(map_path)
        
        # Gun timer
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_cooldown = 200
       
       # Enemy timer
        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event, 500)
        self.start_pos = []    
        
        # Audio
        self.shoot_sound = pygame.mixer.Sound(join(dirname(abspath(__file__)), "..", "audio", "shoot.wav"))
        self.shoot_sound.set_volume(0.2)
        self.impact_sound = pygame.mixer.Sound(join(dirname(abspath(__file__)), "..", "audio", "impact.ogg"))
        self.shoot_sound.set_volume(0.2)
        self.music = pygame.mixer.Sound(join(dirname(abspath(__file__)), "..", "audio", "music.wav"))
        self.music.set_volume(0.2)
        self.music.play(loops = -1) # Plays forever
        
        # Setup  
        self.load_images()
        self.setup()
       
    def load_images(self):
        self.bullet_surf = pygame.image.load(join(dirname(dirname(abspath(__file__))), "images","gun","bullet.png")).convert_alpha()

        folders = list(walk(join(dirname(dirname(abspath(__file__))), "images", "enemies")))[0][1]
        self.enemy_frames = {}
        for folder in folders:
            for folder_path, _, file_names in walk(join(dirname(dirname(abspath(__file__))), "images", "enemies", folder)):
                self.enemy_frames[folder] = []
                for file_name in sorted(file_names, key = lambda name: int(name.split(".")[0])):
                    full_path = join(dirname(dirname(abspath(__file__))), folder_path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    self.enemy_frames[folder].append(surf)          
              
    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.shoot_sound.play()
            pos = self.gun.rect.center + self.gun.player_direction * 70
            Bullet(self.bullet_surf,pos,self.gun.player_direction,(self.all_sprites, self.bullet_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
    
    def gun_timer(self):#
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time  - self.shoot_time >= self.gun_cooldown:
                self.can_shoot = True           

    def setup(self):
        # Load ground tiles
        ground_layer = self.map.get_layer_by_name("Ground") 
        if ground_layer:
            for x, y, image in ground_layer.tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
            
        # Load object sprites
        objects_layer = self.map.get_layer_by_name("Objects")
        if objects_layer:
            for obj in objects_layer:
                CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))
            
        # Load collision tiles
        collisions_layer = self.map.get_layer_by_name("Collisions")
        if collisions_layer:
            for obj in collisions_layer:
                CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites) 
    
        for obj in self.map.get_layer_by_name("Entities"):
            if obj.name == "Player":
                # Player
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites) 
                self.gun = Gun(self.player, self.all_sprites)
            else:
                self.start_pos.append((obj.x, obj.y))
       
    def bullet_collision(self):
        if self.bullet_sprites:
            for bullet in self.bullet_sprites:
                collision_sprites = pygame.sprite.spritecollide(bullet,self.enemy_sprites, False, pygame.sprite.collide_mask) 
                if collision_sprites:
                    self.impact_sound.play()
                    for sprite in collision_sprites:
                        sprite.destroy()
                    bullet.kill()
                 
    def player_collision(self):
        if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False, pygame.sprite.collide_mask):
            self.running = False
                                      
    def run(self):
        while self.running:
            # Delta time
            dt = self.clock.tick() / 1000
            
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.enemy_event:
                    Enemy(choice(self.start_pos), choice(list(self.enemy_frames.values())), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites)
                    
            # Update
            self.gun_timer()
            self.input()
            self.all_sprites.update(dt)
            self.bullet_collision()
            self.player_collision()
            
            # Draw
            self.display_surface.fill("black")
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()
                    
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()

