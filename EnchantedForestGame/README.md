I asked AI to generate a fun project for me to build so here it is:
🏰 The Enchanted Forest Adventure
A text‑based game that uses every single concept from your list – except type casting (no int(), float(), str(), bool(), etc. – all user input stays as strings, and numbers are only used internally).
You’ll explore rooms, collect magical items, and aim to find the Crystal of Eternity while managing your health.

🎯 What You’ll Practice
Concept	How you’ll use it
Variables & Data Types	name (str), health (int), gold (int), is_alive (bool)
Lists	Player inventory (mutable, ordered collection)
Tuples	Room coordinates (x, y) or movement directions like ("north", "south")
Sets	Track which rooms you’ve already visited
Dictionaries	Define the game world: room data (description, connections, items)
Operators	Arithmetic (health -= 2), comparison (if health <= 0), logical (and/or)
Conditionals	if/elif/else for movement, taking items, winning, losing
Loops	while True for the main game loop, for to display inventory
Functions	Define move(), look(), take(), use() with clear roles
Built-in functions	print(), input(), len(), sorted(), lower(), capitalize()
Strings	f‑strings, .strip(), .split(), .join(), multi‑line strings
Exceptions	try/except for when users type unrecognised commands
Comments	Explain tricky logic, document functions
Type Annotations	Add hints to every function: def move(direction: str) -> bool:
🗺️ The World (Your Starter Map)
We have 6 rooms arranged like this:

text
     ┌─────────┐
     │  Forest  │ ──── │  Cave   │
     │ (start)  │      │         │
     └────┬────┘      └────┬────┘
          │                │
     ┌────┴────┐      ┌────┴────┐
     │  River  │ ──── │  Ruins  │
     │         │      │         │
     └─────────┘      └────┬────┘
                            │
                     ┌──────┴──────┐
                     │  Mountain   │
                     │  (treasure) │
                     └─────────────┘
Each room has:

A description (string)

A dictionary of connections (e.g. {"north": "Cave"})

A list of items lying there (e.g. ["sword", "potion"])

⚔️ Game Rules
Start in the Forest with 10 health and an empty inventory.

Commands you can type (case‑insensitive):

go north / go south / go east / go west

look – re‑read the room description

take <item> – pick up an item

inventory – see what you’re carrying

use <item> – use an item (e.g. potion heals 3 HP)

quit – end the game

Winning – reach the Mountain and type take crystal (the crystal is there).
You win immediately!

Losing – if health drops to 0 or below, game over.

Traps – some rooms have hidden dangers. For example, entering the Cave without a torch costs you 2 health. The River might wash away one of your items (random chance).

Visited Set – each time you enter a room, add its name to a set. At the end, print how many unique rooms you visited.

🧩 Your Tasks (Step‑by‑Step)
1. Define the World (Dictionary)
python
rooms: dict[str, dict] = {
    "Forest": {
        "desc": "Sunlight filters through tall oaks. Paths lead north and south.",
        "exits": {"north": "Cave", "south": "River"},
        "items": ["stick"]
    },
    # ... define all 6 rooms
}
2. Player State (Variables)
python
player_name: str = input("What's your name, adventurer? ").strip().capitalize()
health: int = 10
inventory: list[str] = []
visited: set[str] = set()
current_room: str = "Forest"
game_over: bool = False
3. Helper Functions (with type annotations)
describe(room: str) -> None – prints description + exits + items.

move(direction: str) -> bool – updates current_room, returns True if successful.

take_item(item: str) -> None – removes from room, appends to inventory.

use_item(item: str) -> None – implements effects (heal, light torch, etc.).

check_traps(room: str) -> None – applies room‑specific effects.

4. The Main Loop
while not game_over:

Get user input, strip extra spaces.

Split into command and target (e.g. "go north" → ["go", "north"]).

Use try/except to handle IndexError if the user types only one word.

Use conditionals to route the command.

Built‑ins you’ll love: len(inventory), sorted(visited), ", ".join(inventory).

5. Add Excitement
Cave: if you don’t have "torch" in inventory, lose 2 health.

River: 30% chance to lose a random item (use random.choice() – it’s a built‑in from the random module, but you’re allowed to import it).

Ruins: contains a "potion" that heals +3.

Mountain: contains the "crystal" – taking it wins the game.

6. Final Touch
After the game ends (win or lose), display:

Total moves made (use a counter variable).

Unique rooms visited (length of the visited set).

Final inventory and health.

🚫 The "No Type Casting" Rule
You cannot use:

int() – so don’t ask for numeric input.

float(), str(), bool() for conversion.

All user input stays as a string. You compare it directly:

python
if command == "go" and target == "north":
If you need a number from the user, you simply don’t – use words only.
Health changes are done internally with arithmetic (health -= 2) – that’s fine because health is already an integer variable.

📝 Example Skeleton to Get You Started
python
import random

# Type annotations for clarity
rooms: dict[str, dict] = { ... }

def describe(room_name: str) -> None:
    """Print room description, exits, and visible items."""
    room = rooms[room_name]
    print(f"\n📍 {room_name}")
    print(room["desc"])
    # ... exits & items

def move(direction: str) -> bool:
    """Try to move to a neighbouring room. Return True if successful."""
    global current_room
    # ... use rooms[current_room]["exits"].get(direction)

# ... define other functions

# ----- GAME START -----
print("🏞️ Welcome to the Enchanted Forest!\n")
name = input("Your name: ").strip().capitalize()
# ... initialise variables

while not game_over:
    # ... input handling with try/except
    # ... command routing
    pass

# ----- GAME END -----
print("\n--- GAME OVER ---")
print(f"Health: {health}")
print(f"Items: {', '.join(inventory) if inventory else 'empty'}")
print(f"Unique rooms visited: {len(visited)}")
🌟 Stretch Goals (if you finish early)
Add a "score" based on health + gold + items found.

Add a "help" command that lists all possible actions.

Use a tuple to store the player’s last 3 actions (last_actions), and show them when they type "history".

Let the player drop items (drop <item>).

✅ How to Know You’ve Covered Everything
□ Variables & Data Types – name, health, inventory, etc.
□ Lists – inventory and rooms[...]["items"]
□ Tuples – e.g. DIRECTIONS = ("north", "south", "east", "west")
□ Sets – visited
□ Dictionaries – rooms and rooms[room]["exits"]
□ Operators – arithmetic, comparisons, logical
□ Conditionals – all the if/elif/else routing
□ Loops – main while, a for when printing inventory
□ Functions – at least 4–5 well‑defined functions
□ Built‑ins – input, print, len, sorted, lower, join
□ Strings – f‑strings, .strip(), .capitalize()
□ Exceptions – try/except around input().split()
□ Comments – add a comment for every function and tricky block
□ Type Annotations – every function has -> and parameter hints
