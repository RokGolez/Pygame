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
