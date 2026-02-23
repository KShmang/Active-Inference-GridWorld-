# Active-Inference-GridWorld

A learning project exploring active inference — a probabilistic framework that models how agents perceive their environment, form beliefs about it, and take actions to minimize surprise. This project implements a simple grid world environment to study how an agent can navigate toward a goal while avoiding threats.

# The Evironment

A mouse starts at the center of a grid with two key features:

* 🧀 Cheese in the bottom right corner (goal)

* 🐱 Cat in the top left corner (obstacle to avoid)

The agent must learn to navigate toward the cheese while avoiding the cat — a classic setup for studying goal-directed behavior under uncertainty.

# Project Structure 

* [`environment.py`](environment.py) — defines the grid world, agent starting position, goal and obstacle locations

* [`generative_model.py`](generative_model.py) — implements the agent's internal model of the world, encoding beliefs about states and outcomes

* [`generative_model_test.py`](generative_model_test.py) — tests for validating generative model behavior

* [`test_environment.py`](test_environment.py) — tests for validating environment dynamics

## Requirements

- Python 3.13.7
- NumPy
- Matplotlib

To install NumPy and Matplotlib, open your terminal and run:

pip install numpy matplotlib

## Running the Code

Run the environment:

python environment.py

Run the environment tests:

python test_environment.py

Run the generative model tests:

python generative_model_test.py

# Status

Environment and generative model complete. Active inference agent currently in development. This is an ongoing independent learning project being built alongside study of the underlying theory.

# Background & Motivation

Active inference is rooted in the Free Energy Principle developed by Karl Friston. The core idea is that biological agents act to minimize variational free energy — essentially minimizing the gap between what they expect and what they perceive. This project is my hands-on entry point into that framework, motivated by an interest in computational neuroscience and agent-based modeling.
