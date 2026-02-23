
# This line imports the numpy library, which is used for numerical operations like arrays and math. Even if not used much here, it's imported for consistency with other files.
import numpy as np

# Here we define a class called GridWorld. A class is a template for creating objects in Python, and this one represents the environment where the mouse navigates.
class GridWorld:
    # This is the constructor method (__init__), called when you create a new GridWorld object. It sets up initial values.
    def __init__(self): # This DEFINES the method (like writing a recipe) and it's called when you create a new GridWorld object.
        # self.size sets the dimension of the grid to 5, meaning a 5x5 grid of cells where the mouse can move.
        self.size = 5
        # self.cheese defines the goal position as (4,4), the bottom-right corner in a 0-indexed grid.
        self.cheese = (4, 4)
        # self.cat defines a danger position at (0,0), the top-left corner.
        self.cat = (0, 0)
        # self.pos sets the starting position of the mouse to [2,2], the center. It's a list so it can be modified easily.
        self.pos = [2, 2]          # start center and the mouse's starting position
    
    # This method 'step' handles moving the mouse based on the given action (like "UP"). It updates position and returns the new observation.
    def step(self, action):
        # Unpack the current position into x and y variables for easier reading and modification.
        x, y = self.pos
        # If the action is "UP" and y is greater than 0 (not at top), decrease y to move up.
        if action == "UP" and y > 0: y -= 1
        # Similarly for "DOWN": increase y if not at bottom (y < 4 for size 5).
        if action == "DOWN"  and y < 4: y += 1
        # For "LEFT": decrease x if not at left edge.
        if action == "LEFT"  and x > 0: x -= 1
        # For "RIGHT": increase x if not at right edge.
        if action == "RIGHT" and x < 4: x += 1
        # Update self.pos with the new [x, y] values.
        self.pos = [x, y]   
        # Call the observe method to get what the mouse senses now and return it.
        return self.observe()
    
    # The observe method returns an integer representing the type of cell: 0=cheese (good), 3=cat (bad), 1=edge, 2=empty.
    def observe(self):
        # Convert list to tuple for comparison with cheese position.
        if tuple(self.pos) == self.cheese: return 0   # cheese is the goal
        # Check for cat position.
        if tuple(self.pos) == self.cat:    return 3   # danger is the cat
        # Check if on boundary (edge).
        if self.pos[0] in [0,4] or self.pos[1] in [0,4]: return 1  # edge is the walls
        # Default: empty space.
        return 2                                      # empty is the empty space for the mouse to move around in

