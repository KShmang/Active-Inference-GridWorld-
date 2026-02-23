# This is a special kind of comment called a docstring. It's enclosed in triple quotes and describes what the whole file does. This file is a Python script (a program) that tests the GridWorld environment and creates visual pictures (plots) to show what the grid looks like and if everything works correctly.
"""
Visualization and testing script for GridWorld environment
Tests all functionality and creates visualizations to confirm everything works correctly
"""

# The next line is an import statement. 'import' is a keyword (special word) in Python that brings in tools from a library called numpy. A library is like a toolbox with pre-made functions. numpy helps with math and lists of numbers (called arrays). We give it a shortcut name 'np' to type less.
import numpy as np

# This imports 'pyplot' from a library called matplotlib. Matplotlib is for drawing graphs and images. 'pyplot' is the part for plotting, and we call it 'plt' for short.
import matplotlib.pyplot as plt

# This imports a specific tool called Rectangle from matplotlib.patches. Patches are shapes you can draw on plots, like rectangles, but we might not use it directly here—it's included for possible future use.
from matplotlib.patches import Rectangle

# Now we're importing 'sys' and 'os'. These are built-in libraries (come with Python). 'sys' gives access to system-related things, like where Python looks for files. 'os' helps with operating system tasks, like handling file paths (locations of files on your computer).
import sys
import os

# This line modifies 'sys.path', which is a list (ordered collection) of folders where Python searches for modules (files with code). We append (add to the end) a path: os.path.dirname gets the directory (folder) name, os.path.abspath gets the full absolute path of this file (__file__ is a special variable meaning "this file"), and we do dirname twice to get the parent folder of 'tests/'. This lets Python find 'environment.py' in the main project folder.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# This import brings in the GridWorld class from the file environment.py. 'from ... import' means take this specific thing (GridWorld) from that file. A class is like a blueprint for creating objects (things with properties and behaviors).
from environment import GridWorld


