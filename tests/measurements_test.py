""" Unittest File for verification of the Pauli measurements

"""


import pytest
import numpy as np
from unittest.mock import MagicMock
import graphepp as gg


def test_PauliZ():
    test_state = gg.Graph(3, ((0, 1), (1, 0), (1, 2), (2, 0)))
    test_state_expectation = gg.Graph(3, ((2, 0),))
    test_state_measured = gg.local_PauliZ(test_state, n=1)

    assert test_state_measured == test_state_expectation


def test_PauliY():
    test_state = gg.Graph(3, ((0, 1), (1, 0), (1, 2), (2, 0)))
    test_state_expectation = gg.Graph(3, ((),))
    test_state_measured = gg.local_PauliY(test_state, n=1)

    assert test_state_measured == test_state_expectation


def test_PauliX():
    test_state = gg.Graph(5, ((0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 3)))
    test_state_expectation = gg.Graph(5, ((1, 3), (0, 3), (3, 4), (0, 4)))
    test_state_measured = gg.local_PauliX(test_state, n=2, neighbor=1)

    assert test_state_measured == test_state_expectation
