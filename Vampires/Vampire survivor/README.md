# Vampires

A top-down shooter game built using Python and `pygame-ce`. Navigate as a player in a map populated with enemies, dodging and shooting your way through the game world.

## Features

- **Player Movement**: Move the player character around the game map.
- **Shooting Mechanism**: Shoot bullets in the direction the player is facing, with a cooldown timer to prevent rapid firing.
- **Enemies**: Enemies populate the game world and react to the player.
- **Collision Detection**: Collisions between the player, bullets, and enemies are handled to create interactive gameplay.
- **Cooldown and Timers**: Features a cooldown timer for shooting, as well as a delay when the player collides with enemies.
- **Map Layout**: Built using a `.tmx` file (Tile Map XML) for structured map layout.

## Requirements

- Python 3.12
- `pygame-ce` 2.5.1
- `pytmx` for handling the Tiled map

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vampires.git
   cd vampires
