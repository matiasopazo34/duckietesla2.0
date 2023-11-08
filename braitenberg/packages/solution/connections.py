from typing import Tuple
from solution.preprocessing import preprocess #preprocess devuelve la matriz de 0 y 1
import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32") #se generan ceros
    # these are random values
    res[:, shape[1]//2] = 1
    res[:, shape[1]//2] = -1
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[:, shape[1]//2] = 1
    res[:, shape[1]//2] = -1
    # ---
    return res
