In this Pygame project, the code is split into several classes that follow Object-Oriented Programming (OOP) principles, making it modular and easy to maintain:

- **Game Class**: Manages game initialization, setup, input, and the main loop. It coordinates interactions between the player, enemies, and objects.
- **Player Class**: Represents the player, handling movement and shooting.
- **Enemy Class**: Spawns enemies and manages their behavior.
- **Gun and Bullet Classes**: Handle the shooting mechanic, with cooldown and collision detection.
- **Sprites**: All game objects (player, enemies, bullets) are managed through Pygame's sprite groups for collision detection and updates.

This structure promotes clean, reusable code by separating concerns into distinct classes and using sprite-based handling for game objects.

### Code Structure

The project is split into different files to maintain modularity and improve readability:

- **`main.py`**: The core of the game, responsible for setting up and running the game loop. It handles input, game mechanics, and interactions between objects.
- **`player.py`**: Contains the `Player` class, which manages player movement, shooting, and interaction with the game world.
- **`sprites.py`**: Defines various game objects, such as enemies, bullets, and sprites, including their behavior and interactions.
- **`settings.py`**: Contains global constants, such as window size and other configuration values used throughout the game.
- **`groups.py`**: Manages sprite groups for collision detection and updates.
- **`data/maps/world.tmx`**: The tilemap used to define the game world layout.

By splitting the code across these files, each part of the game logic is isolated, making the code easier to manage and expand upon.

## Gameplay video

Check out this video on LinkedIn: [LinkedIn Post](https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7258779468171825152?compact=1)
