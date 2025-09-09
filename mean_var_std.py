import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(input_list).reshape(3, 3)
    
    # Convert all NumPy types to native Python types
    calculations = {
        'mean': [list(map(float, np.mean(arr, axis=0))), 
                 list(map(float, np.mean(arr, axis=1))), 
                 float(np.mean(arr))],
        'variance': [list(map(float, np.var(arr, axis=0))), 
                    list(map(float, np.var(arr, axis=1))), 
                    float(np.var(arr))],
        'standard deviation': [list(map(float, np.std(arr, axis=0))), 
                              list(map(float, np.std(arr, axis=1))), 
                              float(np.std(arr))],
        'max': [list(map(int, np.max(arr, axis=0))), 
               list(map(int, np.max(arr, axis=1))), 
               int(np.max(arr))],
        'min': [list(map(int, np.min(arr, axis=0))), 
               list(map(int, np.min(arr, axis=1))), 
               int(np.min(arr))],
        'sum': [list(map(int, np.sum(arr, axis=0))), 
               list(map(int, np.sum(arr, axis=1))), 
               int(np.sum(arr))]
    }

    return calculations
