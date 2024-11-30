## Vampire Survival Game

A 2D action-survival game developed using Pygame. The player controls a character to survive against waves of enemies. The game features mechanics like bullet shooting, enemy spawning, collision detection, and map interactions. Players must navigate through the map while avoiding enemy damage.

### Code Structure

The project is organized into several files to maintain clarity and improve modularity:

- **`main.py`**: The game’s main engine, handling the game loop, events, input, and updating the game world.
- **`player.py`**: Contains the `Player` class, which controls the player’s movements, shooting, and health.
- **`sprites.py`**: Manages game objects like bullets, enemies, and other visual elements.
- **`settings.py`**: Holds constants such as screen dimensions, player stats, and other game settings.
- **`groups.py`**: Contains sprite groups for efficient collision detection and updates.
- **`data/maps/world.tmx`**: The tilemap that defines the world layout and environment.

By structuring the code in this way, each part of the game’s logic is modular, making the project easier to extend and maintain.

## Gameplay video

Check out this video on LinkedIn: [LinkedIn Post](https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7258779468171825152?compact=1)
