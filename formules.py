from decimal import Decimal
from unittest import result
import numpy as np
from combinatoric import Combinatoric as cb

def bernully(p : float, n : int, m : int) -> float:
    result = cb.combinations_without_repeats(n, m) * p ** m * (1 - p) ** (n - m)
    return round(result, 12)

def pollinom(n : int, p_array : list[float], m_array : list[int]) -> float:
    result = 1
    for i in range(len(p_array)):
        result *= p_array[i] ** m_array[i]
    result *= cb.permutation_with_repeats(n, m_array)
    return round(result, 12)

def puasson(p : float, n : int, m : int) -> float:
    result = (np.exp(n * p * -1) * (n * p) ** m) / np.math.factorial(m)
    return round(result, 12)