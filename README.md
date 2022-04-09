# arculus-pong

### Setup
- Install Python [preferrably v3.9+](https://www.python.org/downloads/)


### Clone the repository
- Run the command: `git clone git@github.com:luckyadogun/arculus-pong.git`
- Navigate into the source director: `cd arculus-pong`
- Create a virtual environment: `python3 -m virtualenv venv --python=python3.9`
- Activate the environment: `source venv/bin/activate`
- Install the requirements: `pip install -r requirements.txt` 

### Run the program
- Navigate to the source file and execute: `cd src && python main.py`
- Stop the program from your CLI: `ctrl + C`


### Task trade-offs
- The task asked for network capabilities: 
    This implementation doesn't contain any network functionalities and its only CLI based.
    While the scope wasn't fully understood by me, given enough time, it could have used a
    * WSGI server
    * Handle Input using webforms
    * Display the resulting interface using HTML/CSS/JS
    * Ability to multi-players


### How it works
The `main.py` contains the following classes:

- `GamingInterface()`: Responsible for programming settings gaming screen, and user inputs.
- `Ball()`: Interactive object between Player() and Opponent() objects
- `Player()`: Creates a player object that interacts with the ball and an opponent
- `Opponent()`: Creates a opponent (similar to player) object that interacts with the ball and players


### How this code can be made better
- The classes could be refactored into separate modules for testing and easy of change
- Integrating a test-case
- Duck-typing: Some of the classes share similar methods which could be extracted so it can be easily maintenable.
- Create multi-players with a network capabilities to add new players
- Showcase scores
- Dockerize the code to make it OS agnostic and setup-friendly
- And more.

#### Requirement/Packages
- This package was built using [PyGame](https://www.pygame.org/docs/)