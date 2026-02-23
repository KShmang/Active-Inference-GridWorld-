# Import statement: numpy is a library for arrays and math, crucial for the matrices used in active inference calculations.
import numpy as np

# Class definition: GenerativeModel encapsulates the agent's internal worldview in active inference, predicting observations and states to minimize 'surprise' (free energy).
class GenerativeModel:
    # Constructor: Sets up all parameters when creating the model. grid_size is optional, defaults to 5.
    def __init__(self, grid_size=5):
        # Store the grid size, e.g., 5 for 5x5.
        self.grid_size = grid_size
        # Compute number of states: total positions, 25 for 5x5.
        self.num_states = grid_size * grid_size
        # Number of observation types, as defined in environment.
        self.num_observations = 4  # 0: cheese, 1: edge, 2: empty, 3: danger
        # Number of possible actions.
        self.num_actions = 4  # 0: UP, 1: DOWN, 2: LEFT, 3: RIGHT
        # List of action strings for reference.
        self.actions = ["UP", "DOWN", "LEFT", "RIGHT"]

        # Explain state indexing: 1D number from 2D position, row-major order.
        self.cheese_state = 4*grid_size + 4  # (4,4)
        self.cat_state = 0  # (0,0)

        # Prior beliefs: array of equal probabilities (1/25 each), agent's starting assumption about position.
        self.prior_states = np.ones(self.num_states) / self.num_states

        # Build and store A matrix (observation model).
        self.A = self._build_observation_model()

        # Build and store B matrix (transition model).
        self.B = self._build_transition_model()

        # C: Preference vector, log-probabilities favoring good outcomes (cheese high, danger low).
        self.C = np.array([10.0, 0.0, 0.0, -10.0])  # Strong preference for cheese, aversion to danger

    # Private method to construct A: a matrix where rows are observations, columns states, values probabilities.
    def _build_observation_model(self):
        A = np.zeros((self.num_observations, self.num_states))
        for s in range(self.num_states):
            x, y = divmod(s, self.grid_size)
            if (x, y) == (4, 4):
                A[0, s] = 1.0  # cheese
            elif (x, y) == (0, 0):
                A[3, s] = 1.0  # danger
            elif x in [0,4] or y in [0,4]:
                A[1, s] = 1.0  # edge
            else:
                A[2, s] = 1.0  # empty
        return A

    # Private method for B: 3D array for P(next_state | current_state, action).
    def _build_transition_model(self):
        B = np.zeros((self.num_states, self.num_states, self.num_actions))
        for s in range(self.num_states):
            x, y = divmod(s, self.grid_size)
            for a in range(self.num_actions):
                nx, ny = x, y
                if a == 0 and y > 0: ny -= 1  # UP
                elif a == 1 and y < self.grid_size-1: ny += 1  # DOWN
                elif a == 2 and x > 0: nx -= 1  # LEFT
                elif a == 3 and x < self.grid_size-1: nx += 1  # RIGHT
                ns = ny * self.grid_size + nx
                B[ns, s, a] = 1.0  # Deterministic
        return B

    # VFE calculation: Math formula for variational free energy, used to update beliefs.
    def variational_free_energy(self, q_s, obs):
        log_lik = np.dot(q_s, np.log(self.A[obs] + 1e-16))
        kl_div = np.dot(q_s, np.log(q_s / self.prior_states + 1e-16))
        return - (log_lik - kl_div)

    # EFE calculation: Expected free energy for action selection.
    def expected_free_energy(self, q_s, action):
        q_sp = np.dot(self.B[:, :, action], q_s)
        q_op = np.dot(self.A, q_sp)
        pragmatic = np.dot(q_op, self.C)
        epistemic = -np.sum(q_op * np.log(q_op + 1e-16))
        return - (pragmatic + epistemic)