# Here we define a function named visualize_grid_world. A function is a named block of code that can be called (run) multiple times. It takes inputs (parameters): 'env' is the environment object, 'title' is a string (text) with a default value if not provided.
def visualize_grid_world(env, title="Grid World Environment"):

    # Docstring inside the function, explaining what it does in more detail.
    """Create a comprehensive visualization of the grid world"""

    # This creates a figure (like a canvas for drawing) and two axes (subplots, areas to plot on) side by side. plt.subplots is a function from matplotlib that returns the figure and axes. (1,2) means 1 row, 2 columns, figsize sets the size in inches.
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Create an array (2D list) of zeros with shape (5,5) if env.size is 5. This will hold color values for the plot.
    grid = np.zeros((env.size, env.size))

    # Another similar array for storing observation numbers.
    obs_grid = np.zeros((env.size, env.size))
    
    # Copy the current position of the environment to restore later. env.pos is a list, .copy() makes a new list with the same values.
    original_pos = env.pos.copy()

    # A for loop: This repeats the code inside for each value of y from 0 to env.size-1 (e.g., 0 to 4). 'range' generates numbers.
    for y in range(env.size):

        # Nested for loop: For each y, loop over x from 0 to 4.
        for x in range(env.size):

            # Set the environment's position to [x, y]. This is temporary for checking the observation at this spot.
            env.pos = [x, y]

            # Call the observe method (function) of env to get the observation number (0-3) at this position, store in variable 'obs'.
            obs = env.observe()

            # Store 'obs' in the obs_grid at row y, column x.
            obs_grid[y, x] = obs

            # An if statement: Checks conditions. If obs is 0 (cheese), set grid[y,x] to 1 (for full color intensity).
            if obs == 0:  # cheese

                grid[y, x] = 1

            # elif (else if): If not 0, check if 1 (edge), set to 0.3 (medium low intensity).
            elif obs == 1:  # edge

                grid[y, x] = 0.3

            # Another elif for 2 (empty), set to 0.1 (low intensity).
            elif obs == 2:  # empty

                grid[y, x] = 0.1

            # Last elif for 3 (danger), set to 0.8 (high intensity).
            elif obs == 3:  # danger

                grid[y, x] = 0.8
    
    # After loops, restore the position to what it was before.
    env.pos = original_pos
    
    # Use imshow on ax1 to display the grid as an image, with color map 'RdYlGn' (red to yellow to green), values from 0 to 1, keeping aspect ratio equal for square cells.
    im1 = ax1.imshow(grid, cmap='RdYlGn', vmin=0, vmax=1, aspect='equal')
    
    # Assign variables for plotting: Swap x and y for cheese because plotting uses (x,y) but our grid uses row (y), column (x).
    cheese_y, cheese_x = env.cheese[1], env.cheese[0]

    # Same swap for cat position.
    cat_y, cat_x = env.cat[1], env.cat[0]

    # Swap for current position.
    pos_y, pos_x = env.pos[1], env.pos[0]
    
    # For loop to draw grid lines: i goes from 0 to 5 (env.size + 1).
    for i in range(env.size + 1):

        # Draw horizontal line at y = i - 0.5, black, thin.
        ax1.axhline(i - 0.5, color='black', linewidth=0.5)

        # Draw vertical line at x = i - 0.5.
        ax1.axvline(i - 0.5, color='black', linewidth=0.5)
    
    # Plot a point for cheese: ax1.plot draws on the axis, with coordinates, marker 'P' (plus), color gold, size 25, black edge, label for legend.
    ax1.plot(cheese_x, cheese_y, 'P', color='gold', markersize=25, 
             markeredgecolor='black', markeredgewidth=2, label='Cheese')
    
    # Plot cat: marker 'X', red.
    ax1.plot(cat_x, cat_y, 'X', color='red', markersize=25, 
             markeredgecolor='black', markeredgewidth=2, label='Cat (Danger)')
    
    # Plot current position: marker 'o' (circle), steelblue.
    ax1.plot(pos_x, pos_y, 'o', color='steelblue', markersize=20, 
             markeredgecolor='black', markeredgewidth=2, label='Current Position')
    
    # Set the x-axis limits to show from -0.5 to 4.5, centering the grid.
    ax1.set_xlim(-0.5, env.size - 0.5)

    # Set y-limits similarly.
    ax1.set_ylim(-0.5, env.size - 0.5)

    # Set x-ticks (labels on axis) to 0,1,2,3,4.
    ax1.set_xticks(range(env.size))

    # Set y-ticks.
    ax1.set_yticks(range(env.size))

    # Label the x-axis with text 'X coordinate'.
    ax1.set_xlabel('X coordinate')

    # Label y-axis.
    ax1.set_ylabel('Y coordinate')

    # Set the title of the plot, using f-string (formatted string) to include the 'title' parameter and add 'Observation Map'.
    ax1.set_title(f'{title}\nObservation Map')

    # Add a legend (key) in the upper right, showing labels like 'Cheese'.
    ax1.legend(loc='upper right')

    # Invert the y-axis so 0 is at the top, like how maps often have (0,0) at top-left.
    ax1.invert_yaxis()

    # For the second subplot: Display obs_grid as image with 'viridis' color map, values 0 to 3.
    im2 = ax2.imshow(obs_grid, cmap='viridis', aspect='equal', vmin=0, vmax=3)
    
    # Loop to draw white grid lines on ax2.
    for i in range(env.size + 1):

        ax2.axhline(i - 0.5, color='white', linewidth=0.5)

        ax2.axvline(i - 0.5, color='white', linewidth=0.5)
    
    # Nested loops to add text to each cell in the plot.
    for y in range(env.size):

        for x in range(env.size):

            # Convert the grid value to integer (whole number).
            obs_val = int(obs_grid[y, x])

            # Use a dictionary (key-value map) to get the label text for the obs value.
            obs_label = {0: 'Cheese', 1: 'Edge', 2: 'Empty', 3: 'Danger'}[obs_val]

            # Add text to the plot at position (x,y), with the value and label, centered (ha='center', va='center'), small font, color chosen for visibility, bold.
            ax2.text(x, y, f'{obs_val}\n({obs_label})', 
                    ha='center', va='center', fontsize=8, 
                    color='white' if obs_val in [2, 3] else 'black',
                    weight='bold')
    
    # Set limits for ax2, same as ax1.
    ax2.set_xlim(-0.5, env.size - 0.5)

    ax2.set_ylim(-0.5, env.size - 0.5)

    ax2.set_xticks(range(env.size))

    ax2.set_yticks(range(env.size))

    ax2.set_xlabel('X coordinate')

    ax2.set_ylabel('Y coordinate')

    ax2.set_title('Observation Values\n(0=Cheese, 1=Edge, 2=Empty, 3=Danger)')

    ax2.invert_yaxis()
    
    # Adjust the layout so plots don't overlap.
    plt.tight_layout()

    # Return the fig object so it can be used or saved outside the function.
    return fig

