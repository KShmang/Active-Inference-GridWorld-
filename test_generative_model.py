# Sys and os for path adjustment.
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import unittest
from generative_model import GenerativeModel

class TestGenerativeModel(unittest.TestCase):
    def setUp(self):
        self.gm = GenerativeModel(grid_size=5)

    def test_observation_model(self):
        self.assertEqual(self.gm.A[0, 24], 1.0)
        self.assertEqual(self.gm.A[3, 0], 1.0)
        self.assertEqual(self.gm.A[1, 5], 1.0)
        self.assertEqual(self.gm.A[2, 12], 1.0)

    def test_transition_model(self):
        self.assertEqual(self.gm.B[13, 12, 3], 1.0)
        self.assertEqual(self.gm.B[0, 0, 2], 1.0)

    def test_free_energy_functions(self):
        q_s = np.ones(self.gm.num_states) / self.gm.num_states
        obs = 2
        vfe = self.gm.variational_free_energy(q_s, obs)
        self.assertTrue(np.isfinite(vfe))
        efe = self.gm.expected_free_energy(q_s, 0)
        self.assertTrue(np.isfinite(efe))

if __name__ == '__main__':
    unittest.main()
