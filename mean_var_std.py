import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(numbers).reshape(3, 3)

    calculations = {
        'mean': [list(np.mean(array, axis=0)), list(np.mean(array, axis=1)), np.mean(array)],
        'variance': [list(np.var(array, axis=0)), list(np.var(array, axis=1)), np.var(array)],
        'standard deviation': [list(np.std(array, axis=0)), list(np.std(array, axis=1)), np.std(array)],
        'max': [list(np.max(array, axis=0)), list(np.max(array, axis=1)), np.max(array)],
        'min': [list(np.min(array, axis=0)), list(np.min(array, axis=1)), np.min(array)],
        'sum': [list(np.sum(array, axis=0)), list(np.sum(array, axis=1)), np.sum(array)]
    }

    return calculations