# Empty line for separation.

# Define test_movement function: This tests if moving in the environment works, including boundaries.
def test_movement(env):

    """Test all movement actions"""  # Docstring.

    # Print a line of 60 '=' for visual separation in the console (terminal output).
    print("\n" + "="*60)

    print("TESTING MOVEMENT ACTIONS")

    print("="*60)
    
    # Set position to center [2,2].
    env.pos = [2, 2]

    # Print using f-string (formats text with variables).
    print(f"\nStarting position: {env.pos}")

    print(f"Initial observation: {env.observe()} (Empty)")
    
    # Create a list (ordered collection) of strings for actions.
    actions = ["UP", "DOWN", "LEFT", "RIGHT"]

    # For each action in the list.
    for action in actions:

        # Copy current position to old_pos.
        old_pos = env.pos.copy()

        # Call step with action, get new obs.
        obs = env.step(action)

        # Dictionary to map number to name.
        obs_name = {0: "Cheese", 1: "Edge", 2: "Empty", 3: "Danger"}[obs]

        # Print formatted string with action, positions, obs.
        print(f"Action: {action:5} | Position: {old_pos} -> {env.pos} | Observation: {obs} ({obs_name})")

        # Reset position.
        env.pos = [2, 2]
    
    # Print subheader.
    print("\n--- Testing Boundary Conditions ---")

    # Set to [0,0].
    env.pos = [0, 0]

    print(f"Position: {env.pos}")

    obs = env.step("UP")

    print(f"Try UP from (0,0): Position stays at {env.pos} (boundary respected)")

    obs = env.step("LEFT")

    print(f"Try LEFT from (0,0): Position stays at {env.pos} (boundary respected)")
    
    # Set to [4,4].
    env.pos = [4, 4]

    print(f"\nPosition: {env.pos}")

    obs = env.step("DOWN")

    print(f"Try DOWN from (4,4): Position stays at {env.pos} (boundary respected)")

    obs = env.step("RIGHT")

    print(f"Try RIGHT from (4,4): Position stays at {env.pos} (boundary respected)")

# Empty line.

# Define test_observations: Tests what observe returns at different spots.
def test_observations(env):

    """Test observation function at key positions"""

    print("\n" + "="*60)

    print("TESTING OBSERVATIONS")

    print("="*60)
    
    # List of lists (each inner list has position and description).
    test_positions = [
        ([4, 4], "Cheese position"),
        ([0, 0], "Cat position (Danger)"),
        ([0, 2], "Left edge"),
        ([4, 2], "Right edge"),
        ([2, 0], "Top edge"),
        ([2, 4], "Bottom edge"),
        ([2, 2], "Center (Empty)"),
    ]
    
    original_pos = env.pos.copy()

    # For each item in test_positions, unpack to pos and description.
    for pos, description in test_positions:

        env.pos = pos

        obs = env.observe()

        obs_name = {0: "Cheese", 1: "Edge", 2: "Empty", 3: "Danger"}[obs]

        print(f"Position {pos}: Observation = {obs} ({obs_name}) - {description}")
    
    env.pos = original_pos

