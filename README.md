# Superman Pygame

A simple Superman-themed Flappy Bird style game built with Python and Pygame.

## Features

- Superman character that can jump to avoid obstacles
- Pipe obstacles with dynamic gap sizing
- Score tracking
- Game states: Start screen, Playing, Game Over, Paused
- Background music and sound effects

## Project Structure

```
superman-pygame/
├── .venv/                 # Virtual environment
├── src/                   # Source code
│   ├── __init__.py
│   ├── main.py           # Main game file
│   ├── game/             # Game modules
│   │   ├── __init__.py
│   │   ├── superman.py   # Superman class
│   │   ├── pipe.py       # Pipe class
│   │   └── game_state.py # Game state management
│   └── config/           # Configuration
│       ├── __init__.py
│       └── settings.py   # Game settings
├── assets/               # Game assets
│   ├── images/           # Image files
│   └── sounds/           # Audio files
├── requirements.txt      # Python dependencies
├── README.md
└── run.py               # Entry point
```

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vaibhavkulshrestha12/superman-pygame.git
   cd superman-pygame
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   # On Windows (bash):
   source .venv/Scripts/activate
   # On Windows (cmd):
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. **Make sure your virtual environment is activated**
2. **Run the game:**
   ```bash
   python run.py
   ```

## Controls

- **SPACE**: Jump (during game) / Start game / Restart after game over
- **P**: Pause/Unpause the game
- **Close window**: Quit the game

## Game Rules

- Press SPACE to make Superman jump
- Avoid hitting the pipes or the ground
- Your score increases as you pass through pipes
- The gap between pipes gets smaller as your score increases
- Try to achieve the highest score possible!

## Dependencies

- pygame==2.6.1

## Development

The code is organized into modules for better maintainability:

- `src/main.py`: Main game class and entry point
- `src/game/superman.py`: Superman character logic
- `src/game/pipe.py`: Pipe obstacle logic  
- `src/game/game_state.py`: Game state management
- `src/config/settings.py`: Game configuration and constants

## Contributing

Feel free to fork this project and submit pull requests for any improvements!