# Empty line.

# Define visualize_path: Similar to first vis, but for a path of movements.
def visualize_path(env, actions_sequence):

    """Visualize a path through the environment"""

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    
    env.pos = [2, 2]

    path = [env.pos.copy()]
    
    for action in actions_sequence:

        env.step(action)

        path.append(env.pos.copy())
    
    grid = np.zeros((env.size, env.size))

    for y in range(env.size):

        for x in range(env.size):

            env.pos = [x, y]

            obs = env.observe()

            if obs == 0: grid[y, x] = 1

            elif obs == 1: grid[y, x] = 0.3

            elif obs == 2: grid[y, x] = 0.1

            elif obs == 3: grid[y, x] = 0.8
    
    env.pos = path[-1]
    
    ax.imshow(grid, cmap='RdYlGn', vmin=0, vmax=1, aspect='equal')
    
    for i in range(env.size + 1):

        ax.axhline(i - 0.5, color='black', linewidth=0.5)

        ax.axvline(i - 0.5, color='black', linewidth=0.5)
    
    path_array = np.array(path)

    ax.plot(path_array[:, 0], path_array[:, 1], 'o-', color='steelblue', linewidth=3, markersize=10, label='Path', zorder=5)
    
    ax.plot(path[0][0], path[0][1], 's', color='lime', markersize=15, markeredgecolor='black', markeredgewidth=2, label='Start', zorder=6)
    
    ax.plot(path[-1][0], path[-1][1], 'D', color='purple', markersize=15, markeredgecolor='black', markeredgewidth=2, label='End', zorder=6)
    
    ax.plot(env.cheese[0], env.cheese[1], 'P', color='gold', markersize=25, markeredgecolor='black', markeredgewidth=2, label='Cheese', zorder=6)
    
    ax.plot(env.cat[0], env.cat[1], 'X', color='red', markersize=25, markeredgecolor='black', markeredgewidth=2, label='Cat (Danger)', zorder=6)
    
    ax.set_xlim(-0.5, env.size - 0.5)

    ax.set_ylim(-0.5, env.size - 0.5)

    ax.set_xticks(range(env.size))

    ax.set_yticks(range(env.size))

    ax.set_xlabel('X coordinate')

    ax.set_ylabel('Y coordinate')

    ax.set_title('Example Path Through Grid World')

    ax.legend(loc='upper right')

    ax.invert_yaxis()
    
    plt.tight_layout()

    return fig

# Define main: The entry point function that runs everything when the script is executed.
def main():

    """Run all tests and visualizations"""

    print("="*60)

    print("GRID WORLD ENVIRONMENT TESTING & VISUALIZATION")

    print("="*60)
    
    env = GridWorld()
    
    print(f"\nEnvironment initialized:")

    print(f"  Grid size: {env.size}x{env.size}")

    print(f"  Cheese position: {env.cheese}")

    print(f"  Cat position: {env.cat}")

    print(f"  Starting position: {env.pos}")
    
    test_observations(env)
    
    test_movement(env)
    
    print("\n" + "="*60)

    print("GENERATING VISUALIZATIONS")

    print("="*60)
    
    fig1 = visualize_grid_world(env, "Grid World Environment - Complete View")

    plt.savefig('visualizations/environment_visualization.png', dpi=150, bbox_inches='tight')

    print("\n[OK] Saved: visualizations/environment_visualization.png")
    
    example_path = ["RIGHT", "RIGHT", "DOWN", "DOWN", "RIGHT", "RIGHT"]

    fig2 = visualize_path(env, example_path)

    plt.savefig('visualizations/environment_path_example.png', dpi=150, bbox_inches='tight')

    print("[OK] Saved: visualizations/environment_path_example.png")
    
    print("\n" + "="*60)

    print("ALL TESTS COMPLETE!")

    print("="*60)

    print("\nVisualizations saved. Displaying plots...")
    
    plt.show()

# This is a common Python pattern: If this file is the main one being run (not imported), execute main().
if __name__ == "__main__":

    main()

